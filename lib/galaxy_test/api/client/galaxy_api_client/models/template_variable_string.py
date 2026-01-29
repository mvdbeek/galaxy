from dataclasses import dataclass

from .help__38 import Help38
from .template_variable_string_label import TemplateVariableStringLabel
from .template_variable_string_validators import TemplateVariableStringValidators

__all__ = ["TemplateVariableString"]


@dataclass
class TemplateVariableString:
    """
    TemplateVariableString dataclass

    Args:
        help_ (Help38 | None)    : Maps from 'help'
        name (str)               :
        type_ (str)              : Maps from 'type'
        default (str | None)     :
        label (TemplateVariableStringLabel | None)
                                 :
        validators (TemplateVariableStringValidators | None)
                                 :
    """

    help_: Help38 | None  # Maps from 'help'
    name: str
    type_: str  # Maps from 'type'
    default: str | None = ""
    label: TemplateVariableStringLabel | None = None
    validators: TemplateVariableStringValidators | None = None

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
