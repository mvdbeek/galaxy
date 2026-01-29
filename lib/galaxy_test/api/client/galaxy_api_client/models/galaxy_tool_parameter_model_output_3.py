from typing import TypeAlias

from .base_url_parameter_model import BaseUrlParameterModel
from .boolean_parameter_model import BooleanParameterModel
from .color_parameter_model import ColorParameterModel
from .conditional_parameter_model_output import ConditionalParameterModelOutput
from .data_collection_parameter_model import DataCollectionParameterModel
from .data_column_parameter_model import DataColumnParameterModel
from .data_parameter_model import DataParameterModel
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

__all__ = ["GalaxyToolParameterModelOutput3"]

GalaxyToolParameterModelOutput3: TypeAlias = (
    BaseUrlParameterModel
    | BooleanParameterModel
    | ColorParameterModel
    | ConditionalParameterModelOutput
    | DataCollectionParameterModel
    | DataColumnParameterModel
    | DataParameterModel
    | DirectoryUriParameterModel
    | DrillDownParameterModelOutput
    | FloatParameterModel
    | GenomeBuildParameterModel
    | GroupTagParameterModel
    | HiddenParameterModel
    | IntegerParameterModel
    | RepeatParameterModelOutput
    | RulesParameterModel
    | SectionParameterModelOutput
    | SelectParameterModel
    | TextParameterModel
)
