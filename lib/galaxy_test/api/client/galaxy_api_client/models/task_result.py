from dataclasses import dataclass

from .task_state import TaskState

__all__ = ["TaskResult"]


@dataclass
class TaskResult:
    """
    Contains information about the result of an asynchronous task.

    Args:
        result (str)             : The result message of the task. Empty if the task is
                                   still running. If the task failed, this will contain the
                                   exception message.
        state (TaskState)        : Enum representing the possible states of a task.
    """

    result: str  # The result message of the task. Empty if the task is still running. If the task failed, this will contain the exception message.
    state: TaskState  # Enum representing the possible states of a task.
