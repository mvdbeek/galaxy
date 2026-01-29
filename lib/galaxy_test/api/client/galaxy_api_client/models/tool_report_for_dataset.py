from dataclasses import dataclass

from .tool_report_for_dataset_content import ToolReportForDatasetContent
from .tool_report_for_dataset_generate_time import ToolReportForDatasetGenerateTime
from .tool_report_for_dataset_generate_version import ToolReportForDatasetGenerateVersion

__all__ = ["ToolReportForDataset"]


@dataclass
class ToolReportForDataset:
    """
    ToolReportForDataset dataclass

    Args:
        content (ToolReportForDatasetContent | None)
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        generate_time (ToolReportForDatasetGenerateTime | None)
                                 : The version of Galaxy this object was generated with.
        generate_version (ToolReportForDatasetGenerateVersion | None)
                                 : The version of Galaxy this object was generated with.
    """

    content: ToolReportForDatasetContent | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    generate_time: ToolReportForDatasetGenerateTime | None = (
        None  # The version of Galaxy this object was generated with.
    )
    generate_version: ToolReportForDatasetGenerateVersion | None = (
        None  # The version of Galaxy this object was generated with.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "generate_time": "generate_time",
            "generate_version": "generate_version",
        }
        key_transform_with_dump = {
            "content": "content",
            "generate_time": "generate_time",
            "generate_version": "generate_version",
        }
