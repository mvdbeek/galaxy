from dataclasses import dataclass

from .refactor_action_execution import RefactorActionExecution

__all__ = ["RefactorResponse"]


@dataclass
class RefactorResponse:
    """
    RefactorResponse dataclass.

    Args:
        action_executions (List[RefactorActionExecution])
                                 :
        dry_run (bool)           :
        workflow (str)           :
    """

    action_executions: list[RefactorActionExecution]
    dry_run: bool
    workflow: str
