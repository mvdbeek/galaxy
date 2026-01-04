from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.landing_request_state import LandingRequestState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_landing_request_request_state_type_0 import ToolLandingRequestRequestStateType0


T = TypeVar("T", bound="ToolLandingRequest")


@_attrs_define
class ToolLandingRequest:
    """
    Attributes:
        state (LandingRequestState):
        tool_id (str):
        uuid (str): Universal unique identifier for this dataset.
        origin (None | str | Unset):
        request_state (None | ToolLandingRequestRequestStateType0 | Unset):
        tool_version (None | str | Unset):
    """

    state: LandingRequestState
    tool_id: str
    uuid: str
    origin: None | str | Unset = UNSET
    request_state: None | ToolLandingRequestRequestStateType0 | Unset = UNSET
    tool_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_landing_request_request_state_type_0 import ToolLandingRequestRequestStateType0

        state = self.state.value

        tool_id = self.tool_id

        uuid = self.uuid

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        request_state: dict[str, Any] | None | Unset
        if isinstance(self.request_state, Unset):
            request_state = UNSET
        elif isinstance(self.request_state, ToolLandingRequestRequestStateType0):
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
                "state": state,
                "tool_id": tool_id,
                "uuid": uuid,
            }
        )
        if origin is not UNSET:
            field_dict["origin"] = origin
        if request_state is not UNSET:
            field_dict["request_state"] = request_state
        if tool_version is not UNSET:
            field_dict["tool_version"] = tool_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_landing_request_request_state_type_0 import ToolLandingRequestRequestStateType0

        d = dict(src_dict)
        state = LandingRequestState(d.pop("state"))

        tool_id = d.pop("tool_id")

        uuid = d.pop("uuid")

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_request_state(data: object) -> None | ToolLandingRequestRequestStateType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_state_type_0 = ToolLandingRequestRequestStateType0.from_dict(data)

                return request_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolLandingRequestRequestStateType0 | Unset, data)

        request_state = _parse_request_state(d.pop("request_state", UNSET))

        def _parse_tool_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_version = _parse_tool_version(d.pop("tool_version", UNSET))

        tool_landing_request = cls(
            state=state,
            tool_id=tool_id,
            uuid=uuid,
            origin=origin,
            request_state=request_state,
            tool_version=tool_version,
        )

        tool_landing_request.additional_properties = d
        return tool_landing_request

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
