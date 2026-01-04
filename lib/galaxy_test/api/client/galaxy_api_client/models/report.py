from dataclasses import dataclass

__all__ = ["Report"]


@dataclass
class Report:
    """
    Report dataclass.

    Args:
        markdown (str)           :
    """

    markdown: str
