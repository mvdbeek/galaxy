from dataclasses import dataclass

from .code_desc import CodeDesc
from .desc import Desc
from .match import Match
from .stream import Stream

__all__ = ["RegexJobMessage"]


@dataclass
class RegexJobMessage:
    """
    RegexJobMessage dataclass.

    Args:
        desc (Optional[Desc])    :
        error_level (float)      :
        match (Optional[Match])  :
        stream (Optional[Stream]):
        type_ (str)              :
        code_desc (Optional[CodeDesc])
                                 :
    """

    desc: Desc | None
    error_level: float
    match: Match | None
    stream: Stream | None
    type_: str
    code_desc: CodeDesc | None = None
