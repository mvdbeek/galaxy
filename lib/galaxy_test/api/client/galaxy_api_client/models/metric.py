from dataclasses import dataclass

__all__ = ["Metric"]


@dataclass
class Metric:
    """
    Metric dataclass

    Args:
        args (str)               : A JSON string containing an array of extra data.
        level (int)              : An integer representing the metric's log level.
        namespace (str)          : Label indicating the source of the metric.
        time_ (str)              : The timestamp in ISO format. (maps from 'time')
    """

    args: str  # A JSON string containing an array of extra data.
    level: int  # An integer representing the metric's log level.
    namespace: str  # Label indicating the source of the metric.
    time_: str  # The timestamp in ISO format. (maps from 'time')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "args": "args",
            "level": "level",
            "namespace": "namespace",
            "time": "time_",
        }
        key_transform_with_dump = {
            "args": "args",
            "level": "level",
            "namespace": "namespace",
            "time_": "time",
        }
