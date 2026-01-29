from dataclasses import dataclass

from .anon_user_model_quota_percent import AnonUserModelQuotaPercent

__all__ = ["AnonUserModel"]


@dataclass
class AnonUserModel:
    """
    AnonUserModel dataclass

    Args:
        nice_total_disk_usage (str)
                                 : Size of all non-purged, unique datasets of the user in a
                                   nice format.
        total_disk_usage (float) : Size of all non-purged, unique datasets of the user in
                                   bytes.
        quota_percent (AnonUserModelQuotaPercent | None)
                                 : Percentage of the storage quota applicable to the user.
    """

    nice_total_disk_usage: str  # Size of all non-purged, unique datasets of the user in a nice format.
    total_disk_usage: float  # Size of all non-purged, unique datasets of the user in bytes.
    quota_percent: AnonUserModelQuotaPercent | None = None  # Percentage of the storage quota applicable to the user.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "nice_total_disk_usage": "nice_total_disk_usage",
            "quota_percent": "quota_percent",
            "total_disk_usage": "total_disk_usage",
        }
        key_transform_with_dump = {
            "nice_total_disk_usage": "nice_total_disk_usage",
            "quota_percent": "quota_percent",
            "total_disk_usage": "total_disk_usage",
        }
