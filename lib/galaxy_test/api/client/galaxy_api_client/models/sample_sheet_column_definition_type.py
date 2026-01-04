from enum import Enum


class SampleSheetColumnDefinitionType(str, Enum):
    BOOLEAN = "boolean"
    ELEMENT_IDENTIFIER = "element_identifier"
    FLOAT = "float"
    INT = "int"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
