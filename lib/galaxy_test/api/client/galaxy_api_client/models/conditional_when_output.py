from dataclasses import dataclass
from typing import Any

from .conditional_when_output_discriminator import ConditionalWhenOutputDiscriminator

__all__ = ["ConditionalWhenOutput"]


@dataclass
class ConditionalWhenOutput:
    """
    ConditionalWhenOutput dataclass

    Args:
        discriminator (ConditionalWhenOutputDiscriminator)
                                 :
        is_default_when (bool)   :
        parameters (dict[str, Any])
                                 : [Circular reference detected:
                                   ConditionalWhenOutputParameters ->
                                   ConditionalWhenOutputParametersItem ->
                                   RepeatParameterModelOutput ->
                                   RepeatParameterModelOutputParameters ->
                                   RepeatParameterModelOutputParametersItem ->
                                   ConditionalWhenOutputParameters]
    """

    discriminator: ConditionalWhenOutputDiscriminator
    is_default_when: bool
    parameters: dict[
        str, Any
    ]  # [Circular reference detected: ConditionalWhenOutputParameters -> ConditionalWhenOutputParametersItem -> RepeatParameterModelOutput -> RepeatParameterModelOutputParameters -> RepeatParameterModelOutputParametersItem -> ConditionalWhenOutputParameters]

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
