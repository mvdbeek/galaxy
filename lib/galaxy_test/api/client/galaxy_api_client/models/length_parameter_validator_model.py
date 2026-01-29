from dataclasses import dataclass

from .anonymous_array_item_56_type_enum import AnonymousArrayItem56TypeEnum
from .length_parameter_validator_model_message import LengthParameterValidatorModelMessage
from .max_ import Max_
from .min_ import Min_

__all__ = ["LengthParameterValidatorModel"]


@dataclass
class LengthParameterValidatorModel:
    """
    LengthParameterValidatorModel dataclass

    Args:
        implicit (bool | None)   :
        max_ (Max_ | None)       : Maps from 'max'
        message (LengthParameterValidatorModelMessage | None)
                                 :
        min_ (Min_ | None)       : Maps from 'min'
        negate (bool | None)     :
        type_ (AnonymousArrayItem56TypeEnum | None)
                                 : Maps from 'type'
    """

    implicit: bool | None = False
    max_: Max_ | None = None  # Maps from 'max'
    message: LengthParameterValidatorModelMessage | None = None
    min_: Min_ | None = None  # Maps from 'min'
    negate: bool | None = False
    type_: AnonymousArrayItem56TypeEnum | None = AnonymousArrayItem56TypeEnum.LENGTH  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "implicit": "implicit",
            "max": "max_",
            "message": "message",
            "min": "min_",
            "negate": "negate",
            "type": "type_",
        }
        key_transform_with_dump = {
            "implicit": "implicit",
            "max_": "max",
            "message": "message",
            "min_": "min",
            "negate": "negate",
            "type_": "type",
        }
