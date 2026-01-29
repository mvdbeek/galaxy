from dataclasses import dataclass, field

from .float_parameter_model_argument import FloatParameterModelArgument
from .float_parameter_model_label import FloatParameterModelLabel
from .float_parameter_model_value import FloatParameterModelValue
from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__4 import Help4
from .in_range_parameter_validator_model import InRangeParameterValidatorModel
from .max__4 import Max4
from .min__4 import Min4

__all__ = ["FloatParameterModel"]


@dataclass
class FloatParameterModel:
    """
    FloatParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        argument (FloatParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help4 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (FloatParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        max_ (Max4 | None)       : Maps from 'max'
        min_ (Min4 | None)       : Maps from 'min'
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
        validators (List[InRangeParameterValidatorModel] | None)
                                 :
        value (FloatParameterModelValue | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    argument: FloatParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help4 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: FloatParameterModelLabel | None = None  # Will be displayed on the tool page as the label of the parameter.
    max_: Max4 | None = None  # Maps from 'max'
    min_: Min4 | None = None  # Maps from 'min'
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_float"
    validators: list[InRangeParameterValidatorModel] | None = field(default_factory=list)
    value: FloatParameterModelValue | None = None

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
            "max_": "max",
            "min_": "min",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "type_": "type",
            "validators": "validators",
            "value": "value",
        }
