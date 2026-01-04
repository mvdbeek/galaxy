from dataclasses import dataclass

from .quota_percent import QuotaPercent

__all__ = ["AnonUserModel"]


@dataclass
class AnonUserModel:
    """
    AnonUserModel dataclass.

    Args:
        nice_total_disk_usage (str)
                                 : Size of all non-purged, unique datasets of the user in a
                                   nice format.
        total_disk_usage (float) : Size of all non-purged, unique datasets of the user in
                                   bytes.
        quota_percent (Optional[QuotaPercent])
                                 : Percentage of the storage quota applicable to the user.
    """

    nice_total_disk_usage: str  # Size of all non-purged, unique datasets of the user in a nice format.
    total_disk_usage: float  # Size of all non-purged, unique datasets of the user in bytes.
    quota_percent: QuotaPercent | None = None  # Percentage of the storage quota applicable to the user.
