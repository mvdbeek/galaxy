from dataclasses import dataclass

from .errors import Errors
from .generate_time import GenerateTime
from .generate_version import GenerateVersion
from .histories import Histories
from .history_dataset_collections import HistoryDatasetCollections
from .history_datasets import HistoryDatasets
from .invocation_markdown import InvocationMarkdown
from .invocations import Invocations
from .jobs import Jobs
from .markdown import Markdown
from .workflows import Workflows

__all__ = ["InvocationReport"]


@dataclass
class InvocationReport:
    """
    Report describing workflow invocation

    Args:
        id_ (str)                : The workflow this invocation has been triggered for.
        model_class (str)        : The name of the database model class.
        title (str)              : The name of the report.
        username (str)           : The name of the user who owns this report.
        errors (Optional[Errors]): Collection of messages indicating that the resource was
                                   not shared with some (or all users) due to an error.
        generate_time (Optional[GenerateTime])
                                 : The version of Galaxy this object was generated with.
        generate_version (Optional[GenerateVersion])
                                 : The version of Galaxy this object was generated with.
        histories (Optional[Histories])
                                 : Histories associated with the invocation.
        history_dataset_collections (Optional[HistoryDatasetCollections])
                                 : History dataset collections associated with the
                                   invocation.
        history_datasets (Optional[HistoryDatasets])
                                 : History datasets associated with the invocation.
        invocation_markdown (Optional[InvocationMarkdown])
                                 : Raw galaxy-flavored markdown contents of the report.
        invocations (Optional[Invocations])
                                 : Other invocations associated with the invocation.
        jobs (Optional[Jobs])    : Jobs associated with the invocation.
        markdown (Optional[Markdown])
                                 : Raw galaxy-flavored markdown contents of the report.
        render_format (Optional[str])
                                 : Format of the invocation report.
        workflows (Optional[Workflows])
                                 : Workflows associated with the invocation.
    """

    id_: str  # The workflow this invocation has been triggered for.
    model_class: str  # The name of the database model class.
    title: str  # The name of the report.
    username: str  # The name of the user who owns this report.
    errors: Errors | None = (
        None  # Collection of messages indicating that the resource was not shared with some (or all users) due to an error.
    )
    generate_time: GenerateTime | None = None  # The version of Galaxy this object was generated with.
    generate_version: GenerateVersion | None = None  # The version of Galaxy this object was generated with.
    histories: Histories | None = None  # Histories associated with the invocation.
    history_dataset_collections: HistoryDatasetCollections | None = (
        None  # History dataset collections associated with the invocation.
    )
    history_datasets: HistoryDatasets | None = None  # History datasets associated with the invocation.
    invocation_markdown: InvocationMarkdown | None = None  # Raw galaxy-flavored markdown contents of the report.
    invocations: Invocations | None = None  # Other invocations associated with the invocation.
    jobs: Jobs | None = None  # Jobs associated with the invocation.
    markdown: Markdown | None = None  # Raw galaxy-flavored markdown contents of the report.
    render_format: str | None = "markdown"  # Format of the invocation report.
    workflows: Workflows | None = None  # Workflows associated with the invocation.
