from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_ai_agents_error_analysis_analyze_error_error_details_type_0 import (
        BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0,
    )


T = TypeVar("T", bound="BodyAiAgentsErrorAnalysisAnalyzeError")


@_attrs_define
class BodyAiAgentsErrorAnalysisAnalyzeError:
    """
    Attributes:
        query (str): Description of the error or problem
        error_details (BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0 | None | Unset): Additional error details
        job_id (None | str | Unset): Job ID for context
    """

    query: str
    error_details: BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0 | None | Unset = UNSET
    job_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.body_ai_agents_error_analysis_analyze_error_error_details_type_0 import (
            BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0,
        )

        query = self.query

        error_details: dict[str, Any] | None | Unset
        if isinstance(self.error_details, Unset):
            error_details = UNSET
        elif isinstance(self.error_details, BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0):
            error_details = self.error_details.to_dict()
        else:
            error_details = self.error_details

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if error_details is not UNSET:
            field_dict["error_details"] = error_details
        if job_id is not UNSET:
            field_dict["job_id"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_ai_agents_error_analysis_analyze_error_error_details_type_0 import (
            BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0,
        )

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_error_details(data: object) -> BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_details_type_0 = BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0.from_dict(data)

                return error_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetailsType0 | None | Unset, data)

        error_details = _parse_error_details(d.pop("error_details", UNSET))

        def _parse_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        body_ai_agents_error_analysis_analyze_error = cls(
            query=query,
            error_details=error_details,
            job_id=job_id,
        )

        body_ai_agents_error_analysis_analyze_error.additional_properties = d
        return body_ai_agents_error_analysis_analyze_error

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
