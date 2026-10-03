from typing import Any

import pytest
from gxformat2 import python_to_workflow

from galaxy.managers.workflows import WorkflowContentsManager
from .workflow_support import (
    MockTrans,
    yaml_to_model,
)


@pytest.fixture
def export_context():
    trans = MockTrans()
    trans.app.config.default_workflow_export_format = "format2"
    manager = WorkflowContentsManager(trans.app, trans.app.trs_proxy)
    return trans, manager


def _workflow(trans, duplicate_labels=False, nested=False):
    steps: list[dict[str, Any]] = [
        {
            "type": "data_input",
            "label": f"input_{i}",
            "workflow_outputs": [
                {"output_name": "output", "label": "duplicate" if duplicate_labels else f"output_{i}"}
            ],
        }
        for i in range(2)
    ]
    if nested:
        steps = [{"type": "subworkflow", "subworkflow": {"name": "nested", "steps": steps}}]
    workflow = yaml_to_model({"steps": steps})
    workflow.name = "export test"
    stored = trans.save_workflow(workflow)
    stored.name = workflow.name
    return stored


def test_default_format2_export(export_context):
    trans, manager = export_context
    stored = _workflow(trans)
    exported = manager.workflow_to_dict(trans, stored)
    assert exported["class"] == "GalaxyWorkflow"
    assert exported["version"] == 0
    restored = python_to_workflow(exported, None, None)
    assert restored["name"] == stored.name
    assert {step["label"] for step in restored["steps"].values()} == {"input_0", "input_1"}
    assert {output["label"] for step in restored["steps"].values() for output in step["workflow_outputs"]} == {
        "output_0",
        "output_1",
    }


def test_explicit_native_export(export_context):
    trans, manager = export_context
    stored = _workflow(trans)
    exported = manager.workflow_to_dict(trans, stored, style="ga")
    assert exported["format-version"] == "0.1"
    assert len(exported["steps"]) == 2


def test_explicit_format2_overrides_native_default(export_context):
    trans, manager = export_context
    trans.app.config.default_workflow_export_format = "ga"
    stored = _workflow(trans)
    exported = manager.workflow_to_dict(trans, stored, style="format2")
    assert exported["class"] == "GalaxyWorkflow"


@pytest.mark.parametrize("nested", [False, True])
def test_default_export_preserves_duplicate_labels(export_context, nested):
    trans, manager = export_context
    stored = _workflow(trans, duplicate_labels=True, nested=nested)
    exported = manager.workflow_to_dict(trans, stored)
    assert exported == manager.workflow_to_dict(trans, stored, style="ga")
    assert exported["format-version"] == "0.1"
    if nested:
        exported = exported["steps"][0]["subworkflow"]
    assert [output["label"] for step in exported["steps"].values() for output in step["workflow_outputs"]] == [
        "duplicate",
        "duplicate",
    ]


@pytest.mark.parametrize("style", ["format2", "format2_wrapped_yaml"])
def test_explicit_format2_does_not_fall_back(export_context, style):
    trans, manager = export_context
    stored = _workflow(trans, duplicate_labels=True)
    with pytest.raises(AssertionError):
        manager.workflow_to_dict(trans, stored, style=style)


def test_wrapped_yaml_export(export_context):
    trans, manager = export_context
    exported = manager.workflow_to_dict(trans, _workflow(trans), style="format2_wrapped_yaml")
    assert "class: GalaxyWorkflow" in exported["yaml_content"]
