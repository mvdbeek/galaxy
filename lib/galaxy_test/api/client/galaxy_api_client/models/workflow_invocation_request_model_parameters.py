from typing import Any, TypeAlias

__all__ = ["WorkflowInvocationRequestModelParameters"]

WorkflowInvocationRequestModelParameters: TypeAlias = dict[str, Any] | None
"""Alias for Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead. If these are set, the workflow was not executed in a best-practice fashion and we the resulting invocation request may not fully reflect the executed workflow state."""
