from dataclasses import dataclass

from .user_value import UserValue

__all__ = ["ItemTagsResponse"]


@dataclass
class ItemTagsResponse:
    """
    Response schema for showing an item tag.

    Args:
        id_ (str)                :
        model_class (str)        :
        user_tname (str)         :
        user_value (Optional[UserValue])
                                 :
    """

    id_: str
    model_class: str
    user_tname: str
    user_value: UserValue | None = None
