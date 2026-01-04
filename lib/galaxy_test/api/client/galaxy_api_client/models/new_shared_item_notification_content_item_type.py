from enum import Enum


class NewSharedItemNotificationContentItemType(str, Enum):
    HISTORY = "history"
    PAGE = "page"
    VISUALIZATION = "visualization"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
