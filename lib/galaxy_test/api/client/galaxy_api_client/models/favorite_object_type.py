from enum import Enum


class FavoriteObjectType(str, Enum):
    TOOLS = "tools"

    def __str__(self) -> str:
        return str(self.value)
