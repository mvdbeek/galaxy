from dataclasses import dataclass

__all__ = ["ChangeDbkeyOperationParams"]


@dataclass
class ChangeDbkeyOperationParams:
    """
    ChangeDbkeyOperationParams dataclass.

    Args:
        dbkey (str)              :
        type_ (str)              :
    """

    dbkey: str
    type_: str
