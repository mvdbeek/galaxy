from dataclasses import dataclass

from .input_ import Input_
from .output import Output

__all__ = ["DisconnectAction"]


@dataclass
class DisconnectAction:
    """
    DisconnectAction dataclass.

    Args:
        action_type (str)        :
        input_ (Input_)          :
        output (Output)          :
    """

    action_type: str
    input_: Input_
    output: Output
