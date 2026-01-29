from dataclasses import dataclass, field

from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__3 import Help3
from .in_range_parameter_validator_model import InRangeParameterValidatorModel
from .integer_parameter_model_argument import IntegerParameterModelArgument
from .integer_parameter_model_label import IntegerParameterModelLabel
from .integer_parameter_model_value import IntegerParameterModelValue
from .max__2 import Max2
from .min__2 import Min2

__all__ = ["IntegerParameterModel"]


@dataclass
class IntegerParameterModel:
    """
    IntegerParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        argument (IntegerParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help3 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (IntegerParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        max_ (Max2 | None)       : Maps from 'max'
        min_ (Min2 | None)       : Maps from 'min'
        optional (bool | None)   :
        parameter_type (str | None)
                                 :
        validators (List[InRangeParameterValidatorModel] | None)
                                 :
        value (IntegerParameterModelValue | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    argument: IntegerParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help3 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: IntegerParameterModelLabel | None = None  # Will be displayed on the tool page as the label of the parameter.
    max_: Max2 | None = None  # Maps from 'max'
    min_: Min2 | None = None  # Maps from 'min'
    optional: bool | None = False
    parameter_type: str | None = "gx_integer"
    validators: list[InRangeParameterValidatorModel] | None = field(default_factory=list)
    value: IntegerParameterModelValue | None = None

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
