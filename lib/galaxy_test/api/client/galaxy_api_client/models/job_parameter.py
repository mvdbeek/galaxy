from dataclasses import dataclass

from .notes import Notes
from .value import Value

__all__ = ["JobParameter"]


@dataclass
class JobParameter:
    """
    JobParameter dataclass.

    Args:
        depth (int)              : The depth of the job parameter.
        text (str)               : Text associated with the job parameter.
        notes (Optional[Notes])  : Notes associated with the job parameter.
        value (Optional[Value])  : TODO
    """

    depth: int  # The depth of the job parameter.
    text: str  # Text associated with the job parameter.
    notes: Notes | None = None  # Notes associated with the job parameter.
    value: Value | None = False  # TODO
