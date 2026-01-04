from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentsObject")


@_attrs_define
class ContentsObject:
    """
    Attributes:
        name (str): A name declared by the bundle author that must be used when materialising this object, overriding
            any name directly associated with the object itself. The name must be unique within the containing bundle. This
            string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore
            [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable
            filenames].
        contents (list[ContentsObject] | None | Unset): If this ContentsObject describes a nested bundle and the caller
            specified "?expand=true" on the request, then this contents array must be present and describe the objects
            within the nested bundle.
        drs_uri (list[str] | None | Unset): A list of full DRS identifier URI paths that may be used to obtain the
            object. These URIs may be external to this DRS instance.
        id (None | str | Unset): A DRS identifier of a `DrsObject` (either a single blob or a nested bundle). If this
            ContentsObject is an object within a nested bundle, then the id is optional. Otherwise, the id is required.
    """

    name: str
    contents: list[ContentsObject] | None | Unset = UNSET
    drs_uri: list[str] | None | Unset = UNSET
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        contents: list[dict[str, Any]] | None | Unset
        if isinstance(self.contents, Unset):
            contents = UNSET
        elif isinstance(self.contents, list):
            contents = []
            for contents_type_0_item_data in self.contents:
                contents_type_0_item = contents_type_0_item_data.to_dict()
                contents.append(contents_type_0_item)

        else:
            contents = self.contents

        drs_uri: list[str] | None | Unset
        if isinstance(self.drs_uri, Unset):
            drs_uri = UNSET
        elif isinstance(self.drs_uri, list):
            drs_uri = self.drs_uri

        else:
            drs_uri = self.drs_uri

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if contents is not UNSET:
            field_dict["contents"] = contents
        if drs_uri is not UNSET:
            field_dict["drs_uri"] = drs_uri
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_contents(data: object) -> list[ContentsObject] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contents_type_0 = []
                _contents_type_0 = data
                for contents_type_0_item_data in _contents_type_0:
                    contents_type_0_item = ContentsObject.from_dict(contents_type_0_item_data)

                    contents_type_0.append(contents_type_0_item)

                return contents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContentsObject] | None | Unset, data)

        contents = _parse_contents(d.pop("contents", UNSET))

        def _parse_drs_uri(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                drs_uri_type_0 = cast(list[str], data)

                return drs_uri_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        drs_uri = _parse_drs_uri(d.pop("drs_uri", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        contents_object = cls(
            name=name,
            contents=contents,
            drs_uri=drs_uri,
            id=id,
        )

        contents_object.additional_properties = d
        return contents_object

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
