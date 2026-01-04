from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_link_incoming_kwd_type_0 import CreateLinkIncomingKwdType0


T = TypeVar("T", bound="CreateLinkIncoming")


@_attrs_define
class CreateLinkIncoming:
    """
    Attributes:
        app_name (str):
        dataset_id (str):
        link_name (str):
        kwd (CreateLinkIncomingKwdType0 | None | Unset):
    """

    app_name: str
    dataset_id: str
    link_name: str
    kwd: CreateLinkIncomingKwdType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_link_incoming_kwd_type_0 import CreateLinkIncomingKwdType0

        app_name = self.app_name

        dataset_id = self.dataset_id

        link_name = self.link_name

        kwd: dict[str, Any] | None | Unset
        if isinstance(self.kwd, Unset):
            kwd = UNSET
        elif isinstance(self.kwd, CreateLinkIncomingKwdType0):
            kwd = self.kwd.to_dict()
        else:
            kwd = self.kwd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_name": app_name,
                "dataset_id": dataset_id,
                "link_name": link_name,
            }
        )
        if kwd is not UNSET:
            field_dict["kwd"] = kwd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_link_incoming_kwd_type_0 import CreateLinkIncomingKwdType0

        d = dict(src_dict)
        app_name = d.pop("app_name")

        dataset_id = d.pop("dataset_id")

        link_name = d.pop("link_name")

        def _parse_kwd(data: object) -> CreateLinkIncomingKwdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kwd_type_0 = CreateLinkIncomingKwdType0.from_dict(data)

                return kwd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateLinkIncomingKwdType0 | None | Unset, data)

        kwd = _parse_kwd(d.pop("kwd", UNSET))

        create_link_incoming = cls(
            app_name=app_name,
            dataset_id=dataset_id,
            link_name=link_name,
            kwd=kwd,
        )

        create_link_incoming.additional_properties = d
        return create_link_incoming

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
