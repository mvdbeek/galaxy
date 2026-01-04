from enum import Enum, unique

__all__ = ["ActionType"]


@unique
class ActionType(str, Enum):
    """
    Types of actions agents can suggest.

    Args:
        tool_run (str)           : Value for TOOL_RUN
        documentation (str)      : Value for DOCUMENTATION
        contact_support (str)    : Value for CONTACT_SUPPORT
        view_external (str)      : Value for VIEW_EXTERNAL
        save_tool (str)          : Value for SAVE_TOOL
        refine_query (str)       : Value for REFINE_QUERY
    """

    TOOL_RUN = "tool_run"
    DOCUMENTATION = "documentation"
    CONTACT_SUPPORT = "contact_support"
    VIEW_EXTERNAL = "view_external"
    SAVE_TOOL = "save_tool"
    REFINE_QUERY = "refine_query"
