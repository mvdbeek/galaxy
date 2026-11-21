"""Workflow loops: a subworkflow step that runs its subworkflow once per iteration.

The step's ``when`` expression is evaluated before every iteration on the input object of the
iteration about to run. Inputs named in the loop take the output of the previous iteration that
their rule names, all other inputs keep the value they had in the first iteration. Each iteration
is a child invocation, registered with its ``iteration`` number and ``loop_outcome``. The
scheduler side is ``WorkflowProgress.execute_loop`` in ``galaxy.workflow.run``.
"""

import re
from copy import deepcopy
from enum import StrEnum
from typing import (
    Any,
    TYPE_CHECKING,
)
from uuid import uuid4

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
)
from sqlalchemy import (
    func,
    select,
    union_all,
)

from galaxy import model
from galaxy.exceptions import (
    ConfigDoesNotAllowException,
    RequestParameterInvalidException,
)
from galaxy.model.base import ensure_object_added_to_session
from galaxy.schema.invocation import (
    FailureReason,
    InvocationFailureLoopFailed,
    InvocationFailureOutputNotFound,
    InvocationUnexpectedFailure,
    LoopOutcome,
)
from galaxy.tools.parameters.workflow_utils import NO_REPLACEMENT
from galaxy.workflow.modules import (
    FailWorkflowEvaluation,
    workflow_step_name,
)

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from galaxy.model import (
        Workflow,
        WorkflowStep,
    )

MAX_LOOP_NESTING_DEPTH = 4
# ``inputs.name`` or ``inputs["name"]`` in a ``when`` expression.
WHEN_INPUT_REFERENCE = re.compile(r"""inputs(?:\.([A-Za-z_]\w*)|\[\s*["']([^"']+)["']\s*\])""")


class LoopInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    output_source: str = Field(description="Label of the subworkflow output fed back into this input.")


class LoopOutputMethod(StrEnum):
    last_iteration = "last_iteration"
    all_iterations = "all_iterations"


class WorkflowLoop(BaseModel):
    model_config = ConfigDict(extra="forbid")

    inputs: dict[str, LoopInput] = Field(min_length=1)
    output_method: LoopOutputMethod = LoopOutputMethod.last_iteration


def parse_loop(value: Any) -> WorkflowLoop:
    try:
        return WorkflowLoop.model_validate(value)
    except ValidationError as e:
        raise RequestParameterInvalidException(f"Invalid loop definition: {e}")


def workflow_has_loop(workflow: "Workflow") -> bool:
    return any(
        step.loop is not None or (step.subworkflow is not None and workflow_has_loop(step.subworkflow))
        for step in workflow.steps
    )


def loop_nesting_depth(workflow: "Workflow") -> int:
    depth = 0
    for step in workflow.steps:
        if step.subworkflow is not None:
            depth = max(depth, (step.loop is not None) + loop_nesting_depth(step.subworkflow))
    return depth


def check_loops_enabled(enabled: bool) -> None:
    if not enabled:
        raise ConfigDoesNotAllowException(
            "This workflow contains a loop, but workflow loops are not enabled on this Galaxy server."
        )


def validate_workflow_loops(workflow: "Workflow", enabled: bool) -> None:
    """Refuse loops this server cannot run, in ``workflow`` and its subworkflows."""
    if not workflow_has_loop(workflow):
        return
    check_loops_enabled(enabled)
    if loop_nesting_depth(workflow) > MAX_LOOP_NESTING_DEPTH:
        raise RequestParameterInvalidException(f"Workflow loops may be nested at most {MAX_LOOP_NESTING_DEPTH} deep.")
    _validate_steps(workflow)


def _validate_steps(workflow: "Workflow") -> None:
    for step in workflow.steps:
        if step.loop is not None:
            _validate_loop_step(step)
        if step.subworkflow is not None:
            if step.loop is None and workflow_has_loop(step.subworkflow) and _statically_mapped_over(step):
                raise RequestParameterInvalidException(_mapping_message(step))
            _validate_steps(step.subworkflow)


def _validate_loop_step(step: "WorkflowStep") -> None:
    name = workflow_step_name(step)
    if step.type != "subworkflow" or step.subworkflow is None:
        raise RequestParameterInvalidException(f"Step {name}: a loop is only allowed on a subworkflow step.")
    loop = parse_loop(step.loop)
    for step_input in step.inputs:
        if step_input.default_value_set or step_input.value_from is not None:
            raise RequestParameterInvalidException(
                f"Step {name}: a default or value_from on input '{step_input.name}' of a loop step is not supported yet."
            )
    if not step.when_expression:
        raise RequestParameterInvalidException(f"Step {name}: a loop step needs a 'when' expression.")
    connected_inputs = {connection.input_name for connection in step.input_connections}
    for match in WHEN_INPUT_REFERENCE.finditer(str(step.when_expression)):
        input_name = match.group(1) or match.group(2)
        if input_name not in connected_inputs:
            raise RequestParameterInvalidException(
                f"Step {name}: the 'when' expression uses input '{input_name}', which is not connected."
            )
    if loop.output_method != LoopOutputMethod.last_iteration:
        raise RequestParameterInvalidException(
            f"Step {name}: loop output_method '{loop.output_method}' is not supported yet."
        )
    input_labels = {input_step.label for input_step in step.subworkflow.input_steps}
    output_labels = set(step.subworkflow.workflow_output_labels)
    for input_name, rule in loop.inputs.items():
        if input_name not in input_labels:
            raise RequestParameterInvalidException(
                f"Step {name}: loop input '{input_name}' is not an input of the subworkflow."
            )
        if rule.output_source not in output_labels:
            raise RequestParameterInvalidException(
                f"Step {name}: loop output_source '{rule.output_source}' is not an output of the subworkflow."
            )
    if _statically_mapped_over(step):
        raise RequestParameterInvalidException(_mapping_message(step))


def validate_loop_request(workflow: "Workflow", inputs: dict[int, Any]) -> None:
    """Refuse a run request whose collection inputs would map over a loop step they are connected to."""
    for step in workflow.steps:
        if step.subworkflow is None or (step.loop is None and not workflow_has_loop(step.subworkflow)):
            continue
        for connection in step.input_connections:
            supplied = inputs.get(connection.output_step.id)
            if isinstance(supplied, model.HistoryDatasetCollectionAssociation) and _maps_over(
                supplied.collection.collection_type, connection.input_subworkflow_step
            ):
                raise RequestParameterInvalidException(_mapping_message(step))


def _statically_mapped_over(step: "WorkflowStep") -> bool:
    """Whether a collection input step connected to ``step`` is deeper than the subworkflow input it feeds."""
    return any(
        connection.output_step.type == "data_collection_input"
        and _maps_over(
            (connection.output_step.tool_inputs or {}).get("collection_type"), connection.input_subworkflow_step
        )
        for connection in step.input_connections
    )


def _maps_over(collection_type: str | None, subworkflow_input: "WorkflowStep | None") -> bool:
    if not collection_type or subworkflow_input is None:
        return False
    if subworkflow_input.type != "data_collection_input":
        return True
    input_type = (subworkflow_input.tool_inputs or {}).get("collection_type")
    return bool(input_type) and collection_type.endswith(f":{input_type}")


def _mapping_message(step: "WorkflowStep") -> str:
    if step.loop is not None:
        return f"Step {workflow_step_name(step)}: mapping over a loop step is not supported."
    return f"Step {workflow_step_name(step)}: mapping over a subworkflow that contains a loop is not supported."


def copy_invocation_request(template: model.WorkflowInvocation) -> model.WorkflowInvocation:
    """Copy the request of a child invocation, as created at request time, to run another iteration.

    Nested subworkflow steps get a fresh copy of their own request-time child, so an inner loop
    starts again from its first iteration.
    """
    child = model.WorkflowInvocation()
    child.uuid = uuid4()
    child.state = model.WorkflowInvocation.states.NEW
    child.workflow = template.workflow
    ensure_object_added_to_session(child, object_in_session=template)
    child.history = template.history
    child.input_parameters = [
        model.WorkflowRequestInputParameter(name=parameter.name, value=parameter.value, type=parameter.type)
        for parameter in template.input_parameters
    ]
    child.step_states = [
        model.WorkflowRequestStepState(workflow_step=step_state.workflow_step, value=deepcopy(step_state.value))
        for step_state in template.step_states
    ]
    first_associations: dict[int, model.WorkflowInvocationToSubworkflowInvocationAssociation] = {}
    for association in template.subworkflow_invocations:
        current = first_associations.get(association.workflow_step_id)
        if current is None or (association.iteration or 0) < (current.iteration or 0):
            first_associations[association.workflow_step_id] = association
    for association in first_associations.values():
        nested = copy_invocation_request(association.subworkflow_invocation)
        nested_association = child.attach_subworkflow_invocation_for_step(association.workflow_step, nested)
        nested_association.iteration = association.iteration
    return child


def loop_failure(step: "WorkflowStep", details: str) -> FailWorkflowEvaluation:
    return FailWorkflowEvaluation(
        why=InvocationFailureLoopFailed(reason=FailureReason.loop_failed, workflow_step_id=step.id, details=details)
    )


def iteration_outputs(iteration: model.WorkflowInvocation) -> dict[str, Any]:
    """Return the recorded outputs of an iteration's subworkflow invocation, by output label."""
    outputs: dict[str, Any] = {}
    for output_dataset in iteration.output_datasets:
        outputs[output_dataset.workflow_output.label] = output_dataset.dataset
    for output_collection in iteration.output_dataset_collections:
        outputs[output_collection.workflow_output.label] = output_collection.dataset_collection
    for output_value in iteration.output_values:
        value = output_value.value
        if isinstance(value, dict) and value.get("__class__") == "NoReplacement":
            value = NO_REPLACEMENT
        outputs[output_value.workflow_output.label] = value
    return outputs


def next_iteration_inputs(
    step: "WorkflowStep", loop: WorkflowLoop, first_inputs: dict[str, Any], previous_outputs: dict[str, Any]
) -> dict[str, Any]:
    """Return the input object of the next iteration.

    Each looped input takes the previous iteration's output its rule names, null and skipped
    values included; all other inputs keep their value from the first iteration.
    """
    inputs = dict(first_inputs)
    for input_name, rule in loop.inputs.items():
        if rule.output_source not in previous_outputs:
            raise FailWorkflowEvaluation(
                why=InvocationFailureOutputNotFound(
                    reason=FailureReason.output_not_found,
                    workflow_step_id=step.id,
                    output_name=rule.output_source,
                    dependent_workflow_step_id=step.id,
                )
            )
        inputs[input_name] = previous_outputs[rule.output_source]
    return inputs


def check_feedback(
    step: "WorkflowStep", loop: WorkflowLoop, first_inputs: dict[str, Any], next_inputs: dict[str, Any]
) -> None:
    """Refuse fed-back values the next iteration cannot take.

    A dataset collection input must get a collection, other inputs must not, and a fed-back
    collection must keep the collection type, the element identifiers and their order of the
    first iteration's collection. Null and skipped values are passed on.
    """
    assert step.subworkflow
    subworkflow_inputs = {input_step.label: input_step for input_step in step.subworkflow.input_steps}
    for input_name, rule in loop.inputs.items():
        value = next_inputs[input_name]
        if value is None or value is NO_REPLACEMENT:
            continue
        is_collection = isinstance(value, model.HistoryDatasetCollectionAssociation)
        if subworkflow_inputs[input_name].type == "data_collection_input" and not is_collection:
            raise loop_failure(
                step, f"Loop input '{input_name}' takes a dataset collection, output '{rule.output_source}' is not one."
            )
        if subworkflow_inputs[input_name].type != "data_collection_input" and is_collection:
            raise loop_failure(
                step,
                f"Loop input '{input_name}' does not take a dataset collection, output '{rule.output_source}' is one.",
            )
        first_value = first_inputs.get(input_name)
        if (
            is_collection
            and isinstance(first_value, model.HistoryDatasetCollectionAssociation)
            and _collection_shape(value.collection) != _collection_shape(first_value.collection)
        ):
            raise loop_failure(
                step,
                f"Loop input '{input_name}' must keep its collection type, element identifiers and their order.",
            )


def _collection_shape(collection: model.DatasetCollection) -> tuple[Any, ...]:
    return (
        collection.collection_type,
        tuple(
            (
                element.element_identifier,
                _collection_shape(element.child_collection) if element.child_collection else None,
            )
            for element in collection.elements
        ),
    )


def iteration_job_states(session: "Session", invocation_id: int) -> dict[str, int]:
    """Return each state of the jobs of an invocation and its nested subworkflow invocations,
    with the lowest id of a job in that state.

    One query, whatever the number of jobs and nested invocations.
    """
    association = model.WorkflowInvocationToSubworkflowInvocationAssociation
    tree = (
        select(model.WorkflowInvocation.id)
        .where(model.WorkflowInvocation.id == invocation_id)
        .cte("loop_iteration_invocations", recursive=True)
    )
    # UNION rather than UNION ALL: the same result for a tree, and it ends on a cycle.
    tree = tree.union(
        select(association.subworkflow_invocation_id).where(association.workflow_invocation_id == tree.c.id)
    )
    step = model.WorkflowInvocationStep
    job_association = model.ImplicitCollectionJobsJobAssociation
    in_tree = step.workflow_invocation_id.in_(select(tree.c.id))
    jobs = union_all(
        select(model.Job.id, model.Job.state).join(step, step.job_id == model.Job.id).where(in_tree),
        select(model.Job.id, model.Job.state)
        .join(job_association, job_association.job_id == model.Job.id)
        .join(step, step.implicit_collection_jobs_id == job_association.implicit_collection_jobs_id)
        .where(in_tree),
    ).subquery()
    rows = session.execute(select(jobs.c.state, func.min(jobs.c.id)).group_by(jobs.c.state))
    return {state: job_id for state, job_id in rows if state is not None}


def fail_unstarted_iteration(association: model.WorkflowInvocationToSubworkflowInvocationAssociation) -> None:
    """Record a failed iteration whose subworkflow invocation never ran, and fail that invocation and its
    request-time children, so that none of them waits to be scheduled."""
    association.loop_outcome = LoopOutcome.FAILED
    pending = [association.subworkflow_invocation]
    while pending:
        invocation = pending.pop()
        if invocation.state == model.WorkflowInvocation.states.NEW:
            invocation.state = model.WorkflowInvocation.states.FAILED
            invocation.add_message(
                InvocationUnexpectedFailure(
                    reason=FailureReason.unexpected_failure,
                    details="The loop ended before this iteration started.",
                )
            )
            pending.extend(nested.subworkflow_invocation for nested in invocation.subworkflow_invocations)
