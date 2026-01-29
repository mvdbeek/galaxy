from dataclasses import dataclass
from typing import Any

from .galaxy_tool_parameter_model_input_type_enum import GalaxyToolParameterModelInputTypeEnum
from .help__25 import Help25
from .max__7 import Max7
from .min__7 import Min7
from .repeat_parameter_model_input_argument import RepeatParameterModelInputArgument
from .repeat_parameter_model_input_label import RepeatParameterModelInputLabel

__all__ = ["RepeatParameterModelInput"]


@dataclass
class RepeatParameterModelInput:
    """
    RepeatParameterModelInput dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameters (dict[str, Any])
                                 : [Circular reference detected:
                                   RepeatParameterModelInputParameters ->
                                   RepeatParameterModelInputParametersItem ->
                                   SectionParameterModelInput ->
                                   SectionParameterModelInputParameters ->
                                   SectionParameterModelInputParametersItem ->
                                   RepeatParameterModelInputParameters]
        type_ (GalaxyToolParameterModelInputTypeEnum)
                                 : Maps from 'type'
        argument (RepeatParameterModelInputArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help25 | None)    : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (RepeatParameterModelInputLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        max_ (Max7 | None)       : Maps from 'max'
        min_ (Min7 | None)       : Maps from 'min'
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameters: dict[
        str, Any
    ]  # [Circular reference detected: RepeatParameterModelInputParameters -> RepeatParameterModelInputParametersItem -> SectionParameterModelInput -> SectionParameterModelInputParameters -> SectionParameterModelInputParametersItem -> RepeatParameterModelInputParameters]
    type_: GalaxyToolParameterModelInputTypeEnum  # Maps from 'type'
    argument: RepeatParameterModelInputArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help25 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: RepeatParameterModelInputLabel | None = (
        None  # Will be displayed on the tool page as the label of the parameter.
    )
    max_: Max7 | None = None  # Maps from 'max'
    min_: Min7 | None = None  # Maps from 'min'
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_repeat"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "argument": "argument",
            "help": "help_",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "max": "max_",
            "min": "min_",
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
            "max_": "max",
            "min_": "min",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "parameters": "parameters",
            "type_": "type",
        }
