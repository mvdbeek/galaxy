from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .in_range_parameter_validator_model import InRangeParameterValidatorModel
from .length_parameter_validator_model import LengthParameterValidatorModel
from .regex_parameter_validator_model import RegexParameterValidatorModel

__all__ = ["AnonymousArrayItem50", "AnonymousArrayItem50Discriminator"]


@dataclass(frozen=True)
class AnonymousArrayItem50Discriminator:
    """Discriminator metadata for AnonymousArrayItem50 union."""

    property_name: str = "type"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("in_range", "InRangeParameterValidatorModel"),
        ("length", "LengthParameterValidatorModel"),
        ("regex", "RegexParameterValidatorModel"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .in_range_parameter_validator_model import InRangeParameterValidatorModel
        from .length_parameter_validator_model import LengthParameterValidatorModel
        from .regex_parameter_validator_model import RegexParameterValidatorModel

        return {
            "in_range": InRangeParameterValidatorModel,
            "length": LengthParameterValidatorModel,
            "regex": RegexParameterValidatorModel,
        }


AnonymousArrayItem50: TypeAlias = Annotated[
    RegexParameterValidatorModel | InRangeParameterValidatorModel | LengthParameterValidatorModel,
    AnonymousArrayItem50Discriminator(),
]
