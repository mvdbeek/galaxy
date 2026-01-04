from dataclasses import dataclass

__all__ = ["ChangeDatatypeOperationParams"]


@dataclass
class ChangeDatatypeOperationParams:
    """
    ChangeDatatypeOperationParams dataclass.

    Args:
        datatype (str)           :
        type_ (str)              :
    """

    datatype: str
    type_: str
