from typing import TypeAlias

from .user_model import UserModel

__all__ = ["ConfigurationWhoami200Response"]

ConfigurationWhoami200Response: TypeAlias = UserModel | None
