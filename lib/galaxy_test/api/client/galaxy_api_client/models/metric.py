from dataclasses import dataclass

__all__ = ["Metric"]


@dataclass
class Metric:
    """
    Metric dataclass.

    Args:
        args (str)               : A JSON string containing an array of extra data.
        level (int)              : An integer representing the metric's log level.
        namespace (str)          : Label indicating the source of the metric.
        time_ (str)              : The timestamp in ISO format.
    """

    args: str  # A JSON string containing an array of extra data.
    level: int  # An integer representing the metric's log level.
    namespace: str  # Label indicating the source of the metric.
    time_: str  # The timestamp in ISO format.
