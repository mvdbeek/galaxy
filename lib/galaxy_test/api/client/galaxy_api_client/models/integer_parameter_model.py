from dataclasses import dataclass, field

from .argument import Argument
from .help_ import Help_
from .in_range_parameter_validator_model import InRangeParameterValidatorModel
from .label import Label
from .max_ import Max_
from .min_ import Min_
from .value import Value

__all__ = ["IntegerParameterModel"]


@dataclass
class IntegerParameterModel:
    """
    IntegerParameterModel dataclass.

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (str)              :
        argument (Optional[Argument])
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        hidden (Optional[bool])  :
        is_dynamic (Optional[bool])
                                 :
        label (Optional[Label])  : Label of the input.
        max_ (Optional[Max_])    :
        min_ (Optional[Min_])    :
        optional (Optional[bool]):
        parameter_type (Optional[str])
                                 :
        validators (Optional[List[InRangeParameterValidatorModel]])
                                 :
        value (Optional[Value])  : TODO
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: str
    argument: Argument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help_ | None = None  # Help text shown below the tool interface.
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: Label | None = None  # Label of the input.
    max_: Max_ | None = None
    min_: Min_ | None = None
    optional: bool | None = False
    parameter_type: str | None = "gx_integer"
    validators: list[InRangeParameterValidatorModel] | None = field(default_factory=list)
    value: Value | None = False  # TODO
