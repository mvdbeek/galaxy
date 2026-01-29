from dataclasses import dataclass

from .boolean_parameter_model_argument import BooleanParameterModelArgument
from .boolean_parameter_model_falsevalue import BooleanParameterModelFalsevalue
from .boolean_parameter_model_label import BooleanParameterModelLabel
from .boolean_parameter_model_truevalue import BooleanParameterModelTruevalue
from .boolean_parameter_model_value import BooleanParameterModelValue
from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__5 import Help5

__all__ = ["BooleanParameterModel"]


@dataclass
class BooleanParameterModel:
    """
    BooleanParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        argument (BooleanParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        falsevalue (BooleanParameterModelFalsevalue | None)
                                 :
        help_ (Help5 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (BooleanParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
        truevalue (BooleanParameterModelTruevalue | None)
                                 :
        value (BooleanParameterModelValue | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    argument: BooleanParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    falsevalue: BooleanParameterModelFalsevalue | None = None
    help_: Help5 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: BooleanParameterModelLabel | None = None  # Will be displayed on the tool page as the label of the parameter.
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_boolean"
    truevalue: BooleanParameterModelTruevalue | None = None
    value: BooleanParameterModelValue | None = False

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "argument": "argument",
            "falsevalue": "falsevalue",
            "help": "help_",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "truevalue": "truevalue",
            "type": "type_",
            "value": "value",
        }
        key_transform_with_dump = {
            "argument": "argument",
            "falsevalue": "falsevalue",
            "help_": "help",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "truevalue": "truevalue",
            "type_": "type",
            "value": "value",
        }
