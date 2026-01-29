from dataclasses import dataclass

__all__ = ["InvocationUpdatePayload"]


@dataclass
class InvocationUpdatePayload:
    """
    InvocationUpdatePayload dataclass.

    Args:
        action (bool)            : Whether to take action on the invocation step.
    """

    action: bool  # Whether to take action on the invocation step.
