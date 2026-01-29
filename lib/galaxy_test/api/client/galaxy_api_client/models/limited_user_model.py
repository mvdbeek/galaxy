from dataclasses import dataclass

from .email_ import Email_
from .limited_user_model_username import LimitedUserModelUsername

__all__ = ["LimitedUserModel"]


@dataclass
class LimitedUserModel:
    """
    This is used when config options (expose_user_name and expose_user_email) are in place.

    Args:
        id_ (str)                : Encoded ID of the user (maps from 'id')
        email_ (Email_ | None)   : Maps from 'email'
        username (LimitedUserModelUsername | None)
                                 :
    """

    id_: str  # Encoded ID of the user (maps from 'id')
    email_: Email_ | None = None  # Maps from 'email'
    username: LimitedUserModelUsername | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email": "email_",
            "id": "id_",
            "username": "username",
        }
        key_transform_with_dump = {
            "email_": "email",
            "id_": "id",
            "username": "username",
        }
