from dataclasses import dataclass

from .item_tags_payload_item_tags import ItemTagsPayloadItemTags
from .taggable_item_class import TaggableItemClass

__all__ = ["ItemTagsPayload"]


@dataclass
class ItemTagsPayload:
    """
    ItemTagsPayload dataclass

    Args:
        item_class (TaggableItemClass)
                                 :
        item_id (str)            : The `encoded identifier` of the item whose tags will be
                                   updated.
        item_tags (ItemTagsPayloadItemTags | None)
                                 : The list of tags that will replace the current tags
                                   associated with the item.
    """

    item_class: TaggableItemClass
    item_id: str  # The `encoded identifier` of the item whose tags will be updated.
    item_tags: ItemTagsPayloadItemTags | None = (
        None  # The list of tags that will replace the current tags associated with the item.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "item_class": "item_class",
            "item_id": "item_id",
            "item_tags": "item_tags",
        }
        key_transform_with_dump = {
            "item_class": "item_class",
            "item_id": "item_id",
            "item_tags": "item_tags",
        }
