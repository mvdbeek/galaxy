from dataclasses import dataclass

__all__ = ["InvocationCancellationUserRequestResponse"]


@dataclass
class InvocationCancellationUserRequestResponse:
    """
    InvocationCancellationUserRequestResponse dataclass.

    Args:
        reason (str)             :
    """

    reason: str
