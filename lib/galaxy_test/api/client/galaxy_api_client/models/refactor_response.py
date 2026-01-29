from dataclasses import dataclass

from .refactor_action_execution import RefactorActionExecution

__all__ = ["RefactorResponse"]


@dataclass
class RefactorResponse:
    """
    RefactorResponse dataclass

    Args:
        action_executions (List[RefactorActionExecution])
                                 :
        dry_run (bool)           :
        workflow (str)           :
    """

    action_executions: list[RefactorActionExecution]
    dry_run: bool
    workflow: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_executions": "action_executions",
            "dry_run": "dry_run",
            "workflow": "workflow",
        }
        key_transform_with_dump = {
            "action_executions": "action_executions",
            "dry_run": "dry_run",
            "workflow": "workflow",
        }
