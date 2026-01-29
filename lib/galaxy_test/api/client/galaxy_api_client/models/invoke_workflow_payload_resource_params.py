from typing import Any, TypeAlias

__all__ = ["InvokeWorkflowPayloadResourceParams"]

InvokeWorkflowPayloadResourceParams: TypeAlias = dict[str, Any] | None
"""Alias for If a workflow_resource_params_file file is defined and the target workflow is configured to consumer resource parameters, they can be specified with this parameter. See https://github.com/galaxyproject/galaxy/pull/4830 for more information."""
