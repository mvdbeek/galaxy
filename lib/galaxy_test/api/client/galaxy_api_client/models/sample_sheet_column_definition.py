from dataclasses import dataclass

from .sample_sheet_column_definition_default_value import SampleSheetColumnDefinitionDefaultValue
from .sample_sheet_column_definition_description import SampleSheetColumnDefinitionDescription
from .sample_sheet_column_definition_restrictions import SampleSheetColumnDefinitionRestrictions
from .sample_sheet_column_definition_suggestions import SampleSheetColumnDefinitionSuggestions
from .sample_sheet_column_definition_validators import SampleSheetColumnDefinitionValidators
from .type__3 import Type3

__all__ = ["SampleSheetColumnDefinition"]


@dataclass
class SampleSheetColumnDefinition:
    """
    SampleSheetColumnDefinition dataclass

    Args:
        name (str)               :
        optional (bool)          :
        type_ (Type3)            : Maps from 'type'
        default_value (SampleSheetColumnDefinitionDefaultValue | None)
                                 :
        description (SampleSheetColumnDefinitionDescription | None)
                                 :
        restrictions (SampleSheetColumnDefinitionRestrictions | None)
                                 :
        suggestions (SampleSheetColumnDefinitionSuggestions | None)
                                 :
        validators (SampleSheetColumnDefinitionValidators | None)
                                 :
    """

    name: str
    optional: bool
    type_: Type3  # Maps from 'type'
    default_value: SampleSheetColumnDefinitionDefaultValue | None = None
    description: SampleSheetColumnDefinitionDescription | None = None
    restrictions: SampleSheetColumnDefinitionRestrictions | None = None
    suggestions: SampleSheetColumnDefinitionSuggestions | None = None
    validators: SampleSheetColumnDefinitionValidators | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "default_value": "default_value",
            "description": "description",
            "name": "name",
            "optional": "optional",
            "restrictions": "restrictions",
            "suggestions": "suggestions",
            "type": "type_",
            "validators": "validators",
        }
        key_transform_with_dump = {
            "default_value": "default_value",
            "description": "description",
            "name": "name",
            "optional": "optional",
            "restrictions": "restrictions",
            "suggestions": "suggestions",
            "type_": "type",
            "validators": "validators",
        }
