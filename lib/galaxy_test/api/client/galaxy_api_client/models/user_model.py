from dataclasses import dataclass

from .last_password_change import LastPasswordChange

__all__ = ["UserModel"]


@dataclass
class UserModel:
    """
    User in a transaction context.

    Args:
        active (bool)            : User is active
        deleted (bool)           :  User is deleted
        email_ (str)             : Email of the user
        id_ (str)                : Encoded ID of the user
        last_password_change (Optional[LastPasswordChange])
                                 :
        model_class (str)        : The name of the database model class.
        username (str)           : The name of the user.
    """

    active: bool  # User is active
    deleted: bool  #  User is deleted
    email_: str  # Email of the user
    id_: str  # Encoded ID of the user
    last_password_change: LastPasswordChange | None
    model_class: str  # The name of the database model class.
    username: str  # The name of the user.
