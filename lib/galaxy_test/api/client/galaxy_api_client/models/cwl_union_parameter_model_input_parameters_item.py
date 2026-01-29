from typing import TypeAlias

from .cwl_boolean_parameter_model import CwlBooleanParameterModel
from .cwl_directory_parameter_model import CwlDirectoryParameterModel
from .cwl_file_parameter_model import CwlFileParameterModel
from .cwl_float_parameter_model import CwlFloatParameterModel
from .cwl_integer_parameter_model import CwlIntegerParameterModel
from .cwl_null_parameter_model import CwlNullParameterModel
from .cwl_string_parameter_model import CwlStringParameterModel
from .cwl_union_parameter_model_input import CwlUnionParameterModelInput

__all__ = ["CwlUnionParameterModelInputParametersItem"]

CwlUnionParameterModelInputParametersItem: TypeAlias = (
    CwlIntegerParameterModel
    | CwlFloatParameterModel
    | CwlStringParameterModel
    | CwlBooleanParameterModel
    | CwlNullParameterModel
    | CwlFileParameterModel
    | CwlDirectoryParameterModel
    | CwlUnionParameterModelInput
)
