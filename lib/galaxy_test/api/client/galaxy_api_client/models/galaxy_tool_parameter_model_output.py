from dataclasses import dataclass, field
from typing import Annotated, TypeAlias, Union

from .base_url_parameter_model import BaseUrlParameterModel
from .boolean_parameter_model import BooleanParameterModel
from .color_parameter_model import ColorParameterModel
from .conditional_parameter_model_output_2 import ConditionalParameterModelOutput2
from .data_collection_parameter_model import DataCollectionParameterModel
from .data_column_parameter_model import DataColumnParameterModel
from .data_parameter_model import DataParameterModel
from .directory_uri_parameter_model import DirectoryUriParameterModel
from .drill_down_parameter_model_output_2 import DrillDownParameterModelOutput2
from .float_parameter_model import FloatParameterModel
from .genome_build_parameter_model import GenomeBuildParameterModel
from .group_tag_parameter_model import GroupTagParameterModel
from .hidden_parameter_model import HiddenParameterModel
from .integer_parameter_model import IntegerParameterModel
from .repeat_parameter_model_output_3 import RepeatParameterModelOutput3
from .rules_parameter_model import RulesParameterModel
from .section_parameter_model_output_3 import SectionParameterModelOutput3
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

__all__ = ["GalaxyToolParameterModelOutput", "GalaxyToolParameterModelOutputDiscriminator"]


@dataclass(frozen=True)
class GalaxyToolParameterModelOutputDiscriminator:
    """Discriminator metadata for GalaxyToolParameterModelOutput union."""

    property_name: str = "type"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("baseurl", "BaseUrlParameterModel"),
        ("boolean", "BooleanParameterModel"),
        ("color", "ColorParameterModel"),
        ("conditional", "ConditionalParameterModelOutput"),
        ("data", "DataParameterModel"),
        ("data_collection", "DataCollectionParameterModel"),
        ("data_column", "DataColumnParameterModel"),
        ("directory", "DirectoryUriParameterModel"),
        ("drill_down", "DrillDownParameterModelOutput"),
        ("float", "FloatParameterModel"),
        ("genomebuild", "GenomeBuildParameterModel"),
        ("group_tag", "GroupTagParameterModel"),
        ("hidden", "HiddenParameterModel"),
        ("integer", "IntegerParameterModel"),
        ("repeat", "RepeatParameterModelOutput"),
        ("rules", "RulesParameterModel"),
        ("section", "SectionParameterModelOutput"),
        ("select", "SelectParameterModel"),
        ("text", "TextParameterModel"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .base_url_parameter_model import BaseUrlParameterModel
        from .boolean_parameter_model import BooleanParameterModel
        from .color_parameter_model import ColorParameterModel
        from .conditional_parameter_model_output import ConditionalParameterModelOutput
        from .data_parameter_model import DataParameterModel
        from .data_collection_parameter_model import DataCollectionParameterModel
        from .data_column_parameter_model import DataColumnParameterModel
        from .directory_uri_parameter_model import DirectoryUriParameterModel
        from .drill_down_parameter_model_output import DrillDownParameterModelOutput
        from .float_parameter_model import FloatParameterModel
        from .genome_build_parameter_model import GenomeBuildParameterModel
        from .group_tag_parameter_model import GroupTagParameterModel
        from .hidden_parameter_model import HiddenParameterModel
        from .integer_parameter_model import IntegerParameterModel
        from .repeat_parameter_model_output import RepeatParameterModelOutput
        from .rules_parameter_model import RulesParameterModel
        from .section_parameter_model_output import SectionParameterModelOutput
        from .select_parameter_model import SelectParameterModel
        from .text_parameter_model import TextParameterModel

        return {
            "baseurl": BaseUrlParameterModel,
            "boolean": BooleanParameterModel,
            "color": ColorParameterModel,
            "conditional": ConditionalParameterModelOutput,
            "data": DataParameterModel,
            "data_collection": DataCollectionParameterModel,
            "data_column": DataColumnParameterModel,
            "directory": DirectoryUriParameterModel,
            "drill_down": DrillDownParameterModelOutput,
            "float": FloatParameterModel,
            "genomebuild": GenomeBuildParameterModel,
            "group_tag": GroupTagParameterModel,
            "hidden": HiddenParameterModel,
            "integer": IntegerParameterModel,
            "repeat": RepeatParameterModelOutput,
            "rules": RulesParameterModel,
            "section": SectionParameterModelOutput,
            "select": SelectParameterModel,
            "text": TextParameterModel,
        }


GalaxyToolParameterModelOutput: TypeAlias = Annotated[
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
        DrillDownParameterModelOutput2,
        GroupTagParameterModel,
        BaseUrlParameterModel,
        GenomeBuildParameterModel,
        ColorParameterModel,
        ConditionalParameterModelOutput2,
        RepeatParameterModelOutput3,
        SectionParameterModelOutput3,
    ],
    GalaxyToolParameterModelOutputDiscriminator(),
]
