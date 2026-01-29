from dataclasses import dataclass

from .badge_dict import BadgeDict
from .concrete_object_store_model_description import ConcreteObjectStoreModelDescription
from .concrete_object_store_model_device import ConcreteObjectStoreModelDevice
from .concrete_object_store_model_name import ConcreteObjectStoreModelName
from .concrete_object_store_model_object_expires_after_days import ConcreteObjectStoreModelObjectExpiresAfterDays
from .concrete_object_store_model_object_store_id import ConcreteObjectStoreModelObjectStoreId
from .quota_model import QuotaModel

__all__ = ["ConcreteObjectStoreModel"]


@dataclass
class ConcreteObjectStoreModel:
    """
    ConcreteObjectStoreModel dataclass

    Args:
        badges (List[BadgeDict]) :
        private (bool)           :
        quota (QuotaModel)       :
        description (ConcreteObjectStoreModelDescription | None)
                                 :
        device (ConcreteObjectStoreModelDevice | None)
                                 :
        name (ConcreteObjectStoreModelName | None)
                                 :
        object_expires_after_days (ConcreteObjectStoreModelObjectExpiresAfterDays | None)
                                 :
        object_store_id (ConcreteObjectStoreModelObjectStoreId | None)
                                 :
    """

    badges: list[BadgeDict]
    private: bool
    quota: QuotaModel
    description: ConcreteObjectStoreModelDescription | None = None
    device: ConcreteObjectStoreModelDevice | None = None
    name: ConcreteObjectStoreModelName | None = None
    object_expires_after_days: ConcreteObjectStoreModelObjectExpiresAfterDays | None = None
    object_store_id: ConcreteObjectStoreModelObjectStoreId | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "badges": "badges",
            "description": "description",
            "device": "device",
            "name": "name",
            "object_expires_after_days": "object_expires_after_days",
            "object_store_id": "object_store_id",
            "private": "private",
            "quota": "quota",
        }
        key_transform_with_dump = {
            "badges": "badges",
            "description": "description",
            "device": "device",
            "name": "name",
            "object_expires_after_days": "object_expires_after_days",
            "object_store_id": "object_store_id",
            "private": "private",
            "quota": "quota",
        }
