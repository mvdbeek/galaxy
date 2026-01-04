from dataclasses import dataclass

__all__ = ["UpdateNameAction"]


@dataclass
class UpdateNameAction:
    """
    UpdateNameAction dataclass.

    Args:
        action_type (str)        :
        name (str)               :
    """

    action_type: str
    name: str
