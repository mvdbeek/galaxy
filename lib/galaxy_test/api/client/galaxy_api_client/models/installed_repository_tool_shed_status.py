from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstalledRepositoryToolShedStatus")


@_attrs_define
class InstalledRepositoryToolShedStatus:
    """
    Attributes:
        revision_update (str):
        latest_installable_revision (None | str | Unset): Most recent version available on the tool shed
        repository_deprecated (None | str | Unset): Repository has been depreciated on the tool shed
        revision_upgrade (None | str | Unset):
    """

    revision_update: str
    latest_installable_revision: None | str | Unset = UNSET
    repository_deprecated: None | str | Unset = UNSET
    revision_upgrade: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision_update = self.revision_update

        latest_installable_revision: None | str | Unset
        if isinstance(self.latest_installable_revision, Unset):
            latest_installable_revision = UNSET
        else:
            latest_installable_revision = self.latest_installable_revision

        repository_deprecated: None | str | Unset
        if isinstance(self.repository_deprecated, Unset):
            repository_deprecated = UNSET
        else:
            repository_deprecated = self.repository_deprecated

        revision_upgrade: None | str | Unset
        if isinstance(self.revision_upgrade, Unset):
            revision_upgrade = UNSET
        else:
            revision_upgrade = self.revision_upgrade

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revision_update": revision_update,
            }
        )
        if latest_installable_revision is not UNSET:
            field_dict["latest_installable_revision"] = latest_installable_revision
        if repository_deprecated is not UNSET:
            field_dict["repository_deprecated"] = repository_deprecated
        if revision_upgrade is not UNSET:
            field_dict["revision_upgrade"] = revision_upgrade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revision_update = d.pop("revision_update")

        def _parse_latest_installable_revision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_installable_revision = _parse_latest_installable_revision(d.pop("latest_installable_revision", UNSET))

        def _parse_repository_deprecated(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_deprecated = _parse_repository_deprecated(d.pop("repository_deprecated", UNSET))

        def _parse_revision_upgrade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revision_upgrade = _parse_revision_upgrade(d.pop("revision_upgrade", UNSET))

        installed_repository_tool_shed_status = cls(
            revision_update=revision_update,
            latest_installable_revision=latest_installable_revision,
            repository_deprecated=repository_deprecated,
            revision_upgrade=revision_upgrade,
        )

        installed_repository_tool_shed_status.additional_properties = d
        return installed_repository_tool_shed_status

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
