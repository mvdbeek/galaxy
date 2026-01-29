from dataclasses import dataclass

from .dataset_source_type import DatasetSourceType
from .dataset_state import DatasetState
from .hda_object_accessible import HdaObjectAccessible
from .hda_object_copied_from_ldda_id import HdaObjectCopiedFromLddaId

__all__ = ["HdaObject"]


@dataclass
class HdaObject:
    """
    History Dataset Association Object

    Args:
        history_id (str)         :
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        purged (bool)            :
        state (DatasetState)     :
        tags (List[str])         :
        accessible (HdaObjectAccessible | None)
                                 :
        copied_from_ldda_id (HdaObjectCopiedFromLddaId | None)
                                 :
        hda_ldda (DatasetSourceType | None)
                                 :
    """

    history_id: str
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    purged: bool
    state: DatasetState
    tags: list[str]
    accessible: HdaObjectAccessible | None = None
    copied_from_ldda_id: HdaObjectCopiedFromLddaId | None = None
    hda_ldda: DatasetSourceType | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "accessible": "accessible",
            "copied_from_ldda_id": "copied_from_ldda_id",
            "hda_ldda": "hda_ldda",
            "history_id": "history_id",
            "id": "id_",
            "model_class": "model_class",
            "purged": "purged",
            "state": "state",
            "tags": "tags",
        }
        key_transform_with_dump = {
            "accessible": "accessible",
            "copied_from_ldda_id": "copied_from_ldda_id",
            "hda_ldda": "hda_ldda",
            "history_id": "history_id",
            "id_": "id",
            "model_class": "model_class",
            "purged": "purged",
            "state": "state",
            "tags": "tags",
        }
