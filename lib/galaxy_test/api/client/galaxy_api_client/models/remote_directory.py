from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RemoteDirectory")


@_attrs_define
class RemoteDirectory:
    """
    Attributes:
        class_ (Literal['Directory']):
        name (str): The name of the entry.
        path (str): The path of the entry.
        uri (str): The URI of the entry.
    """

    class_: Literal["Directory"]
    name: str
    path: str
    uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_ = self.class_

        name = self.name

        path = self.path

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class": class_,
                "name": name,
                "path": path,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_ = cast(Literal["Directory"], d.pop("class"))
        if class_ != "Directory":
            raise ValueError(f"class must match const 'Directory', got '{class_}'")

        name = d.pop("name")

        path = d.pop("path")

        uri = d.pop("uri")

        remote_directory = cls(
            class_=class_,
            name=name,
            path=path,
            uri=uri,
        )

        remote_directory.additional_properties = d
        return remote_directory

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
