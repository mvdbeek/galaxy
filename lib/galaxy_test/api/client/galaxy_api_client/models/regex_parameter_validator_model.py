from dataclasses import dataclass

from .message import Message

__all__ = ["RegexParameterValidatorModel"]


@dataclass
class RegexParameterValidatorModel:
    """
    Check if a regular expression **matches** the value, i.e. appears at the beginning of
    the value. To enforce a match of the complete value use ``$`` at the end of the
    expression. The expression is given is the content of the validator tag. Note that for
    ``selects`` each option is checked separately.

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
    type_: str | None = "regex"
