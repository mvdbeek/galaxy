from typing import Any

import pytest

from galaxy.tool_util_models import (
    lift_user_tool_source,
    UserToolSource,
    YamlToolSource,
)
from galaxy.tool_util_models.user_tool_labels import MAX_LABEL_LENGTH

TOOL = {
    "class": "GalaxyUserTool",
    "id": "label_tool",
    "name": "Label tool",
    "version": "1.0.0",
    "container": "busybox",
    "shell_command": "cat '$(inputs.input.path)' > out.txt",
    "inputs": [
        {"type": "data", "name": "input", "format": "txt"},
        {"type": "integer", "name": "n", "value": 1},
    ],
}


def _tool(label: str, **output: Any) -> dict[str, Any]:
    return {**TOOL, "outputs": [{"type": "data", "name": "out", "from_work_dir": "out.txt", "label": label, **output}]}


def test_admin_yaml_tool_labels_not_restricted():
    representation = {**_tool("${tool.name} on ${on_string}"), "class": "GalaxyTool"}
    representation.pop("container")
    YamlToolSource(**representation)


def test_lift_keeps_valid_label():
    status, tool, changed = lift_user_tool_source(_tool("$(inputs.input.name) n=$(inputs.n)"))
    assert (status, changed) == ("ok", [])
    assert isinstance(tool, UserToolSource)


@pytest.mark.parametrize(
    "stored,lifted",
    [
        (
            "${on_string} $(inputs.input.name) $(inputs.missing) $(1 + 1)",
            "\\${on_string} $(inputs.input.name) \\$(inputs.missing) \\$(1 + 1)",
        ),
        ("x" * (MAX_LABEL_LENGTH + 10), "x" * MAX_LABEL_LENGTH),
    ],
)
def test_lift_rewrites_rejected_labels(stored, lifted):
    status, tool, changed = lift_user_tool_source(_tool(stored))
    assert (status, changed) == ("lifted", ["outputs.0.label"])
    assert isinstance(tool, UserToolSource)
    assert tool.outputs[0].label == lifted


def test_lift_escapes_label_hidden_behind_extra_field():
    status, tool, changed = lift_user_tool_source(_tool("${on_string}", stale_field=True))
    assert status == "lifted"
    assert sorted(changed) == ["outputs.0.label", "outputs.0.stale_field"]
    assert isinstance(tool, UserToolSource)
    assert tool.outputs[0].label == "\\${on_string}"


def test_lift_leaves_other_errors_invalid():
    status, _, errors = lift_user_tool_source({**_tool("${on_string}"), "version": None})
    assert status == "invalid"
    assert errors
