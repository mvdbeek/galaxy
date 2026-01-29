from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar

__all__ = ["ArchivedHistoryDetailedStateIds"]


@dataclass
class ArchivedHistoryDetailedStateIds:
    """
    A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into List[str] instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become List[str] instances
        obj = structure_from_dict({"key": {"field": "value"}}, ArchivedHistoryDetailedStateIds)

        # Access returns typed List[str] instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, list[str]] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "List[str]"

    def get(self, key: str, default: list[str] | None = None) -> list[str] | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> list[str]:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
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

    def values(self) -> ValuesView[list[str]]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, list[str]]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for ArchivedHistoryDetailedStateIds
def _structure_archivedhistorydetailedstateids(
    data: dict[str, Any], _: type[ArchivedHistoryDetailedStateIds]
) -> ArchivedHistoryDetailedStateIds:
    """Structure hook for cattrs to handle ArchivedHistoryDetailedStateIds deserialization with typed values."""
    if data is None:
        return ArchivedHistoryDetailedStateIds()
    if isinstance(data, ArchivedHistoryDetailedStateIds):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(list[str], "__dataclass_fields__"):
        _register_structure_hooks_recursively(list[str])

    # Deserialize each value into List[str]
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, list[str]] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, list[str])

    return ArchivedHistoryDetailedStateIds(_data=structured_data)


def _unstructure_archivedhistorydetailedstateids(instance: ArchivedHistoryDetailedStateIds) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle ArchivedHistoryDetailedStateIds serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(ArchivedHistoryDetailedStateIds, _structure_archivedhistorydetailedstateids)
converter.register_unstructure_hook(ArchivedHistoryDetailedStateIds, _unstructure_archivedhistorydetailedstateids)
