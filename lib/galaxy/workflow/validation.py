"""Workflow validation utilities.

This module provides static validation checks for workflows that can be
performed without executing the workflow.
"""

import re
from typing import (
    List,
    Optional,
    Set,
    TYPE_CHECKING,
)

from galaxy import exceptions

if TYPE_CHECKING:
    from galaxy.model import (
        Workflow,
        WorkflowStep,
    )


def get_when_expression_inputs(when_expression: Optional[str]) -> Set[str]:
    """Extract input names referenced in a when expression.

    When expressions use CWL syntax like $(inputs.should_run) or ${inputs.should_run}.
    Returns a set of input names referenced.
    """
    if not when_expression:
        return set()
    # Match patterns like $(inputs.name) or ${inputs.name}
    pattern = r"\$[\(\{]inputs\.(\w+)[\)\}]"
    return set(re.findall(pattern, when_expression))


class WorkflowValidationError:
    """Represents a validation error in a workflow."""

    def __init__(
        self,
        message: str,
        step: Optional["WorkflowStep"] = None,
        workflow_path: Optional[List[str]] = None,
    ):
        self.message = message
        self.step = step
        self.workflow_path = workflow_path or []

    def __str__(self) -> str:
        if self.workflow_path:
            path_str = " -> ".join(self.workflow_path)
            return f"[{path_str}] {self.message}"
        return self.message


def validate_workflow(
    workflow: "Workflow",
    workflow_path: Optional[List[str]] = None,
) -> List[WorkflowValidationError]:
    """Validate a workflow and return a list of validation errors.

    This performs static validation checks that don't require workflow execution.
    Descends into subworkflows to validate them as well.

    Args:
        workflow: The workflow to validate
        workflow_path: Path of workflow names for nested subworkflow context

    Returns:
        List of WorkflowValidationError objects describing any issues found
    """
    errors: List[WorkflowValidationError] = []
    workflow_path = workflow_path or []
    current_path = workflow_path + [workflow.name or "Unnamed workflow"]

    # Check for empty workflow
    if len(workflow.steps) == 0:
        errors.append(
            WorkflowValidationError(
                "Workflow cannot be run because it does not have any steps",
                workflow_path=current_path,
            )
        )

    # Check for cycles
    if workflow.has_cycles:
        errors.append(
            WorkflowValidationError(
                "Workflow cannot be run because it contains cycles",
                workflow_path=current_path,
            )
        )

    # Validate each step
    for step in workflow.steps:
        step_errors = _validate_step(step, current_path)
        errors.extend(step_errors)

        # Descend into subworkflows
        if step.type == "subworkflow" and step.subworkflow:
            subworkflow_errors = validate_workflow(
                step.subworkflow,
                workflow_path=current_path,
            )
            errors.extend(subworkflow_errors)

    return errors


def _validate_step(
    step: "WorkflowStep",
    workflow_path: List[str],
) -> List[WorkflowValidationError]:
    """Validate a single workflow step."""
    errors: List[WorkflowValidationError] = []
    step_label = step.label or f"step {step.order_index + 1}"

    # Check for disconnected when inputs
    if step.when_expression:
        referenced_inputs = get_when_expression_inputs(step.when_expression)
        # Get names of inputs that have connections
        connected_inputs: Set[str] = set()
        for step_input in step.inputs:
            if step_input.connections:
                connected_inputs.add(step_input.name)

        missing_inputs = referenced_inputs - connected_inputs

        if missing_inputs:
            errors.append(
                WorkflowValidationError(
                    f"Step '{step_label}' has a conditional expression that references "
                    f"disconnected input(s): {', '.join(sorted(missing_inputs))}",
                    step=step,
                    workflow_path=workflow_path,
                )
            )

    return errors


def validate_workflow_for_run(workflow: "Workflow") -> None:
    """Validate a workflow before running and raise exception if invalid.

    Args:
        workflow: The workflow to validate

    Raises:
        MessageException: If the workflow has validation errors
    """
    errors = validate_workflow(workflow)
    if errors:
        # Combine all error messages
        error_messages = [str(e) for e in errors]
        if len(error_messages) == 1:
            raise exceptions.MessageException(error_messages[0])
        else:
            raise exceptions.MessageException(
                "Workflow has validation errors:\n" + "\n".join(f"- {msg}" for msg in error_messages)
            )
