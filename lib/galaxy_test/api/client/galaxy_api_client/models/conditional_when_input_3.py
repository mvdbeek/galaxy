from dataclasses import dataclass

from .discriminator import Discriminator
from .parameters import Parameters

__all__ = ["ConditionalWhenInput3"]


@dataclass
class ConditionalWhenInput3:
    """
    ConditionalWhenInput3 dataclass.

    Args:
        discriminator (Discriminator)
                                 :
        is_default_when (bool)   :
        parameters (Parameters)  :
    """

    discriminator: Discriminator
    is_default_when: bool
    parameters: Parameters
