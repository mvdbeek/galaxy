from enum import Enum, unique

__all__ = ["ItemType"]


@unique
class ItemType(str, Enum):
    """
    The type of the shared item.

    Args:
        history (str)            : Value for HISTORY
        workflow (str)           : Value for WORKFLOW
        visualization (str)      : Value for VISUALIZATION
        page (str)               : Value for PAGE
    """

    HISTORY = "history"
    WORKFLOW = "workflow"
    VISUALIZATION = "visualization"
    PAGE = "page"
