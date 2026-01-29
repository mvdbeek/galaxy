from dataclasses import dataclass

__all__ = ["UserDeletionPayload"]


@dataclass
class UserDeletionPayload:
    """
    UserDeletionPayload dataclass

    Args:
        purge (bool | None)      : Purge the user. Deprecated, please use the `purge` query
                                   parameter instead.
    """

    purge: bool | None = False  # Purge the user. Deprecated, please use the `purge` query parameter instead.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "purge": "purge",
        }
        key_transform_with_dump = {
            "purge": "purge",
        }
