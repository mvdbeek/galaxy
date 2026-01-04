from dataclasses import dataclass

from .discriminator import Discriminator
from .parameters import Parameters

__all__ = ["ConditionalWhenOutput3"]


@dataclass
class ConditionalWhenOutput3:
    """
    ConditionalWhenOutput3 dataclass.

    Args:
        discriminator (Discriminator)
                                 :
        is_default_when (bool)   :
        parameters (Parameters)  :
    """

    discriminator: Discriminator
    is_default_when: bool
    parameters: Parameters
