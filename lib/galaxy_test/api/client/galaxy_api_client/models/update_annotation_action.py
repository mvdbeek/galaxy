from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["UpdateAnnotationAction"]


@dataclass
class UpdateAnnotationAction:
    """
    UpdateAnnotationAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        annotation (str)         :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    annotation: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "annotation": "annotation",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "annotation": "annotation",
        }
