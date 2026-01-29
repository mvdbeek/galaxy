from typing import TypeAlias

__all__ = ["InputParameterStepToolUuid"]

InputParameterStepToolUuid: TypeAlias = str | None
"""Alias for The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set."""
