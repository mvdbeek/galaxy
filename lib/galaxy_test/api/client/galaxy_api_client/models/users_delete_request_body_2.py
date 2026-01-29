from typing import TypeAlias

from .user_deletion_payload import UserDeletionPayload

__all__ = ["UsersDeleteRequestBody2"]

UsersDeleteRequestBody2: TypeAlias = UserDeletionPayload | None
