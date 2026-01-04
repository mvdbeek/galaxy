from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invocation_report_errors_type_0_item import InvocationReportErrorsType0Item
    from ..models.invocation_report_histories_type_0 import InvocationReportHistoriesType0
    from ..models.invocation_report_history_dataset_collections_type_0 import (
        InvocationReportHistoryDatasetCollectionsType0,
    )
    from ..models.invocation_report_history_datasets_type_0 import InvocationReportHistoryDatasetsType0
    from ..models.invocation_report_invocations_type_0 import InvocationReportInvocationsType0
    from ..models.invocation_report_jobs_type_0 import InvocationReportJobsType0
    from ..models.invocation_report_workflows_type_0 import InvocationReportWorkflowsType0


T = TypeVar("T", bound="InvocationReport")


@_attrs_define
class InvocationReport:
    """Report describing workflow invocation

    Attributes:
        id (str): The workflow this invocation has been triggered for. Example: 0123456789ABCDEF.
        model_class (Literal['Report']): The name of the database model class.
        title (str): The name of the report.
        username (str): The name of the user who owns this report.
        errors (list[InvocationReportErrorsType0Item] | None | Unset): Errors associated with the invocation.
        generate_time (None | str | Unset): The version of Galaxy this object was generated with.
        generate_version (None | str | Unset): The version of Galaxy this object was generated with.
        histories (InvocationReportHistoriesType0 | None | Unset): Histories associated with the invocation.
        history_dataset_collections (InvocationReportHistoryDatasetCollectionsType0 | None | Unset): History dataset
            collections associated with the invocation.
        history_datasets (InvocationReportHistoryDatasetsType0 | None | Unset): History datasets associated with the
            invocation.
        invocation_markdown (None | str | Unset): Raw galaxy-flavored markdown contents of the report.
        invocations (InvocationReportInvocationsType0 | None | Unset): Other invocations associated with the invocation.
        jobs (InvocationReportJobsType0 | None | Unset): Jobs associated with the invocation.
        markdown (None | str | Unset): Raw galaxy-flavored markdown contents of the report.
        render_format (Literal['markdown'] | Unset): Format of the invocation report. Default: 'markdown'.
        workflows (InvocationReportWorkflowsType0 | None | Unset): Workflows associated with the invocation.
    """

    id: str
    model_class: Literal["Report"]
    title: str
    username: str
    errors: list[InvocationReportErrorsType0Item] | None | Unset = UNSET
    generate_time: None | str | Unset = UNSET
    generate_version: None | str | Unset = UNSET
    histories: InvocationReportHistoriesType0 | None | Unset = UNSET
    history_dataset_collections: InvocationReportHistoryDatasetCollectionsType0 | None | Unset = UNSET
    history_datasets: InvocationReportHistoryDatasetsType0 | None | Unset = UNSET
    invocation_markdown: None | str | Unset = UNSET
    invocations: InvocationReportInvocationsType0 | None | Unset = UNSET
    jobs: InvocationReportJobsType0 | None | Unset = UNSET
    markdown: None | str | Unset = UNSET
    render_format: Literal["markdown"] | Unset = "markdown"
    workflows: InvocationReportWorkflowsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invocation_report_histories_type_0 import InvocationReportHistoriesType0
        from ..models.invocation_report_history_dataset_collections_type_0 import (
            InvocationReportHistoryDatasetCollectionsType0,
        )
        from ..models.invocation_report_history_datasets_type_0 import InvocationReportHistoryDatasetsType0
        from ..models.invocation_report_invocations_type_0 import InvocationReportInvocationsType0
        from ..models.invocation_report_jobs_type_0 import InvocationReportJobsType0
        from ..models.invocation_report_workflows_type_0 import InvocationReportWorkflowsType0

        id = self.id

        model_class = self.model_class

        title = self.title

        username = self.username

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        generate_time: None | str | Unset
        if isinstance(self.generate_time, Unset):
            generate_time = UNSET
        else:
            generate_time = self.generate_time

        generate_version: None | str | Unset
        if isinstance(self.generate_version, Unset):
            generate_version = UNSET
        else:
            generate_version = self.generate_version

        histories: dict[str, Any] | None | Unset
        if isinstance(self.histories, Unset):
            histories = UNSET
        elif isinstance(self.histories, InvocationReportHistoriesType0):
            histories = self.histories.to_dict()
        else:
            histories = self.histories

        history_dataset_collections: dict[str, Any] | None | Unset
        if isinstance(self.history_dataset_collections, Unset):
            history_dataset_collections = UNSET
        elif isinstance(self.history_dataset_collections, InvocationReportHistoryDatasetCollectionsType0):
            history_dataset_collections = self.history_dataset_collections.to_dict()
        else:
            history_dataset_collections = self.history_dataset_collections

        history_datasets: dict[str, Any] | None | Unset
        if isinstance(self.history_datasets, Unset):
            history_datasets = UNSET
        elif isinstance(self.history_datasets, InvocationReportHistoryDatasetsType0):
            history_datasets = self.history_datasets.to_dict()
        else:
            history_datasets = self.history_datasets

        invocation_markdown: None | str | Unset
        if isinstance(self.invocation_markdown, Unset):
            invocation_markdown = UNSET
        else:
            invocation_markdown = self.invocation_markdown

        invocations: dict[str, Any] | None | Unset
        if isinstance(self.invocations, Unset):
            invocations = UNSET
        elif isinstance(self.invocations, InvocationReportInvocationsType0):
            invocations = self.invocations.to_dict()
        else:
            invocations = self.invocations

        jobs: dict[str, Any] | None | Unset
        if isinstance(self.jobs, Unset):
            jobs = UNSET
        elif isinstance(self.jobs, InvocationReportJobsType0):
            jobs = self.jobs.to_dict()
        else:
            jobs = self.jobs

        markdown: None | str | Unset
        if isinstance(self.markdown, Unset):
            markdown = UNSET
        else:
            markdown = self.markdown

        render_format = self.render_format

        workflows: dict[str, Any] | None | Unset
        if isinstance(self.workflows, Unset):
            workflows = UNSET
        elif isinstance(self.workflows, InvocationReportWorkflowsType0):
            workflows = self.workflows.to_dict()
        else:
            workflows = self.workflows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model_class": model_class,
                "title": title,
                "username": username,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors
        if generate_time is not UNSET:
            field_dict["generate_time"] = generate_time
        if generate_version is not UNSET:
            field_dict["generate_version"] = generate_version
        if histories is not UNSET:
            field_dict["histories"] = histories
        if history_dataset_collections is not UNSET:
            field_dict["history_dataset_collections"] = history_dataset_collections
        if history_datasets is not UNSET:
            field_dict["history_datasets"] = history_datasets
        if invocation_markdown is not UNSET:
            field_dict["invocation_markdown"] = invocation_markdown
        if invocations is not UNSET:
            field_dict["invocations"] = invocations
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if markdown is not UNSET:
            field_dict["markdown"] = markdown
        if render_format is not UNSET:
            field_dict["render_format"] = render_format
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invocation_report_errors_type_0_item import InvocationReportErrorsType0Item
        from ..models.invocation_report_histories_type_0 import InvocationReportHistoriesType0
        from ..models.invocation_report_history_dataset_collections_type_0 import (
            InvocationReportHistoryDatasetCollectionsType0,
        )
        from ..models.invocation_report_history_datasets_type_0 import InvocationReportHistoryDatasetsType0
        from ..models.invocation_report_invocations_type_0 import InvocationReportInvocationsType0
        from ..models.invocation_report_jobs_type_0 import InvocationReportJobsType0
        from ..models.invocation_report_workflows_type_0 import InvocationReportWorkflowsType0

        d = dict(src_dict)
        id = d.pop("id")

        model_class = cast(Literal["Report"], d.pop("model_class"))
        if model_class != "Report":
            raise ValueError(f"model_class must match const 'Report', got '{model_class}'")

        title = d.pop("title")

        username = d.pop("username")

        def _parse_errors(data: object) -> list[InvocationReportErrorsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = InvocationReportErrorsType0Item.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InvocationReportErrorsType0Item] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_generate_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generate_time = _parse_generate_time(d.pop("generate_time", UNSET))

        def _parse_generate_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generate_version = _parse_generate_version(d.pop("generate_version", UNSET))

        def _parse_histories(data: object) -> InvocationReportHistoriesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                histories_type_0 = InvocationReportHistoriesType0.from_dict(data)

                return histories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvocationReportHistoriesType0 | None | Unset, data)

        histories = _parse_histories(d.pop("histories", UNSET))

        def _parse_history_dataset_collections(
            data: object,
        ) -> InvocationReportHistoryDatasetCollectionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                history_dataset_collections_type_0 = InvocationReportHistoryDatasetCollectionsType0.from_dict(data)

                return history_dataset_collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvocationReportHistoryDatasetCollectionsType0 | None | Unset, data)

        history_dataset_collections = _parse_history_dataset_collections(d.pop("history_dataset_collections", UNSET))

        def _parse_history_datasets(data: object) -> InvocationReportHistoryDatasetsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                history_datasets_type_0 = InvocationReportHistoryDatasetsType0.from_dict(data)

                return history_datasets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvocationReportHistoryDatasetsType0 | None | Unset, data)

        history_datasets = _parse_history_datasets(d.pop("history_datasets", UNSET))

        def _parse_invocation_markdown(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invocation_markdown = _parse_invocation_markdown(d.pop("invocation_markdown", UNSET))

        def _parse_invocations(data: object) -> InvocationReportInvocationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocations_type_0 = InvocationReportInvocationsType0.from_dict(data)

                return invocations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvocationReportInvocationsType0 | None | Unset, data)

        invocations = _parse_invocations(d.pop("invocations", UNSET))

        def _parse_jobs(data: object) -> InvocationReportJobsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                jobs_type_0 = InvocationReportJobsType0.from_dict(data)

                return jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvocationReportJobsType0 | None | Unset, data)

        jobs = _parse_jobs(d.pop("jobs", UNSET))

        def _parse_markdown(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        markdown = _parse_markdown(d.pop("markdown", UNSET))

        render_format = cast(Literal["markdown"] | Unset, d.pop("render_format", UNSET))
        if render_format != "markdown" and not isinstance(render_format, Unset):
            raise ValueError(f"render_format must match const 'markdown', got '{render_format}'")

        def _parse_workflows(data: object) -> InvocationReportWorkflowsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workflows_type_0 = InvocationReportWorkflowsType0.from_dict(data)

                return workflows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvocationReportWorkflowsType0 | None | Unset, data)

        workflows = _parse_workflows(d.pop("workflows", UNSET))

        invocation_report = cls(
            id=id,
            model_class=model_class,
            title=title,
            username=username,
            errors=errors,
            generate_time=generate_time,
            generate_version=generate_version,
            histories=histories,
            history_dataset_collections=history_dataset_collections,
            history_datasets=history_datasets,
            invocation_markdown=invocation_markdown,
            invocations=invocations,
            jobs=jobs,
            markdown=markdown,
            render_format=render_format,
            workflows=workflows,
        )

        invocation_report.additional_properties = d
        return invocation_report

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
