from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar, Union

__all__ = ["ParsedWorkbookRowsItem"]


@dataclass
class ParsedWorkbookRowsItem:
    """
    Generic JSON value object that preserves arbitrary data.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into Union[int, float, bool, str] | None instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become Union[int, float, bool, str] | None instances
        obj = structure_from_dict({"key": {"field": "value"}}, ParsedWorkbookRowsItem)

        # Access returns typed Union[int, float, bool, str] | None instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, int | float | bool | str | None] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "Union[int, float, bool, str] | None"

    def get(
        self, key: str, default: int | float | bool | str | None | None = None
    ) -> int | float | bool | str | None | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> int | float | bool | str | None:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: int | float | bool | str | None) -> None:
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

    def values(self) -> ValuesView[int | float | bool | str | None]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, int | float | bool | str | None]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for ParsedWorkbookRowsItem
def _structure_parsedworkbookrowsitem(data: dict[str, Any], _: type[ParsedWorkbookRowsItem]) -> ParsedWorkbookRowsItem:
    """Structure hook for cattrs to handle ParsedWorkbookRowsItem deserialization with typed values."""
    if data is None:
        return ParsedWorkbookRowsItem()
    if isinstance(data, ParsedWorkbookRowsItem):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(Union[int, float, bool, str] | None, "__dataclass_fields__"):
        _register_structure_hooks_recursively(Union[int, float, bool, str] | None)

    # Deserialize each value into Union[int, float, bool, str] | None
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, int | float | bool | str | None] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, Union[int, float, bool, str] | None)

    return ParsedWorkbookRowsItem(_data=structured_data)


def _unstructure_parsedworkbookrowsitem(instance: ParsedWorkbookRowsItem) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle ParsedWorkbookRowsItem serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(ParsedWorkbookRowsItem, _structure_parsedworkbookrowsitem)
converter.register_unstructure_hook(ParsedWorkbookRowsItem, _unstructure_parsedworkbookrowsitem)
