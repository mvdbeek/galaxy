from dataclasses import dataclass

from .user_quota_usage_quota import UserQuotaUsageQuota
from .user_quota_usage_quota_bytes import UserQuotaUsageQuotaBytes
from .user_quota_usage_quota_percent import UserQuotaUsageQuotaPercent
from .user_quota_usage_quota_source_label import UserQuotaUsageQuotaSourceLabel

__all__ = ["UserQuotaUsage"]


@dataclass
class UserQuotaUsage:
    """
    UserQuotaUsage dataclass

    Args:
        total_disk_usage (float) :
        quota (UserQuotaUsageQuota | None)
                                 :
        quota_bytes (UserQuotaUsageQuotaBytes | None)
                                 :
        quota_percent (UserQuotaUsageQuotaPercent | None)
                                 :
        quota_source_label (UserQuotaUsageQuotaSourceLabel | None)
                                 :
    """

    total_disk_usage: float
    quota: UserQuotaUsageQuota | None = None
    quota_bytes: UserQuotaUsageQuotaBytes | None = None
    quota_percent: UserQuotaUsageQuotaPercent | None = None
    quota_source_label: UserQuotaUsageQuotaSourceLabel | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "quota": "quota",
            "quota_bytes": "quota_bytes",
            "quota_percent": "quota_percent",
            "quota_source_label": "quota_source_label",
            "total_disk_usage": "total_disk_usage",
        }
        key_transform_with_dump = {
            "quota": "quota",
            "quota_bytes": "quota_bytes",
            "quota_percent": "quota_percent",
            "quota_source_label": "quota_source_label",
            "total_disk_usage": "total_disk_usage",
        }
