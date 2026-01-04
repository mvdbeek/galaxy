from typing import TypeAlias

from .create_link_step import CreateLinkStep

__all__ = ["PreparableSteps"]

PreparableSteps: TypeAlias = list[CreateLinkStep] | None
