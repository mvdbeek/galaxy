from dataclasses import dataclass

from .help_ import Help_
from .label import Label

__all__ = ["TemplateSecret"]


@dataclass
class TemplateSecret:
    """
    TemplateSecret dataclass.

    Args:
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        name (str)               :
        label (Optional[Label])  : Label of the input.
    """

    help_: Help_ | None  # Help text shown below the tool interface.
    name: str
    label: Label | None = None  # Label of the input.
