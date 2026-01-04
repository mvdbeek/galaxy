from typing import TypeAlias

from .workflow_invocation_response import WorkflowInvocationResponse

__all__ = ["WorkflowsInvocationsInvoke200Response2"]

WorkflowsInvocationsInvoke200Response2: TypeAlias = list[WorkflowInvocationResponse] | WorkflowInvocationResponse
