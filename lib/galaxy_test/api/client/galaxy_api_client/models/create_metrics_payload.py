from dataclasses import dataclass, field

from .metric import Metric

__all__ = ["CreateMetricsPayload"]


@dataclass
class CreateMetricsPayload:
    """
    CreateMetricsPayload dataclass.

    Args:
        metrics (Optional[List[Metric]])
                                 :
    """

    metrics: list[Metric] | None = field(default_factory=list)
