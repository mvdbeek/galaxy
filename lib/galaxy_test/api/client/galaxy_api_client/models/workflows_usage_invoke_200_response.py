from typing import TypeAlias

from .workflow_invocation_response import WorkflowInvocationResponse

__all__ = ["WorkflowsUsageInvoke200Response"]

WorkflowsUsageInvoke200Response: TypeAlias = WorkflowInvocationResponse | list[WorkflowInvocationResponse]
