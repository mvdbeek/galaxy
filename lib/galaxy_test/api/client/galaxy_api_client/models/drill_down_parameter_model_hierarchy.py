from enum import Enum


class DrillDownParameterModelHierarchy(str, Enum):
    EXACT = "exact"
    RECURSE = "recurse"

    def __str__(self) -> str:
        return str(self.value)
