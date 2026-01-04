from dataclasses import dataclass

__all__ = ["SetSlugPayload"]


@dataclass
class SetSlugPayload:
    """
    SetSlugPayload dataclass.

    Args:
        new_slug (str)           : The slug that will be used to access this shared item.
    """

    new_slug: str  # The slug that will be used to access this shared item.
