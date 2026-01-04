from dataclasses import dataclass

__all__ = ["RemoveUnlabeledWorkflowOutputs"]


@dataclass
class RemoveUnlabeledWorkflowOutputs:
    """
    RemoveUnlabeledWorkflowOutputs dataclass.

    Args:
        action_type (str)        :
    """

    action_type: str
