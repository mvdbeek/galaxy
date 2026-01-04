from dataclasses import dataclass

from .action import Action
from .refactor_action_execution_message import RefactorActionExecutionMessage

__all__ = ["RefactorActionExecution"]


@dataclass
class RefactorActionExecution:
    """
    RefactorActionExecution dataclass.

    Args:
        action (Optional[Action]): Indicates what action should be performed on the dataset.
        messages (List[RefactorActionExecutionMessage])
                                 :
    """

    action: Action | None  # Indicates what action should be performed on the dataset.
    messages: list[RefactorActionExecutionMessage]
