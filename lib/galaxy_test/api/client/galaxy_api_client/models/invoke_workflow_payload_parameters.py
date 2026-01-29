from typing import Any, TypeAlias

__all__ = ["InvokeWorkflowPayloadParameters"]

InvokeWorkflowPayloadParameters: TypeAlias = dict[str, Any] | None
"""Alias for Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead."""
