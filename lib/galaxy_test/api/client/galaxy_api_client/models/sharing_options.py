from enum import Enum


class SharingOptions(str, Enum):
    MAKE_ACCESSIBLE_TO_SHARED = "make_accessible_to_shared"
    MAKE_PUBLIC = "make_public"
    NO_CHANGES = "no_changes"

    def __str__(self) -> str:
        return str(self.value)
