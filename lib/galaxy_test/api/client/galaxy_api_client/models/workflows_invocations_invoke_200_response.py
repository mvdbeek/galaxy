from typing import TypeAlias

from .workflow_invocation_response import WorkflowInvocationResponse

__all__ = ["WorkflowsInvocationsInvoke200Response"]

WorkflowsInvocationsInvoke200Response: TypeAlias = WorkflowInvocationResponse | list[WorkflowInvocationResponse]
