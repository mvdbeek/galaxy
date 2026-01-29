from typing import TypeAlias

from .remote_user_creation_payload import RemoteUserCreationPayload
from .user_creation_payload import UserCreationPayload

__all__ = ["UsersCreateRequestBody"]

UsersCreateRequestBody: TypeAlias = UserCreationPayload | RemoteUserCreationPayload
"""Alias for The values to add create a user."""
