from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.files_source_supports import FilesSourceSupports


T = TypeVar("T", bound="FilesSourcePlugin")


@_attrs_define
class FilesSourcePlugin:
    """
    Attributes:
        browsable (bool): Whether this file source plugin can list items.
        id (str): The `FilesSource` plugin identifier
        label (str): The display label for this plugin.
        type_ (str): The type of the plugin.
        writable (bool): Whether this files source plugin allows write access.
        doc (None | str | Unset): Documentation or extended description for this plugin.
        requires_groups (None | str | Unset): Only users belonging to the groups specified here can access this files
            source.
        requires_roles (None | str | Unset): Only users with the roles specified here can access this files source.
        supports (FilesSourceSupports | Unset):
        url (None | str | Unset): Optional URL that might be provided by some plugins to link to the remote source.
    """

    browsable: bool
    id: str
    label: str
    type_: str
    writable: bool
    doc: None | str | Unset = UNSET
    requires_groups: None | str | Unset = UNSET
    requires_roles: None | str | Unset = UNSET
    supports: FilesSourceSupports | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        browsable = self.browsable

        id = self.id

        label = self.label

        type_ = self.type_

        writable = self.writable

        doc: None | str | Unset
        if isinstance(self.doc, Unset):
            doc = UNSET
        else:
            doc = self.doc

        requires_groups: None | str | Unset
        if isinstance(self.requires_groups, Unset):
            requires_groups = UNSET
        else:
            requires_groups = self.requires_groups

        requires_roles: None | str | Unset
        if isinstance(self.requires_roles, Unset):
            requires_roles = UNSET
        else:
            requires_roles = self.requires_roles

        supports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supports, Unset):
            supports = self.supports.to_dict()

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "browsable": browsable,
                "id": id,
                "label": label,
                "type": type_,
                "writable": writable,
            }
        )
        if doc is not UNSET:
            field_dict["doc"] = doc
        if requires_groups is not UNSET:
            field_dict["requires_groups"] = requires_groups
        if requires_roles is not UNSET:
            field_dict["requires_roles"] = requires_roles
        if supports is not UNSET:
            field_dict["supports"] = supports
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.files_source_supports import FilesSourceSupports

        d = dict(src_dict)
        browsable = d.pop("browsable")

        id = d.pop("id")

        label = d.pop("label")

        type_ = d.pop("type")

        writable = d.pop("writable")

        def _parse_doc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        doc = _parse_doc(d.pop("doc", UNSET))

        def _parse_requires_groups(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requires_groups = _parse_requires_groups(d.pop("requires_groups", UNSET))

        def _parse_requires_roles(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requires_roles = _parse_requires_roles(d.pop("requires_roles", UNSET))

        _supports = d.pop("supports", UNSET)
        supports: FilesSourceSupports | Unset
        if isinstance(_supports, Unset):
            supports = UNSET
        else:
            supports = FilesSourceSupports.from_dict(_supports)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        files_source_plugin = cls(
            browsable=browsable,
            id=id,
            label=label,
            type_=type_,
            writable=writable,
            doc=doc,
            requires_groups=requires_groups,
            requires_roles=requires_roles,
            supports=supports,
            url=url,
        )

        files_source_plugin.additional_properties = d
        return files_source_plugin

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
