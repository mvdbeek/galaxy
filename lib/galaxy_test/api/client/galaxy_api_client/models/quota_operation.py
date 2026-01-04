from enum import Enum


class QuotaOperation(str, Enum):
    VALUE_0 = "="
    VALUE_1 = "+"
    VALUE_2 = "-"

    def __str__(self) -> str:
        return str(self.value)
