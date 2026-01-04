from dataclasses import dataclass

__all__ = ["CreateEntryPayload"]


@dataclass
class CreateEntryPayload:
    """
    CreateEntryPayload dataclass.

    Args:
        name (str)               : The name of the entry to create.
        target (str)             : The target file source to create the entry in.
    """

    name: str  # The name of the entry to create.
    target: str  # The target file source to create the entry in.
