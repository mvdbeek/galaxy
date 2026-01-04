from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_library_folder_item import FileLibraryFolderItem
    from ..models.folder_library_folder_item import FolderLibraryFolderItem
    from ..models.library_folder_metadata import LibraryFolderMetadata


T = TypeVar("T", bound="LibraryFolderContentsIndexResult")


@_attrs_define
class LibraryFolderContentsIndexResult:
    """
    Attributes:
        folder_contents (list[FileLibraryFolderItem | FolderLibraryFolderItem]):
        metadata (LibraryFolderMetadata):
    """

    folder_contents: list[FileLibraryFolderItem | FolderLibraryFolderItem]
    metadata: LibraryFolderMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_library_folder_item import FileLibraryFolderItem

        folder_contents = []
        for folder_contents_item_data in self.folder_contents:
            folder_contents_item: dict[str, Any]
            if isinstance(folder_contents_item_data, FileLibraryFolderItem):
                folder_contents_item = folder_contents_item_data.to_dict()
            else:
                folder_contents_item = folder_contents_item_data.to_dict()

            folder_contents.append(folder_contents_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folder_contents": folder_contents,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_library_folder_item import FileLibraryFolderItem
        from ..models.folder_library_folder_item import FolderLibraryFolderItem
        from ..models.library_folder_metadata import LibraryFolderMetadata

        d = dict(src_dict)
        folder_contents = []
        _folder_contents = d.pop("folder_contents")
        for folder_contents_item_data in _folder_contents:

            def _parse_folder_contents_item(data: object) -> FileLibraryFolderItem | FolderLibraryFolderItem:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    folder_contents_item_type_0 = FileLibraryFolderItem.from_dict(data)

                    return folder_contents_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                folder_contents_item_type_1 = FolderLibraryFolderItem.from_dict(data)

                return folder_contents_item_type_1

            folder_contents_item = _parse_folder_contents_item(folder_contents_item_data)

            folder_contents.append(folder_contents_item)

        metadata = LibraryFolderMetadata.from_dict(d.pop("metadata"))

        library_folder_contents_index_result = cls(
            folder_contents=folder_contents,
            metadata=metadata,
        )

        library_folder_contents_index_result.additional_properties = d
        return library_folder_contents_index_result

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
