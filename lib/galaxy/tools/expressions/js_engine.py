"""A sandboxed JavaScript engine for evaluating CWL/ECMAScript expressions.

Galaxy evaluates workflow ``when``/``valueFrom`` expressions and expression-tool
scripts as JavaScript. Historically this ran in a Node.js subprocess via
``vm.runInNewContext``, which is not a security boundary: from inside that context
``globalThis.constructor.constructor`` reaches the host ``Function`` and therefore
``process`` and ``require('child_process')``, allowing arbitrary code execution as
the Galaxy service account on the control-plane host.

The engine here runs the same expressions in an embedded V8 isolate (``mini-racer``)
that has no Node bindings: there is no ``process``, ``require`` or ``child_process``
in scope for an escape to reach. It registers itself as the ``cwl_utils`` expression
engine so that every ``cwl_utils.expression.do_eval``/``interpolate`` call made by
Galaxy is evaluated inside the isolate rather than in Node.
"""

import functools
import json
import logging
import os
import platform
import shlex
import shutil
import subprocess
import sys
import threading
from collections.abc import Sequence
from typing import (
    Any,
    cast,
)

from cwl_utils.errors import JavascriptException
from cwl_utils.sandboxjs import (
    default_timeout,
    NodeJSEngine,
    set_js_engine,
)
from cwl_utils.types import CWLOutputType
from py_mini_racer import (
    JSEvalException,
    JSOOMException,
    JSParseException,
    JSTimeoutException,
)

from galaxy_ext.expressions import sandbox_worker
from galaxy_ext.expressions.sandbox_worker import run_program

# Upper bound on the V8 heap for a single evaluation. A hostile expression can still
# spin the CPU until the timeout fires, but it cannot exhaust control-plane memory.
MEMORY_LIMIT_BYTES = 200 * 1024 * 1024

# Absolute path to the out-of-process worker, launched under an isolation command
# (e.g. bubblewrap) when one is configured. It is run by path rather than with
# ``-m`` so it works even when ``galaxy_ext`` is not importable in a bare subprocess
# (e.g. run-from-source deployments that add lib/ to sys.path without exporting
# PYTHONPATH). The worker itself imports no Galaxy code.
WORKER_SCRIPT = os.path.abspath(sandbox_worker.__file__)

# Extra time granted to the jailed subprocess over the in-VM timeout before it is
# hard-killed, so the V8 timeout normally fires first with a clean error.
SUBPROCESS_GRACE_SECONDS = 10.0

# Config values that select the built-in bubblewrap recipe instead of a literal command.
BUBBLEWRAP_KEYWORDS = frozenset({"bubblewrap", "bwrap"})

# System paths the worker's interpreter and py_mini_racer's V8 library may need
# (dynamic linker, shared libraries, binaries). Bound read-only and best-effort, so a
# path missing on a given distro (e.g. merged-/usr where /lib is a symlink) is skipped.
BUBBLEWRAP_SYSTEM_PATHS = (
    "/usr",
    "/lib",
    "/lib64",
    "/bin",
    "/sbin",
    "/etc/ld.so.cache",
    "/etc/ld.so.preload",
)

_MR_EXCEPTIONS = (JSEvalException, JSParseException, JSTimeoutException, JSOOMException)

log = logging.getLogger(__name__)


def _bubblewrap_command(bwrap: str) -> tuple[str, ...]:
    """Build the built-in bubblewrap jail command.

    Read-only-binds only what the worker needs to run -- the Python runtime, the
    worker script, and the system libraries/binaries -- and gives it ``/proc``, a
    minimal ``/dev`` and a private writable ``/tmp``. Galaxy's config, database, home
    directory and the rest of the filesystem are deliberately NOT mounted, so even a
    compromised worker cannot read secrets from disk. The environment is cleared and
    the PID/IPC/UTS namespaces are unshared. The Python interpreter and worker script
    are appended by the caller.

    The network namespace is intentionally NOT unshared: ``--unshare-net`` makes bwrap
    bring up a loopback interface, which requires privileges not available in many
    container/CI hosts (``bwrap: loopback: Failed RTM_NEWADDR: Operation not
    permitted``) -- and Galaxy is frequently deployed in such environments. Operators
    who can unshare the network, or who want stricter egress control, can add
    ``--unshare-net`` (or enforce egress at the network layer) via a custom command.
    """
    # Bind the Python installation (base + any virtualenv) and the worker script; these
    # cover the interpreter, its standard library, and py_mini_racer's V8 library
    # regardless of whether Galaxy runs from a venv, a system install, or a conda env.
    # sys.executable is often a symlink (a venv, or uv's standalone Python) whose real
    # binary and shared libraries live in a separate tree outside sys.prefix/base_prefix;
    # resolve it and bind that tree too, so the interpreter can be exec'd and loaded
    # inside the jail rather than failing with "execvp ...: No such file or directory".
    real_executable = os.path.realpath(sys.executable)
    real_executable_root = os.path.dirname(os.path.dirname(real_executable))
    ro_binds = [
        sys.base_prefix,
        sys.prefix,
        real_executable,
        real_executable_root,
        WORKER_SCRIPT,
        *BUBBLEWRAP_SYSTEM_PATHS,
    ]
    args = [
        "--unshare-pid",
        "--unshare-ipc",
        "--unshare-uts",
        "--die-with-parent",
        "--new-session",
        "--clearenv",
    ]
    seen: set[str] = set()
    for path in ro_binds:
        if path and path not in seen:
            seen.add(path)
            args += ["--ro-bind-try", path, path]
    # A fresh private tmpfs (not the host /tmp) for anything that needs scratch space;
    # TMPDIR is set explicitly since --clearenv wiped it, so tempfile resolves here.
    args += [
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--tmpfs",
        "/tmp",
        "--setenv",
        "TMPDIR",
        "/tmp",
        "--chdir",
        "/tmp",
    ]
    return (bwrap, *args)


@functools.cache
def resolve_isolation_command(setting: str) -> tuple[str, ...] | None:
    """Resolve the ``expression_evaluation_isolation_command`` setting to a wrapper.

    - empty -> ``None`` (evaluate in-process)
    - ``"bubblewrap"``/``"bwrap"`` -> the built-in bubblewrap command, but only on
      Linux with ``bwrap`` on PATH; otherwise ``None`` (in-process) with a one-time
      warning, so a macOS dev box or a host without bubblewrap degrades cleanly
    - anything else -> the value parsed as a literal command prefix, used as-is

    Cached so the PATH lookup and any warning happen once per distinct setting.
    """
    setting = (setting or "").strip()
    if not setting:
        return None
    if setting.lower() in BUBBLEWRAP_KEYWORDS:
        if platform.system() != "Linux":
            log.warning(
                "Expression isolation %r is only supported on Linux; evaluating expressions in-process.", setting
            )
            return None
        bwrap = shutil.which("bwrap")
        if bwrap is None:
            log.warning(
                "Expression isolation requested but 'bwrap' (bubblewrap) was not found on PATH; "
                "evaluating expressions in-process."
            )
            return None
        return _bubblewrap_command(bwrap)
    return tuple(shlex.split(setting))


def evaluate_program(
    program: str,
    timeout: float = default_timeout,
    sandbox_command: Sequence[str] | None = None,
) -> CWLOutputType:
    """Run a self-contained JS program in a fresh, isolated V8 context.

    ``program`` must yield a JSON string as its final value (i.e. end in
    ``JSON.stringify(...)``) so the result round-trips as JSON, matching the
    contract of the historical Node engine (``json.loads`` of its stdout).

    A new isolate is created per call so state (including prototype pollution) from
    one untrusted expression cannot leak into another. When ``sandbox_command`` is
    given, the evaluation runs in a separate worker process launched under that
    command (e.g. ``bwrap ...``) for defence-in-depth OS-level containment;
    otherwise it runs in-process.
    """
    if sandbox_command:
        return _evaluate_in_subprocess(program, timeout, sandbox_command)
    try:
        return run_program(program, timeout, MEMORY_LIMIT_BYTES)
    except _MR_EXCEPTIONS as e:
        raise JavascriptException(str(e)) from e


def _evaluate_in_subprocess(program: str, timeout: float, sandbox_command: Sequence[str]) -> CWLOutputType:
    argv = [*sandbox_command, sys.executable, WORKER_SCRIPT]
    request = json.dumps({"program": program, "timeout": timeout, "memory_limit": MEMORY_LIMIT_BYTES})
    try:
        proc = subprocess.run(
            argv,
            input=request.encode("utf-8"),
            capture_output=True,
            timeout=timeout + SUBPROCESS_GRACE_SECONDS,
        )
    except FileNotFoundError as e:
        raise JavascriptException(f"Expression isolation command not found: {sandbox_command[0]!r}") from e
    except subprocess.TimeoutExpired as e:
        raise JavascriptException("Expression evaluation timed out in the isolation sandbox") from e
    if proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", "replace").strip()[:500]
        raise JavascriptException(f"Expression isolation worker exited with code {proc.returncode}: {detail}")
    try:
        response = json.loads(proc.stdout.decode("utf-8"))
    except ValueError as e:
        raise JavascriptException(f"Malformed response from expression isolation worker: {proc.stdout!r}") from e
    if "error" in response:
        raise JavascriptException(response["error"])
    return cast(CWLOutputType, response["result"])


class SandboxedJSEngine(NodeJSEngine):
    """A ``cwl_utils`` JS engine backed by an embedded V8 isolate instead of Node.

    Only :meth:`eval` (full JavaScript expressions) is overridden. ``regex_eval``
    (pure-Python CWL parameter-reference resolution, e.g. ``$(inputs.foo)``) is
    inherited unchanged from :class:`NodeJSEngine` and never touches JavaScript.
    """

    def eval(
        self,
        scan: str,
        jslib: str = "",
        timeout: float = default_timeout,
        force_docker_pull: bool = False,
        debug: bool = False,
        js_console: bool = False,
        container_engine: str = "docker",
        sandbox_command: Sequence[str] | None = None,
        **kwargs: Any,
    ) -> CWLOutputType:
        if isinstance(scan, str) and len(scan) > 1 and scan[0] == "{":
            inner = scan
        else:
            inner = f"{{return ({scan});}}"
        program = f'"use strict";\n{jslib}\nJSON.stringify((function(){inner})())'
        return evaluate_program(program, timeout, sandbox_command=sandbox_command)


_registered: bool = False
_lock = threading.Lock()


def register() -> None:
    """Install the sandboxed engine as the process-wide ``cwl_utils`` JS engine.

    Idempotent and thread-safe. Call before any expression is evaluated so no code
    path falls back to the unsafe Node ``vm`` engine.
    """
    global _registered
    with _lock:
        if not _registered:
            set_js_engine(SandboxedJSEngine())
            _registered = True


def build_evaluate_program(new_input: dict[str, Any]) -> str:
    """Assemble the program for the expression-tool (``evaluate``) input contract.

    Mirrors the variable bindings the retired ``cwlNodeEngine.js`` produced
    (``$job``/``$self``/``$runtime``/``$tmpdir``/``$outdir`` plus ``engineConfig``
    lines) so expression tools behave identically, minus the Node ``vm`` sink.
    """
    script = new_input["script"]
    if isinstance(script, str) and len(script) > 0 and script[0] == "{":
        # A ``{...}`` body is a function body: wrap and invoke it.
        exp = "{return function()" + script + "();}"
    elif isinstance(script, str):
        # A bare string is a raw JavaScript expression, inserted verbatim.
        exp = "{return " + script + ";}"
    else:
        # Non-string literals (numbers, bools, null): their JSON form is a valid
        # JS literal, matching the historical engine's ``"{return " + value`` coercion.
        exp = "{return " + json.dumps(script) + ";}"

    lines = ['"use strict";']
    for line in new_input.get("engineConfig") or []:
        lines.append(line)

    def _js_var(name: str, key: str) -> str:
        # JSON.stringify(undefined) rendered as the JS literal `undefined`, as the
        # old engine did for keys absent from the input payload.
        if key not in new_input:
            return f"var {name} = undefined;"
        return f"var {name} = {json.dumps(new_input[key])};"

    lines.append(_js_var("$job", "job"))
    lines.append(_js_var("$self", "context"))
    lines.append(_js_var("$runtime", "runtime"))
    lines.append(_js_var("$tmpdir", "tmpdir"))
    lines.append(_js_var("$outdir", "outdir"))
    lines.append(f"JSON.stringify((function(){exp})())")
    return "\n".join(lines)
