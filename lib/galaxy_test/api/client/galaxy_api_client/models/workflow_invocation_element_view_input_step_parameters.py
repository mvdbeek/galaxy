from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar

from .invocation_input_parameter import InvocationInputParameter

__all__ = ["WorkflowInvocationElementViewInputStepParameters"]


@dataclass
class WorkflowInvocationElementViewInputStepParameters:
    """
    Input step parameters of the workflow invocation.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into InvocationInputParameter instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become InvocationInputParameter instances
        obj = structure_from_dict({"key": {"field": "value"}}, WorkflowInvocationElementViewInputStepParameters)

        # Access returns typed InvocationInputParameter instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, InvocationInputParameter] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "InvocationInputParameter"

    def get(self, key: str, default: InvocationInputParameter | None = None) -> InvocationInputParameter | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> InvocationInputParameter:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: InvocationInputParameter) -> None:
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

    def values(self) -> ValuesView[InvocationInputParameter]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, InvocationInputParameter]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for WorkflowInvocationElementViewInputStepParameters
def _structure_workflowinvocationelementviewinputstepparameters(
    data: dict[str, Any], _: type[WorkflowInvocationElementViewInputStepParameters]
) -> WorkflowInvocationElementViewInputStepParameters:
    """Structure hook for cattrs to handle WorkflowInvocationElementViewInputStepParameters deserialization with typed values."""
    if data is None:
        return WorkflowInvocationElementViewInputStepParameters()
    if isinstance(data, WorkflowInvocationElementViewInputStepParameters):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(InvocationInputParameter, "__dataclass_fields__"):
        _register_structure_hooks_recursively(InvocationInputParameter)

    # Deserialize each value into InvocationInputParameter
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, InvocationInputParameter] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, InvocationInputParameter)

    return WorkflowInvocationElementViewInputStepParameters(_data=structured_data)


def _unstructure_workflowinvocationelementviewinputstepparameters(
    instance: WorkflowInvocationElementViewInputStepParameters,
) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle WorkflowInvocationElementViewInputStepParameters serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(
    WorkflowInvocationElementViewInputStepParameters, _structure_workflowinvocationelementviewinputstepparameters
)
converter.register_unstructure_hook(
    WorkflowInvocationElementViewInputStepParameters, _unstructure_workflowinvocationelementviewinputstepparameters
)
