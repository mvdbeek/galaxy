from typing import TypeAlias

from .base_url_parameter_model import BaseUrlParameterModel
from .boolean_parameter_model import BooleanParameterModel
from .color_parameter_model import ColorParameterModel
from .conditional_parameter_model_input import ConditionalParameterModelInput
from .data_collection_parameter_model import DataCollectionParameterModel
from .data_column_parameter_model import DataColumnParameterModel
from .data_parameter_model import DataParameterModel
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

__all__ = ["GalaxyToolParameterModelInput4"]

GalaxyToolParameterModelInput4: TypeAlias = (
    BaseUrlParameterModel
    | BooleanParameterModel
    | ColorParameterModel
    | ConditionalParameterModelInput
    | DataCollectionParameterModel
    | DataColumnParameterModel
    | DataParameterModel
    | DirectoryUriParameterModel
    | DrillDownParameterModelInput
    | FloatParameterModel
    | GenomeBuildParameterModel
    | GroupTagParameterModel
    | HiddenParameterModel
    | IntegerParameterModel
    | RepeatParameterModelInput
    | RulesParameterModel
    | SectionParameterModelInput
    | SelectParameterModel
    | TextParameterModel
)
