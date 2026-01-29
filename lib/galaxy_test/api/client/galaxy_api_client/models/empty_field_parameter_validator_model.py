from dataclasses import dataclass

from .empty_field_parameter_validator_model_message import EmptyFieldParameterValidatorModelMessage

__all__ = ["EmptyFieldParameterValidatorModel"]


@dataclass
class EmptyFieldParameterValidatorModel:
    """
    EmptyFieldParameterValidatorModel dataclass

    Args:
        implicit (bool | None)   :
        message (EmptyFieldParameterValidatorModelMessage | None)
                                 :
        negate (bool | None)     :
        type_ (str | None)       : Maps from 'type'
    """

    implicit: bool | None = False
    message: EmptyFieldParameterValidatorModelMessage | None = None
    negate: bool | None = False
    type_: str | None = "empty_field"  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "implicit": "implicit",
            "message": "message",
            "negate": "negate",
            "type": "type_",
        }
        key_transform_with_dump = {
            "implicit": "implicit",
            "message": "message",
            "negate": "negate",
            "type_": "type",
        }
