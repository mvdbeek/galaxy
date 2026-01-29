from typing import TypeAlias

__all__ = ["InvokeWorkflowPayloadHistory"]

InvokeWorkflowPayloadHistory: TypeAlias = str | None
"""Alias for The encoded history id - passed exactly like this 'hist_id=...' -  into which to import. Or the name of the new history into which to import."""
