from enum import Enum


class RoleDefinitionModelRoleType(str, Enum):
    ADMIN = "admin"
    USER_TOOL_CREATE = "user_tool_create"
    USER_TOOL_EXECUTE = "user_tool_execute"

    def __str__(self) -> str:
        return str(self.value)
