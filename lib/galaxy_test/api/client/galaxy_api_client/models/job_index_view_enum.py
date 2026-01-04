from enum import Enum


class JobIndexViewEnum(str, Enum):
    ADMIN_JOB_LIST = "admin_job_list"
    COLLECTION = "collection"

    def __str__(self) -> str:
        return str(self.value)
