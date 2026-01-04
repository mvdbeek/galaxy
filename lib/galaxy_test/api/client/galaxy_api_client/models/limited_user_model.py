from dataclasses import dataclass

from .email_ import Email_
from .username import Username

__all__ = ["LimitedUserModel"]


@dataclass
class LimitedUserModel:
    """
    This is used when config options (expose_user_name and expose_user_email) are in place.

    Args:
        id_ (str)                : Encoded ID of the user
        email_ (Optional[Email_]): Email address for communication with the user. Only
                                   required for anonymous users.
        username (Optional[Username])
                                 : The name of the user.
    """

    id_: str  # Encoded ID of the user
    email_: Email_ | None = None  # Email address for communication with the user. Only required for anonymous users.
    username: Username | None = None  # The name of the user.
