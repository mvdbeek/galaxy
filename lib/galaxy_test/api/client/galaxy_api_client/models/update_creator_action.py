from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum
from .update_creator_action_creator import UpdateCreatorActionCreator

__all__ = ["UpdateCreatorAction"]


@dataclass
class UpdateCreatorAction:
    """
    UpdateCreatorAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        creator (UpdateCreatorActionCreator | None)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    creator: UpdateCreatorActionCreator | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "creator": "creator",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "creator": "creator",
        }
