from dataclasses import dataclass

__all__ = ["HdaDestination"]


@dataclass
class HdaDestination:
    """
    HdaDestination dataclass.

    Args:
        type_ (str)              :
    """

    type_: str
