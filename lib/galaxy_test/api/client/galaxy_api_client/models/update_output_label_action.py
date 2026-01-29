from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum
from .update_output_label_action_output import UpdateOutputLabelActionOutput

__all__ = ["UpdateOutputLabelAction"]


@dataclass
class UpdateOutputLabelAction:
    """
    UpdateOutputLabelAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        output (UpdateOutputLabelActionOutput)
                                 :
        output_label (str)       :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    output: UpdateOutputLabelActionOutput
    output_label: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "output": "output",
            "output_label": "output_label",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "output": "output",
            "output_label": "output_label",
        }
