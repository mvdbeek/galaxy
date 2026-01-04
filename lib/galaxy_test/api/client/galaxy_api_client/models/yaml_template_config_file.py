from dataclasses import dataclass

from .filename import Filename
from .name import Name

__all__ = ["YamlTemplateConfigFile"]


@dataclass
class YamlTemplateConfigFile:
    """
    YamlTemplateConfigFile dataclass.

    Args:
        content (str)            :
        eval_engine (Optional[str])
                                 :
        filename (Optional[Filename])
                                 :
        name (Optional[Name])    : The name of the creator.
    """

    content: str
    eval_engine: str | None = "ecmascript"
    filename: Filename | None = None
    name: Name | None = None  # The name of the creator.
