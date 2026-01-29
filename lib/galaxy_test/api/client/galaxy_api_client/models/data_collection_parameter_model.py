from dataclasses import dataclass, field

from .data_collection_parameter_model_argument import DataCollectionParameterModelArgument
from .data_collection_parameter_model_collection_type import DataCollectionParameterModelCollectionType
from .data_collection_parameter_model_label import DataCollectionParameterModelLabel
from .data_collection_parameter_model_value import DataCollectionParameterModelValue
from .galaxy_tool_parameter_model_output_type_enum import GalaxyToolParameterModelOutputTypeEnum
from .help__9 import Help9

__all__ = ["DataCollectionParameterModel"]


@dataclass
class DataCollectionParameterModel:
    """
    DataCollectionParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        type_ (GalaxyToolParameterModelOutputTypeEnum)
                                 : Maps from 'type'
        value (DataCollectionParameterModelValue)
                                 :
        argument (DataCollectionParameterModelArgument | None)
                                 : If the parameter reflects just one command line argument
                                   of a certain tool, this tag should be set to that
                                   particular argument. It is rendered in parenthesis after
                                   the help section, and it will create the name attribute
                                   (if not given explicitly) from the argument attribute by
                                   stripping leading dashes and replacing all remaining
                                   dashes by underscores (e.g. if argument="--long-
                                   parameter" then name="long_parameter" is implicit).
        collection_type (DataCollectionParameterModelCollectionType | None)
                                 :
        extensions (List[str] | None)
                                 :
        help_ (Help9 | None)     : Short bit of text, rendered on the tool form just below
                                   the associated field to provide information about the
                                   field. (maps from 'help')
        hidden (bool | None)     :
        is_dynamic (bool | None) :
        label (DataCollectionParameterModelLabel | None)
                                 : Will be displayed on the tool page as the label of the
                                   parameter.
        optional (bool | None)   : If `false`, parameter must have a value.
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    type_: GalaxyToolParameterModelOutputTypeEnum  # Maps from 'type'
    value: DataCollectionParameterModelValue
    argument: DataCollectionParameterModelArgument | None = (
        None  # If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).
    )
    collection_type: DataCollectionParameterModelCollectionType | None = None
    extensions: list[str] | None = field(default_factory=list)
    help_: Help9 | None = (
        None  # Short bit of text, rendered on the tool form just below the associated field to provide information about the field. (maps from 'help')
    )
    hidden: bool | None = False
    is_dynamic: bool | None = False
    label: DataCollectionParameterModelLabel | None = (
        None  # Will be displayed on the tool page as the label of the parameter.
    )
    optional: bool | None = False  # If `false`, parameter must have a value.
    parameter_type: str | None = "gx_data_collection"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "argument": "argument",
            "collection_type": "collection_type",
            "extensions": "extensions",
            "help": "help_",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "type": "type_",
            "value": "value",
        }
        key_transform_with_dump = {
            "argument": "argument",
            "collection_type": "collection_type",
            "extensions": "extensions",
            "help_": "help",
            "hidden": "hidden",
            "is_dynamic": "is_dynamic",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "parameter_type": "parameter_type",
            "type_": "type",
            "value": "value",
        }
