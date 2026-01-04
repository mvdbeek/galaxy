from dataclasses import dataclass

from .argument import Argument
from .extensions import Extensions
from .help_ import Help_
from .label import Label
from .max_ import Max_
from .min_ import Min_

__all__ = ["DataParameterModel"]


@dataclass
class DataParameterModel:
    """
    DataParameterModel dataclass.

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
        extensions (Optional[Extensions])
                                 : Limit inputs to datasets with these extensions. Use
                                   'data' to allow all input datasets.
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        hidden (Optional[bool])  :
        is_dynamic (Optional[bool])
                                 :
        label (Optional[Label])  : Label of the input.
        max_ (Optional[Max_])    :
        min_ (Optional[Min_])    :
        multiple (Optional[bool]): Allow multiple values to be selected.
        optional (Optional[bool]): If `false`, parameter must have a value.
        parameter_type (Optional[str])
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: str
    argument: Argument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    extensions: Extensions | None = (
        None  # Limit inputs to datasets with these extensions. Use 'data' to allow all input datasets.
    )
    help_: Help_ | None = None  # Help text shown below the tool interface.
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: Label | None = None  # Label of the input.
    max_: Max_ | None = None
    min_: Min_ | None = None
    multiple: bool | None = False  # Allow multiple values to be selected.
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_data"
