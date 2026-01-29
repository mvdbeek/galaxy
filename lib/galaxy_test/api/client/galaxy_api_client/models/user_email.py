from dataclasses import dataclass

__all__ = ["UserEmail"]


@dataclass
class UserEmail:
    """
    UserEmail dataclass

    Args:
        email_ (str)             : The email of the user. (maps from 'email')
        id_ (str)                : The encoded ID of the user. (maps from 'id')
    """

    email_: str  # The email of the user. (maps from 'email')
    id_: str  # The encoded ID of the user. (maps from 'id')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email": "email_",
            "id": "id_",
        }
        key_transform_with_dump = {
            "email_": "email",
            "id_": "id",
        }
