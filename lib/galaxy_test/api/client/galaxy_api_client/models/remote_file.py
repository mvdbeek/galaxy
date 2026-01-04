from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remote_file_hash import RemoteFileHash


T = TypeVar("T", bound="RemoteFile")


@_attrs_define
class RemoteFile:
    """
    Attributes:
        class_ (Literal['File']):
        ctime (str): The creation time of the file.
        name (str): The name of the entry.
        path (str): The path of the entry.
        size (int): The size of the file in bytes.
        uri (str): The URI of the entry.
        hashes (list[RemoteFileHash] | None | Unset): List of precomputed hashes for the file, if available.
    """

    class_: Literal["File"]
    ctime: str
    name: str
    path: str
    size: int
    uri: str
    hashes: list[RemoteFileHash] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_ = self.class_

        ctime = self.ctime

        name = self.name

        path = self.path

        size = self.size

        uri = self.uri

        hashes: list[dict[str, Any]] | None | Unset
        if isinstance(self.hashes, Unset):
            hashes = UNSET
        elif isinstance(self.hashes, list):
            hashes = []
            for hashes_type_0_item_data in self.hashes:
                hashes_type_0_item = hashes_type_0_item_data.to_dict()
                hashes.append(hashes_type_0_item)

        else:
            hashes = self.hashes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class": class_,
                "ctime": ctime,
                "name": name,
                "path": path,
                "size": size,
                "uri": uri,
            }
        )
        if hashes is not UNSET:
            field_dict["hashes"] = hashes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remote_file_hash import RemoteFileHash

        d = dict(src_dict)
        class_ = cast(Literal["File"], d.pop("class"))
        if class_ != "File":
            raise ValueError(f"class must match const 'File', got '{class_}'")

        ctime = d.pop("ctime")

        name = d.pop("name")

        path = d.pop("path")

        size = d.pop("size")

        uri = d.pop("uri")

        def _parse_hashes(data: object) -> list[RemoteFileHash] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hashes_type_0 = []
                _hashes_type_0 = data
                for hashes_type_0_item_data in _hashes_type_0:
                    hashes_type_0_item = RemoteFileHash.from_dict(hashes_type_0_item_data)

                    hashes_type_0.append(hashes_type_0_item)

                return hashes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RemoteFileHash] | None | Unset, data)

        hashes = _parse_hashes(d.pop("hashes", UNSET))

        remote_file = cls(
            class_=class_,
            ctime=ctime,
            name=name,
            path=path,
            size=size,
            uri=uri,
            hashes=hashes,
        )

        remote_file.additional_properties = d
        return remote_file

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
