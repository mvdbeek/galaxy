from dataclasses import dataclass, field

from .data_parameter_model_argument import DataParameterModelArgument
from .data_parameter_model_label import DataParameterModelLabel
from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__8 import Help8
from .max__5 import Max5
from .min__5 import Min5

__all__ = ["DataParameterModel"]


@dataclass
class DataParameterModel:
    """
    DataParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        argument (DataParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        extensions (List[str] | None)
                                 : Limit inputs to datasets with these extensions. Use
                                   'data' to allow all input datasets.
        help_ (Help8 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (DataParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        max_ (Max5 | None)       : Maps from 'max'
        min_ (Min5 | None)       : Maps from 'min'
        multiple (bool | None)   : Allow multiple values to be selected.
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    argument: DataParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    extensions: list[str] | None = field(
        default_factory=list
    )  # Limit inputs to datasets with these extensions. Use 'data' to allow all input datasets.
    help_: Help8 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: DataParameterModelLabel | None = None  # Will be displayed on the tool page as the label of the parameter.
    max_: Max5 | None = None  # Maps from 'max'
    min_: Min5 | None = None  # Maps from 'min'
    multiple: bool | None = False  # Allow multiple values to be selected.
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_data"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "argument": "argument",
            "extensions": "extensions",
            "help": "help_",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "max": "max_",
            "min": "min_",
            "multiple": "multiple",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "type": "type_",
        }
        key_transform_with_dump = {
            "argument": "argument",
            "extensions": "extensions",
            "help_": "help",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "max_": "max",
            "min_": "min",
            "multiple": "multiple",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "type_": "type",
        }
