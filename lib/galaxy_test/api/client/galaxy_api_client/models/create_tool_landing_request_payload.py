from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_tool_landing_request_payload_request_state_type_0 import (
        CreateToolLandingRequestPayloadRequestStateType0,
    )


T = TypeVar("T", bound="CreateToolLandingRequestPayload")


@_attrs_define
class CreateToolLandingRequestPayload:
    """
    Attributes:
        tool_id (str):
        client_secret (None | str | Unset):
        origin (None | str | Unset): The origin of the landing request.
        public (bool | Unset):  Default: False.
        request_state (CreateToolLandingRequestPayloadRequestStateType0 | None | Unset):
        tool_version (None | str | Unset):
    """

    tool_id: str
    client_secret: None | str | Unset = UNSET
    origin: None | str | Unset = UNSET
    public: bool | Unset = False
    request_state: CreateToolLandingRequestPayloadRequestStateType0 | None | Unset = UNSET
    tool_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_tool_landing_request_payload_request_state_type_0 import (
            CreateToolLandingRequestPayloadRequestStateType0,
        )

        tool_id = self.tool_id

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
        elif isinstance(self.request_state, CreateToolLandingRequestPayloadRequestStateType0):
            request_state = self.request_state.to_dict()
        else:
            request_state = self.request_state

        tool_version: None | str | Unset
        if isinstance(self.tool_version, Unset):
            tool_version = UNSET
        else:
            tool_version = self.tool_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tool_id": tool_id,
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
        if tool_version is not UNSET:
            field_dict["tool_version"] = tool_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_tool_landing_request_payload_request_state_type_0 import (
            CreateToolLandingRequestPayloadRequestStateType0,
        )

        d = dict(src_dict)
        tool_id = d.pop("tool_id")

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

        def _parse_request_state(data: object) -> CreateToolLandingRequestPayloadRequestStateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_state_type_0 = CreateToolLandingRequestPayloadRequestStateType0.from_dict(data)

                return request_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateToolLandingRequestPayloadRequestStateType0 | None | Unset, data)

        request_state = _parse_request_state(d.pop("request_state", UNSET))

        def _parse_tool_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_version = _parse_tool_version(d.pop("tool_version", UNSET))

        create_tool_landing_request_payload = cls(
            tool_id=tool_id,
            client_secret=client_secret,
            origin=origin,
            public=public,
            request_state=request_state,
            tool_version=tool_version,
        )

        create_tool_landing_request_payload.additional_properties = d
        return create_tool_landing_request_payload

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
