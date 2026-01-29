from dataclasses import dataclass

__all__ = ["SetSlugPayload"]


@dataclass
class SetSlugPayload:
    """
    SetSlugPayload dataclass

    Args:
        new_slug (str)           : The slug that will be used to access this shared item.
    """

    new_slug: str  # The slug that will be used to access this shared item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "new_slug": "new_slug",
        }
        key_transform_with_dump = {
            "new_slug": "new_slug",
        }
