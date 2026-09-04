import os
import platform
import shutil
import subprocess
import sys

import pytest
from cwl_utils.errors import (
    JavascriptException,
    WorkflowException,
)

from galaxy.tools.expressions import (
    do_eval,
    evaluate,
)
from galaxy.tools.expressions.js_engine import (
    _bubblewrap_command,
    evaluate_program,
    resolve_isolation_command,
    SandboxedJSEngine,
)

# A benign stand-in for a real jail command (e.g. bwrap): `/usr/bin/env` just execs
# the worker argv appended after it, exercising the out-of-process plumbing without
# needing bubblewrap installed.
_PASSTHROUGH_SANDBOX = ["/usr/bin/env"]
_needs_env = pytest.mark.skipif(
    not os.path.exists("/usr/bin/env"), reason="requires /usr/bin/env for the out-of-process worker test"
)


def _bwrap_can_sandbox() -> bool:
    # bubblewrap must be installed AND actually able to set up its sandbox here.
    # Namespace creation, uid-map setup, and exec inside the jail can all be blocked
    # on locked-down hosts and CI runners; a plain "is bwrap on PATH" check is not
    # enough. Probe the real recipe by running the interpreter on an empty program.
    command = resolve_isolation_command("bubblewrap")
    if not command:
        return False
    try:
        proc = subprocess.run([*command, sys.executable, "-c", ""], capture_output=True, timeout=15)
    except (OSError, subprocess.SubprocessError):
        return False
    return proc.returncode == 0


_needs_bwrap = pytest.mark.skipif(
    not _bwrap_can_sandbox(),
    reason="bubblewrap not installed or cannot set up a sandbox in this environment",
)


def test_evaluate():
    # Expression-tool script path: a `{...}` body is treated as a function body.
    assert evaluate(None, {"script": "{return 5;}"}) == 5
    assert evaluate(None, {"script": "{return {out1: 1 + 2, out2: 'x'};}"}) == {"out1": 3, "out2": "x"}
    assert evaluate(None, {"script": "{return $job.a + 1;}", "job": {"a": 41}}) == 42
    # A bare (non-`{...}`) script is a raw JavaScript expression.
    assert evaluate(None, {"script": "$job.a + 1", "job": {"a": 41}}) == 42


def test_do_eval_parameter_reference():
    # Bare parameter references resolve in pure Python and never touch JavaScript.
    assert do_eval("$(inputs.should_run)", {"should_run": True}) is True
    assert do_eval("$(inputs.nested.value)", {"nested": {"value": 7}}) == 7


def test_do_eval_javascript_expression():
    # Expression-bearing `$(...)` and `${...}` bodies are evaluated as JavaScript.
    assert do_eval('$(inputs.format != "bwa_mem2_index")', {"format": "bwa_mem2_index"}) is False
    assert do_eval('$(inputs.format != "bwa_mem2_index")', {"format": "other"}) is True
    assert do_eval("${ return 1 + 1 > 1; }", {}) is True


@pytest.mark.parametrize(
    "payload",
    [
        # The published exploit gadgets: reach the host Function constructor and try
        # to get at Node's `process`/`require('child_process')`. In the embedded V8
        # isolate there is no `process`, so each either fails closed or yields nothing.
        "${ return globalThis.constructor.constructor(\"return process.mainModule.require('child_process').execSync('id')\")(); }",
        "${ return globalThis.constructor.constructor(\"return process\")().getBuiltinModule('child_process'); }",
    ],
)
def test_do_eval_sandbox_blocks_process_escape(payload):
    with pytest.raises((JavascriptException, WorkflowException)):
        do_eval(payload, {})


def test_do_eval_process_is_undefined():
    # The escape's own fingerprint: `typeof process` is "undefined" in the isolate,
    # so the Function constructor is reachable but has nothing dangerous to return.
    result = do_eval(
        '${ return String(globalThis.constructor.constructor("return typeof process")()); }',
        {},
    )
    assert result == "undefined"


def test_sandbox_engine_timeout():
    # A runaway expression is killed rather than hanging the scheduler.
    engine = SandboxedJSEngine()
    with pytest.raises(JavascriptException):
        engine.eval("{while (true) {}}", timeout=1)


@_needs_env
def test_out_of_process_evaluation():
    # With a sandbox command set, evaluation runs in a separate worker process.
    program = '"use strict";\nJSON.stringify((function(){return 1 + 2;})())'
    assert evaluate_program(program, sandbox_command=_PASSTHROUGH_SANDBOX) == 3


@_needs_env
def test_out_of_process_do_eval_and_escape():
    # The sandbox_command flows through cwl_utils to the worker, and the escape
    # remains blocked out-of-process too.
    assert do_eval("${ return 6 * 7; }", {}, sandbox_command=_PASSTHROUGH_SANDBOX) == 42
    with pytest.raises((JavascriptException, WorkflowException)):
        do_eval(
            '${ return globalThis.constructor.constructor("return process")(); }',
            {},
            sandbox_command=_PASSTHROUGH_SANDBOX,
        )


def test_missing_sandbox_command_raises():
    program = '"use strict";\nJSON.stringify((function(){return 1;})())'
    with pytest.raises(JavascriptException):
        evaluate_program(program, sandbox_command=["/nonexistent/jail/binary"])


def test_resolve_isolation_none():
    assert resolve_isolation_command("") is None
    assert resolve_isolation_command("   ") is None


def test_resolve_isolation_custom_command():
    assert resolve_isolation_command("/usr/bin/env --unset=FOO") == ("/usr/bin/env", "--unset=FOO")


def test_resolve_isolation_bubblewrap_matches_environment():
    # No mocking: resolve against the real host. On Linux with bwrap installed the
    # keyword yields a real bwrap command; anywhere else it degrades to in-process.
    resolved = resolve_isolation_command("bubblewrap")
    if resolved is None:
        assert platform.system() != "Linux" or shutil.which("bwrap") is None
    else:
        assert resolved[0].endswith("bwrap")
        assert "--unshare-pid" in resolved
        assert "--ro-bind-try" in resolved


def test_bubblewrap_command_minimal_binds():
    # The built-in jail mounts only what the worker needs -- the Python runtime, the
    # worker script and system libs -- and never the whole root filesystem.
    argv = _bubblewrap_command("/usr/bin/bwrap")
    assert argv[0] == "/usr/bin/bwrap"
    for flag in ("--unshare-pid", "--clearenv", "--proc", "--tmpfs"):
        assert flag in argv
    # The Python prefix is bound so the interpreter and py_mini_racer are available.
    assert sys.prefix in argv
    # Crucially, the root filesystem is NOT bound.
    pairs = list(zip(argv, argv[1:], argv[2:]))
    assert ("--ro-bind", "/", "/") not in pairs
    assert ("--ro-bind-try", "/", "/") not in pairs


@_needs_bwrap
def test_bubblewrap_real_execution():
    # Real bubblewrap: the built-in jail actually runs, its minimal bind set is
    # sufficient for the worker, expressions evaluate correctly, and the escape stays
    # blocked inside the jail. Skipped unless Linux with bwrap installed.
    sandbox = resolve_isolation_command("bubblewrap")
    assert sandbox is not None
    ok = '"use strict";\nJSON.stringify((function(){return 6 * 7;})())'
    assert evaluate_program(ok, sandbox_command=sandbox) == 42
    escape = (
        '"use strict";\n'
        'JSON.stringify((function(){return String(globalThis.constructor.constructor("return typeof process")());})())'
    )
    assert evaluate_program(escape, sandbox_command=sandbox) == "undefined"
