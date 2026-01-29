from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar

from .invocation_output import InvocationOutput

__all__ = ["WorkflowInvocationElementViewOutputs"]


@dataclass
class WorkflowInvocationElementViewOutputs:
    """
    Output datasets of the workflow invocation.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into InvocationOutput instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become InvocationOutput instances
        obj = structure_from_dict({"key": {"field": "value"}}, WorkflowInvocationElementViewOutputs)

        # Access returns typed InvocationOutput instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, InvocationOutput] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "InvocationOutput"

    def get(self, key: str, default: InvocationOutput | None = None) -> InvocationOutput | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> InvocationOutput:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: InvocationOutput) -> None:
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

    def values(self) -> ValuesView[InvocationOutput]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, InvocationOutput]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for WorkflowInvocationElementViewOutputs
def _structure_workflowinvocationelementviewoutputs(
    data: dict[str, Any], _: type[WorkflowInvocationElementViewOutputs]
) -> WorkflowInvocationElementViewOutputs:
    """Structure hook for cattrs to handle WorkflowInvocationElementViewOutputs deserialization with typed values."""
    if data is None:
        return WorkflowInvocationElementViewOutputs()
    if isinstance(data, WorkflowInvocationElementViewOutputs):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(InvocationOutput, "__dataclass_fields__"):
        _register_structure_hooks_recursively(InvocationOutput)

    # Deserialize each value into InvocationOutput
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, InvocationOutput] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, InvocationOutput)

    return WorkflowInvocationElementViewOutputs(_data=structured_data)


def _unstructure_workflowinvocationelementviewoutputs(instance: WorkflowInvocationElementViewOutputs) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle WorkflowInvocationElementViewOutputs serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(WorkflowInvocationElementViewOutputs, _structure_workflowinvocationelementviewoutputs)
converter.register_unstructure_hook(
    WorkflowInvocationElementViewOutputs, _unstructure_workflowinvocationelementviewoutputs
)
