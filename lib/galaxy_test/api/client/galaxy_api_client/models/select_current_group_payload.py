from dataclasses import dataclass

from .current_group_id import CurrentGroupId

__all__ = ["SelectCurrentGroupPayload"]


@dataclass
class SelectCurrentGroupPayload:
    """
    SelectCurrentGroupPayload dataclass.

    Args:
        user_credentials_id (str): The ID of the user credentials to update.
        current_group_id (Optional[CurrentGroupId])
                                 : The ID of the currently active credential group.
    """

    user_credentials_id: str  # The ID of the user credentials to update.
    current_group_id: CurrentGroupId | None = None  # The ID of the currently active credential group.
