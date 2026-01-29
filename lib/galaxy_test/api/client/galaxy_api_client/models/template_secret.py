from dataclasses import dataclass

from .help__37 import Help37
from .template_secret_label import TemplateSecretLabel

__all__ = ["TemplateSecret"]


@dataclass
class TemplateSecret:
    """
    TemplateSecret dataclass

    Args:
        help_ (Help37 | None)    : Maps from 'help'
        name (str)               :
        label (TemplateSecretLabel | None)
                                 :
    """

    help_: Help37 | None  # Maps from 'help'
    name: str
    label: TemplateSecretLabel | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "help": "help_",
            "label": "label",
            "name": "name",
        }
        key_transform_with_dump = {
            "help_": "help",
            "label": "label",
            "name": "name",
        }
