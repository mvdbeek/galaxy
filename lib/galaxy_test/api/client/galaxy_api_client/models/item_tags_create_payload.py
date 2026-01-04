from dataclasses import dataclass

from .value import Value

__all__ = ["ItemTagsCreatePayload"]


@dataclass
class ItemTagsCreatePayload:
    """
    Payload schema for creating an item tag.

    Args:
        value (Optional[Value])  : TODO
    """

    value: Value | None = False  # TODO
