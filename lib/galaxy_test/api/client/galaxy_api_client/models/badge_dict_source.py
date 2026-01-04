from enum import Enum


class BadgeDictSource(str, Enum):
    ADMIN = "admin"
    GALAXY = "galaxy"

    def __str__(self) -> str:
        return str(self.value)
