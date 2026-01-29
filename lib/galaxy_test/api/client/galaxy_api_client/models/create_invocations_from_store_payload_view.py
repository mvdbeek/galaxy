from typing import TypeAlias

from .invocation_serialization_view import InvocationSerializationView

__all__ = ["CreateInvocationsFromStorePayloadView"]

CreateInvocationsFromStorePayloadView: TypeAlias = InvocationSerializationView | None
"""Alias for The name of the view used to serialize this item. This will return a predefined set of attributes of the item."""
