from dataclasses import dataclass

__all__ = ["UserCreationPayload"]


@dataclass
class UserCreationPayload:
    """
    UserCreationPayload dataclass

    Args:
        email_ (str)             : Email of the user (maps from 'email')
        password (str)           : The password of the user.
        username (str)           : The name of the user.
    """

    email_: str  # Email of the user (maps from 'email')
    password: str  # The password of the user.
    username: str  # The name of the user.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email": "email_",
            "password": "password",
            "username": "username",
        }
        key_transform_with_dump = {
            "email_": "email",
            "password": "password",
            "username": "username",
        }
