from dataclasses import dataclass

from .code_desc import CodeDesc
from .desc import Desc

__all__ = ["ExitCodeJobMessage"]


@dataclass
class ExitCodeJobMessage:
    """
    ExitCodeJobMessage dataclass.

    Args:
        desc (Optional[Desc])    :
        error_level (float)      :
        exit_code (int)          :
        type_ (str)              :
        code_desc (Optional[CodeDesc])
                                 :
    """

    desc: Desc | None
    error_level: float
    exit_code: int
    type_: str
    code_desc: CodeDesc | None = None
