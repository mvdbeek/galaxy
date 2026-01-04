from dataclasses import dataclass

__all__ = ["HdcaDestination"]


@dataclass
class HdcaDestination:
    """
    HdcaDestination dataclass.

    Args:
        type_ (str)              :
    """

    type_: str
