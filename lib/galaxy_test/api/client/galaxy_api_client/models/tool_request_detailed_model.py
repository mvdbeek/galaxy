from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_request_state import ToolRequestState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request import Request
    from ..models.tool_request_implicit_collection_reference import ToolRequestImplicitCollectionReference
    from ..models.tool_request_job_reference import ToolRequestJobReference


T = TypeVar("T", bound="ToolRequestDetailedModel")


@_attrs_define
class ToolRequestDetailedModel:
    """
    Attributes:
        id (str): Encoded ID of the role Example: 0123456789ABCDEF.
        request (Request):
        state (ToolRequestState):
        state_message (None | str):
        implicit_collections (list[ToolRequestImplicitCollectionReference] | Unset):
        jobs (list[ToolRequestJobReference] | Unset):
    """

    id: str
    request: Request
    state: ToolRequestState
    state_message: None | str
    implicit_collections: list[ToolRequestImplicitCollectionReference] | Unset = UNSET
    jobs: list[ToolRequestJobReference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        request = self.request.to_dict()

        state = self.state.value

        state_message: None | str
        state_message = self.state_message

        implicit_collections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.implicit_collections, Unset):
            implicit_collections = []
            for implicit_collections_item_data in self.implicit_collections:
                implicit_collections_item = implicit_collections_item_data.to_dict()
                implicit_collections.append(implicit_collections_item)

        jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "request": request,
                "state": state,
                "state_message": state_message,
            }
        )
        if implicit_collections is not UNSET:
            field_dict["implicit_collections"] = implicit_collections
        if jobs is not UNSET:
            field_dict["jobs"] = jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request import Request
        from ..models.tool_request_implicit_collection_reference import ToolRequestImplicitCollectionReference
        from ..models.tool_request_job_reference import ToolRequestJobReference

        d = dict(src_dict)
        id = d.pop("id")

        request = Request.from_dict(d.pop("request"))

        state = ToolRequestState(d.pop("state"))

        def _parse_state_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_message = _parse_state_message(d.pop("state_message"))

        _implicit_collections = d.pop("implicit_collections", UNSET)
        implicit_collections: list[ToolRequestImplicitCollectionReference] | Unset = UNSET
        if _implicit_collections is not UNSET:
            implicit_collections = []
            for implicit_collections_item_data in _implicit_collections:
                implicit_collections_item = ToolRequestImplicitCollectionReference.from_dict(
                    implicit_collections_item_data
                )

                implicit_collections.append(implicit_collections_item)

        _jobs = d.pop("jobs", UNSET)
        jobs: list[ToolRequestJobReference] | Unset = UNSET
        if _jobs is not UNSET:
            jobs = []
            for jobs_item_data in _jobs:
                jobs_item = ToolRequestJobReference.from_dict(jobs_item_data)

                jobs.append(jobs_item)

        tool_request_detailed_model = cls(
            id=id,
            request=request,
            state=state,
            state_message=state_message,
            implicit_collections=implicit_collections,
            jobs=jobs,
        )

        tool_request_detailed_model.additional_properties = d
        return tool_request_detailed_model

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
