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

import json
import threading
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
    MiniRacer,
)

# Upper bound on the V8 heap for a single evaluation. A hostile expression can still
# spin the CPU until the timeout fires, but it cannot exhaust control-plane memory.
MEMORY_LIMIT_BYTES = 200 * 1024 * 1024

_MR_EXCEPTIONS = (JSEvalException, JSParseException, JSTimeoutException, JSOOMException)


def evaluate_program(program: str, timeout: float = default_timeout) -> CWLOutputType:
    """Run a self-contained JS program in a fresh, isolated V8 context.

    ``program`` must yield a JSON string as its final value (i.e. end in
    ``JSON.stringify(...)``) so the result round-trips as JSON, matching the
    contract of the historical Node engine (``json.loads`` of its stdout). A new
    isolate is created per call so state (including prototype pollution) from one
    untrusted expression cannot leak into another.
    """
    ctx = MiniRacer()
    ctx.set_hard_memory_limit(MEMORY_LIMIT_BYTES)
    try:
        raw = ctx.eval(program, timeout_sec=timeout)
    except _MR_EXCEPTIONS as e:
        raise JavascriptException(str(e)) from e
    finally:
        ctx.close()
    if not isinstance(raw, (str, bytes, bytearray)):
        # JSON.stringify(undefined) yields JS ``undefined``; treat any non-string
        # result as null.
        return cast(CWLOutputType, None)
    return json.loads(raw)


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
        **kwargs: Any,
    ) -> CWLOutputType:
        if isinstance(scan, str) and len(scan) > 1 and scan[0] == "{":
            inner = scan
        else:
            inner = f"{{return ({scan});}}"
        program = f'"use strict";\n{jslib}\nJSON.stringify((function(){inner})())'
        return evaluate_program(program, timeout)


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
        # Non-string literals: their JSON form is a valid JS literal.
        exp = "{return " + json.dumps(script) + ";}"

    lines = ['"use strict";']
    for line in new_input.get("engineConfig") or []:
        lines.append(line)

    def _js_var(name: str, key: str) -> str:
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
