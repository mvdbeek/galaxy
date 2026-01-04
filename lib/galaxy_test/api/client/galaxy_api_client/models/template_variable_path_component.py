from dataclasses import dataclass

from .default import Default
from .help_ import Help_
from .label import Label
from .validators import Validators

__all__ = ["TemplateVariablePathComponent"]


@dataclass
class TemplateVariablePathComponent:
    """
    TemplateVariablePathComponent dataclass.

    Args:
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        name (str)               :
        type_ (str)              :
        default (Optional[Default])
                                 : Whether or not this is a default quota. Valid values are
                                   ``no``, ``unregistered``, ``registered``. Calling this
                                   method with ``default="no"`` on a non-default quota will
                                   throw an error. Not passing this parameter is equivalent
                                   to passing ``no``.
        label (Optional[Label])  : Label of the input.
        validators (Optional[Validators])
                                 :
    """

    help_: Help_ | None  # Help text shown below the tool interface.
    name: str
    type_: str
    default: Default | None = (
        None  # Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. Calling this method with ``default="no"`` on a non-default quota will throw an error. Not passing this parameter is equivalent to passing ``no``.
    )
    label: Label | None = None  # Label of the input.
    validators: Validators | None = None
