from dataclasses import dataclass

from .message import Message

__all__ = ["EmptyFieldParameterValidatorModel"]


@dataclass
class EmptyFieldParameterValidatorModel:
    """
    EmptyFieldParameterValidatorModel dataclass.

    Args:
        implicit (Optional[bool]):
        message (Optional[Message])
                                 : The optional message sent with the error report.
        negate (Optional[bool])  :
        type_ (Optional[str])    :
    """

    implicit: bool | None = False
    message: Message | None = None  # The optional message sent with the error report.
    negate: bool | None = False
    type_: str | None = "empty_field"
