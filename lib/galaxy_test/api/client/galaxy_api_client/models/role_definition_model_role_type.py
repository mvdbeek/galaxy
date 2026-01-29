from enum import Enum, unique

__all__ = ["RoleDefinitionModelRoleType"]


@unique
class RoleDefinitionModelRoleType(str, Enum):
    """
    RoleDefinitionModelRoleType Enum

    Args:
        admin (str)              : Value for ADMIN
        user_tool_create (str)   : Value for USER_TOOL_CREATE
        user_tool_execute (str)  : Value for USER_TOOL_EXECUTE
    """

    ADMIN = "admin"
    USER_TOOL_CREATE = "user_tool_create"
    USER_TOOL_EXECUTE = "user_tool_execute"
