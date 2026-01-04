from enum import Enum


class ActionType(str, Enum):
    CONTACT_SUPPORT = "contact_support"
    DOCUMENTATION = "documentation"
    REFINE_QUERY = "refine_query"
    SAVE_TOOL = "save_tool"
    TOOL_RUN = "tool_run"
    VIEW_EXTERNAL = "view_external"

    def __str__(self) -> str:
        return str(self.value)
