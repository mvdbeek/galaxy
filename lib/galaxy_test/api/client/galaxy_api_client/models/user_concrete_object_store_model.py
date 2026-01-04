from dataclasses import dataclass

from .badge_dict import BadgeDict
from .description import Description
from .device import Device
from .name import Name
from .object_expires_after_days import ObjectExpiresAfterDays
from .object_store_id import ObjectStoreId
from .quota_model import QuotaModel
from .secrets import Secrets
from .type_ import Type_
from .variables import Variables

__all__ = ["UserConcreteObjectStoreModel"]


@dataclass
class UserConcreteObjectStoreModel:
    """
    UserConcreteObjectStoreModel dataclass.

    Args:
        active (bool)            :
        badges (List[BadgeDict]) :
        hidden (bool)            :
        private (bool)           :
        purged (bool)            :
        quota (QuotaModel)       :
        secrets (Secrets)        :
        template_id (str)        :
        template_version (int)   :
        type_ (Type_)            : The type of content to be created in the history.
        uuid_ (str)              :
        variables (Variables)    :
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

    active: bool
    badges: list[BadgeDict]
    hidden: bool
    private: bool
    purged: bool
    quota: QuotaModel
    secrets: Secrets
    template_id: str
    template_version: int
    type_: Type_  # The type of content to be created in the history.
    uuid_: str
    variables: Variables
    description: Description | None = ""  # Detailed text description for this Quota.
    device: Device | None = None
    name: Name | None = None  # The name of the creator.
    object_expires_after_days: ObjectExpiresAfterDays | None = None
    object_store_id: ObjectStoreId | None = None  # The ID of the object store that this dataset is stored in.
