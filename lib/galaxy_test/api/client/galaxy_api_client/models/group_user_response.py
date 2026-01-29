from dataclasses import dataclass

__all__ = ["GroupUserResponse"]


@dataclass
class GroupUserResponse:
    """
    GroupUserResponse dataclass.

    Args:
        email_ (str)             : Email of the user
        id_ (str)                :
        url (str)                : The relative URL to access this item.
    """

    email_: str  # Email of the user
    id_: str
    url: str  # The relative URL to access this item.
