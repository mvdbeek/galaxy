from dataclasses import dataclass

__all__ = ["InvocationUpdatePayload"]


@dataclass
class InvocationUpdatePayload:
    """
    InvocationUpdatePayload dataclass

    Args:
        action (bool)            : Whether to take action on the invocation step.
    """

    action: bool  # Whether to take action on the invocation step.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action": "action",
        }
        key_transform_with_dump = {
            "action": "action",
        }
