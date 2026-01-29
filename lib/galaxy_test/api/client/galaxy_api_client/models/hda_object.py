from dataclasses import dataclass

from .accessible import Accessible
from .copied_from_ldda_id import CopiedFromLddaId
from .dataset_source_type import DatasetSourceType
from .dataset_state import DatasetState
from .tags import Tags

__all__ = ["HdaObject"]


@dataclass
class HdaObject:
    """
    History Dataset Association Object

    Args:
        history_id (str)         :
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        purged (bool)            :
        state (DatasetState)     :
        tags (Tags)              : The collection of tags associated with an item.
        accessible (Optional[Accessible])
                                 : Whether this item is accessible to the current user due
                                   to permissions.
        copied_from_ldda_id (Optional[CopiedFromLddaId])
                                 :
        hda_ldda (Optional[DatasetSourceType])
                                 :
    """

    history_id: str
    id_: str
    model_class: str  # The name of the database model class.
    purged: bool
    state: DatasetState
    tags: Tags  # The collection of tags associated with an item.
    accessible: Accessible | None = None  # Whether this item is accessible to the current user due to permissions.
    copied_from_ldda_id: CopiedFromLddaId | None = None
    hda_ldda: DatasetSourceType | None = None
