"""
Shared utilities for resolving outputs from workflow invocations.

This module provides a centralized implementation for resolving outputs
from workflow invocations, used both during invocation creation (immediate
resolution) and during scheduling (deferred resolution).
"""

from typing import (
    Optional,
    TYPE_CHECKING,
    Union,
)

if TYPE_CHECKING:
    from galaxy.model import (
        HistoryDatasetAssociation,
        HistoryDatasetCollectionAssociation,
        WorkflowInvocation,
        WorkflowInvocationInputDependency,
        WorkflowOutput,
    )


def resolve_output_by_workflow_output(
    source_invocation: "WorkflowInvocation",
    workflow_output: "WorkflowOutput",
) -> tuple[
    Optional[Union["HistoryDatasetAssociation", "HistoryDatasetCollectionAssociation"]],
    Optional[int],
    Optional[int],
]:
    """
    Resolve an output from an invocation by workflow output definition.

    Args:
        source_invocation: The invocation to resolve output from
        workflow_output: The workflow output definition to look for

    Returns:
        A tuple of (content, resolved_dataset_id, resolved_collection_id) where:
        - content: The resolved dataset/collection if available, None if not yet available
        - resolved_dataset_id: The dataset ID if resolved to a dataset
        - resolved_collection_id: The collection ID if resolved to a collection
    """
    # Check output datasets first
    for output_assoc in source_invocation.output_datasets:
        if output_assoc.workflow_output_id == workflow_output.id:
            return output_assoc.dataset, output_assoc.dataset_id, None

    # Check output collections
    for output_assoc in source_invocation.output_dataset_collections:
        if output_assoc.workflow_output_id == workflow_output.id:
            return output_assoc.dataset_collection, None, output_assoc.dataset_collection_id

    return None, None, None


def resolve_output_by_step(
    source_invocation: "WorkflowInvocation",
    step_id: int,
    output_name: str,
) -> tuple[
    Optional[Union["HistoryDatasetAssociation", "HistoryDatasetCollectionAssociation"]],
    Optional[int],
    Optional[int],
]:
    """
    Resolve an output from an invocation by step ID and output name.

    Args:
        source_invocation: The invocation to resolve output from
        step_id: The workflow step ID to look for
        output_name: The name of the output on the step

    Returns:
        A tuple of (content, resolved_dataset_id, resolved_collection_id) where:
        - content: The resolved dataset/collection if available, None if not yet available
        - resolved_dataset_id: The dataset ID if resolved to a dataset
        - resolved_collection_id: The collection ID if resolved to a collection
    """
    for step_inv in source_invocation.steps:
        if step_inv.workflow_step_id == step_id:
            # Check output datasets
            for output in step_inv.output_datasets:
                if output.output_name == output_name:
                    return output.dataset, output.dataset_id, None

            # Check output collections
            for output in step_inv.output_dataset_collections:
                if output.output_name == output_name:
                    return output.dataset_collection, None, output.dataset_collection_id

            # Step found but output not available yet
            break

    return None, None, None


def resolve_dependency(
    dependency: "WorkflowInvocationInputDependency",
    source_invocation: "WorkflowInvocation",
    workflow_output: Optional["WorkflowOutput"] = None,
) -> tuple[
    Optional[Union["HistoryDatasetAssociation", "HistoryDatasetCollectionAssociation"]],
    bool,
]:
    """
    Resolve a dependency and update its resolved_dataset_id or resolved_collection_id.

    Args:
        dependency: The dependency to resolve
        source_invocation: The source invocation providing the output
        workflow_output: The workflow output definition (if resolving by label)

    Returns:
        A tuple of (content, resolved) where:
        - content: The resolved dataset/collection if available
        - resolved: Whether the dependency was successfully resolved
    """
    content = None
    resolved_dataset_id = None
    resolved_collection_id = None

    if dependency.source_workflow_output_id and workflow_output:
        content, resolved_dataset_id, resolved_collection_id = resolve_output_by_workflow_output(
            source_invocation, workflow_output
        )
    elif dependency.source_step_id and dependency.source_output_name:
        content, resolved_dataset_id, resolved_collection_id = resolve_output_by_step(
            source_invocation, dependency.source_step_id, dependency.source_output_name
        )

    if resolved_dataset_id is not None:
        dependency.resolved_dataset_id = resolved_dataset_id
        return content, True
    elif resolved_collection_id is not None:
        dependency.resolved_collection_id = resolved_collection_id
        return content, True

    return None, False
