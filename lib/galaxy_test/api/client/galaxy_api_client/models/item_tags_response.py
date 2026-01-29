from dataclasses import dataclass

from .item_tags_response_user_value import ItemTagsResponseUserValue

__all__ = ["ItemTagsResponse"]


@dataclass
class ItemTagsResponse:
    """
    Response schema for showing an item tag.

    Args:
        id_ (str)                : Maps from 'id'
        model_class (str)        :
        user_tname (str)         :
        user_value (ItemTagsResponseUserValue | None)
                                 :
    """

    id_: str  # Maps from 'id'
    model_class: str
    user_tname: str
    user_value: ItemTagsResponseUserValue | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "model_class": "model_class",
            "user_tname": "user_tname",
            "user_value": "user_value",
        }
        key_transform_with_dump = {
            "id_": "id",
            "model_class": "model_class",
            "user_tname": "user_tname",
            "user_value": "user_value",
        }
