from enum import Enum


class InvocationSerializationView(str, Enum):
    COLLECTION = "collection"
    ELEMENT = "element"

    def __str__(self) -> str:
        return str(self.value)
