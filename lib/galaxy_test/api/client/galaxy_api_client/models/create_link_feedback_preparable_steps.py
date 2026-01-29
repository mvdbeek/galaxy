from typing import TypeAlias

from .create_link_step import CreateLinkStep

__all__ = ["CreateLinkFeedbackPreparableSteps"]

CreateLinkFeedbackPreparableSteps: TypeAlias = list[CreateLinkStep] | None
