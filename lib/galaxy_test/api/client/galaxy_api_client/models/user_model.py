from dataclasses import dataclass

from .user_model_last_password_change import UserModelLastPasswordChange

__all__ = ["UserModel"]


@dataclass
class UserModel:
    """
    User in a transaction context.

    Args:
        active (bool)            : User is active
        deleted (bool)           :  User is deleted
        email_ (str)             : Email of the user (maps from 'email')
        id_ (str)                : Encoded ID of the user (maps from 'id')
        last_password_change (UserModelLastPasswordChange)
                                 :
        model_class (str)        : The name of the database model class.
        username (str)           : The name of the user.
    """

    active: bool  # User is active
    deleted: bool  #  User is deleted
    email_: str  # Email of the user (maps from 'email')
    id_: str  # Encoded ID of the user (maps from 'id')
    last_password_change: UserModelLastPasswordChange
    model_class: str  # The name of the database model class.
    username: str  # The name of the user.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "deleted": "deleted",
            "email": "email_",
            "id": "id_",
            "last_password_change": "last_password_change",
            "model_class": "model_class",
            "username": "username",
        }
        key_transform_with_dump = {
            "active": "active",
            "deleted": "deleted",
            "email_": "email",
            "id_": "id",
            "last_password_change": "last_password_change",
            "model_class": "model_class",
            "username": "username",
        }
