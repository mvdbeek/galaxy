from enum import Enum


class Requirement(str, Enum):
    ADMIN = "admin"
    LOGGED_IN = "logged_in"
    NEW_HISTORY = "new_history"

    def __str__(self) -> str:
        return str(self.value)
