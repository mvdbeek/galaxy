from dataclasses import dataclass

__all__ = ["JobLock"]


@dataclass
class JobLock:
    """
    JobLock dataclass

    Args:
        active (bool)            : If active, jobs will not dispatch
    """

    active: bool  # If active, jobs will not dispatch

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
        }
        key_transform_with_dump = {
            "active": "active",
        }
