from dataclasses import dataclass

from .conditional_when_output_discriminator import ConditionalWhenOutputDiscriminator
from .conditional_when_output_parameters import ConditionalWhenOutputParameters

__all__ = ["ConditionalWhenOutput2"]


@dataclass
class ConditionalWhenOutput2:
    """
    ConditionalWhenOutput2 dataclass

    Args:
        discriminator (ConditionalWhenOutputDiscriminator)
                                 :
        is_default_when (bool)   :
        parameters (ConditionalWhenOutputParameters)
                                 :
    """

    discriminator: ConditionalWhenOutputDiscriminator
    is_default_when: bool
    parameters: ConditionalWhenOutputParameters

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
