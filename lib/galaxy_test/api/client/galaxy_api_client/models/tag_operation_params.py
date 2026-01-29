from dataclasses import dataclass

from .tags import Tags
from .type_ import Type_

__all__ = ["TagOperationParams"]


@dataclass
class TagOperationParams:
    """
    TagOperationParams dataclass.

    Args:
        tags (Tags)              : The collection of tags associated with an item.
        type_ (Type_)            : The type of content to be created in the history.
    """

    tags: Tags  # The collection of tags associated with an item.
    type_: Type_  # The type of content to be created in the history.
