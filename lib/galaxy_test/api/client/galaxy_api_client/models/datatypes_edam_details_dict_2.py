from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar

from .datatype_edam_details_2 import DatatypeEdamDetails2

__all__ = ["DatatypesEdamDetailsDict2"]


@dataclass
class DatatypesEdamDetailsDict2:
    """
    Generic JSON value object that preserves arbitrary data.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into DatatypeEdamDetails2 instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become DatatypeEdamDetails2 instances
        obj = structure_from_dict({"key": {"field": "value"}}, DatatypesEdamDetailsDict2)

        # Access returns typed DatatypeEdamDetails2 instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, DatatypeEdamDetails2] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "DatatypeEdamDetails2"

    def get(self, key: str, default: DatatypeEdamDetails2 | None = None) -> DatatypeEdamDetails2 | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> DatatypeEdamDetails2:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: DatatypeEdamDetails2) -> None:
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

    def values(self) -> ValuesView[DatatypeEdamDetails2]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, DatatypeEdamDetails2]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for DatatypesEdamDetailsDict2
def _structure_datatypesedamdetailsdict2(
    data: dict[str, Any], _: type[DatatypesEdamDetailsDict2]
) -> DatatypesEdamDetailsDict2:
    """Structure hook for cattrs to handle DatatypesEdamDetailsDict2 deserialization with typed values."""
    if data is None:
        return DatatypesEdamDetailsDict2()
    if isinstance(data, DatatypesEdamDetailsDict2):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(DatatypeEdamDetails2, "__dataclass_fields__"):
        _register_structure_hooks_recursively(DatatypeEdamDetails2)

    # Deserialize each value into DatatypeEdamDetails2
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, DatatypeEdamDetails2] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, DatatypeEdamDetails2)

    return DatatypesEdamDetailsDict2(_data=structured_data)


def _unstructure_datatypesedamdetailsdict2(instance: DatatypesEdamDetailsDict2) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle DatatypesEdamDetailsDict2 serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(DatatypesEdamDetailsDict2, _structure_datatypesedamdetailsdict2)
converter.register_unstructure_hook(DatatypesEdamDetailsDict2, _unstructure_datatypesedamdetailsdict2)
