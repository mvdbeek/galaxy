from dataclasses import dataclass, field

from .argument import Argument
from .help_ import Help_
from .label import Label
from .no_options_parameter_validator_model import NoOptionsParameterValidatorModel
from .options import Options

__all__ = ["SelectParameterModel"]


@dataclass
class SelectParameterModel:
    """
    SelectParameterModel dataclass.

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
        multiple (Optional[bool]):
        optional (Optional[bool]): If `false`, parameter must have a value.
        options (Optional[Options])
                                 :
        parameter_type (Optional[str])
                                 :
        validators (Optional[List[NoOptionsParameterValidatorModel]])
                                 :
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
    multiple: bool | None = False
    optional: bool | None = False  # If `false`, parameter must have a value.
    options: Options | None = None
    parameter_type: str | None = "gx_select"
    validators: list[NoOptionsParameterValidatorModel] | None = field(default_factory=list)
