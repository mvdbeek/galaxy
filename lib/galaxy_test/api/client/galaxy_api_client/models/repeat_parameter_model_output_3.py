from dataclasses import dataclass

from .help__29 import Help29
from .max__8 import Max8
from .min__8 import Min8
from .repeat_parameter_model_output_argument import RepeatParameterModelOutputArgument
from .repeat_parameter_model_output_label import RepeatParameterModelOutputLabel
from .repeat_parameter_model_output_parameters import RepeatParameterModelOutputParameters

__all__ = ["RepeatParameterModelOutput3"]


@dataclass
class RepeatParameterModelOutput3:
    """
    RepeatParameterModelOutput3 dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameters (RepeatParameterModelOutputParameters)
                                 :
        type_ (str)              : Maps from 'type'
        argument (RepeatParameterModelOutputArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help29 | None)    : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (RepeatParameterModelOutputLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        max_ (Max8 | None)       : Maps from 'max'
        min_ (Min8 | None)       : Maps from 'min'
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameters: RepeatParameterModelOutputParameters
    type_: str  # Maps from 'type'
    argument: RepeatParameterModelOutputArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help29 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: RepeatParameterModelOutputLabel | None = (
        None  # Will be displayed on the tool page as the label of the parameter.
    )
    max_: Max8 | None = None  # Maps from 'max'
    min_: Min8 | None = None  # Maps from 'min'
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
