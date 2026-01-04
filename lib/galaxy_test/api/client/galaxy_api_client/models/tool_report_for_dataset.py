from dataclasses import dataclass

from .content import Content
from .generate_time import GenerateTime
from .generate_version import GenerateVersion

__all__ = ["ToolReportForDataset"]


@dataclass
class ToolReportForDataset:
    """
    ToolReportForDataset dataclass.

    Args:
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        generate_time (Optional[GenerateTime])
                                 : The version of Galaxy this object was generated with.
        generate_version (Optional[GenerateVersion])
                                 : The version of Galaxy this object was generated with.
    """

    content: Content | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    generate_time: GenerateTime | None = None  # The version of Galaxy this object was generated with.
    generate_version: GenerateVersion | None = None  # The version of Galaxy this object was generated with.
