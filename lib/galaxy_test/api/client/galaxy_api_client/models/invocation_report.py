from dataclasses import dataclass

from .invocation_report_errors import InvocationReportErrors
from .invocation_report_generate_time import InvocationReportGenerateTime
from .invocation_report_generate_version import InvocationReportGenerateVersion
from .invocation_report_histories import InvocationReportHistories
from .invocation_report_history_dataset_collections import InvocationReportHistoryDatasetCollections
from .invocation_report_history_datasets import InvocationReportHistoryDatasets
from .invocation_report_invocation_markdown import InvocationReportInvocationMarkdown
from .invocation_report_invocations import InvocationReportInvocations
from .invocation_report_jobs import InvocationReportJobs
from .invocation_report_markdown import InvocationReportMarkdown
from .invocation_report_workflows import InvocationReportWorkflows

__all__ = ["InvocationReport"]


@dataclass
class InvocationReport:
    """
    Report describing workflow invocation

    Args:
        id_ (str)                : The workflow this invocation has been triggered for.
                                   (maps from 'id')
        model_class (str)        : The name of the database model class.
        title (str)              : The name of the report.
        username (str)           : The name of the user who owns this report.
        errors (InvocationReportErrors | None)
                                 : Errors associated with the invocation.
        generate_time (InvocationReportGenerateTime | None)
                                 : The version of Galaxy this object was generated with.
        generate_version (InvocationReportGenerateVersion | None)
                                 : The version of Galaxy this object was generated with.
        histories (InvocationReportHistories | None)
                                 : Histories associated with the invocation.
        history_dataset_collections (InvocationReportHistoryDatasetCollections | None)
                                 : History dataset collections associated with the
                                   invocation.
        history_datasets (InvocationReportHistoryDatasets | None)
                                 : History datasets associated with the invocation.
        invocation_markdown (InvocationReportInvocationMarkdown | None)
                                 : Raw galaxy-flavored markdown contents of the report.
        invocations (InvocationReportInvocations | None)
                                 : Other invocations associated with the invocation.
        jobs (InvocationReportJobs | None)
                                 : Jobs associated with the invocation.
        markdown (InvocationReportMarkdown | None)
                                 : Raw galaxy-flavored markdown contents of the report.
        render_format (str | None): Format of the invocation report.
        workflows (InvocationReportWorkflows | None)
                                 : Workflows associated with the invocation.
    """

    id_: str  # The workflow this invocation has been triggered for. (maps from 'id')
    model_class: str  # The name of the database model class.
    title: str  # The name of the report.
    username: str  # The name of the user who owns this report.
    errors: InvocationReportErrors | None = None  # Errors associated with the invocation.
    generate_time: InvocationReportGenerateTime | None = None  # The version of Galaxy this object was generated with.
    generate_version: InvocationReportGenerateVersion | None = (
        None  # The version of Galaxy this object was generated with.
    )
    histories: InvocationReportHistories | None = None  # Histories associated with the invocation.
    history_dataset_collections: InvocationReportHistoryDatasetCollections | None = (
        None  # History dataset collections associated with the invocation.
    )
    history_datasets: InvocationReportHistoryDatasets | None = None  # History datasets associated with the invocation.
    invocation_markdown: InvocationReportInvocationMarkdown | None = (
        None  # Raw galaxy-flavored markdown contents of the report.
    )
    invocations: InvocationReportInvocations | None = None  # Other invocations associated with the invocation.
    jobs: InvocationReportJobs | None = None  # Jobs associated with the invocation.
    markdown: InvocationReportMarkdown | None = None  # Raw galaxy-flavored markdown contents of the report.
    render_format: str | None = "markdown"  # Format of the invocation report.
    workflows: InvocationReportWorkflows | None = None  # Workflows associated with the invocation.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "errors": "errors",
            "generate_time": "generate_time",
            "generate_version": "generate_version",
            "histories": "histories",
            "history_dataset_collections": "history_dataset_collections",
            "history_datasets": "history_datasets",
            "id": "id_",
            "invocation_markdown": "invocation_markdown",
            "invocations": "invocations",
            "jobs": "jobs",
            "markdown": "markdown",
            "model_class": "model_class",
            "render_format": "render_format",
            "title": "title",
            "username": "username",
            "workflows": "workflows",
        }
        key_transform_with_dump = {
            "errors": "errors",
            "generate_time": "generate_time",
            "generate_version": "generate_version",
            "histories": "histories",
            "history_dataset_collections": "history_dataset_collections",
            "history_datasets": "history_datasets",
            "id_": "id",
            "invocation_markdown": "invocation_markdown",
            "invocations": "invocations",
            "jobs": "jobs",
            "markdown": "markdown",
            "model_class": "model_class",
            "render_format": "render_format",
            "title": "title",
            "username": "username",
            "workflows": "workflows",
        }
