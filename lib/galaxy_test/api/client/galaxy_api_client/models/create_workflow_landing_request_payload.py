from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workflow_landing_request_payload_workflow_target_type import (
    CreateWorkflowLandingRequestPayloadWorkflowTargetType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_workflow_landing_request_payload_request_state_type_0 import (
        CreateWorkflowLandingRequestPayloadRequestStateType0,
    )


T = TypeVar("T", bound="CreateWorkflowLandingRequestPayload")


@_attrs_define
class CreateWorkflowLandingRequestPayload:
    """
    Attributes:
        workflow_id (str):
        workflow_target_type (CreateWorkflowLandingRequestPayloadWorkflowTargetType):
        client_secret (None | str | Unset):
        origin (None | str | Unset): The origin of the landing request.
        public (bool | Unset): If workflow landing request is public anyone with the uuid can use the landing request.
            If not public the request must be claimed before use and additional verification might occur. Default: False.
        request_state (CreateWorkflowLandingRequestPayloadRequestStateType0 | None | Unset):
    """

    workflow_id: str
    workflow_target_type: CreateWorkflowLandingRequestPayloadWorkflowTargetType
    client_secret: None | str | Unset = UNSET
    origin: None | str | Unset = UNSET
    public: bool | Unset = False
    request_state: CreateWorkflowLandingRequestPayloadRequestStateType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workflow_landing_request_payload_request_state_type_0 import (
            CreateWorkflowLandingRequestPayloadRequestStateType0,
        )

        workflow_id = self.workflow_id

        workflow_target_type = self.workflow_target_type.value

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        public = self.public

        request_state: dict[str, Any] | None | Unset
        if isinstance(self.request_state, Unset):
            request_state = UNSET
        elif isinstance(self.request_state, CreateWorkflowLandingRequestPayloadRequestStateType0):
            request_state = self.request_state.to_dict()
        else:
            request_state = self.request_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflow_id": workflow_id,
                "workflow_target_type": workflow_target_type,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if origin is not UNSET:
            field_dict["origin"] = origin
        if public is not UNSET:
            field_dict["public"] = public
        if request_state is not UNSET:
            field_dict["request_state"] = request_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_landing_request_payload_request_state_type_0 import (
            CreateWorkflowLandingRequestPayloadRequestStateType0,
        )

        d = dict(src_dict)
        workflow_id = d.pop("workflow_id")

        workflow_target_type = CreateWorkflowLandingRequestPayloadWorkflowTargetType(d.pop("workflow_target_type"))

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        public = d.pop("public", UNSET)

        def _parse_request_state(data: object) -> CreateWorkflowLandingRequestPayloadRequestStateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_state_type_0 = CreateWorkflowLandingRequestPayloadRequestStateType0.from_dict(data)

                return request_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateWorkflowLandingRequestPayloadRequestStateType0 | None | Unset, data)

        request_state = _parse_request_state(d.pop("request_state", UNSET))

        create_workflow_landing_request_payload = cls(
            workflow_id=workflow_id,
            workflow_target_type=workflow_target_type,
            client_secret=client_secret,
            origin=origin,
            public=public,
            request_state=request_state,
        )

        create_workflow_landing_request_payload.additional_properties = d
        return create_workflow_landing_request_payload

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
