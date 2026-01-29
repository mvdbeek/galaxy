from typing import TypeAlias

from .user_deletion_payload import UserDeletionPayload

__all__ = ["UsersDeleteRequestBody"]

UsersDeleteRequestBody: TypeAlias = UserDeletionPayload | None
