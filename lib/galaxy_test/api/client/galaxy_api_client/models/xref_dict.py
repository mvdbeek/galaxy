from dataclasses import dataclass

__all__ = ["XrefDict"]


@dataclass
class XrefDict:
    """
    XrefDict dataclass.

    Args:
        type_ (str)              :
        value (str)              :
    """

    type_: str
    value: str
