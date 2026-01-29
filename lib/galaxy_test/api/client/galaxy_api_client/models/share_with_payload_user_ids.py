from typing import TypeAlias

from .share_with_payload_user_ids_item import ShareWithPayloadUserIdsItem

__all__ = ["ShareWithPayloadUserIds"]

ShareWithPayloadUserIds: TypeAlias = list[ShareWithPayloadUserIdsItem]
"""Alias for A collection of encoded IDs (or email addresses) of users that this resource will be shared with."""
