from dataclasses import dataclass

from .code_desc import CodeDesc
from .desc import Desc

__all__ = ["MaxDiscoveredFilesJobMessage"]


@dataclass
class MaxDiscoveredFilesJobMessage:
    """
    MaxDiscoveredFilesJobMessage dataclass.

    Args:
        desc (Optional[Desc])    :
        error_level (float)      :
        type_ (str)              :
        code_desc (Optional[CodeDesc])
                                 :
    """

    desc: Desc | None
    error_level: float
    type_: str
    code_desc: CodeDesc | None = None
