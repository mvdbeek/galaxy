from dataclasses import dataclass

from .select_current_group_payload_current_group_id import SelectCurrentGroupPayloadCurrentGroupId

__all__ = ["SelectCurrentGroupPayload"]


@dataclass
class SelectCurrentGroupPayload:
    """
    SelectCurrentGroupPayload dataclass

    Args:
        user_credentials_id (str): The ID of the user credentials to update.
        current_group_id (SelectCurrentGroupPayloadCurrentGroupId | None)
                                 : The ID of the group to set as current (None to unset).
    """

    user_credentials_id: str  # The ID of the user credentials to update.
    current_group_id: SelectCurrentGroupPayloadCurrentGroupId | None = (
        None  # The ID of the group to set as current (None to unset).
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "current_group_id": "current_group_id",
            "user_credentials_id": "user_credentials_id",
        }
        key_transform_with_dump = {
            "current_group_id": "current_group_id",
            "user_credentials_id": "user_credentials_id",
        }
