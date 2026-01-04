from dataclasses import dataclass

from .variables import Variables

__all__ = ["TestUpdateInstancePayload"]


@dataclass
class TestUpdateInstancePayload:
    """
    TestUpdateInstancePayload dataclass.

    Args:
        variables (Optional[Variables])
                                 :
    """

    variables: Variables | None = None
