from dataclasses import dataclass

from .annotation import Annotation
from .deleted import Deleted
from .name import Name
from .tags import Tags
from .visible import Visible

__all__ = ["UpdateHistoryContentsPayload"]


@dataclass
class UpdateHistoryContentsPayload:
    """
    Can contain arbitrary/dynamic fields that will be updated for a particular history item.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        deleted (Optional[Deleted])
                                 : Whether this Visualization has been deleted.
        name (Optional[Name])    : The name of the creator.
        tags (Optional[Tags])    : A list of tags to add to this item.
        visible (Optional[Visible])
                                 : Whether this item is visible in the history.
    """

    annotation: Annotation | None = None  # The annotation of this Visualization.
    deleted: Deleted | None = False  # Whether this Visualization has been deleted.
    name: Name | None = None  # The name of the creator.
    tags: Tags | None = None  # A list of tags to add to this item.
    visible: Visible | None = None  # Whether this item is visible in the history.
