from collections.abc import Sequence
from typing import (
    Optional,
)

from cwl_utils.expression import do_eval as _do_eval
from cwl_utils.types import (
    CWLObjectType,
    CWLOutputType,
)

from galaxy.tool_util_models.tool_source import JavascriptRequirement
from .js_engine import (
    build_evaluate_program,
    evaluate_program,
    register,
)


def do_eval(
    expression: str,
    jobinput: CWLObjectType,
    javascript_requirements: list[JavascriptRequirement] | None = None,
    outdir: str | None = None,
    tmpdir: str | None = None,
    context: Optional["CWLOutputType"] = None,
    sandbox_command: Sequence[str] | None = None,
):
    # Ensure every cwl_utils expression evaluation runs in the sandboxed V8 isolate
    # rather than the Node ``vm`` engine (which is not a security boundary).
    # ``sandbox_command``, when set, additionally runs each evaluation in a jailed
    # worker process (e.g. under bubblewrap) for OS-level containment.
    register()
    requirements: list[CWLObjectType] = []
    if javascript_requirements:
        for req in javascript_requirements:
            if expression_lib := req.expression_lib:
                requirements.append({"class": "InlineJavascriptRequirement", "expressionLib": expression_lib})  # type: ignore[dict-item] # very strange, a list[str] literal works
            else:
                requirements.append({"class": "InlineJavascriptRequirement"})
    else:
        requirements = [{"class": "InlineJavascriptRequirement"}]
    return _do_eval(
        expression,
        jobinput,
        requirements,
        None,
        None,
        {},
        context=context,
        cwlVersion="v1.2.1",
        sandbox_command=sandbox_command,
    )


def evaluate(config, input):
    # ``config`` is retained for backwards compatibility but is no longer used: the
    # expression runs in an embedded V8 isolate, not an external node process.
    register()

    default_context = {
        "engineConfig": [],
        "job": {},
        "context": None,
        "outdir": None,
        "tmpdir": None,
    }

    new_input = default_context
    new_input.update(input)

    program = build_evaluate_program(new_input)
    return evaluate_program(program)
