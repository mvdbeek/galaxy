from enum import Enum, unique

__all__ = ["JobIndexViewEnum"]


@unique
class JobIndexViewEnum(str, Enum):
    """
    JobIndexViewEnum Enum

    Args:
        collection (str)         : Value for COLLECTION
        admin_job_list (str)     : Value for ADMIN_JOB_LIST
    """

    COLLECTION = "collection"
    ADMIN_JOB_LIST = "admin_job_list"
