from dataclasses import dataclass

from .badge_dict import BadgeDict
from .description import Description
from .device import Device
from .name import Name
from .object_expires_after_days import ObjectExpiresAfterDays
from .object_store_id import ObjectStoreId
from .quota_model import QuotaModel

__all__ = ["ConcreteObjectStoreModel"]


@dataclass
class ConcreteObjectStoreModel:
    """
    ConcreteObjectStoreModel dataclass.

    Args:
        badges (List[BadgeDict]) :
        private (bool)           :
        quota (QuotaModel)       :
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        device (Optional[Device]):
        name (Optional[Name])    : The name of the creator.
        object_expires_after_days (Optional[ObjectExpiresAfterDays])
                                 :
        object_store_id (Optional[ObjectStoreId])
                                 : The ID of the object store that this dataset is stored
                                   in.
    """

    badges: list[BadgeDict]
    private: bool
    quota: QuotaModel
    description: Description | None = ""  # Detailed text description for this Quota.
    device: Device | None = None
    name: Name | None = None  # The name of the creator.
    object_expires_after_days: ObjectExpiresAfterDays | None = None
    object_store_id: ObjectStoreId | None = None  # The ID of the object store that this dataset is stored in.
