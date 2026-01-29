from dataclasses import dataclass

from .help__39 import Help39
from .template_variable_integer_label import TemplateVariableIntegerLabel
from .template_variable_integer_validators import TemplateVariableIntegerValidators

__all__ = ["TemplateVariableInteger"]


@dataclass
class TemplateVariableInteger:
    """
    TemplateVariableInteger dataclass

    Args:
        help_ (Help39 | None)    : Maps from 'help'
        name (str)               :
        type_ (str)              : Maps from 'type'
        default (int | None)     :
        label (TemplateVariableIntegerLabel | None)
                                 :
        validators (TemplateVariableIntegerValidators | None)
                                 :
    """

    help_: Help39 | None  # Maps from 'help'
    name: str
    type_: str  # Maps from 'type'
    default: int | None = 0
    label: TemplateVariableIntegerLabel | None = None
    validators: TemplateVariableIntegerValidators | None = None

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
