from dataclasses import dataclass

from .max_ import Max_
from .message import Message
from .min_ import Min_

__all__ = ["LengthParameterValidatorModel"]


@dataclass
class LengthParameterValidatorModel:
    """
    LengthParameterValidatorModel dataclass.

    Args:
        implicit (Optional[bool]):
        max_ (Optional[Max_])    :
        message (Optional[Message])
                                 : The optional message sent with the error report.
        min_ (Optional[Min_])    :
        negate (Optional[bool])  :
        type_ (Optional[str])    :
    """

    implicit: bool | None = False
    max_: Max_ | None = None
    message: Message | None = None  # The optional message sent with the error report.
    min_: Min_ | None = None
    negate: bool | None = False
    type_: str | None = "length"
