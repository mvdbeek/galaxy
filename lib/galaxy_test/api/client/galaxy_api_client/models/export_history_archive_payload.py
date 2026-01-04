from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportHistoryArchivePayload")


@_attrs_define
class ExportHistoryArchivePayload:
    """
    Attributes:
        directory_uri (None | str | Unset): A writable directory destination where the history will be exported using
            the `galaxy.files` URI infrastructure.
        file_name (None | str | Unset): The name of the file containing the exported history.
        force (bool | None | Unset): Whether to force a rebuild of the history archive.
        gzip (bool | None | Unset): Whether to export as gzip archive. Default: True.
        include_deleted (bool | None | Unset): Whether to include deleted datasets in the exported archive. Default:
            False.
        include_hidden (bool | None | Unset): Whether to include hidden datasets in the exported archive. Default:
            False.
    """

    directory_uri: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    force: bool | None | Unset = UNSET
    gzip: bool | None | Unset = True
    include_deleted: bool | None | Unset = False
    include_hidden: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory_uri: None | str | Unset
        if isinstance(self.directory_uri, Unset):
            directory_uri = UNSET
        else:
            directory_uri = self.directory_uri

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        force: bool | None | Unset
        if isinstance(self.force, Unset):
            force = UNSET
        else:
            force = self.force

        gzip: bool | None | Unset
        if isinstance(self.gzip, Unset):
            gzip = UNSET
        else:
            gzip = self.gzip

        include_deleted: bool | None | Unset
        if isinstance(self.include_deleted, Unset):
            include_deleted = UNSET
        else:
            include_deleted = self.include_deleted

        include_hidden: bool | None | Unset
        if isinstance(self.include_hidden, Unset):
            include_hidden = UNSET
        else:
            include_hidden = self.include_hidden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if directory_uri is not UNSET:
            field_dict["directory_uri"] = directory_uri
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if force is not UNSET:
            field_dict["force"] = force
        if gzip is not UNSET:
            field_dict["gzip"] = gzip
        if include_deleted is not UNSET:
            field_dict["include_deleted"] = include_deleted
        if include_hidden is not UNSET:
            field_dict["include_hidden"] = include_hidden

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_directory_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory_uri = _parse_directory_uri(d.pop("directory_uri", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_force(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force = _parse_force(d.pop("force", UNSET))

        def _parse_gzip(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        gzip = _parse_gzip(d.pop("gzip", UNSET))

        def _parse_include_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_deleted = _parse_include_deleted(d.pop("include_deleted", UNSET))

        def _parse_include_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_hidden = _parse_include_hidden(d.pop("include_hidden", UNSET))

        export_history_archive_payload = cls(
            directory_uri=directory_uri,
            file_name=file_name,
            force=force,
            gzip=gzip,
            include_deleted=include_deleted,
            include_hidden=include_hidden,
        )

        export_history_archive_payload.additional_properties = d
        return export_history_archive_payload

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
