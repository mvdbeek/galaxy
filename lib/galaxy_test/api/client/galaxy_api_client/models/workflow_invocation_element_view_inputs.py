from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar

from .invocation_input import InvocationInput

__all__ = ["WorkflowInvocationElementViewInputs"]


@dataclass
class WorkflowInvocationElementViewInputs:
    """
    Input datasets/dataset collections of the workflow invocation.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into InvocationInput instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become InvocationInput instances
        obj = structure_from_dict({"key": {"field": "value"}}, WorkflowInvocationElementViewInputs)

        # Access returns typed InvocationInput instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, InvocationInput] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "InvocationInput"

    def get(self, key: str, default: InvocationInput | None = None) -> InvocationInput | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> InvocationInput:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: InvocationInput) -> None:
        """Set value for key."""
        self._data[key] = value

    def __contains__(self, key: str) -> bool:
        """Check if key exists."""
        return key in self._data

    def __bool__(self) -> bool:
        """Return True if wrapper contains any data."""
        return bool(self._data)

    def keys(self) -> KeysView[str]:
        """Return dictionary keys."""
        return self._data.keys()

    def values(self) -> ValuesView[InvocationInput]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, InvocationInput]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for WorkflowInvocationElementViewInputs
def _structure_workflowinvocationelementviewinputs(
    data: dict[str, Any], _: type[WorkflowInvocationElementViewInputs]
) -> WorkflowInvocationElementViewInputs:
    """Structure hook for cattrs to handle WorkflowInvocationElementViewInputs deserialization with typed values."""
    if data is None:
        return WorkflowInvocationElementViewInputs()
    if isinstance(data, WorkflowInvocationElementViewInputs):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(InvocationInput, "__dataclass_fields__"):
        _register_structure_hooks_recursively(InvocationInput)

    # Deserialize each value into InvocationInput
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, InvocationInput] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, InvocationInput)

    return WorkflowInvocationElementViewInputs(_data=structured_data)


def _unstructure_workflowinvocationelementviewinputs(instance: WorkflowInvocationElementViewInputs) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle WorkflowInvocationElementViewInputs serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(WorkflowInvocationElementViewInputs, _structure_workflowinvocationelementviewinputs)
converter.register_unstructure_hook(
    WorkflowInvocationElementViewInputs, _unstructure_workflowinvocationelementviewinputs
)
