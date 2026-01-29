from dataclasses import dataclass

__all__ = ["RemoteUserCreationPayload"]


@dataclass
class RemoteUserCreationPayload:
    """
    RemoteUserCreationPayload dataclass.

    Args:
        remote_user_email (str)  : Email of the user
    """

    remote_user_email: str  # Email of the user
