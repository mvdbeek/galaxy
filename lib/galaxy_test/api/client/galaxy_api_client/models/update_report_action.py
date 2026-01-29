from dataclasses import dataclass

from .report import Report

__all__ = ["UpdateReportAction"]


@dataclass
class UpdateReportAction:
    """
    UpdateReportAction dataclass.

    Args:
        action_type (str)        :
        report (Report)          :
    """

    action_type: str
    report: Report
