from dataclasses import dataclass

from .extract_untyped_parameter_label import ExtractUntypedParameterLabel
from .extract_untyped_parameter_position import ExtractUntypedParameterPosition
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["ExtractUntypedParameter"]


@dataclass
class ExtractUntypedParameter:
    """
    ExtractUntypedParameter dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        name (str)               :
        label (ExtractUntypedParameterLabel | None)
                                 :
        position (ExtractUntypedParameterPosition | None)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    name: str
    label: ExtractUntypedParameterLabel | None = None
    position: ExtractUntypedParameterPosition | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "label": "label",
            "name": "name",
            "position": "position",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "label": "label",
            "name": "name",
            "position": "position",
        }
