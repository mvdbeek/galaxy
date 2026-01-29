from dataclasses import dataclass

__all__ = ["Report"]


@dataclass
class Report:
    """
    Report dataclass

    Args:
        markdown (str)           :
    """

    markdown: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "markdown": "markdown",
        }
        key_transform_with_dump = {
            "markdown": "markdown",
        }
