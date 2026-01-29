from dataclasses import dataclass

__all__ = ["JobMetric"]


@dataclass
class JobMetric:
    """
    JobMetric dataclass.

    Args:
        name (str)               : The name of the metric variable.
        plugin (str)             : The instrumenter plugin that generated this metric.
        raw_value (str)          : The raw value of the metric as a string.
        title (str)              : A descriptive title for this metric.
        value (str)              : The textual representation of the metric value.
    """

    name: str  # The name of the metric variable.
    plugin: str  # The instrumenter plugin that generated this metric.
    raw_value: str  # The raw value of the metric as a string.
    title: str  # A descriptive title for this metric.
    value: str  # The textual representation of the metric value.
