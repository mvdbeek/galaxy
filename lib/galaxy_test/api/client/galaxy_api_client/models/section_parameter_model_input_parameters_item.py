from typing import TypeAlias

from .base_url_parameter_model import BaseUrlParameterModel
from .boolean_parameter_model import BooleanParameterModel
from .color_parameter_model import ColorParameterModel
from .conditional_parameter_model_input_3 import ConditionalParameterModelInput3
from .cwl_boolean_parameter_model import CwlBooleanParameterModel
from .cwl_directory_parameter_model import CwlDirectoryParameterModel
from .cwl_file_parameter_model import CwlFileParameterModel
from .cwl_float_parameter_model import CwlFloatParameterModel
from .cwl_integer_parameter_model import CwlIntegerParameterModel
from .cwl_null_parameter_model import CwlNullParameterModel
from .cwl_string_parameter_model import CwlStringParameterModel
from .cwl_union_parameter_model_input_3 import CwlUnionParameterModelInput3
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
from .repeat_parameter_model_input import RepeatParameterModelInput
from .rules_parameter_model import RulesParameterModel
from .section_parameter_model_input import SectionParameterModelInput
from .select_parameter_model import SelectParameterModel
from .text_parameter_model import TextParameterModel

__all__ = ["SectionParameterModelInputParametersItem"]

SectionParameterModelInputParametersItem: TypeAlias = (
    CwlIntegerParameterModel
    | CwlFloatParameterModel
    | CwlStringParameterModel
    | CwlBooleanParameterModel
    | CwlNullParameterModel
    | CwlFileParameterModel
    | CwlDirectoryParameterModel
    | CwlUnionParameterModelInput3
    | TextParameterModel
    | IntegerParameterModel
    | FloatParameterModel
    | BooleanParameterModel
    | HiddenParameterModel
    | SelectParameterModel
    | DataParameterModel
    | DataCollectionParameterModel
    | DataColumnParameterModel
    | DirectoryUriParameterModel
    | RulesParameterModel
    | DrillDownParameterModelInput2
    | GroupTagParameterModel
    | BaseUrlParameterModel
    | GenomeBuildParameterModel
    | ColorParameterModel
    | ConditionalParameterModelInput3
    | RepeatParameterModelInput
    | SectionParameterModelInput
)
