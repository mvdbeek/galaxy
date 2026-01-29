from dataclasses import dataclass, field
from typing import Annotated, TypeAlias, Union

from .base_url_parameter_model import BaseUrlParameterModel
from .boolean_parameter_model import BooleanParameterModel
from .color_parameter_model import ColorParameterModel
from .conditional_parameter_model_input_2 import ConditionalParameterModelInput2
from .data_collection_parameter_model import DataCollectionParameterModel
from .data_column_parameter_model import DataColumnParameterModel
from .data_parameter_model import DataParameterModel
from .directory_uri_parameter_model import DirectoryUriParameterModel
from .drill_down_parameter_model_input_2 import DrillDownParameterModelInput2
from .float_parameter_model import FloatParameterModel
from .genome_build_parameter_model import GenomeBuildParameterModel
from .group_tag_parameter_model import GroupTagParameterModel
from .hidden_parameter_model import HiddenParameterModel
from .integer_parameter_model import IntegerParameterModel
from .repeat_parameter_model_input_3 import RepeatParameterModelInput3
from .rules_parameter_model import RulesParameterModel
from .section_parameter_model_input_3 import SectionParameterModelInput3
from .select_parameter_model import SelectParameterModel
from .text_parameter_model import TextParameterModel

from .base_url_parameter_model import BaseUrlParameterModel
from .boolean_parameter_model import BooleanParameterModel
from .color_parameter_model import ColorParameterModel
from .data_collection_parameter_model import DataCollectionParameterModel
from .data_column_parameter_model import DataColumnParameterModel
from .data_parameter_model import DataParameterModel
from .directory_uri_parameter_model import DirectoryUriParameterModel
from .float_parameter_model import FloatParameterModel
from .genome_build_parameter_model import GenomeBuildParameterModel
from .group_tag_parameter_model import GroupTagParameterModel
from .hidden_parameter_model import HiddenParameterModel
from .integer_parameter_model import IntegerParameterModel
from .rules_parameter_model import RulesParameterModel
from .select_parameter_model import SelectParameterModel
from .text_parameter_model import TextParameterModel

__all__ = ["GalaxyToolParameterModelInput2", "GalaxyToolParameterModelInput2Discriminator"]


@dataclass(frozen=True)
class GalaxyToolParameterModelInput2Discriminator:
    """Discriminator metadata for GalaxyToolParameterModelInput2 union."""

    property_name: str = "type"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("baseurl", "BaseUrlParameterModel"),
        ("boolean", "BooleanParameterModel"),
        ("color", "ColorParameterModel"),
        ("conditional", "ConditionalParameterModelInput"),
        ("data", "DataParameterModel"),
        ("data_collection", "DataCollectionParameterModel"),
        ("data_column", "DataColumnParameterModel"),
        ("directory", "DirectoryUriParameterModel"),
        ("drill_down", "DrillDownParameterModelInput"),
        ("float", "FloatParameterModel"),
        ("genomebuild", "GenomeBuildParameterModel"),
        ("group_tag", "GroupTagParameterModel"),
        ("hidden", "HiddenParameterModel"),
        ("integer", "IntegerParameterModel"),
        ("repeat", "RepeatParameterModelInput"),
        ("rules", "RulesParameterModel"),
        ("section", "SectionParameterModelInput"),
        ("select", "SelectParameterModel"),
        ("text", "TextParameterModel"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .base_url_parameter_model import BaseUrlParameterModel
        from .boolean_parameter_model import BooleanParameterModel
        from .color_parameter_model import ColorParameterModel
        from .conditional_parameter_model_input import ConditionalParameterModelInput
        from .data_parameter_model import DataParameterModel
        from .data_collection_parameter_model import DataCollectionParameterModel
        from .data_column_parameter_model import DataColumnParameterModel
        from .directory_uri_parameter_model import DirectoryUriParameterModel
        from .drill_down_parameter_model_input import DrillDownParameterModelInput
        from .float_parameter_model import FloatParameterModel
        from .genome_build_parameter_model import GenomeBuildParameterModel
        from .group_tag_parameter_model import GroupTagParameterModel
        from .hidden_parameter_model import HiddenParameterModel
        from .integer_parameter_model import IntegerParameterModel
        from .repeat_parameter_model_input import RepeatParameterModelInput
        from .rules_parameter_model import RulesParameterModel
        from .section_parameter_model_input import SectionParameterModelInput
        from .select_parameter_model import SelectParameterModel
        from .text_parameter_model import TextParameterModel

        return {
            "baseurl": BaseUrlParameterModel,
            "boolean": BooleanParameterModel,
            "color": ColorParameterModel,
            "conditional": ConditionalParameterModelInput,
            "data": DataParameterModel,
            "data_collection": DataCollectionParameterModel,
            "data_column": DataColumnParameterModel,
            "directory": DirectoryUriParameterModel,
            "drill_down": DrillDownParameterModelInput,
            "float": FloatParameterModel,
            "genomebuild": GenomeBuildParameterModel,
            "group_tag": GroupTagParameterModel,
            "hidden": HiddenParameterModel,
            "integer": IntegerParameterModel,
            "repeat": RepeatParameterModelInput,
            "rules": RulesParameterModel,
            "section": SectionParameterModelInput,
            "select": SelectParameterModel,
            "text": TextParameterModel,
        }


GalaxyToolParameterModelInput2: TypeAlias = Annotated[
    Union[
        TextParameterModel,
        IntegerParameterModel,
        FloatParameterModel,
        BooleanParameterModel,
        HiddenParameterModel,
        SelectParameterModel,
        DataParameterModel,
        DataCollectionParameterModel,
        DataColumnParameterModel,
        DirectoryUriParameterModel,
        RulesParameterModel,
        DrillDownParameterModelInput2,
        GroupTagParameterModel,
        BaseUrlParameterModel,
        GenomeBuildParameterModel,
        ColorParameterModel,
        ConditionalParameterModelInput2,
        RepeatParameterModelInput3,
        SectionParameterModelInput3,
    ],
    GalaxyToolParameterModelInput2Discriminator(),
]
