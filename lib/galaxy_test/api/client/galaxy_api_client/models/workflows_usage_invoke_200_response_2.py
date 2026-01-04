from typing import TypeAlias

from .workflow_invocation_response import WorkflowInvocationResponse

__all__ = ["WorkflowsUsageInvoke200Response2"]

WorkflowsUsageInvoke200Response2: TypeAlias = list[WorkflowInvocationResponse] | WorkflowInvocationResponse
