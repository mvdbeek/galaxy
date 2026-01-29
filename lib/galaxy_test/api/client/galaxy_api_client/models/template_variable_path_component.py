from dataclasses import dataclass

from .help__40 import Help40
from .template_variable_path_component_default import TemplateVariablePathComponentDefault
from .template_variable_path_component_label import TemplateVariablePathComponentLabel
from .template_variable_path_component_validators import TemplateVariablePathComponentValidators

__all__ = ["TemplateVariablePathComponent"]


@dataclass
class TemplateVariablePathComponent:
    """
    TemplateVariablePathComponent dataclass

    Args:
        help_ (Help40 | None)    : Maps from 'help'
        name (str)               :
        type_ (str)              : Maps from 'type'
        default (TemplateVariablePathComponentDefault | None)
                                 :
        label (TemplateVariablePathComponentLabel | None)
                                 :
        validators (TemplateVariablePathComponentValidators | None)
                                 :
    """

    help_: Help40 | None  # Maps from 'help'
    name: str
    type_: str  # Maps from 'type'
    default: TemplateVariablePathComponentDefault | None = None
    label: TemplateVariablePathComponentLabel | None = None
    validators: TemplateVariablePathComponentValidators | None = None

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
