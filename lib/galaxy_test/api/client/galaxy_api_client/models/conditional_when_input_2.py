from dataclasses import dataclass

from .conditional_when_input_discriminator import ConditionalWhenInputDiscriminator
from .conditional_when_input_parameters import ConditionalWhenInputParameters

__all__ = ["ConditionalWhenInput2"]


@dataclass
class ConditionalWhenInput2:
    """
    ConditionalWhenInput2 dataclass

    Args:
        discriminator (ConditionalWhenInputDiscriminator)
                                 :
        is_default_when (bool)   :
        parameters (ConditionalWhenInputParameters)
                                 :
    """

    discriminator: ConditionalWhenInputDiscriminator
    is_default_when: bool
    parameters: ConditionalWhenInputParameters

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "discriminator": "discriminator",
            "is_default_when": "is_default_when",
            "parameters": "parameters",
        }
        key_transform_with_dump = {
            "discriminator": "discriminator",
            "is_default_when": "is_default_when",
            "parameters": "parameters",
        }
