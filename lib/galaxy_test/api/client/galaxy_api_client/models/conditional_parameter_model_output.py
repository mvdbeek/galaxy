from dataclasses import dataclass

from .conditional_parameter_model_output_argument import ConditionalParameterModelOutputArgument
from .conditional_parameter_model_output_help import ConditionalParameterModelOutputHelp
from .conditional_parameter_model_output_label import ConditionalParameterModelOutputLabel
from .conditional_parameter_model_output_test_parameter import ConditionalParameterModelOutputTestParameter
from .conditional_when_output import ConditionalWhenOutput
from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum

__all__ = ["ConditionalParameterModelOutput"]


@dataclass
class ConditionalParameterModelOutput:
    """
    ConditionalParameterModelOutput dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        test_parameter (ConditionalParameterModelOutputTestParameter)
                                 :
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        whens (List[ConditionalWhenOutput])
                                 :
        argument (ConditionalParameterModelOutputArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (ConditionalParameterModelOutputHelp | None)
                                 : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (ConditionalParameterModelOutputLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    test_parameter: ConditionalParameterModelOutputTestParameter
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    whens: list[ConditionalWhenOutput]
    argument: ConditionalParameterModelOutputArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: ConditionalParameterModelOutputHelp | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: ConditionalParameterModelOutputLabel | None = (
        None  # Will be displayed on the tool page as the label of the parameter.
    )
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_conditional"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "argument": "argument",
            "help": "help_",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "test_parameter": "test_parameter",
            "type": "type_",
            "whens": "whens",
        }
        key_transform_with_dump = {
            "argument": "argument",
            "help_": "help",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "test_parameter": "test_parameter",
            "type_": "type",
            "whens": "whens",
        }
