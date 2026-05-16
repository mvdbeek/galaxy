from types import SimpleNamespace

from galaxy.tools.template_dispatch import (
    evaluate_tool_template,
    project_wrapped_params_to_cwl_inputs,
)


def test_no_tool_uses_cheetah():
    # `$x` is Cheetah substitution; `do_eval` would not recognise it.
    result = evaluate_tool_template(None, "$x", {"x": "foo"})
    assert result == "foo"


def test_galaxy_tool_uses_cheetah():
    tool = SimpleNamespace(tool_format="GalaxyTool")
    result = evaluate_tool_template(tool, "$x", {"x": "foo"})
    assert result == "foo"


def test_galaxy_user_tool_uses_do_eval():
    tool = SimpleNamespace(tool_format="GalaxyUserTool")
    result = evaluate_tool_template(
        tool,
        "$(inputs.sample_name)",
        cwl_inputs={"sample_name": "abc"},
    )
    assert result == "abc"


def test_galaxy_user_tool_template_string_substitution():
    tool = SimpleNamespace(tool_format="GalaxyUserTool")
    result = evaluate_tool_template(
        tool,
        "result for $(inputs.sample_name)",
        cwl_inputs={"sample_name": "foo"},
    )
    assert result == "result for foo"


def test_galaxy_user_tool_literal_string_passes_through():
    # Plain text (no $(...) parameter reference and no ${...} JS block) is
    # returned unchanged by do_eval.
    tool = SimpleNamespace(tool_format="GalaxyUserTool")
    result = evaluate_tool_template(
        tool,
        "plain literal text",
        cwl_inputs={"sample_name": "abc"},
    )
    assert result == "plain literal text"


def test_project_wrapped_params_filters_internal_and_coerces():
    class _Wrapper:
        def __init__(self, v):
            self._v = v

        def __str__(self):
            return self._v

    out = project_wrapped_params_to_cwl_inputs(
        {
            "sample_name": _Wrapper("foo"),
            "__user__": _Wrapper("internal"),
            "n": _Wrapper("42"),
        }
    )
    assert out == {"sample_name": "foo", "n": "42"}
