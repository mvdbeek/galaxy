from dataclasses import dataclass

from .argument import Argument
from .conditional_when_input_3 import ConditionalWhenInput3
from .help_ import Help_
from .label import Label
from .test_parameter import TestParameter

__all__ = ["ConditionalParameterModelInput"]


@dataclass
class ConditionalParameterModelInput:
    """
    ConditionalParameterModelInput dataclass.

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        test_parameter (TestParameter)
                                 :
        type_ (str)              :
        whens (List[ConditionalWhenInput3])
                                 :
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
        optional (Optional[bool]): If `false`, parameter must have a value.
        parameter_type (Optional[str])
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    test_parameter: TestParameter
    type_: str
    whens: list[ConditionalWhenInput3]
    argument: Argument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help_ | None = None  # Help text shown below the tool interface.
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: Label | None = None  # Label of the input.
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_conditional"
