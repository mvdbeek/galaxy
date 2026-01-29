from dataclasses import dataclass

from .drill_down_parameter_model_output_argument import DrillDownParameterModelOutputArgument
from .drill_down_parameter_model_output_hierarchy import DrillDownParameterModelOutputHierarchy
from .drill_down_parameter_model_output_label import DrillDownParameterModelOutputLabel
from .drill_down_parameter_model_output_options import DrillDownParameterModelOutputOptions
from .help__30 import Help30

__all__ = ["DrillDownParameterModelOutput2"]


@dataclass
class DrillDownParameterModelOutput2:
    """
    DrillDownParameterModelOutput2 dataclass

    Args:
        hierarchy (DrillDownParameterModelOutputHierarchy)
                                 :
        multiple (bool)          :
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (str)              : Maps from 'type'
        argument (DrillDownParameterModelOutputArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help30 | None)    : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (DrillDownParameterModelOutputLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        options (DrillDownParameterModelOutputOptions | None)
                                 :
        parameter_type (str | None)
                                 :
    """

    hierarchy: DrillDownParameterModelOutputHierarchy
    multiple: bool
    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: str  # Maps from 'type'
    argument: DrillDownParameterModelOutputArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help30 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: DrillDownParameterModelOutputLabel | None = (
        None  # Will be displayed on the tool page as the label of the parameter.
    )
    optional: bool | None = False  # If `false`, parameter must have a value.
    options: DrillDownParameterModelOutputOptions | None = None
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
