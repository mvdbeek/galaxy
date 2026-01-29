from dataclasses import dataclass

from .creator import Creator

__all__ = ["UpdateCreatorAction"]


@dataclass
class UpdateCreatorAction:
    """
    UpdateCreatorAction dataclass.

    Args:
        action_type (str)        :
        creator (Optional[Creator])
                                 : Additional information about the creator (or multiple
                                   creators) of this workflow.
    """

    action_type: str
    creator: Creator | None = None  # Additional information about the creator (or multiple creators) of this workflow.
