from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyToolsFetchFetchForm")


@_attrs_define
class BodyToolsFetchFetchForm:
    """
    Attributes:
        history_id (Any):
        targets (Any):
        files (list[File] | None | Unset):
        landing_uuid (Any | Unset):
    """

    history_id: Any
    targets: Any
    files: list[File] | None | Unset = UNSET
    landing_uuid: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history_id = self.history_id

        targets = self.targets

        files: list[FileTypes] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_tuple()

                files.append(files_type_0_item)

        else:
            files = self.files

        landing_uuid = self.landing_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_id": history_id,
                "targets": targets,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files
        if landing_uuid is not UNSET:
            field_dict["landing_uuid"] = landing_uuid

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("history_id", (None, str(self.history_id).encode(), "text/plain")))

        files.append(("targets", (None, str(self.targets).encode(), "text/plain")))

        if not isinstance(self.files, Unset):
            if isinstance(self.files, list):
                for files_type_0_item_element in self.files:
                    files.append(("files", files_type_0_item_element.to_tuple()))
            else:
                files.append(("files", (None, str(self.files).encode(), "text/plain")))

        if not isinstance(self.landing_uuid, Unset):
            files.append(("landing_uuid", (None, str(self.landing_uuid).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        history_id = d.pop("history_id")

        targets = d.pop("targets")

        def _parse_files(data: object) -> list[File] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in _files_type_0:
                    files_type_0_item = File(payload=BytesIO(files_type_0_item_data))

                    files_type_0.append(files_type_0_item)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[File] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        landing_uuid = d.pop("landing_uuid", UNSET)

        body_tools_fetch_fetch_form = cls(
            history_id=history_id,
            targets=targets,
            files=files,
            landing_uuid=landing_uuid,
        )

        body_tools_fetch_fetch_form.additional_properties = d
        return body_tools_fetch_fetch_form

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
