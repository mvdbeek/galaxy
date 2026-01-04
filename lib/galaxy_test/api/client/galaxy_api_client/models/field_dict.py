from dataclasses import dataclass

from .format_ import Format_
from .type_ import Type_

__all__ = ["FieldDict"]


@dataclass
class FieldDict:
    """
    FieldDict dataclass.

    Args:
        name (str)               :
        type_ (Type_)            : The type of content to be created in the history.
        format_ (Optional[Format_])
                                 : The short name for the output datatype.
    """

    name: str
    type_: Type_  # The type of content to be created in the history.
    format_: Format_ | None = None  # The short name for the output datatype.
