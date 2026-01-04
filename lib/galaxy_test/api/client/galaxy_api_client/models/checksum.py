from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Checksum")


@_attrs_define
class Checksum:
    """
    Attributes:
        checksum (str): The hex-string encoded checksum for the data
        type_ (str): The digest method used to create the checksum.
            The value (e.g. `sha-256`) SHOULD be listed as `Hash Name String` in the https://www.iana.org/assignments/named-
            information/named-information.xhtml#hash-alg[IANA Named Information Hash Algorithm Registry]. Other values MAY
            be used, as long as implementors are aware of the issues discussed in
            https://tools.ietf.org/html/rfc6920#section-9.4[RFC6920].
            GA4GH may provide more explicit guidance for use of non-IANA-registered algorithms in the future. Until then, if
            implementers do choose such an algorithm (e.g. because it's implemented by their storage provider), they SHOULD
            use an existing standard `type` value such as `md5`, `etag`, `crc32c`, `trunc512`, or `sha1`.
    """

    checksum: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum = self.checksum

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checksum": checksum,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checksum = d.pop("checksum")

        type_ = d.pop("type")

        checksum = cls(
            checksum=checksum,
            type_=type_,
        )

        checksum.additional_properties = d
        return checksum

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
