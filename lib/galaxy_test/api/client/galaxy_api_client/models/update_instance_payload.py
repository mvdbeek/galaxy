from dataclasses import dataclass

from .active import Active
from .description import Description
from .hidden import Hidden
from .name import Name
from .variables import Variables

__all__ = ["UpdateInstancePayload"]


@dataclass
class UpdateInstancePayload:
    """
    UpdateInstancePayload dataclass.

    Args:
        active (Optional[Active]): User is active
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        hidden (Optional[Hidden]): If true, the output will not be shown in the history.
        name (Optional[Name])    : The name of the creator.
        variables (Optional[Variables])
                                 :
    """

    active: Active | None = True  # User is active
    description: Description | None = ""  # Detailed text description for this Quota.
    hidden: Hidden | None = False  # If true, the output will not be shown in the history.
    name: Name | None = None  # The name of the creator.
    variables: Variables | None = None
