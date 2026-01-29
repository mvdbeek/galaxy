from dataclasses import dataclass

from .sample_sheet_column_definition_model_default_value import SampleSheetColumnDefinitionModelDefaultValue
from .sample_sheet_column_definition_model_description import SampleSheetColumnDefinitionModelDescription
from .sample_sheet_column_definition_model_restrictions import SampleSheetColumnDefinitionModelRestrictions
from .sample_sheet_column_definition_model_suggestions import SampleSheetColumnDefinitionModelSuggestions
from .sample_sheet_column_definition_model_validators import SampleSheetColumnDefinitionModelValidators
from .type__6 import Type6

__all__ = ["SampleSheetColumnDefinitionModel"]


@dataclass
class SampleSheetColumnDefinitionModel:
    """
    SampleSheetColumnDefinitionModel dataclass

    Args:
        name (str)               :
        optional (bool)          :
        type_ (Type6)            : Maps from 'type'
        default_value (SampleSheetColumnDefinitionModelDefaultValue | None)
                                 :
        description (SampleSheetColumnDefinitionModelDescription | None)
                                 :
        restrictions (SampleSheetColumnDefinitionModelRestrictions | None)
                                 :
        suggestions (SampleSheetColumnDefinitionModelSuggestions | None)
                                 :
        validators (SampleSheetColumnDefinitionModelValidators | None)
                                 :
    """

    name: str
    optional: bool
    type_: Type6  # Maps from 'type'
    default_value: SampleSheetColumnDefinitionModelDefaultValue | None = None
    description: SampleSheetColumnDefinitionModelDescription | None = None
    restrictions: SampleSheetColumnDefinitionModelRestrictions | None = None
    suggestions: SampleSheetColumnDefinitionModelSuggestions | None = None
    validators: SampleSheetColumnDefinitionModelValidators | None = None

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
