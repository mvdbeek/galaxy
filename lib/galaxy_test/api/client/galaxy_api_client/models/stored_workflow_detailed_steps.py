from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar, Union

from .input_data_collection_step import InputDataCollectionStep
from .input_data_step import InputDataStep
from .input_parameter_step import InputParameterStep
from .pause_step import PauseStep
from .subworkflow_step import SubworkflowStep
from .tool_step import ToolStep

__all__ = ["StoredWorkflowDetailedSteps"]


@dataclass
class StoredWorkflowDetailedSteps:
    """
    A dictionary with information about all the steps of the workflow.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep] instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep] instances
        obj = structure_from_dict({"key": {"field": "value"}}, StoredWorkflowDetailedSteps)

        # Access returns typed Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep] instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[
        str, InputDataStep | InputDataCollectionStep | InputParameterStep | PauseStep | ToolStep | SubworkflowStep
    ] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = (
        "Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep]"
    )

    def get(
        self,
        key: str,
        default: InputDataStep
        | InputDataCollectionStep
        | InputParameterStep
        | PauseStep
        | ToolStep
        | SubworkflowStep
        | None = None,
    ) -> InputDataStep | InputDataCollectionStep | InputParameterStep | PauseStep | ToolStep | SubworkflowStep | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(
        self, key: str
    ) -> InputDataStep | InputDataCollectionStep | InputParameterStep | PauseStep | ToolStep | SubworkflowStep:
        """Get value for key."""
        return self._data[key]

    def __setitem__(
        self,
        key: str,
        value: InputDataStep | InputDataCollectionStep | InputParameterStep | PauseStep | ToolStep | SubworkflowStep,
    ) -> None:
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

    def values(
        self,
    ) -> ValuesView[
        InputDataStep | InputDataCollectionStep | InputParameterStep | PauseStep | ToolStep | SubworkflowStep
    ]:
        """Return dictionary values."""
        return self._data.values()

    def items(
        self,
    ) -> ItemsView[
        str, InputDataStep | InputDataCollectionStep | InputParameterStep | PauseStep | ToolStep | SubworkflowStep
    ]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for StoredWorkflowDetailedSteps
def _structure_storedworkflowdetailedsteps(
    data: dict[str, Any], _: type[StoredWorkflowDetailedSteps]
) -> StoredWorkflowDetailedSteps:
    """Structure hook for cattrs to handle StoredWorkflowDetailedSteps deserialization with typed values."""
    if data is None:
        return StoredWorkflowDetailedSteps()
    if isinstance(data, StoredWorkflowDetailedSteps):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(
        Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep],
        "__dataclass_fields__",
    ):
        _register_structure_hooks_recursively(
            Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep]
        )

    # Deserialize each value into Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep]
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[
        str, InputDataStep | InputDataCollectionStep | InputParameterStep | PauseStep | ToolStep | SubworkflowStep
    ] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(
            value,
            Union[InputDataStep, InputDataCollectionStep, InputParameterStep, PauseStep, ToolStep, SubworkflowStep],
        )

    return StoredWorkflowDetailedSteps(_data=structured_data)


def _unstructure_storedworkflowdetailedsteps(instance: StoredWorkflowDetailedSteps) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle StoredWorkflowDetailedSteps serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(StoredWorkflowDetailedSteps, _structure_storedworkflowdetailedsteps)
converter.register_unstructure_hook(StoredWorkflowDetailedSteps, _unstructure_storedworkflowdetailedsteps)
