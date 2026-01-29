from dataclasses import dataclass

from .item_tags import ItemTags
from .taggable_item_class import TaggableItemClass

__all__ = ["ItemTagsPayload"]


@dataclass
class ItemTagsPayload:
    """
    ItemTagsPayload dataclass.

    Args:
        item_class (TaggableItemClass)
                                 :
        item_id (str)            : The `encoded identifier` of the item whose tags will be
                                   updated.
        item_tags (Optional[ItemTags])
                                 : The list of tags that will replace the current tags
                                   associated with the item.
    """

    item_class: TaggableItemClass
    item_id: str  # The `encoded identifier` of the item whose tags will be updated.
    item_tags: ItemTags | None = None  # The list of tags that will replace the current tags associated with the item.
