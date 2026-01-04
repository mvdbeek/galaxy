from enum import Enum, unique

__all__ = ["RefactorActionExecutionMessageTypeEnum"]


@unique
class RefactorActionExecutionMessageTypeEnum(str, Enum):
    """
    RefactorActionExecutionMessageTypeEnum Enum

    Args:
        tool_version_change (str): Value for TOOL_VERSION_CHANGE
        tool_state_adjustment (str)
                                 : Value for TOOL_STATE_ADJUSTMENT
        connection_drop_forced (str)
                                 : Value for CONNECTION_DROP_FORCED
        workflow_output_drop_forced (str)
                                 : Value for WORKFLOW_OUTPUT_DROP_FORCED
    """

    TOOL_VERSION_CHANGE = "tool_version_change"
    TOOL_STATE_ADJUSTMENT = "tool_state_adjustment"
    CONNECTION_DROP_FORCED = "connection_drop_forced"
    WORKFLOW_OUTPUT_DROP_FORCED = "workflow_output_drop_forced"
