from dataclasses import dataclass

__all__ = ["UpgradeAllStepsAction"]


@dataclass
class UpgradeAllStepsAction:
    """
    UpgradeAllStepsAction dataclass.

    Args:
        action_type (str)        :
    """

    action_type: str
