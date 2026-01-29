from dataclasses import dataclass, field

from .metric import Metric

__all__ = ["CreateMetricsPayload"]


@dataclass
class CreateMetricsPayload:
    """
    CreateMetricsPayload dataclass

    Args:
        metrics (List[Metric] | None)
                                 :
    """

    metrics: list[Metric] | None = field(default_factory=list)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "metrics": "metrics",
        }
        key_transform_with_dump = {
            "metrics": "metrics",
        }
