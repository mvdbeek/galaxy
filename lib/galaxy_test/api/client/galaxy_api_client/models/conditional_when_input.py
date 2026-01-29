from dataclasses import dataclass
from typing import Any

from .conditional_when_input_discriminator import ConditionalWhenInputDiscriminator

__all__ = ["ConditionalWhenInput"]


@dataclass
class ConditionalWhenInput:
    """
    ConditionalWhenInput dataclass

    Args:
        discriminator (ConditionalWhenInputDiscriminator)
                                 :
        is_default_when (bool)   :
        parameters (dict[str, Any])
                                 : [Circular reference detected:
                                   ConditionalWhenInputParameters ->
                                   ConditionalWhenInputParametersItem ->
                                   RepeatParameterModelInput ->
                                   RepeatParameterModelInputParameters ->
                                   RepeatParameterModelInputParametersItem ->
                                   ConditionalWhenInputParameters]
    """

    discriminator: ConditionalWhenInputDiscriminator
    is_default_when: bool
    parameters: dict[
        str, Any
    ]  # [Circular reference detected: ConditionalWhenInputParameters -> ConditionalWhenInputParametersItem -> RepeatParameterModelInput -> RepeatParameterModelInputParameters -> RepeatParameterModelInputParametersItem -> ConditionalWhenInputParameters]

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
