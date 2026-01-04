from dataclasses import dataclass

from .badge_dict import BadgeDict
from .concrete_object_store_quota_source_details import ConcreteObjectStoreQuotaSourceDetails
from .description import Description
from .hashes import Hashes
from .name import Name
from .object_store_id import ObjectStoreId
from .percent_used import PercentUsed
from .sources import Sources

__all__ = ["DatasetStorageDetails"]


@dataclass
class DatasetStorageDetails:
    """
    DatasetStorageDetails dataclass.

    Args:
        badges (List[BadgeDict]) : A list of badges describing object store properties for
                                   concrete object store dataset is stored in.
        dataset_state (str)      : The model state of the supplied dataset instance.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        hashes (Optional[Hashes]): List of precomputed hashes for the file, if available.
        name (Optional[Name])    : The name of the creator.
        object_store_id (Optional[ObjectStoreId])
                                 : The ID of the object store that this dataset is stored
                                   in.
        percent_used (Optional[PercentUsed])
                                 : The percentage indicating how full the store is.
        private (bool)           : Indicator of whether the objectstore is marked as
                                   private.
        quota (ConcreteObjectStoreQuotaSourceDetails)
                                 :
        relocatable (bool)       : Indicator of whether the objectstore for this dataset can
                                   be switched by this user.
        shareable (bool)         : Is this dataset shareable.
        sources (Sources)        : The file sources associated with the supplied dataset
                                   instance.
    """

    badges: list[
        BadgeDict
    ]  # A list of badges describing object store properties for concrete object store dataset is stored in.
    dataset_state: str  # The model state of the supplied dataset instance.
    description: Description | None  # Detailed text description for this Quota.
    hashes: Hashes | None  # List of precomputed hashes for the file, if available.
    name: Name | None  # The name of the creator.
    object_store_id: ObjectStoreId | None  # The ID of the object store that this dataset is stored in.
    percent_used: PercentUsed | None  # The percentage indicating how full the store is.
    private: bool  # Indicator of whether the objectstore is marked as private.
    quota: ConcreteObjectStoreQuotaSourceDetails
    relocatable: bool  # Indicator of whether the objectstore for this dataset can be switched by this user.
    shareable: bool  # Is this dataset shareable.
    sources: Sources  # The file sources associated with the supplied dataset instance.
