from dataclasses import dataclass

__all__ = ["DeletedCustomBuild"]


@dataclass
class DeletedCustomBuild:
    """
    DeletedCustomBuild dataclass.

    Args:
        message (str)            : Confirmation of the custom build deletion.
    """

    message: str  # Confirmation of the custom build deletion.
