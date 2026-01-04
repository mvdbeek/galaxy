from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.landing_request_state import LandingRequestState
from ..models.workflow_landing_request_workflow_target_type import WorkflowLandingRequestWorkflowTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_state import RequestState


T = TypeVar("T", bound="WorkflowLandingRequest")


@_attrs_define
class WorkflowLandingRequest:
    """
    Attributes:
        request_state (RequestState):
        state (LandingRequestState):
        uuid (str): Universal unique identifier for this dataset.
        workflow_id (str):
        workflow_target_type (WorkflowLandingRequestWorkflowTargetType):
        origin (None | str | Unset):
    """

    request_state: RequestState
    state: LandingRequestState
    uuid: str
    workflow_id: str
    workflow_target_type: WorkflowLandingRequestWorkflowTargetType
    origin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_state = self.request_state.to_dict()

        state = self.state.value

        uuid = self.uuid

        workflow_id = self.workflow_id

        workflow_target_type = self.workflow_target_type.value

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_state": request_state,
                "state": state,
                "uuid": uuid,
                "workflow_id": workflow_id,
                "workflow_target_type": workflow_target_type,
            }
        )
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_state import RequestState

        d = dict(src_dict)
        request_state = RequestState.from_dict(d.pop("request_state"))

        state = LandingRequestState(d.pop("state"))

        uuid = d.pop("uuid")

        workflow_id = d.pop("workflow_id")

        workflow_target_type = WorkflowLandingRequestWorkflowTargetType(d.pop("workflow_target_type"))

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        workflow_landing_request = cls(
            request_state=request_state,
            state=state,
            uuid=uuid,
            workflow_id=workflow_id,
            workflow_target_type=workflow_target_type,
            origin=origin,
        )

        workflow_landing_request.additional_properties = d
        return workflow_landing_request

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
