from dataclasses import dataclass

from .anonymous_array_item_56_type_enum import AnonymousArrayItem56TypeEnum
from .regex_parameter_validator_model_message import RegexParameterValidatorModelMessage

__all__ = ["RegexParameterValidatorModel"]


@dataclass
class RegexParameterValidatorModel:
    """
    Check if a regular expression **matches** the value, i.e. appears at the beginning of
    the value. To enforce a match of the complete value use ``$`` at the end of the
    expression. The expression is given is the content of the validator tag. Note that for
    ``selects`` each option is checked separately.

    Args:
        expression (str)         :
        implicit (bool | None)   :
        message (RegexParameterValidatorModelMessage | None)
                                 :
        negate (bool | None)     :
        type_ (AnonymousArrayItem56TypeEnum | None)
                                 : Maps from 'type'
    """

    expression: str
    implicit: bool | None = False
    message: RegexParameterValidatorModelMessage | None = None
    negate: bool | None = False
    type_: AnonymousArrayItem56TypeEnum | None = AnonymousArrayItem56TypeEnum.REGEX  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "expression": "expression",
            "implicit": "implicit",
            "message": "message",
            "negate": "negate",
            "type": "type_",
        }
        key_transform_with_dump = {
            "expression": "expression",
            "implicit": "implicit",
            "message": "message",
            "negate": "negate",
            "type_": "type",
        }
