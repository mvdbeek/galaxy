from dataclasses import dataclass

from .extract_input_action_label import ExtractInputActionLabel
from .extract_input_action_position import ExtractInputActionPosition
from .input__3 import Input3
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["ExtractInputAction"]


@dataclass
class ExtractInputAction:
    """
    ExtractInputAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        input_ (Input3)          : Maps from 'input'
        label (ExtractInputActionLabel | None)
                                 :
        position (ExtractInputActionPosition | None)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    input_: Input3  # Maps from 'input'
    label: ExtractInputActionLabel | None = None
    position: ExtractInputActionPosition | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "input": "input_",
            "label": "label",
            "position": "position",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "input_": "input",
            "label": "label",
            "position": "position",
        }
