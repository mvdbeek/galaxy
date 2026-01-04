from dataclasses import dataclass

from .help_ import Help_
from .label import Label
from .validators import Validators

__all__ = ["TemplateVariableString"]


@dataclass
class TemplateVariableString:
    """
    TemplateVariableString dataclass.

    Args:
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        name (str)               :
        type_ (str)              :
        default (Optional[str])  :
        label (Optional[Label])  : Label of the input.
        validators (Optional[Validators])
                                 :
    """

    help_: Help_ | None  # Help text shown below the tool interface.
    name: str
    type_: str
    default: str | None = ""
    label: Label | None = None  # Label of the input.
    validators: Validators | None = None
