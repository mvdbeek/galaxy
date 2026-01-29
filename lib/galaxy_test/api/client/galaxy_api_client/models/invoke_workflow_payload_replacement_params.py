from typing import Any, TypeAlias

__all__ = ["InvokeWorkflowPayloadReplacementParams"]

InvokeWorkflowPayloadReplacementParams: TypeAlias = dict[str, Any] | None
"""Alias for Class of parameters mostly used for string replacement in PJAs. In best practice workflows, these should be replaced with input parameters"""
