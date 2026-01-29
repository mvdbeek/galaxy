from dataclasses import dataclass

__all__ = ["ApiKeyResponse"]


@dataclass
class ApiKeyResponse:
    """
    ApiKeyResponse dataclass

    Args:
        api_key (str)            :
    """

    api_key: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "api_key": "api_key",
        }
        key_transform_with_dump = {
            "api_key": "api_key",
        }
