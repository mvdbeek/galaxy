from dataclasses import dataclass

from .help__41 import Help41
from .template_variable_boolean_label import TemplateVariableBooleanLabel
from .template_variable_boolean_validators import TemplateVariableBooleanValidators

__all__ = ["TemplateVariableBoolean"]


@dataclass
class TemplateVariableBoolean:
    """
    TemplateVariableBoolean dataclass

    Args:
        help_ (Help41 | None)    : Maps from 'help'
        name (str)               :
        type_ (str)              : Maps from 'type'
        default (bool | None)    :
        label (TemplateVariableBooleanLabel | None)
                                 :
        validators (TemplateVariableBooleanValidators | None)
                                 :
    """

    help_: Help41 | None  # Maps from 'help'
    name: str
    type_: str  # Maps from 'type'
    default: bool | None = False
    label: TemplateVariableBooleanLabel | None = None
    validators: TemplateVariableBooleanValidators | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "default": "default",
            "help": "help_",
            "label": "label",
            "name": "name",
            "type": "type_",
            "validators": "validators",
        }
        key_transform_with_dump = {
            "default": "default",
            "help_": "help",
            "label": "label",
            "name": "name",
            "type_": "type",
            "validators": "validators",
        }
