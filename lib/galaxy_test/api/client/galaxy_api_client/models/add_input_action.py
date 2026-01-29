from dataclasses import dataclass

from .add_input_action_collection_type import AddInputActionCollectionType
from .add_input_action_default import AddInputActionDefault
from .add_input_action_label import AddInputActionLabel
from .add_input_action_optional import AddInputActionOptional
from .add_input_action_position import AddInputActionPosition
from .add_input_action_restrict_on_connections import AddInputActionRestrictOnConnections
from .add_input_action_restrictions import AddInputActionRestrictions
from .add_input_action_suggestions import AddInputActionSuggestions
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["AddInputAction"]


@dataclass
class AddInputAction:
    """
    AddInputAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        type_ (str)              : Maps from 'type'
        collection_type (AddInputActionCollectionType | None)
                                 :
        default (AddInputActionDefault | None)
                                 :
        label (AddInputActionLabel | None)
                                 :
        optional (AddInputActionOptional | None)
                                 :
        position (AddInputActionPosition | None)
                                 :
        restrict_on_connections (AddInputActionRestrictOnConnections | None)
                                 :
        restrictions (AddInputActionRestrictions | None)
                                 :
        suggestions (AddInputActionSuggestions | None)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    type_: str  # Maps from 'type'
    collection_type: AddInputActionCollectionType | None = None
    default: AddInputActionDefault | None = None
    label: AddInputActionLabel | None = None
    optional: AddInputActionOptional | None = False
    position: AddInputActionPosition | None = None
    restrict_on_connections: AddInputActionRestrictOnConnections | None = None
    restrictions: AddInputActionRestrictions | None = None
    suggestions: AddInputActionSuggestions | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "collection_type": "collection_type",
            "default": "default",
            "label": "label",
            "optional": "optional",
            "position": "position",
            "restrict_on_connections": "restrict_on_connections",
            "restrictions": "restrictions",
            "suggestions": "suggestions",
            "type": "type_",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "collection_type": "collection_type",
            "default": "default",
            "label": "label",
            "optional": "optional",
            "position": "position",
            "restrict_on_connections": "restrict_on_connections",
            "restrictions": "restrictions",
            "suggestions": "suggestions",
            "type_": "type",
        }
