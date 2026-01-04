from enum import Enum


class FieldDictTypeType0(str, Enum):
    BOOLEAN = "boolean"
    FILE = "File"
    FLOAT = "float"
    INT = "int"
    NULL = "null"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
