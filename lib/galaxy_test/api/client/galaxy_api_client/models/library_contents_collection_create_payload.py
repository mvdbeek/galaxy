from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_type import CreateType
from ..models.upload_option import UploadOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_contents_collection_create_payload_element_identifiers_item import (
        LibraryContentsCollectionCreatePayloadElementIdentifiersItem,
    )
    from ..models.library_contents_collection_create_payload_extended_metadata_type_0 import (
        LibraryContentsCollectionCreatePayloadExtendedMetadataType0,
    )


T = TypeVar("T", bound="LibraryContentsCollectionCreatePayload")


@_attrs_define
class LibraryContentsCollectionCreatePayload:
    """
    Attributes:
        collection_type (str):
        create_type (CreateType):
        element_identifiers (list[LibraryContentsCollectionCreatePayloadElementIdentifiersItem]):
        folder_id (str): the encoded id of the parent folder of the new item Example: 0123456789ABCDEF.
        copy_elements (bool | Unset): if True, copy the elements into the collection Default: False.
        extended_metadata (LibraryContentsCollectionCreatePayloadExtendedMetadataType0 | None | Unset): sub-dictionary
            containing any extended metadata to associate with the item
        from_hda_id (None | str | Unset): (only if create_type is 'file') the encoded id of an accessible HDA to copy
            into the library
        from_hdca_id (None | str | Unset): (only if create_type is 'file') the encoded id of an accessible HDCA to copy
            into the library
        hide_source_items (bool | Unset): if True, hide the source items in the collection Default: False.
        ldda_message (str | Unset): the new message attribute of the LDDA created Default: ''.
        name (None | str | Unset):
        tag_using_filenames (bool | Unset): create tags on datasets using the file's original name Default: False.
        tags (list[str] | Unset): create the given list of tags on datasets
        upload_option (UploadOption | Unset):
    """

    collection_type: str
    create_type: CreateType
    element_identifiers: list[LibraryContentsCollectionCreatePayloadElementIdentifiersItem]
    folder_id: str
    copy_elements: bool | Unset = False
    extended_metadata: LibraryContentsCollectionCreatePayloadExtendedMetadataType0 | None | Unset = UNSET
    from_hda_id: None | str | Unset = UNSET
    from_hdca_id: None | str | Unset = UNSET
    hide_source_items: bool | Unset = False
    ldda_message: str | Unset = ""
    name: None | str | Unset = UNSET
    tag_using_filenames: bool | Unset = False
    tags: list[str] | Unset = UNSET
    upload_option: UploadOption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.library_contents_collection_create_payload_extended_metadata_type_0 import (
            LibraryContentsCollectionCreatePayloadExtendedMetadataType0,
        )

        collection_type = self.collection_type

        create_type = self.create_type.value

        element_identifiers = []
        for element_identifiers_item_data in self.element_identifiers:
            element_identifiers_item = element_identifiers_item_data.to_dict()
            element_identifiers.append(element_identifiers_item)

        folder_id = self.folder_id

        copy_elements = self.copy_elements

        extended_metadata: dict[str, Any] | None | Unset
        if isinstance(self.extended_metadata, Unset):
            extended_metadata = UNSET
        elif isinstance(self.extended_metadata, LibraryContentsCollectionCreatePayloadExtendedMetadataType0):
            extended_metadata = self.extended_metadata.to_dict()
        else:
            extended_metadata = self.extended_metadata

        from_hda_id: None | str | Unset
        if isinstance(self.from_hda_id, Unset):
            from_hda_id = UNSET
        else:
            from_hda_id = self.from_hda_id

        from_hdca_id: None | str | Unset
        if isinstance(self.from_hdca_id, Unset):
            from_hdca_id = UNSET
        else:
            from_hdca_id = self.from_hdca_id

        hide_source_items = self.hide_source_items

        ldda_message = self.ldda_message

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        tag_using_filenames = self.tag_using_filenames

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        upload_option: str | Unset = UNSET
        if not isinstance(self.upload_option, Unset):
            upload_option = self.upload_option.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_type": collection_type,
                "create_type": create_type,
                "element_identifiers": element_identifiers,
                "folder_id": folder_id,
            }
        )
        if copy_elements is not UNSET:
            field_dict["copy_elements"] = copy_elements
        if extended_metadata is not UNSET:
            field_dict["extended_metadata"] = extended_metadata
        if from_hda_id is not UNSET:
            field_dict["from_hda_id"] = from_hda_id
        if from_hdca_id is not UNSET:
            field_dict["from_hdca_id"] = from_hdca_id
        if hide_source_items is not UNSET:
            field_dict["hide_source_items"] = hide_source_items
        if ldda_message is not UNSET:
            field_dict["ldda_message"] = ldda_message
        if name is not UNSET:
            field_dict["name"] = name
        if tag_using_filenames is not UNSET:
            field_dict["tag_using_filenames"] = tag_using_filenames
        if tags is not UNSET:
            field_dict["tags"] = tags
        if upload_option is not UNSET:
            field_dict["upload_option"] = upload_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_contents_collection_create_payload_element_identifiers_item import (
            LibraryContentsCollectionCreatePayloadElementIdentifiersItem,
        )
        from ..models.library_contents_collection_create_payload_extended_metadata_type_0 import (
            LibraryContentsCollectionCreatePayloadExtendedMetadataType0,
        )

        d = dict(src_dict)
        collection_type = d.pop("collection_type")

        create_type = CreateType(d.pop("create_type"))

        element_identifiers = []
        _element_identifiers = d.pop("element_identifiers")
        for element_identifiers_item_data in _element_identifiers:
            element_identifiers_item = LibraryContentsCollectionCreatePayloadElementIdentifiersItem.from_dict(
                element_identifiers_item_data
            )

            element_identifiers.append(element_identifiers_item)

        folder_id = d.pop("folder_id")

        copy_elements = d.pop("copy_elements", UNSET)

        def _parse_extended_metadata(
            data: object,
        ) -> LibraryContentsCollectionCreatePayloadExtendedMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extended_metadata_type_0 = LibraryContentsCollectionCreatePayloadExtendedMetadataType0.from_dict(data)

                return extended_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LibraryContentsCollectionCreatePayloadExtendedMetadataType0 | None | Unset, data)

        extended_metadata = _parse_extended_metadata(d.pop("extended_metadata", UNSET))

        def _parse_from_hda_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_hda_id = _parse_from_hda_id(d.pop("from_hda_id", UNSET))

        def _parse_from_hdca_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_hdca_id = _parse_from_hdca_id(d.pop("from_hdca_id", UNSET))

        hide_source_items = d.pop("hide_source_items", UNSET)

        ldda_message = d.pop("ldda_message", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        tag_using_filenames = d.pop("tag_using_filenames", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _upload_option = d.pop("upload_option", UNSET)
        upload_option: UploadOption | Unset
        if isinstance(_upload_option, Unset):
            upload_option = UNSET
        else:
            upload_option = UploadOption(_upload_option)

        library_contents_collection_create_payload = cls(
            collection_type=collection_type,
            create_type=create_type,
            element_identifiers=element_identifiers,
            folder_id=folder_id,
            copy_elements=copy_elements,
            extended_metadata=extended_metadata,
            from_hda_id=from_hda_id,
            from_hdca_id=from_hdca_id,
            hide_source_items=hide_source_items,
            ldda_message=ldda_message,
            name=name,
            tag_using_filenames=tag_using_filenames,
            tags=tags,
            upload_option=upload_option,
        )

        library_contents_collection_create_payload.additional_properties = d
        return library_contents_collection_create_payload

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
