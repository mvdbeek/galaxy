from dataclasses import dataclass

__all__ = ["DeletedCustomBuild"]


@dataclass
class DeletedCustomBuild:
    """
    DeletedCustomBuild dataclass

    Args:
        message (str)            : Confirmation of the custom build deletion.
    """

    message: str  # Confirmation of the custom build deletion.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "message": "message",
        }
        key_transform_with_dump = {
            "message": "message",
        }
