from dataclasses import dataclass, field

from .argument import Argument
from .help_ import Help_
from .label import Label
from .label_value import LabelValue
from .validators import Validators
from .value import Value

__all__ = ["TextParameterModel"]


@dataclass
class TextParameterModel:
    """
    TextParameterModel dataclass.

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (str)              :
        area (Optional[bool])    :
        argument (Optional[Argument])
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        default_options (Optional[List[LabelValue]])
                                 :
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        hidden (Optional[bool])  :
        is_dynamic (Optional[bool])
                                 :
        label (Optional[Label])  : Label of the input.
        optional (Optional[bool]): If `false`, parameter must have a value.
        parameter_type (Optional[str])
                                 :
        validators (Optional[Validators])
                                 :
        value (Optional[Value])  : TODO
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: str
    area: bool | None = False
    argument: Argument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    default_options: list[LabelValue] | None = field(default_factory=list)
    help_: Help_ | None = None  # Help text shown below the tool interface.
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: Label | None = None  # Label of the input.
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_text"
    validators: Validators | None = None
    value: Value | None = False  # TODO
