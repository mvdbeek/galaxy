from dataclasses import dataclass
from datetime import datetime

__all__ = ["ApiKeyModel"]


@dataclass
class ApiKeyModel:
    """
    ApiKeyModel dataclass

    Args:
        create_time (datetime)   : The time and date this API key was created.
        key (str)                : API key to interact with the Galaxy API
    """

    create_time: datetime  # The time and date this API key was created.
    key: str  # API key to interact with the Galaxy API

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_time": "create_time",
            "key": "key",
        }
        key_transform_with_dump = {
            "create_time": "create_time",
            "key": "key",
        }
