from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_hash import FileHash


T = TypeVar("T", bound="FileRequestUri")


@_attrs_define
class FileRequestUri:
    """
    Attributes:
        class_ (Literal['File']):
        ext (str):
        location (str):
        created_from_basename (None | str | Unset):
        dbkey (str | Unset):  Default: '?'.
        deferred (bool | Unset):  Default: False.
        hashes (list[FileHash] | None | Unset):
        info (None | str | Unset):
        name (None | str | Unset):
        space_to_tab (bool | Unset):  Default: False.
        src (None | Unset):
        tags (list[str] | None | Unset):
        to_posix_lines (bool | Unset):  Default: False.
    """

    class_: Literal["File"]
    ext: str
    location: str
    created_from_basename: None | str | Unset = UNSET
    dbkey: str | Unset = "?"
    deferred: bool | Unset = False
    hashes: list[FileHash] | None | Unset = UNSET
    info: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    space_to_tab: bool | Unset = False
    src: None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    to_posix_lines: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        class_ = self.class_

        ext = self.ext

        location = self.location

        created_from_basename: None | str | Unset
        if isinstance(self.created_from_basename, Unset):
            created_from_basename = UNSET
        else:
            created_from_basename = self.created_from_basename

        dbkey = self.dbkey

        deferred = self.deferred

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

        info: None | str | Unset
        if isinstance(self.info, Unset):
            info = UNSET
        else:
            info = self.info

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        space_to_tab = self.space_to_tab

        src = self.src

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        to_posix_lines = self.to_posix_lines

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "class": class_,
                "ext": ext,
                "location": location,
            }
        )
        if created_from_basename is not UNSET:
            field_dict["created_from_basename"] = created_from_basename
        if dbkey is not UNSET:
            field_dict["dbkey"] = dbkey
        if deferred is not UNSET:
            field_dict["deferred"] = deferred
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if info is not UNSET:
            field_dict["info"] = info
        if name is not UNSET:
            field_dict["name"] = name
        if space_to_tab is not UNSET:
            field_dict["space_to_tab"] = space_to_tab
        if src is not UNSET:
            field_dict["src"] = src
        if tags is not UNSET:
            field_dict["tags"] = tags
        if to_posix_lines is not UNSET:
            field_dict["to_posix_lines"] = to_posix_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_hash import FileHash

        d = dict(src_dict)
        class_ = cast(Literal["File"], d.pop("class"))
        if class_ != "File":
            raise ValueError(f"class must match const 'File', got '{class_}'")

        ext = d.pop("ext")

        location = d.pop("location")

        def _parse_created_from_basename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_from_basename = _parse_created_from_basename(d.pop("created_from_basename", UNSET))

        dbkey = d.pop("dbkey", UNSET)

        deferred = d.pop("deferred", UNSET)

        def _parse_hashes(data: object) -> list[FileHash] | None | Unset:
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
                    hashes_type_0_item = FileHash.from_dict(hashes_type_0_item_data)

                    hashes_type_0.append(hashes_type_0_item)

                return hashes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileHash] | None | Unset, data)

        hashes = _parse_hashes(d.pop("hashes", UNSET))

        def _parse_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        info = _parse_info(d.pop("info", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        space_to_tab = d.pop("space_to_tab", UNSET)

        src = d.pop("src", UNSET)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        to_posix_lines = d.pop("to_posix_lines", UNSET)

        file_request_uri = cls(
            class_=class_,
            ext=ext,
            location=location,
            created_from_basename=created_from_basename,
            dbkey=dbkey,
            deferred=deferred,
            hashes=hashes,
            info=info,
            name=name,
            space_to_tab=space_to_tab,
            src=src,
            tags=tags,
            to_posix_lines=to_posix_lines,
        )

        return file_request_uri
