from dataclasses import dataclass

from .badge_dict import BadgeDict
from .quota_model import QuotaModel
from .type__12 import Type12
from .user_concrete_object_store_model_description import UserConcreteObjectStoreModelDescription
from .user_concrete_object_store_model_device import UserConcreteObjectStoreModelDevice
from .user_concrete_object_store_model_name import UserConcreteObjectStoreModelName
from .user_concrete_object_store_model_object_expires_after_days import (
    UserConcreteObjectStoreModelObjectExpiresAfterDays,
)
from .user_concrete_object_store_model_object_store_id import UserConcreteObjectStoreModelObjectStoreId
from .user_concrete_object_store_model_variables import UserConcreteObjectStoreModelVariables

__all__ = ["UserConcreteObjectStoreModel"]


@dataclass
class UserConcreteObjectStoreModel:
    """
    UserConcreteObjectStoreModel dataclass

    Args:
        active (bool)            :
        badges (List[BadgeDict]) :
        hidden (bool)            :
        private (bool)           :
        purged (bool)            :
        quota (QuotaModel)       :
        secrets (List[str])      :
        template_id (str)        :
        template_version (int)   :
        type_ (Type12)           : Maps from 'type'
        uuid_ (str)              : Maps from 'uuid'
        variables (UserConcreteObjectStoreModelVariables)
                                 :
        description (UserConcreteObjectStoreModelDescription | None)
                                 :
        device (UserConcreteObjectStoreModelDevice | None)
                                 :
        name (UserConcreteObjectStoreModelName | None)
                                 :
        object_expires_after_days (UserConcreteObjectStoreModelObjectExpiresAfterDays | None)
                                 :
        object_store_id (UserConcreteObjectStoreModelObjectStoreId | None)
                                 :
    """

    active: bool
    badges: list[BadgeDict]
    hidden: bool
    private: bool
    purged: bool
    quota: QuotaModel
    secrets: list[str]
    template_id: str
    template_version: int
    type_: Type12  # Maps from 'type'
    uuid_: str  # Maps from 'uuid'
    variables: UserConcreteObjectStoreModelVariables
    description: UserConcreteObjectStoreModelDescription | None = None
    device: UserConcreteObjectStoreModelDevice | None = None
    name: UserConcreteObjectStoreModelName | None = None
    object_expires_after_days: UserConcreteObjectStoreModelObjectExpiresAfterDays | None = None
    object_store_id: UserConcreteObjectStoreModelObjectStoreId | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "badges": "badges",
            "description": "description",
            "device": "device",
            "hidden": "hidden",
            "name": "name",
            "object_expires_after_days": "object_expires_after_days",
            "object_store_id": "object_store_id",
            "private": "private",
            "purged": "purged",
            "quota": "quota",
            "secrets": "secrets",
            "template_id": "template_id",
            "template_version": "template_version",
            "type": "type_",
            "uuid": "uuid_",
            "variables": "variables",
        }
        key_transform_with_dump = {
            "active": "active",
            "badges": "badges",
            "description": "description",
            "device": "device",
            "hidden": "hidden",
            "name": "name",
            "object_expires_after_days": "object_expires_after_days",
            "object_store_id": "object_store_id",
            "private": "private",
            "purged": "purged",
            "quota": "quota",
            "secrets": "secrets",
            "template_id": "template_id",
            "template_version": "template_version",
            "type_": "type",
            "uuid_": "uuid",
            "variables": "variables",
        }
