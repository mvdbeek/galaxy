from dataclasses import dataclass

from .concrete_object_store_quota_source_details_source import ConcreteObjectStoreQuotaSourceDetailsSource

__all__ = ["ConcreteObjectStoreQuotaSourceDetails"]


@dataclass
class ConcreteObjectStoreQuotaSourceDetails:
    """
    ConcreteObjectStoreQuotaSourceDetails dataclass

    Args:
        enabled (bool)           : Whether the object store tracks quota on the data
                                   (independent of Galaxy's configuration)
        source (ConcreteObjectStoreQuotaSourceDetailsSource)
                                 : The quota source label corresponding to the object store
                                   the dataset is stored in (or would be stored in)
    """

    enabled: bool  # Whether the object store tracks quota on the data (independent of Galaxy's configuration)
    source: ConcreteObjectStoreQuotaSourceDetailsSource  # The quota source label corresponding to the object store the dataset is stored in (or would be stored in)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "enabled": "enabled",
            "source": "source",
        }
        key_transform_with_dump = {
            "enabled": "enabled",
            "source": "source",
        }
