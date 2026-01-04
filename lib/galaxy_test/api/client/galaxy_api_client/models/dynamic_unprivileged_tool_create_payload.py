from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_tool_source import UserToolSource


T = TypeVar("T", bound="DynamicUnprivilegedToolCreatePayload")


@_attrs_define
class DynamicUnprivilegedToolCreatePayload:
    """
    Attributes:
        representation (UserToolSource):
        active (bool | None | Unset):  Default: True.
        hidden (bool | None | Unset):  Default: False.
        src (Literal['representation'] | Unset):  Default: 'representation'.
    """

    representation: UserToolSource
    active: bool | None | Unset = True
    hidden: bool | None | Unset = False
    src: Literal["representation"] | Unset = "representation"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        representation = self.representation.to_dict()

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        hidden: bool | None | Unset
        if isinstance(self.hidden, Unset):
            hidden = UNSET
        else:
            hidden = self.hidden

        src = self.src

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "representation": representation,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if src is not UNSET:
            field_dict["src"] = src

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_tool_source import UserToolSource

        d = dict(src_dict)
        representation = UserToolSource.from_dict(d.pop("representation"))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hidden = _parse_hidden(d.pop("hidden", UNSET))

        src = cast(Literal["representation"] | Unset, d.pop("src", UNSET))
        if src != "representation" and not isinstance(src, Unset):
            raise ValueError(f"src must match const 'representation', got '{src}'")

        dynamic_unprivileged_tool_create_payload = cls(
            representation=representation,
            active=active,
            hidden=hidden,
            src=src,
        )

        dynamic_unprivileged_tool_create_payload.additional_properties = d
        return dynamic_unprivileged_tool_create_payload

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
