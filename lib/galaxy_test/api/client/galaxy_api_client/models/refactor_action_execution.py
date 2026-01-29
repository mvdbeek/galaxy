from dataclasses import dataclass

from .refactor_action_execution_action import RefactorActionExecutionAction
from .refactor_action_execution_message import RefactorActionExecutionMessage

__all__ = ["RefactorActionExecution"]


@dataclass
class RefactorActionExecution:
    """
    RefactorActionExecution dataclass

    Args:
        action (RefactorActionExecutionAction)
                                 :
        messages (List[RefactorActionExecutionMessage])
                                 :
    """

    action: RefactorActionExecutionAction
    messages: list[RefactorActionExecutionMessage]

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action": "action",
            "messages": "messages",
        }
        key_transform_with_dump = {
            "action": "action",
            "messages": "messages",
        }
