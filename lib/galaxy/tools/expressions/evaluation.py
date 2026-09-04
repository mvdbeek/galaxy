from typing import MutableMapping

from cwl_utils.expression import do_eval as _do_eval

from .js_engine import (
    build_evaluate_program,
    evaluate_program,
    register,
)


def do_eval(expression: str, context: MutableMapping):
    # Ensure every cwl_utils expression evaluation runs in the sandboxed V8 isolate
    # rather than the Node ``vm`` engine (which is not a security boundary).
    register()
    return _do_eval(
        expression,
        context,
        [{"class": "InlineJavascriptRequirement"}],
        None,
        None,
        {},
        cwlVersion="v1.2.1",
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

    return evaluate_program(build_evaluate_program(new_input))
