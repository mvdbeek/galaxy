from typing import TypeAlias

__all__ = ["InvokeWorkflowPayloadParametersNormalized"]

InvokeWorkflowPayloadParametersNormalized: TypeAlias = bool | None
"""Alias for Indicates if legacy parameters are already normalized to be indexed by the order_index and are specified as a dictionary per step. Legacy-style parameters could previously be specified as one parameter per step or by tool ID."""
