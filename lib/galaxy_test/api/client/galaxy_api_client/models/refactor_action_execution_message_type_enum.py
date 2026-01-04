from enum import Enum


class RefactorActionExecutionMessageTypeEnum(str, Enum):
    CONNECTION_DROP_FORCED = "connection_drop_forced"
    TOOL_STATE_ADJUSTMENT = "tool_state_adjustment"
    TOOL_VERSION_CHANGE = "tool_version_change"
    WORKFLOW_OUTPUT_DROP_FORCED = "workflow_output_drop_forced"

    def __str__(self) -> str:
        return str(self.value)
