from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.elements_from_type import ElementsFromType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composite_data_element import CompositeDataElement
    from ..models.extra_files import ExtraFiles
    from ..models.fetch_dataset_hash import FetchDatasetHash
    from ..models.file_data_element import FileDataElement
    from ..models.ftp_import_element import FtpImportElement
    from ..models.pasted_data_element import PastedDataElement
    from ..models.path_data_element import PathDataElement
    from ..models.server_dir_element import ServerDirElement
    from ..models.url_data_element import UrlDataElement


T = TypeVar("T", bound="NestedElement")


@_attrs_define
class NestedElement:
    """
    Attributes:
        elements (list[CompositeDataElement | FileDataElement | FtpImportElement | NestedElement | PastedDataElement |
            PathDataElement | ServerDirElement | UrlDataElement]):
        md5 (None | str | Unset): The MD5 checksum of the dataset. This is a hash of the dataset contents that can be
            used to verify the
            integrity of the dataset. More information on MD5 checksums can be found on
            [Wikipedia](https://en.wikipedia.org/wiki/MD5).
        sha_1 (None | str | Unset): The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be
            used to verify the
            integrity of the dataset. More information on SHA1 checksums can be found on
            [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).
        sha_256 (None | str | Unset): The SHA-256 checksum of the dataset. This is a hash of the dataset contents that
            can be used to verify the
            integrity of the dataset. More information on SHA-256 checksums can be found on
            [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
        sha_512 (None | str | Unset): The SHA-512 checksum of the dataset. This is a hash of the dataset contents that
            can be used to verify the
            integrity of the dataset. More information on SHA-512 checksums can be found on
            [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
        auto_decompress (bool | Unset): This is a boolean value that indicates whether the dataset should be
            automatically decompressed if it is
            compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not
            explicitly set to a compressed datatype.
             Default: False.
        collection_type (None | str | Unset):
        created_from_basename (None | str | Unset):
        dbkey (str | Unset): This identifier is used to associate datasets with specific reference genomes. If set, the
            dbkey
            is a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"
            for mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".
            The Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to
            indicate that the dataset does not have a dbkey set.
             Default: '?'.
        deferred (bool | Unset): This is a boolean value that indicates whether the dataset is deferred. Deferred
            datasets are not
            immediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred
            datasets, most datasets should not be deferred unless you are sure you want to use this feature.
             Default: False.
        description (None | str | Unset):
        ext (str | Unset): The file extension of the dataset. This is shorthand description of the datatype
            corresponding to this dataset.
            The default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on
            the contents of the file.
             Default: 'auto'.
        extra_files (ExtraFiles | None | Unset):
        hashes (list[FetchDatasetHash] | None | Unset):
        info (None | str | Unset): Free text field that can be used to store arbitrary information about the dataset.
            This used to be prominently
            displayed in the Galaxy user interface, but now is largely unused.
        items_from (ElementsFromType | None | Unset):
        name (bool | float | int | None | str | Unset):
        row (list[bool | float | int | None | str] | None | Unset):
        space_to_tab (bool | Unset): This is a boolean value that indicates whether the spaces in the dataset contents
            should be converted to tabs.
            This should typically be set to false for most applications, but sometimes when pasting data into the Galaxy
            user interface, it is useful to set this to true to ensure that the data is converted to a tabular format
            correctly.
             Default: False.
        tags (list[str] | None | Unset): Tags are a way to categorize datasets in Galaxy. They are free-form text
            strings that can be used to
            group datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be
            used to search for datasets in the Galaxy API.
        to_posix_lines (bool | Unset): This is a boolean value that indicates whether the line endings in the dataset
            should be converted to POSIX
            line endings (LF). The Galaxy user interface will typically set this to true so that all datasets default
            to having POSIX line endings as most tools and workflows expect. The actual upload API will default this to
            false
            though assuming the API user is more likely to be want to be precise about file handling details.
             Default: False.
    """

    elements: list[
        CompositeDataElement
        | FileDataElement
        | FtpImportElement
        | NestedElement
        | PastedDataElement
        | PathDataElement
        | ServerDirElement
        | UrlDataElement
    ]
    md5: None | str | Unset = UNSET
    sha_1: None | str | Unset = UNSET
    sha_256: None | str | Unset = UNSET
    sha_512: None | str | Unset = UNSET
    auto_decompress: bool | Unset = False
    collection_type: None | str | Unset = UNSET
    created_from_basename: None | str | Unset = UNSET
    dbkey: str | Unset = "?"
    deferred: bool | Unset = False
    description: None | str | Unset = UNSET
    ext: str | Unset = "auto"
    extra_files: ExtraFiles | None | Unset = UNSET
    hashes: list[FetchDatasetHash] | None | Unset = UNSET
    info: None | str | Unset = UNSET
    items_from: ElementsFromType | None | Unset = UNSET
    name: bool | float | int | None | str | Unset = UNSET
    row: list[bool | float | int | None | str] | None | Unset = UNSET
    space_to_tab: bool | Unset = False
    tags: list[str] | None | Unset = UNSET
    to_posix_lines: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        from ..models.composite_data_element import CompositeDataElement
        from ..models.extra_files import ExtraFiles
        from ..models.file_data_element import FileDataElement
        from ..models.ftp_import_element import FtpImportElement
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        elements = []
        for elements_item_data in self.elements:
            elements_item: dict[str, Any]
            if isinstance(elements_item_data, FileDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, PastedDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, UrlDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, PathDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, ServerDirElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, FtpImportElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, CompositeDataElement):
                elements_item = elements_item_data.to_dict()
            else:
                elements_item = elements_item_data.to_dict()

            elements.append(elements_item)

        md5: None | str | Unset
        if isinstance(self.md5, Unset):
            md5 = UNSET
        else:
            md5 = self.md5

        sha_1: None | str | Unset
        if isinstance(self.sha_1, Unset):
            sha_1 = UNSET
        else:
            sha_1 = self.sha_1

        sha_256: None | str | Unset
        if isinstance(self.sha_256, Unset):
            sha_256 = UNSET
        else:
            sha_256 = self.sha_256

        sha_512: None | str | Unset
        if isinstance(self.sha_512, Unset):
            sha_512 = UNSET
        else:
            sha_512 = self.sha_512

        auto_decompress = self.auto_decompress

        collection_type: None | str | Unset
        if isinstance(self.collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = self.collection_type

        created_from_basename: None | str | Unset
        if isinstance(self.created_from_basename, Unset):
            created_from_basename = UNSET
        else:
            created_from_basename = self.created_from_basename

        dbkey = self.dbkey

        deferred = self.deferred

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ext = self.ext

        extra_files: dict[str, Any] | None | Unset
        if isinstance(self.extra_files, Unset):
            extra_files = UNSET
        elif isinstance(self.extra_files, ExtraFiles):
            extra_files = self.extra_files.to_dict()
        else:
            extra_files = self.extra_files

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

        items_from: None | str | Unset
        if isinstance(self.items_from, Unset):
            items_from = UNSET
        elif isinstance(self.items_from, ElementsFromType):
            items_from = self.items_from.value
        else:
            items_from = self.items_from

        name: bool | float | int | None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        row: list[bool | float | int | None | str] | None | Unset
        if isinstance(self.row, Unset):
            row = UNSET
        elif isinstance(self.row, list):
            row = []
            for row_type_0_item_data in self.row:
                row_type_0_item: bool | float | int | None | str
                row_type_0_item = row_type_0_item_data
                row.append(row_type_0_item)

        else:
            row = self.row

        space_to_tab = self.space_to_tab

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
                "elements": elements,
            }
        )
        if md5 is not UNSET:
            field_dict["MD5"] = md5
        if sha_1 is not UNSET:
            field_dict["SHA-1"] = sha_1
        if sha_256 is not UNSET:
            field_dict["SHA-256"] = sha_256
        if sha_512 is not UNSET:
            field_dict["SHA-512"] = sha_512
        if auto_decompress is not UNSET:
            field_dict["auto_decompress"] = auto_decompress
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if created_from_basename is not UNSET:
            field_dict["created_from_basename"] = created_from_basename
        if dbkey is not UNSET:
            field_dict["dbkey"] = dbkey
        if deferred is not UNSET:
            field_dict["deferred"] = deferred
        if description is not UNSET:
            field_dict["description"] = description
        if ext is not UNSET:
            field_dict["ext"] = ext
        if extra_files is not UNSET:
            field_dict["extra_files"] = extra_files
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if info is not UNSET:
            field_dict["info"] = info
        if items_from is not UNSET:
            field_dict["items_from"] = items_from
        if name is not UNSET:
            field_dict["name"] = name
        if row is not UNSET:
            field_dict["row"] = row
        if space_to_tab is not UNSET:
            field_dict["space_to_tab"] = space_to_tab
        if tags is not UNSET:
            field_dict["tags"] = tags
        if to_posix_lines is not UNSET:
            field_dict["to_posix_lines"] = to_posix_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.composite_data_element import CompositeDataElement
        from ..models.extra_files import ExtraFiles
        from ..models.fetch_dataset_hash import FetchDatasetHash
        from ..models.file_data_element import FileDataElement
        from ..models.ftp_import_element import FtpImportElement
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        d = dict(src_dict)
        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:

            def _parse_elements_item(
                data: object,
            ) -> (
                CompositeDataElement
                | FileDataElement
                | FtpImportElement
                | NestedElement
                | PastedDataElement
                | PathDataElement
                | ServerDirElement
                | UrlDataElement
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_0 = FileDataElement.from_dict(data)

                    return elements_item_type_0_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_1 = PastedDataElement.from_dict(data)

                    return elements_item_type_0_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_2 = UrlDataElement.from_dict(data)

                    return elements_item_type_0_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_3 = PathDataElement.from_dict(data)

                    return elements_item_type_0_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_4 = ServerDirElement.from_dict(data)

                    return elements_item_type_0_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_5 = FtpImportElement.from_dict(data)

                    return elements_item_type_0_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_6 = CompositeDataElement.from_dict(data)

                    return elements_item_type_0_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                elements_item_type_1 = NestedElement.from_dict(data)

                return elements_item_type_1

            elements_item = _parse_elements_item(elements_item_data)

            elements.append(elements_item)

        def _parse_md5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        md5 = _parse_md5(d.pop("MD5", UNSET))

        def _parse_sha_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sha_1 = _parse_sha_1(d.pop("SHA-1", UNSET))

        def _parse_sha_256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sha_256 = _parse_sha_256(d.pop("SHA-256", UNSET))

        def _parse_sha_512(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sha_512 = _parse_sha_512(d.pop("SHA-512", UNSET))

        auto_decompress = d.pop("auto_decompress", UNSET)

        def _parse_collection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type = _parse_collection_type(d.pop("collection_type", UNSET))

        def _parse_created_from_basename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_from_basename = _parse_created_from_basename(d.pop("created_from_basename", UNSET))

        dbkey = d.pop("dbkey", UNSET)

        deferred = d.pop("deferred", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        ext = d.pop("ext", UNSET)

        def _parse_extra_files(data: object) -> ExtraFiles | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_files_type_0 = ExtraFiles.from_dict(data)

                return extra_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExtraFiles | None | Unset, data)

        extra_files = _parse_extra_files(d.pop("extra_files", UNSET))

        def _parse_hashes(data: object) -> list[FetchDatasetHash] | None | Unset:
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
                    hashes_type_0_item = FetchDatasetHash.from_dict(hashes_type_0_item_data)

                    hashes_type_0.append(hashes_type_0_item)

                return hashes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FetchDatasetHash] | None | Unset, data)

        hashes = _parse_hashes(d.pop("hashes", UNSET))

        def _parse_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        info = _parse_info(d.pop("info", UNSET))

        def _parse_items_from(data: object) -> ElementsFromType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                items_from_type_0 = ElementsFromType(data)

                return items_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ElementsFromType | None | Unset, data)

        items_from = _parse_items_from(d.pop("items_from", UNSET))

        def _parse_name(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_row(data: object) -> list[bool | float | int | None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                row_type_0 = []
                _row_type_0 = data
                for row_type_0_item_data in _row_type_0:

                    def _parse_row_type_0_item(data: object) -> bool | float | int | None | str:
                        if data is None:
                            return data
                        return cast(bool | float | int | None | str, data)

                    row_type_0_item = _parse_row_type_0_item(row_type_0_item_data)

                    row_type_0.append(row_type_0_item)

                return row_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool | float | int | None | str] | None | Unset, data)

        row = _parse_row(d.pop("row", UNSET))

        space_to_tab = d.pop("space_to_tab", UNSET)

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

        nested_element = cls(
            elements=elements,
            md5=md5,
            sha_1=sha_1,
            sha_256=sha_256,
            sha_512=sha_512,
            auto_decompress=auto_decompress,
            collection_type=collection_type,
            created_from_basename=created_from_basename,
            dbkey=dbkey,
            deferred=deferred,
            description=description,
            ext=ext,
            extra_files=extra_files,
            hashes=hashes,
            info=info,
            items_from=items_from,
            name=name,
            row=row,
            space_to_tab=space_to_tab,
            tags=tags,
            to_posix_lines=to_posix_lines,
        )

        return nested_element
