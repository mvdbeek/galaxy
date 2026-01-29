from dataclasses import dataclass

from .help_ import Help_
from .label import Label
from .validators import Validators

__all__ = ["TemplateVariableInteger"]


@dataclass
class TemplateVariableInteger:
    """
    TemplateVariableInteger dataclass.

    Args:
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        name (str)               :
        type_ (str)              :
        default (Optional[int])  :
        label (Optional[Label])  : Label of the input.
        validators (Optional[Validators])
                                 :
    """

    help_: Help_ | None  # Help text shown below the tool interface.
    name: str
    type_: str
    default: int | None = 0
    label: Label | None = None  # Label of the input.
    validators: Validators | None = None
