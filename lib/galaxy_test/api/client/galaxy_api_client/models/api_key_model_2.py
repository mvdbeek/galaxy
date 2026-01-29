from dataclasses import dataclass
from datetime import datetime

__all__ = ["ApiKeyModel2"]


@dataclass
class ApiKeyModel2:
    """
    ApiKeyModel2 dataclass.

    Args:
        create_time (datetime)   : The time and date this API key was created.
        key (str)                : API key to interact with the Galaxy API
    """

    create_time: datetime  # The time and date this API key was created.
    key: str  # API key to interact with the Galaxy API
