from dataclasses import dataclass, field

from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__2 import Help2
from .label_value import LabelValue
from .text_parameter_model_argument import TextParameterModelArgument
from .text_parameter_model_label import TextParameterModelLabel
from .text_parameter_model_validators import TextParameterModelValidators
from .text_parameter_model_value import TextParameterModelValue

__all__ = ["TextParameterModel"]


@dataclass
class TextParameterModel:
    """
    TextParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        area (bool | None)       :
        argument (TextParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        default_options (List[LabelValue] | None)
                                 :
        help_ (Help2 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (TextParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
        validators (TextParameterModelValidators | None)
                                 :
        value (TextParameterModelValue | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    area: bool | None = False
    argument: TextParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    default_options: list[LabelValue] | None = field(default_factory=list)
    help_: Help2 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: TextParameterModelLabel | None = None  # Will be displayed on the tool page as the label of the parameter.
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_text"
    validators: TextParameterModelValidators | None = None
    value: TextParameterModelValue | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "area": "area",
            "argument": "argument",
            "default_options": "default_options",
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
            "area": "area",
            "argument": "argument",
            "default_options": "default_options",
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
