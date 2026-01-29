from dataclasses import dataclass

from .drill_down_parameter_model_input_argument import DrillDownParameterModelInputArgument
from .drill_down_parameter_model_input_hierarchy import DrillDownParameterModelInputHierarchy
from .drill_down_parameter_model_input_label import DrillDownParameterModelInputLabel
from .drill_down_parameter_model_input_options import DrillDownParameterModelInputOptions
from .galaxy_tool_parameter_model_input_type_enum import GalaxyToolParameterModelInputTypeEnum
from .help__13 import Help13

__all__ = ["DrillDownParameterModelInput"]


@dataclass
class DrillDownParameterModelInput:
    """
    DrillDownParameterModelInput dataclass

    Args:
        hierarchy (DrillDownParameterModelInputHierarchy)
                                 :
        multiple (bool)          :
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelInputTypeEnum)
                                 : Maps from 'type'
        argument (DrillDownParameterModelInputArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help13 | None)    : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (DrillDownParameterModelInputLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        options (DrillDownParameterModelInputOptions | None)
                                 :
        parameter_type (str | None)
                                 :
    """

    hierarchy: DrillDownParameterModelInputHierarchy
    multiple: bool
    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelInputTypeEnum  # Maps from 'type'
    argument: DrillDownParameterModelInputArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help13 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: DrillDownParameterModelInputLabel | None = (
        None  # Will be displayed on the tool page as the label of the parameter.
    )
    optional: bool | None = False  # If `false`, parameter must have a value.
    options: DrillDownParameterModelInputOptions | None = None
    parameter_type: str | None = "gx_drill_down"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "argument": "argument",
            "help": "help_",
            "hidden": "hidden",
            "hierarchy": "hierarchy",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "multiple": "multiple",
            "name": "name",
            "optional": "optional",
            "options": "options",
            "parameter_type": "parameter_type",
            "type": "type_",
        }
        key_transform_with_dump = {
            "argument": "argument",
            "help_": "help",
            "hidden": "hidden",
            "hierarchy": "hierarchy",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "multiple": "multiple",
            "name": "name",
            "optional": "optional",
            "options": "options",
            "parameter_type": "parameter_type",
            "type_": "type",
        }
