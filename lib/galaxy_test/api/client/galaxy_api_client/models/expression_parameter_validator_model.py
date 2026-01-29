from dataclasses import dataclass

from .message import Message

__all__ = ["ExpressionParameterValidatorModel"]


@dataclass
class ExpressionParameterValidatorModel:
    """
    Check if a one line python expression given expression evaluates to True.  The
    expression is given is the content of the validator tag.

    Args:
        expression (str)         :
        implicit (Optional[bool]):
        message (Optional[Message])
                                 : The optional message sent with the error report.
        negate (Optional[bool])  :
        type_ (Optional[str])    :
    """

    expression: str
    implicit: bool | None = False
    message: Message | None = None  # The optional message sent with the error report.
    negate: bool | None = False
    type_: str | None = "expression"
