from dataclasses import dataclass

__all__ = ["CreateEntryPayload"]


@dataclass
class CreateEntryPayload:
    """
    CreateEntryPayload dataclass

    Args:
        name (str)               : The name of the entry to create.
        target (str)             : The target file source to create the entry in.
    """

    name: str  # The name of the entry to create.
    target: str  # The target file source to create the entry in.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "target": "target",
        }
        key_transform_with_dump = {
            "name": "name",
            "target": "target",
        }
