from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImportToolDataBundleUriSource")


@_attrs_define
class ImportToolDataBundleUriSource:
    """
    Attributes:
        src (Literal['uri']): Indicates that the tool data should be resolved by a URI.
        uri (str): URI to fetch tool data bundle from (file:// URIs are fine because this is an admin-only operation)
    """

    src: Literal["uri"]
    uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src": src,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = cast(Literal["uri"], d.pop("src"))
        if src != "uri":
            raise ValueError(f"src must match const 'uri', got '{src}'")

        uri = d.pop("uri")

        import_tool_data_bundle_uri_source = cls(
            src=src,
            uri=uri,
        )

        import_tool_data_bundle_uri_source.additional_properties = d
        return import_tool_data_bundle_uri_source

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
