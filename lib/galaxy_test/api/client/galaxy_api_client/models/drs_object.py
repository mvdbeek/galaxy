from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_method import AccessMethod
    from ..models.checksum import Checksum
    from ..models.contents_object import ContentsObject


T = TypeVar("T", bound="DrsObject")


@_attrs_define
class DrsObject:
    """
    Attributes:
        checksums (list[Checksum]): The checksum of the `DrsObject`. At least one checksum must be provided.
            For blobs, the checksum is computed over the bytes in the blob.
            For bundles, the checksum is computed over a sorted concatenation of the checksums of its top-level contained
            objects (not recursive, names not included). The list of checksums is sorted alphabetically (hex-code) before
            concatenation and a further checksum is performed on the concatenated checksum value.
            For example, if a bundle contains blobs with the following checksums:
            md5(blob1) = 72794b6d
            md5(blob2) = 5e089d29
            Then the checksum of the bundle is:
            md5( concat( sort( md5(blob1), md5(blob2) ) ) )
            = md5( concat( sort( 72794b6d, 5e089d29 ) ) )
            = md5( concat( 5e089d29, 72794b6d ) )
            = md5( 5e089d2972794b6d )
            = f7a29a04
        created_time (datetime.datetime): Timestamp of content creation in RFC3339.
            (This is the creation time of the underlying content, not of the JSON object.)
        id (str): An identifier unique to this `DrsObject`
        self_uri (str): A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to
            access this object.
            The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and
            pass around.  For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the
            `self_uri` presents you with a hostname and properly encoded DRS ID for use in subsequent `access` endpoint
            calls.
        size (int): For blobs, the blob size in bytes.
            For bundles, the cumulative size, in bytes, of items in the `contents` field.
        access_methods (list[AccessMethod] | None | Unset): The list of access methods that can be used to fetch the
            `DrsObject`.
            Required for single blobs; optional for bundles.
        aliases (list[str] | None | Unset): A list of strings that can be used to find other metadata about this
            `DrsObject` from external metadata sources. These aliases can be used to represent secondary accession numbers
            or external GUIDs.
        contents (list[ContentsObject] | None | Unset): If not set, this `DrsObject` is a single blob.
            If set, this `DrsObject` is a bundle containing the listed `ContentsObject` s (some of which may be further
            nested).
        description (None | str | Unset): A human readable description of the `DrsObject`.
        mime_type (None | str | Unset): A string providing the mime-type of the `DrsObject`.
        name (None | str | Unset): A string that can be used to name a `DrsObject`.
            This string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore
            [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable
            filenames].
        updated_time (datetime.datetime | None | Unset): Timestamp of content update in RFC3339, identical to
            `created_time` in systems that do not support updates. (This is the update time of the underlying content, not
            of the JSON object.)
        version (None | str | Unset): A string representing a version.
            (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.)
    """

    checksums: list[Checksum]
    created_time: datetime.datetime
    id: str
    self_uri: str
    size: int
    access_methods: list[AccessMethod] | None | Unset = UNSET
    aliases: list[str] | None | Unset = UNSET
    contents: list[ContentsObject] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    updated_time: datetime.datetime | None | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksums = []
        for checksums_item_data in self.checksums:
            checksums_item = checksums_item_data.to_dict()
            checksums.append(checksums_item)

        created_time = self.created_time.isoformat()

        id = self.id

        self_uri = self.self_uri

        size = self.size

        access_methods: list[dict[str, Any]] | None | Unset
        if isinstance(self.access_methods, Unset):
            access_methods = UNSET
        elif isinstance(self.access_methods, list):
            access_methods = []
            for access_methods_type_0_item_data in self.access_methods:
                access_methods_type_0_item = access_methods_type_0_item_data.to_dict()
                access_methods.append(access_methods_type_0_item)

        else:
            access_methods = self.access_methods

        aliases: list[str] | None | Unset
        if isinstance(self.aliases, Unset):
            aliases = UNSET
        elif isinstance(self.aliases, list):
            aliases = self.aliases

        else:
            aliases = self.aliases

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        updated_time: None | str | Unset
        if isinstance(self.updated_time, Unset):
            updated_time = UNSET
        elif isinstance(self.updated_time, datetime.datetime):
            updated_time = self.updated_time.isoformat()
        else:
            updated_time = self.updated_time

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checksums": checksums,
                "created_time": created_time,
                "id": id,
                "self_uri": self_uri,
                "size": size,
            }
        )
        if access_methods is not UNSET:
            field_dict["access_methods"] = access_methods
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if contents is not UNSET:
            field_dict["contents"] = contents
        if description is not UNSET:
            field_dict["description"] = description
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if updated_time is not UNSET:
            field_dict["updated_time"] = updated_time
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_method import AccessMethod
        from ..models.checksum import Checksum
        from ..models.contents_object import ContentsObject

        d = dict(src_dict)
        checksums = []
        _checksums = d.pop("checksums")
        for checksums_item_data in _checksums:
            checksums_item = Checksum.from_dict(checksums_item_data)

            checksums.append(checksums_item)

        created_time = isoparse(d.pop("created_time"))

        id = d.pop("id")

        self_uri = d.pop("self_uri")

        size = d.pop("size")

        def _parse_access_methods(data: object) -> list[AccessMethod] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_methods_type_0 = []
                _access_methods_type_0 = data
                for access_methods_type_0_item_data in _access_methods_type_0:
                    access_methods_type_0_item = AccessMethod.from_dict(access_methods_type_0_item_data)

                    access_methods_type_0.append(access_methods_type_0_item)

                return access_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccessMethod] | None | Unset, data)

        access_methods = _parse_access_methods(d.pop("access_methods", UNSET))

        def _parse_aliases(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aliases_type_0 = cast(list[str], data)

                return aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        aliases = _parse_aliases(d.pop("aliases", UNSET))

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mime_type", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_updated_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_time_type_0 = isoparse(data)

                return updated_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_time = _parse_updated_time(d.pop("updated_time", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        drs_object = cls(
            checksums=checksums,
            created_time=created_time,
            id=id,
            self_uri=self_uri,
            size=size,
            access_methods=access_methods,
            aliases=aliases,
            contents=contents,
            description=description,
            mime_type=mime_type,
            name=name,
            updated_time=updated_time,
            version=version,
        )

        drs_object.additional_properties = d
        return drs_object

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
