import pytest
from cwl_utils.errors import (
    JavascriptException,
    WorkflowException,
)

from galaxy.tools.expressions import (
    do_eval,
    evaluate,
)


def test_evaluate():
    # Expression-tool script path: a `{...}` body is treated as a function body.
    assert evaluate(None, {"script": "{return 5;}"}) == 5


def test_do_eval_parameter_reference():
    # Bare parameter references resolve in pure Python and never touch JavaScript.
    assert do_eval("$(inputs.should_run)", {"should_run": True}) is True


def test_do_eval_javascript_expression():
    # A `${...}` body is evaluated as JavaScript in the embedded V8 isolate.
    assert do_eval("${ return 1 + 1 > 1; }", {}) is True


@pytest.mark.parametrize(
    "payload",
    [
        # The published exploit gadgets: reach the host Function constructor and try
        # to get at Node's `process`/`require('child_process')`. In the embedded V8
        # isolate there is no `process`, so each fails closed.
        "${ return globalThis.constructor.constructor(\"return process.mainModule.require('child_process').execSync('id')\")(); }",
        "${ return globalThis.constructor.constructor(\"return process\")().getBuiltinModule('child_process'); }",
    ],
)
def test_do_eval_sandbox_blocks_process_escape(payload):
    with pytest.raises((JavascriptException, WorkflowException)):
        do_eval(payload, {})


def test_do_eval_process_is_undefined():
    # The escape's own fingerprint: `typeof process` is "undefined" in the isolate.
    result = do_eval(
        '${ return String(globalThis.constructor.constructor("return typeof process")()); }',
        {},
    )
    assert result == "undefined"
