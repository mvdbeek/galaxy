from dataclasses import dataclass

__all__ = ["UserDeletionPayload"]


@dataclass
class UserDeletionPayload:
    """
    UserDeletionPayload dataclass.

    Args:
        purge (Optional[bool])   : Purge the user. Deprecated, please use the `purge` query
                                   parameter instead.
    """

    purge: bool | None = False  # Purge the user. Deprecated, please use the `purge` query parameter instead.
