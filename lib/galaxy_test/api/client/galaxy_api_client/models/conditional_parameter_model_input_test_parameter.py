from typing import TypeAlias

from .boolean_parameter_model import BooleanParameterModel
from .select_parameter_model import SelectParameterModel

__all__ = ["ConditionalParameterModelInputTestParameter"]

ConditionalParameterModelInputTestParameter: TypeAlias = BooleanParameterModel | SelectParameterModel
