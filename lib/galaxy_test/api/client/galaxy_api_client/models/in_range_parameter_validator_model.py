from dataclasses import dataclass

from .anonymous_array_item_56_type_enum import AnonymousArrayItem56TypeEnum
from .in_range_parameter_validator_model_message import InRangeParameterValidatorModelMessage
from .max__3 import Max3
from .min__3 import Min3

__all__ = ["InRangeParameterValidatorModel"]


@dataclass
class InRangeParameterValidatorModel:
    """
    InRangeParameterValidatorModel dataclass

    Args:
        exclude_max (bool | None):
        exclude_min (bool | None):
        implicit (bool | None)   :
        max_ (Max3 | None)       : Maps from 'max'
        message (InRangeParameterValidatorModelMessage | None)
                                 :
        min_ (Min3 | None)       : Maps from 'min'
        negate (bool | None)     :
        type_ (AnonymousArrayItem56TypeEnum | None)
                                 : Maps from 'type'
    """

    exclude_max: bool | None = False
    exclude_min: bool | None = False
    implicit: bool | None = False
    max_: Max3 | None = None  # Maps from 'max'
    message: InRangeParameterValidatorModelMessage | None = None
    min_: Min3 | None = None  # Maps from 'min'
    negate: bool | None = False
    type_: AnonymousArrayItem56TypeEnum | None = AnonymousArrayItem56TypeEnum.IN_RANGE  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "exclude_max": "exclude_max",
            "exclude_min": "exclude_min",
            "implicit": "implicit",
            "max": "max_",
            "message": "message",
            "min": "min_",
            "negate": "negate",
            "type": "type_",
        }
        key_transform_with_dump = {
            "exclude_max": "exclude_max",
            "exclude_min": "exclude_min",
            "implicit": "implicit",
            "max_": "max",
            "message": "message",
            "min_": "min",
            "negate": "negate",
            "type_": "type",
        }
