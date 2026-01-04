from dataclasses import dataclass

__all__ = ["JobLock"]


@dataclass
class JobLock:
    """
    JobLock dataclass.

    Args:
        active (bool)            : If active, jobs will not dispatch
    """

    active: bool  # If active, jobs will not dispatch
