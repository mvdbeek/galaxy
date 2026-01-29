from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["UpdateNameAction"]


@dataclass
class UpdateNameAction:
    """
    UpdateNameAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        name (str)               :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    name: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "name": "name",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "name": "name",
        }
