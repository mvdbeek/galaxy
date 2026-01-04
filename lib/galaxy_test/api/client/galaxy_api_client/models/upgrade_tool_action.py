from dataclasses import dataclass

from .step import Step
from .tool_version import ToolVersion

__all__ = ["UpgradeToolAction"]


@dataclass
class UpgradeToolAction:
    """
    UpgradeToolAction dataclass.

    Args:
        action_type (str)        :
        step (Step)              : The target step for this action.
        tool_version (Optional[ToolVersion])
                                 : The version of the tool associated with this step.
    """

    action_type: str
    step: Step  # The target step for this action.
    tool_version: ToolVersion | None = None  # The version of the tool associated with this step.
