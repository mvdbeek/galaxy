from dataclasses import dataclass

from .badge_dict import BadgeDict
from .concrete_object_store_quota_source_details import ConcreteObjectStoreQuotaSourceDetails
from .dataset_storage_details_description import DatasetStorageDetailsDescription
from .dataset_storage_details_hashes import DatasetStorageDetailsHashes
from .dataset_storage_details_name import DatasetStorageDetailsName
from .dataset_storage_details_object_store_id import DatasetStorageDetailsObjectStoreId
from .dataset_storage_details_percent_used import DatasetStorageDetailsPercentUsed
from .dataset_storage_details_sources import DatasetStorageDetailsSources

__all__ = ["DatasetStorageDetails"]


@dataclass
class DatasetStorageDetails:
    """
    DatasetStorageDetails dataclass

    Args:
        badges (List[BadgeDict]) : A list of badges describing object store properties for
                                   concrete object store dataset is stored in.
        dataset_state (str)      : The model state of the supplied dataset instance.
        description (DatasetStorageDetailsDescription)
                                 : A description of how this dataset is stored.
        hashes (DatasetStorageDetailsHashes)
                                 : The file contents hashes associated with the supplied
                                   dataset instance.
        name (DatasetStorageDetailsName)
                                 : The display name of the destination ObjectStore for this
                                   dataset.
        object_store_id (DatasetStorageDetailsObjectStoreId)
                                 : The identifier of the destination ObjectStore for this
                                   dataset.
        percent_used (DatasetStorageDetailsPercentUsed)
                                 : The percentage indicating how full the store is.
        private (bool)           : Indicator of whether the objectstore is marked as
                                   private.
        quota (ConcreteObjectStoreQuotaSourceDetails)
                                 :
        relocatable (bool)       : Indicator of whether the objectstore for this dataset can
                                   be switched by this user.
        shareable (bool)         : Is this dataset shareable.
        sources (DatasetStorageDetailsSources)
                                 : The file sources associated with the supplied dataset
                                   instance.
    """

    badges: list[
        BadgeDict
    ]  # A list of badges describing object store properties for concrete object store dataset is stored in.
    dataset_state: str  # The model state of the supplied dataset instance.
    description: DatasetStorageDetailsDescription  # A description of how this dataset is stored.
    hashes: DatasetStorageDetailsHashes  # The file contents hashes associated with the supplied dataset instance.
    name: DatasetStorageDetailsName  # The display name of the destination ObjectStore for this dataset.
    object_store_id: (
        DatasetStorageDetailsObjectStoreId  # The identifier of the destination ObjectStore for this dataset.
    )
    percent_used: DatasetStorageDetailsPercentUsed  # The percentage indicating how full the store is.
    private: bool  # Indicator of whether the objectstore is marked as private.
    quota: ConcreteObjectStoreQuotaSourceDetails
    relocatable: bool  # Indicator of whether the objectstore for this dataset can be switched by this user.
    shareable: bool  # Is this dataset shareable.
    sources: DatasetStorageDetailsSources  # The file sources associated with the supplied dataset instance.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "badges": "badges",
            "dataset_state": "dataset_state",
            "description": "description",
            "hashes": "hashes",
            "name": "name",
            "object_store_id": "object_store_id",
            "percent_used": "percent_used",
            "private": "private",
            "quota": "quota",
            "relocatable": "relocatable",
            "shareable": "shareable",
            "sources": "sources",
        }
        key_transform_with_dump = {
            "badges": "badges",
            "dataset_state": "dataset_state",
            "description": "description",
            "hashes": "hashes",
            "name": "name",
            "object_store_id": "object_store_id",
            "percent_used": "percent_used",
            "private": "private",
            "quota": "quota",
            "relocatable": "relocatable",
            "shareable": "shareable",
            "sources": "sources",
        }
