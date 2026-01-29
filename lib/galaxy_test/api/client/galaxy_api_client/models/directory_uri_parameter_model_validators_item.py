from typing import TypeAlias

from .empty_field_parameter_validator_model import EmptyFieldParameterValidatorModel
from .expression_parameter_validator_model import ExpressionParameterValidatorModel
from .length_parameter_validator_model import LengthParameterValidatorModel
from .regex_parameter_validator_model import RegexParameterValidatorModel

__all__ = ["DirectoryUriParameterModelValidatorsItem"]

DirectoryUriParameterModelValidatorsItem: TypeAlias = (
    LengthParameterValidatorModel
    | RegexParameterValidatorModel
    | ExpressionParameterValidatorModel
    | EmptyFieldParameterValidatorModel
)
