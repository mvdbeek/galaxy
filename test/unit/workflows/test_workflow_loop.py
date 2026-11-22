from typing import Any

import pytest

from galaxy import model
from galaxy.exceptions import (
    ConfigDoesNotAllowException,
    RequestParameterInvalidException,
)
from galaxy.schema.invocation import FailureReason
from galaxy.tools.parameters.workflow_utils import NO_REPLACEMENT
from galaxy.workflow import modules
from galaxy.workflow.loop import (
    check_feedback,
    copy_invocation_request,
    iteration_outputs,
    next_iteration_inputs,
    parse_loop,
    validate_loop_request,
    validate_workflow_loops,
    WorkflowLoop,
)
from .workflow_support import (
    expression_json_hda,
    yaml_to_model,
)

ADD_ONE_BODY = """
steps:
  - type: parameter_input
    label: i1
    tool_inputs: {parameter_type: integer, optional: false}
  - type: parameter_input
    label: i2
    tool_inputs: {parameter_type: integer, optional: false}
  - type: tool
    tool_id: expression_add_int
    workflow_outputs:
      - {output_name: sum, label: o1}
"""


def loop_step_yaml(
    loop: dict[str, Any] | None = None,
    when: str | None = "$(inputs.i1 < 10)",
    body: str = ADD_ONE_BODY,
    input_type: str = "parameter_input",
    input_tool_inputs: dict[str, Any] | None = None,
) -> dict[str, Any]:
    loop = loop if loop is not None else {"inputs": {"i1": {"output_source": "o1"}}}
    return {
        "steps": [
            {"type": input_type, "label": "i1", "tool_inputs": input_tool_inputs or {"parameter_type": "integer"}},
            {
                "type": "subworkflow",
                "label": "loop",
                "loop": loop,
                "when_expression": when,
                "subworkflow": body,
                "inputs": {
                    "i1": {"connections": [{"@output_step": 0, "output_name": "output", "@input_subworkflow_step": 0}]}
                },
            },
        ]
    }


def assert_refused(workflow: model.Workflow, message: str, enabled: bool = True) -> None:
    with pytest.raises(RequestParameterInvalidException) as exc_info:
        validate_workflow_loops(workflow, enabled)
    assert message in str(exc_info.value)


def test_valid_loop():
    validate_workflow_loops(yaml_to_model(loop_step_yaml()), True)


def test_workflow_without_loop_does_not_need_the_feature():
    workflow = yaml_to_model(loop_step_yaml())
    workflow.steps[1].loop = None
    validate_workflow_loops(workflow, False)


def test_loop_refused_when_feature_is_off():
    with pytest.raises(ConfigDoesNotAllowException) as exc_info:
        validate_workflow_loops(yaml_to_model(loop_step_yaml()), False)
    assert "workflow loops are not enabled" in str(exc_info.value)


def test_loop_step_input_default_refused():
    workflow = yaml_to_model(loop_step_yaml())
    step_input = workflow.steps[1].inputs[0]
    step_input.default_value = 5
    step_input.default_value_set = True
    assert_refused(workflow, "a default or value_from on input 'i1' of a loop step is not supported yet")


def test_loop_step_input_value_from_refused():
    workflow = yaml_to_model(loop_step_yaml())
    workflow.steps[1].inputs[0].value_from = "$(inputs.i1 + 1)"
    assert_refused(workflow, "a default or value_from on input 'i1' of a loop step is not supported yet")


def test_loop_needs_when():
    assert_refused(yaml_to_model(loop_step_yaml(when=None)), "needs a 'when' expression")


def test_loop_when_must_use_connected_inputs():
    assert_refused(yaml_to_model(loop_step_yaml(when="$(inputs.i2 < 10)")), "uses input 'i2', which is not connected")
    assert_refused(
        yaml_to_model(loop_step_yaml(when='$(inputs["i2"] < 10)')), "uses input 'i2', which is not connected"
    )


def test_loop_only_on_subworkflow_step():
    workflow = yaml_to_model(loop_step_yaml())
    tool_step = workflow.steps[1].subworkflow.steps[2]
    tool_step.loop = {"inputs": {"a": {"output_source": "sum"}}}
    tool_step.when_expression = "$(true)"
    assert_refused(workflow, "a loop is only allowed on a subworkflow step")


def test_loop_input_must_be_a_subworkflow_input():
    workflow = yaml_to_model(loop_step_yaml(loop={"inputs": {"missing": {"output_source": "o1"}}}))
    assert_refused(workflow, "loop input 'missing' is not an input of the subworkflow")


def test_loop_output_source_must_be_a_subworkflow_output():
    workflow = yaml_to_model(loop_step_yaml(loop={"inputs": {"i1": {"output_source": "missing"}}}))
    assert_refused(workflow, "loop output_source 'missing' is not an output of the subworkflow")


def test_loop_all_iterations_not_supported_yet():
    loop = {"inputs": {"i1": {"output_source": "o1"}}, "output_method": "all_iterations"}
    assert_refused(yaml_to_model(loop_step_yaml(loop=loop)), "'all_iterations' is not supported yet")


def test_loop_needs_feedback():
    assert_refused(yaml_to_model(loop_step_yaml(loop={"inputs": {}})), "Invalid loop definition")


def test_loop_unknown_key_refused():
    with pytest.raises(RequestParameterInvalidException):
        parse_loop({"inputs": {"i1": {"output_source": "o1", "pick_value": "first_non_null"}}})


def test_loop_input_needs_a_value():
    with pytest.raises(RequestParameterInvalidException) as exc_info:
        parse_loop({"inputs": {"i1": {}}})
    assert "needs output_source, default or value_from" in str(exc_info.value)


def test_loop_value_from_without_output_source():
    validate_workflow_loops(
        yaml_to_model(loop_step_yaml(loop={"inputs": {"i1": {"value_from": "$(inputs.i1 + 1)"}}})), True
    )


def test_loop_value_from_must_use_connected_inputs():
    # The first value_from sees the first iteration's inputs, which hold only connected inputs.
    for value_from in ("$(inputs.i2 + 1)", '$(inputs["i2"])'):
        loop = {"inputs": {"i1": {"value_from": value_from}}}
        assert_refused(
            yaml_to_model(loop_step_yaml(loop=loop)),
            "the value_from of loop input 'i1' uses input 'i2', which is not connected",
        )


def test_loop_value_from_of_unconnected_input_may_not_read_itself():
    loop = {"inputs": {"i2": {"value_from": "$(inputs.i2 + 1)"}, "i1": {"output_source": "o1"}}}
    assert_refused(
        yaml_to_model(loop_step_yaml(loop=loop)),
        "the value_from of loop input 'i2' uses input 'i2', which is not connected",
    )


def test_loop_value_from_must_parse():
    workflow = yaml_to_model(loop_step_yaml(loop={"inputs": {"i1": {"value_from": "$(inputs.i1 + 1"}}}))
    assert_refused(workflow, "loop input 'i1'")


def test_loop_default_must_match_parameter_type():
    for default in (5, -1):
        loop = {"inputs": {"i1": {"output_source": "o1", "default": default}}}
        validate_workflow_loops(yaml_to_model(loop_step_yaml(loop=loop)), True)
    wrong_defaults: list[Any] = ["five", 1.5, True]
    for wrong_default in wrong_defaults:
        loop = {"inputs": {"i1": {"output_source": "o1", "default": wrong_default}}}
        assert_refused(yaml_to_model(loop_step_yaml(loop=loop)), "of loop input 'i1' is not a valid integer value")


def test_loop_default_for_dataset_input_refused():
    loop = {"inputs": {"i1": {"output_source": "o1", "default": 5}}}
    workflow = yaml_to_model(loop_step_yaml(loop=loop, body=COLLECTION_BODY))
    assert_refused(workflow, "a default for loop input 'i1', a dataset or collection input, is not supported")


def test_map_over_loop_step_refused():
    workflow = yaml_to_model(
        loop_step_yaml(input_type="data_collection_input", input_tool_inputs={"collection_type": "list"})
    )
    assert_refused(workflow, "mapping over a loop step is not supported")


def test_map_over_subworkflow_containing_loop_refused():
    inner = loop_step_yaml()
    workflow = yaml_to_model(
        {
            "steps": [
                {"type": "data_collection_input", "label": "i1", "tool_inputs": {"collection_type": "list"}},
                {
                    "type": "subworkflow",
                    "label": "outer",
                    "subworkflow": inner,
                    "inputs": {
                        "i1": {
                            "connections": [{"@output_step": 0, "output_name": "output", "@input_subworkflow_step": 0}]
                        }
                    },
                },
            ]
        }
    )
    assert_refused(workflow, "mapping over a subworkflow that contains a loop is not supported")


def nested_loops(depth: int) -> dict[str, Any]:
    body: Any = ADD_ONE_BODY
    for _ in range(depth):
        body = loop_step_yaml(body=body)
        # The loop's output, so that an outer loop can feed it back.
        body["steps"][1]["workflow_outputs"] = [{"output_name": "o1", "label": "o1"}]
    return body


def test_loop_nesting_depth():
    validate_workflow_loops(yaml_to_model(nested_loops(4)), True)
    assert_refused(yaml_to_model(nested_loops(5)), "nested at most 4 deep")


def test_copy_invocation_request_restarts_inner_loop():
    workflow = yaml_to_model(nested_loops(2))
    outer_step = workflow.steps[1]
    inner_step = outer_step.subworkflow.steps[1]
    template = model.WorkflowInvocation()
    template.history = model.History()
    template.workflow = outer_step.subworkflow
    template.input_parameters = [model.WorkflowRequestInputParameter(name="use_cached_job", value="false", type="meta")]
    template.step_states = [model.WorkflowRequestStepState(workflow_step=inner_step, value={"a": 1})]
    for iteration in range(3):
        inner_invocation = model.WorkflowInvocation()
        inner_invocation.workflow_id = 7 + iteration
        template.attach_subworkflow_invocation_for_step(inner_step, inner_invocation).iteration = iteration

    copy = copy_invocation_request(template)

    assert copy.state == model.WorkflowInvocation.states.NEW
    assert copy.uuid != template.uuid
    assert copy.history is template.history
    assert copy.workflow is template.workflow
    assert [(p.name, p.value, p.type) for p in copy.input_parameters] == [("use_cached_job", "false", "meta")]
    assert copy.step_states[0].workflow_step is inner_step
    assert copy.step_states[0].value == {"a": 1}
    assert copy.step_states[0].value is not template.step_states[0].value
    # Only the first iteration of the inner loop is copied, so the inner loop starts again.
    assert [association.iteration for association in copy.subworkflow_invocations] == [0]
    inner_copy = copy.subworkflow_invocations[0].subworkflow_invocation
    assert inner_copy is not template.subworkflow_invocations[0].subworkflow_invocation
    assert inner_copy.state == model.WorkflowInvocation.states.NEW


COLLECTION_BODY = """
steps:
  - type: data_collection_input
    label: i1
    tool_inputs: {collection_type: list}
  - type: tool
    tool_id: __SORTLIST__
    workflow_outputs:
      - {output_name: output, label: o1}
"""


def _list(identifiers: list[str]) -> model.HistoryDatasetCollectionAssociation:
    collection = model.DatasetCollection(collection_type="list")
    for identifier in identifiers:
        hda = model.HistoryDatasetAssociation(create_dataset=True, flush=False)
        model.DatasetCollectionElement(collection=collection, element=hda, element_identifier=identifier)
    return model.HistoryDatasetCollectionAssociation(collection=collection)


def _loop_step(body: str = ADD_ONE_BODY, loop: dict[str, Any] | None = None) -> tuple[model.WorkflowStep, WorkflowLoop]:
    step = yaml_to_model(loop_step_yaml(body=body, loop=loop)).steps[1]
    return step, parse_loop(step.loop)


def _no_value_from(expression: str, inputs: dict[str, Any], value: Any) -> Any:
    raise AssertionError("no value_from in this loop")


def _next_inputs(
    rule: dict[str, Any], previous_inputs: dict[str, Any], previous_outputs: dict[str, Any], evaluate=_no_value_from
):
    step, loop = _loop_step(loop={"inputs": {"i1": rule}})
    return next_iteration_inputs(step, loop, previous_inputs, previous_outputs, evaluate)


def test_next_iteration_inputs_feed_back_looped_inputs_only():
    assert _next_inputs({"output_source": "o1"}, {"i1": 1, "i2": 5}, {"o1": 2}) == {"i1": 2, "i2": 5}


def test_next_iteration_inputs_pass_skipped_output_on():
    assert _next_inputs({"output_source": "o1"}, {"i1": 1}, {"o1": NO_REPLACEMENT})["i1"] is NO_REPLACEMENT


def test_next_iteration_inputs_missing_output_fails():
    with pytest.raises(modules.FailWorkflowEvaluation) as exc_info:
        _next_inputs({"output_source": "o1"}, {"i1": 1}, {})
    assert exc_info.value.why.reason == FailureReason.output_not_found


def test_default_replaces_null_or_skipped_feedback(tmp_path):
    skipped = expression_json_hda(tmp_path / "skipped.json", "null")
    for fed_back in (None, NO_REPLACEMENT, skipped):
        assert _next_inputs({"output_source": "o1", "default": 5}, {"i1": 1}, {"o1": fed_back})["i1"] == 5
    assert _next_inputs({"output_source": "o1", "default": 5}, {"i1": 1}, {"o1": 0})["i1"] == 0


def test_value_from_sees_previous_inputs_and_value_after_default():
    calls = []

    def evaluate(expression: str, inputs: dict[str, Any], value: Any) -> Any:
        calls.append((expression, inputs, value))
        return 42

    rule = {"output_source": "o1", "default": 5, "value_from": "$(self + inputs.i1)"}
    assert _next_inputs(rule, {"i1": 1, "i2": 7}, {"o1": None}, evaluate)["i1"] == 42
    # CWL v1.3 LoopInput: default first, then valueFrom with self and the previous iteration's inputs.
    assert calls == [("$(self + inputs.i1)", {"i1": 1, "i2": 7}, 5)]


def test_value_from_without_output_source_gets_null_self():
    calls = []

    def evaluate(expression: str, inputs: dict[str, Any], value: Any) -> Any:
        calls.append(value)
        return 2

    assert _next_inputs({"value_from": "$(inputs.i1 + 1)"}, {"i1": 1}, {}, evaluate)["i1"] == 2
    assert calls == [None]


def test_iteration_outputs_read_recorded_outputs():
    step, _ = _loop_step()
    assert step.subworkflow
    workflow_output = step.subworkflow.steps[2].workflow_outputs[0]
    iteration = model.WorkflowInvocation()
    iteration.add_output(workflow_output, workflow_output.workflow_step, {"__class__": "NoReplacement"})
    assert iteration_outputs(iteration) == {"o1": NO_REPLACEMENT}


def _feedback_failure(first: Any, fed_back: Any) -> str:
    step, loop = _loop_step(COLLECTION_BODY)
    with pytest.raises(modules.FailWorkflowEvaluation) as exc_info:
        check_feedback(step, loop, {"i1": first}, {"i1": fed_back})
    assert exc_info.value.why.reason == FailureReason.loop_failed
    return exc_info.value.why.model_dump()["details"]


def test_fed_back_collection_keeps_identifiers_and_order():
    step, loop = _loop_step(COLLECTION_BODY)
    check_feedback(step, loop, {"i1": _list(["a", "b"])}, {"i1": _list(["a", "b"])})
    message = "Loop input 'i1' must keep its collection type, element identifiers and their order."
    assert _feedback_failure(_list(["a", "b"]), _list(["b", "a"])) == message
    assert _feedback_failure(_list(["a", "b"]), _list(["a", "c"])) == message
    assert _feedback_failure(_list(["a", "b"]), _list(["a"])) == message


def test_fed_back_collection_must_stay_a_collection():
    hda = model.HistoryDatasetAssociation(create_dataset=True, flush=False)
    assert _feedback_failure(_list(["a"]), hda) == "Loop input 'i1' takes a dataset collection, output 'o1' is not one."


def test_fed_back_dataset_must_not_become_a_collection():
    step, loop = _loop_step()
    with pytest.raises(modules.FailWorkflowEvaluation) as exc_info:
        check_feedback(step, loop, {"i1": 1}, {"i1": _list(["a"])})
    assert exc_info.value.why.model_dump()["details"] == (
        "Loop input 'i1' does not take a dataset collection, output 'o1' is one."
    )


def test_skipped_feedback_is_not_checked():
    step, loop = _loop_step(COLLECTION_BODY)
    check_feedback(step, loop, {"i1": _list(["a"])}, {"i1": NO_REPLACEMENT})


def test_run_request_refuses_collection_mapping_over_loop_step():
    # The connected input expects a list, as does the loop body, so the workflow saves.
    workflow = yaml_to_model(
        loop_step_yaml(
            body=COLLECTION_BODY, input_type="data_collection_input", input_tool_inputs={"collection_type": "list"}
        )
    )
    validate_workflow_loops(workflow, True)
    nested = model.DatasetCollection(collection_type="list:list")
    model.DatasetCollectionElement(collection=nested, element=_list(["a"]).collection, element_identifier="outer")
    input_step = workflow.steps[0]
    with pytest.raises(RequestParameterInvalidException) as exc_info:
        validate_loop_request(workflow, {input_step.id: model.HistoryDatasetCollectionAssociation(collection=nested)})
    assert "mapping over a loop step is not supported" in str(exc_info.value)
    validate_loop_request(workflow, {input_step.id: _list(["a"])})
