from dataclasses import dataclass

__all__ = ["RemoteUserCreationPayload"]


@dataclass
class RemoteUserCreationPayload:
    """
    RemoteUserCreationPayload dataclass

    Args:
        remote_user_email (str)  : Email of the user
    """

    remote_user_email: str  # Email of the user

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "remote_user_email": "remote_user_email",
        }
        key_transform_with_dump = {
            "remote_user_email": "remote_user_email",
        }
