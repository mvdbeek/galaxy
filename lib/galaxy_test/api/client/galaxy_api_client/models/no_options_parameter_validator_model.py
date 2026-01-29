from dataclasses import dataclass

from .no_options_parameter_validator_model_message import NoOptionsParameterValidatorModelMessage

__all__ = ["NoOptionsParameterValidatorModel"]


@dataclass
class NoOptionsParameterValidatorModel:
    """
    NoOptionsParameterValidatorModel dataclass

    Args:
        implicit (bool | None)   :
        message (NoOptionsParameterValidatorModelMessage | None)
                                 :
        negate (bool | None)     :
        type_ (str | None)       : Maps from 'type'
    """

    implicit: bool | None = False
    message: NoOptionsParameterValidatorModelMessage | None = None
    negate: bool | None = False
    type_: str | None = "no_options"  # Maps from 'type'

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
