from typing import TypeAlias

__all__ = ["ToolStepToolUuid"]

ToolStepToolUuid: TypeAlias = str | None
"""Alias for The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set."""
