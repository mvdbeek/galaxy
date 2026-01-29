from dataclasses import dataclass

from .item_tags_create_payload_value import ItemTagsCreatePayloadValue

__all__ = ["ItemTagsCreatePayload"]


@dataclass
class ItemTagsCreatePayload:
    """
    Payload schema for creating an item tag.

    Args:
        value (ItemTagsCreatePayloadValue | None)
                                 :
    """

    value: ItemTagsCreatePayloadValue | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "value": "value",
        }
        key_transform_with_dump = {
            "value": "value",
        }
