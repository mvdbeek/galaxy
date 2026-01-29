from dataclasses import dataclass

from .galaxy_tool_parameter_model_input_type_enum import GalaxyToolParameterModelInputTypeEnum
from .help__24 import Help24
from .section_parameter_model_input_argument import SectionParameterModelInputArgument
from .section_parameter_model_input_label import SectionParameterModelInputLabel
from .section_parameter_model_input_parameters import SectionParameterModelInputParameters

__all__ = ["SectionParameterModelInput2"]


@dataclass
class SectionParameterModelInput2:
    """
    SectionParameterModelInput2 dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameters (SectionParameterModelInputParameters)
                                 :
        type_ (GalaxyToolParameterModelInputTypeEnum)
                                 : Maps from 'type'
        argument (SectionParameterModelInputArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help24 | None)    : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (SectionParameterModelInputLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameters: SectionParameterModelInputParameters
    type_: GalaxyToolParameterModelInputTypeEnum  # Maps from 'type'
    argument: SectionParameterModelInputArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help24 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: SectionParameterModelInputLabel | None = (
        None  # Will be displayed on the tool page as the label of the parameter.
    )
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_section"

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
            "parameters": "parameters",
            "type": "type_",
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
            "parameters": "parameters",
            "type_": "type",
        }
