from dataclasses import dataclass, field

from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__7 import Help7
from .no_options_parameter_validator_model import NoOptionsParameterValidatorModel
from .select_parameter_model_argument import SelectParameterModelArgument
from .select_parameter_model_label import SelectParameterModelLabel
from .select_parameter_model_options import SelectParameterModelOptions

__all__ = ["SelectParameterModel"]


@dataclass
class SelectParameterModel:
    """
    SelectParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        argument (SelectParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        help_ (Help7 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (SelectParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        multiple (bool | None)   :
        optional (bool | None)   : If `false`, parameter must have a value.
        options (SelectParameterModelOptions | None)
                                 :
        parameter_type (str | None)
                                 :
        validators (List[NoOptionsParameterValidatorModel] | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    argument: SelectParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    help_: Help7 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: SelectParameterModelLabel | None = None  # Will be displayed on the tool page as the label of the parameter.
    multiple: bool | None = False
    optional: bool | None = False  # If `false`, parameter must have a value.
    options: SelectParameterModelOptions | None = None
    parameter_type: str | None = "gx_select"
    validators: list[NoOptionsParameterValidatorModel] | None = field(default_factory=list)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "argument": "argument",
            "help": "help_",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "multiple": "multiple",
            "name": "name",
            "optional": "optional",
            "options": "options",
            "parameter_type": "parameter_type",
            "type": "type_",
            "validators": "validators",
        }
        key_transform_with_dump = {
            "argument": "argument",
            "help_": "help",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "multiple": "multiple",
            "name": "name",
            "optional": "optional",
            "options": "options",
            "parameter_type": "parameter_type",
            "type_": "type",
            "validators": "validators",
        }
