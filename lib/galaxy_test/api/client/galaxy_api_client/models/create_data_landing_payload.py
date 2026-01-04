from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_landing_request_state import DataLandingRequestState


T = TypeVar("T", bound="CreateDataLandingPayload")


@_attrs_define
class CreateDataLandingPayload:
    """
    Attributes:
        request_state (DataLandingRequestState):
        client_secret (None | str | Unset):
        origin (None | str | Unset):
        public (bool | Unset):  Default: False.
    """

    request_state: DataLandingRequestState
    client_secret: None | str | Unset = UNSET
    origin: None | str | Unset = UNSET
    public: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        request_state = self.request_state.to_dict()

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "request_state": request_state,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if origin is not UNSET:
            field_dict["origin"] = origin
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_landing_request_state import DataLandingRequestState

        d = dict(src_dict)
        request_state = DataLandingRequestState.from_dict(d.pop("request_state"))

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

        create_data_landing_payload = cls(
            request_state=request_state,
            client_secret=client_secret,
            origin=origin,
            public=public,
        )

        return create_data_landing_payload
