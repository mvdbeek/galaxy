from dataclasses import dataclass

from .quota import Quota
from .quota_bytes import QuotaBytes
from .quota_percent import QuotaPercent
from .quota_source_label import QuotaSourceLabel

__all__ = ["UserQuotaUsage"]


@dataclass
class UserQuotaUsage:
    """
    UserQuotaUsage dataclass.

    Args:
        total_disk_usage (float) :
        quota (Optional[Quota])  :
        quota_bytes (Optional[QuotaBytes])
                                 : Quota applicable to the user in bytes.
        quota_percent (Optional[QuotaPercent])
                                 : Percentage of the storage quota applicable to the user.
        quota_source_label (Optional[QuotaSourceLabel])
                                 : Quota source label
    """

    total_disk_usage: float
    quota: Quota | None = None
    quota_bytes: QuotaBytes | None = None  # Quota applicable to the user in bytes.
    quota_percent: QuotaPercent | None = None  # Percentage of the storage quota applicable to the user.
    quota_source_label: QuotaSourceLabel | None = None  # Quota source label
