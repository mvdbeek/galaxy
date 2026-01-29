from dataclasses import dataclass

from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__6 import Help6
from .hidden_parameter_model_argument import HiddenParameterModelArgument
from .hidden_parameter_model_label import HiddenParameterModelLabel
from .hidden_parameter_model_validators import HiddenParameterModelValidators
from .hidden_parameter_model_value import HiddenParameterModelValue

__all__ = ["HiddenParameterModel"]


@dataclass
class HiddenParameterModel:
    """
    HiddenParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        value (HiddenParameterModelValue)
                                 :
        argument (HiddenParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help6 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (HiddenParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
        validators (HiddenParameterModelValidators | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    value: HiddenParameterModelValue
    argument: HiddenParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help6 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: HiddenParameterModelLabel | None = None  # Will be displayed on the tool page as the label of the parameter.
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_hidden"
    validators: HiddenParameterModelValidators | None = None

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
            "type": "type_",
            "validators": "validators",
            "value": "value",
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
            "type_": "type",
            "validators": "validators",
            "value": "value",
        }
