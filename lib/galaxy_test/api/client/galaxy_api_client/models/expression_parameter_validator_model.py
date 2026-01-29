from dataclasses import dataclass

from .expression_parameter_validator_model_message import ExpressionParameterValidatorModelMessage

__all__ = ["ExpressionParameterValidatorModel"]


@dataclass
class ExpressionParameterValidatorModel:
    """
    Check if a one line python expression given expression evaluates to True.  The
    expression is given is the content of the validator tag.

    Args:
        expression (str)         :
        implicit (bool | None)   :
        message (ExpressionParameterValidatorModelMessage | None)
                                 :
        negate (bool | None)     :
        type_ (str | None)       : Maps from 'type'
    """

    expression: str
    implicit: bool | None = False
    message: ExpressionParameterValidatorModelMessage | None = None
    negate: bool | None = False
    type_: str | None = "expression"  # Maps from 'type'

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
