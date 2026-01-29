from dataclasses import dataclass

from .type_ import Type_

__all__ = ["ParsedColumn"]


@dataclass
class ParsedColumn:
    """
    ParsedColumn dataclass.

    Args:
        title (str)              :
        type_ (Type_)            : The type of content to be created in the history.
        type_index (int)         :
    """

    title: str
    type_: Type_  # The type of content to be created in the history.
    type_index: int
