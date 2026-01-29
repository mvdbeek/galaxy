from dataclasses import dataclass

__all__ = ["GroupUserResponse"]


@dataclass
class GroupUserResponse:
    """
    GroupUserResponse dataclass

    Args:
        email_ (str)             : Email of the user (maps from 'email')
        id_ (str)                : Maps from 'id'
        url (str)                : The relative URL to access this item.
    """

    email_: str  # Email of the user (maps from 'email')
    id_: str  # Maps from 'id'
    url: str  # The relative URL to access this item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email": "email_",
            "id": "id_",
            "url": "url",
        }
        key_transform_with_dump = {
            "email_": "email",
            "id_": "id",
            "url": "url",
        }
