from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OAuth2Info")


@_attrs_define
class OAuth2Info:
    """
    Attributes:
        authorize_url (str):
    """

    authorize_url: str

    def to_dict(self) -> dict[str, Any]:
        authorize_url = self.authorize_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authorize_url": authorize_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authorize_url = d.pop("authorize_url")

        o_auth_2_info = cls(
            authorize_url=authorize_url,
        )

        return o_auth_2_info
