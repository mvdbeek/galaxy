from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar

from .input_step import InputStep

__all__ = ["SubworkflowStepInputSteps"]


@dataclass
class SubworkflowStepInputSteps:
    """
    A dictionary containing information about the inputs connected to this workflow step.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into InputStep instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become InputStep instances
        obj = structure_from_dict({"key": {"field": "value"}}, SubworkflowStepInputSteps)

        # Access returns typed InputStep instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, InputStep] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "InputStep"

    def get(self, key: str, default: InputStep | None = None) -> InputStep | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> InputStep:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: InputStep) -> None:
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

    def values(self) -> ValuesView[InputStep]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, InputStep]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for SubworkflowStepInputSteps
def _structure_subworkflowstepinputsteps(
    data: dict[str, Any], _: type[SubworkflowStepInputSteps]
) -> SubworkflowStepInputSteps:
    """Structure hook for cattrs to handle SubworkflowStepInputSteps deserialization with typed values."""
    if data is None:
        return SubworkflowStepInputSteps()
    if isinstance(data, SubworkflowStepInputSteps):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(InputStep, "__dataclass_fields__"):
        _register_structure_hooks_recursively(InputStep)

    # Deserialize each value into InputStep
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, InputStep] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, InputStep)

    return SubworkflowStepInputSteps(_data=structured_data)


def _unstructure_subworkflowstepinputsteps(instance: SubworkflowStepInputSteps) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle SubworkflowStepInputSteps serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(SubworkflowStepInputSteps, _structure_subworkflowstepinputsteps)
converter.register_unstructure_hook(SubworkflowStepInputSteps, _unstructure_subworkflowstepinputsteps)
