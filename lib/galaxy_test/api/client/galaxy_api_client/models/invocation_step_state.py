from typing import TypeAlias

from .invocation_step_state_2 import InvocationStepState2
from .job_state import JobState

__all__ = ["InvocationStepState"]

InvocationStepState: TypeAlias = InvocationStepState2 | JobState | None
"""Alias for Describes where in the scheduling process the workflow invocation step is."""
