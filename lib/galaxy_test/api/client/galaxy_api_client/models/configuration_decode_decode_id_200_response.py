from collections.abc import ItemsView, Iterator, KeysView, ValuesView
from dataclasses import dataclass, field
from typing import Any, ClassVar

__all__ = ["ConfigurationDecodeDecodeId200Response"]


@dataclass
class ConfigurationDecodeDecodeId200Response:
    """
    Generic JSON value object that preserves arbitrary data.

    This class wraps a dictionary with typed values, providing dict-like access
    while ensuring values are properly deserialized into int instances.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response - values become int instances
        obj = structure_from_dict({"key": {"field": "value"}}, ConfigurationDecodeDecodeId200Response)

        # Access returns typed int instance
        item = obj["key"]
        print(item.field)  # "value" - direct attribute access

        # Serialize for API request
        data = unstructure_to_dict(obj)
    """

    _data: dict[str, int] = field(default_factory=dict, repr=False)

    # Runtime type information for cattrs deserialization
    _value_type: ClassVar[str] = "int"

    def get(self, key: str, default: int | None = None) -> int | None:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> int:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: int) -> None:
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

    def values(self) -> ValuesView[int]:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> ItemsView[str, int]:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Iterator[str]:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for ConfigurationDecodeDecodeId200Response
def _structure_configurationdecodedecodeid200response(
    data: dict[str, Any], _: type[ConfigurationDecodeDecodeId200Response]
) -> ConfigurationDecodeDecodeId200Response:
    """Structure hook for cattrs to handle ConfigurationDecodeDecodeId200Response deserialization with typed values."""
    if data is None:
        return ConfigurationDecodeDecodeId200Response()
    if isinstance(data, ConfigurationDecodeDecodeId200Response):
        return data

    # Import converter lazily to avoid circular imports
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import (
        _register_structure_hooks_recursively,
        converter,
    )

    # Register hooks for dataclass value types (once, outside loop)
    if hasattr(int, "__dataclass_fields__"):
        _register_structure_hooks_recursively(int)

    # Deserialize each value into int
    # Using converter.structure() for all values - cattrs handles primitives, datetime, bytes, etc.
    structured_data: dict[str, int] = {}
    for key, value in data.items():
        structured_data[key] = converter.structure(value, int)

    return ConfigurationDecodeDecodeId200Response(_data=structured_data)


def _unstructure_configurationdecodedecodeid200response(
    instance: ConfigurationDecodeDecodeId200Response,
) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle ConfigurationDecodeDecodeId200Response serialization."""
    from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

    # Unstructure each value
    return {key: converter.unstructure(value) for key, value in instance._data.items()}


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(
    ConfigurationDecodeDecodeId200Response, _structure_configurationdecodedecodeid200response
)
converter.register_unstructure_hook(
    ConfigurationDecodeDecodeId200Response, _unstructure_configurationdecodedecodeid200response
)
