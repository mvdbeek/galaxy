from enum import Enum


class PersonalNotificationCategory(str, Enum):
    MESSAGE = "message"
    NEW_SHARED_ITEM = "new_shared_item"

    def __str__(self) -> str:
        return str(self.value)
