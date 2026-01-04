from dataclasses import dataclass

__all__ = ["UserCreationPayload"]


@dataclass
class UserCreationPayload:
    """
    UserCreationPayload dataclass.

    Args:
        email_ (str)             : Email of the user
        password (str)           : The password of the user.
        username (str)           : The name of the user.
    """

    email_: str  # Email of the user
    password: str  # The password of the user.
    username: str  # The name of the user.
