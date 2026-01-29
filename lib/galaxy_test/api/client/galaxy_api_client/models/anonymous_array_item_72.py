from dataclasses import dataclass, field
from typing import Any

__all__ = ["AnonymousArrayItem72"]


@dataclass
class AnonymousArrayItem72:
    """
    Generic JSON value object that preserves arbitrary data.

    This class wraps arbitrary JSON objects with no defined schema,
    preserving all data during serialization/deserialization.

    Example:
        from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict, unstructure_to_dict

        # Deserialize from API response
        obj = structure_from_dict({"key": "value"}, AnonymousArrayItem72)

        # Access data
        print(obj["key"])  # "value"
        obj["new_key"] = "new_value"

        # Serialize for API request
        data = unstructure_to_dict(obj)  # {"key": "value", "new_key": "new_value"}
    """

    _data: dict[str, Any] = field(default_factory=dict, repr=False)

    def get(self, key: str, default: Any = None) -> Any:
        """Get value for key, returning default if key not present."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        """Get value for key."""
        return self._data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        """Set value for key."""
        self._data[key] = value

    def __contains__(self, key: str) -> bool:
        """Check if key exists."""
        return key in self._data

    def __bool__(self) -> bool:
        """Return True if wrapper contains any data."""
        return bool(self._data)

    def keys(self) -> Any:
        """Return dictionary keys."""
        return self._data.keys()

    def values(self) -> Any:
        """Return dictionary values."""
        return self._data.values()

    def items(self) -> Any:
        """Return dictionary items."""
        return self._data.items()

    def __iter__(self) -> Any:
        """Iterate over keys."""
        return iter(self._data)

    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)


# Register cattrs hooks for AnonymousArrayItem72
def _structure_anonymousarrayitem72(data: dict[str, Any], _: type[AnonymousArrayItem72]) -> AnonymousArrayItem72:
    """Structure hook for cattrs to handle AnonymousArrayItem72 deserialization."""
    if data is None:
        return AnonymousArrayItem72()
    if isinstance(data, AnonymousArrayItem72):
        return data
    return AnonymousArrayItem72(_data=data)


def _unstructure_anonymousarrayitem72(instance: AnonymousArrayItem72) -> dict[str, Any]:
    """Unstructure hook for cattrs to handle AnonymousArrayItem72 serialization."""
    return instance._data.copy()


# Register hooks with cattrs converter at module import time
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import converter

converter.register_structure_hook(AnonymousArrayItem72, _structure_anonymousarrayitem72)
converter.register_unstructure_hook(AnonymousArrayItem72, _unstructure_anonymousarrayitem72)
