from dataclasses import dataclass

from .create_new_collection_payload_collection_type import CreateNewCollectionPayloadCollectionType
from .create_new_collection_payload_column_definitions import CreateNewCollectionPayloadColumnDefinitions
from .create_new_collection_payload_copy_elements import CreateNewCollectionPayloadCopyElements
from .create_new_collection_payload_element_identifiers import CreateNewCollectionPayloadElementIdentifiers
from .create_new_collection_payload_fields import CreateNewCollectionPayloadFields
from .create_new_collection_payload_folder_id import CreateNewCollectionPayloadFolderId
from .create_new_collection_payload_hide_source_items import CreateNewCollectionPayloadHideSourceItems
from .create_new_collection_payload_history_id import CreateNewCollectionPayloadHistoryId
from .create_new_collection_payload_instance_type import CreateNewCollectionPayloadInstanceType
from .create_new_collection_payload_name import CreateNewCollectionPayloadName
from .create_new_collection_payload_rows import CreateNewCollectionPayloadRows

__all__ = ["CreateNewCollectionPayload"]


@dataclass
class CreateNewCollectionPayload:
    """
    CreateNewCollectionPayload dataclass

    Args:
        collection_type (CreateNewCollectionPayloadCollectionType | None)
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (CreateNewCollectionPayloadColumnDefinitions | None)
                                 : Specify definitions for row data if collection_type is
                                   sample_sheet
        copy_elements (CreateNewCollectionPayloadCopyElements | None)
                                 : Whether to create a copy of the source HDAs for the new
                                   collection.
        element_identifiers (CreateNewCollectionPayloadElementIdentifiers | None)
                                 : List of elements that should be in the new collection.
        fields (CreateNewCollectionPayloadFields | None)
                                 : List of fields to create for this collection. Set to
                                   'auto' to guess fields from identifiers.
        folder_id (CreateNewCollectionPayloadFolderId | None)
                                 : The ID of the library folder that will contain the
                                   collection. Required if `instance_type=library`.
        hide_source_items (CreateNewCollectionPayloadHideSourceItems | None)
                                 : Whether to mark the original HDAs as hidden.
        history_id (CreateNewCollectionPayloadHistoryId | None)
                                 : The ID of the history that will contain the collection.
                                   Required if `instance_type=history`.
        instance_type (CreateNewCollectionPayloadInstanceType | None)
                                 : The type of the instance, either `history` (default) or
                                   `library`.
        name (CreateNewCollectionPayloadName | None)
                                 : The name of the new collection.
        rows (CreateNewCollectionPayloadRows | None)
                                 : Specify rows of metadata data corresponding to an
                                   identifier if collection_type is sample_sheet
    """

    collection_type: CreateNewCollectionPayloadCollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    column_definitions: CreateNewCollectionPayloadColumnDefinitions | None = (
        None  # Specify definitions for row data if collection_type is sample_sheet
    )
    copy_elements: CreateNewCollectionPayloadCopyElements | None = (
        True  # Whether to create a copy of the source HDAs for the new collection.
    )
    element_identifiers: CreateNewCollectionPayloadElementIdentifiers | None = (
        None  # List of elements that should be in the new collection.
    )
    fields: CreateNewCollectionPayloadFields | None = (
        None  # List of fields to create for this collection. Set to 'auto' to guess fields from identifiers.
    )
    folder_id: CreateNewCollectionPayloadFolderId | None = (
        None  # The ID of the library folder that will contain the collection. Required if `instance_type=library`.
    )
    hide_source_items: CreateNewCollectionPayloadHideSourceItems | None = (
        False  # Whether to mark the original HDAs as hidden.
    )
    history_id: CreateNewCollectionPayloadHistoryId | None = (
        None  # The ID of the history that will contain the collection. Required if `instance_type=history`.
    )
    instance_type: CreateNewCollectionPayloadInstanceType | None = (
        "history"  # The type of the instance, either `history` (default) or `library`.
    )
    name: CreateNewCollectionPayloadName | None = None  # The name of the new collection.
    rows: CreateNewCollectionPayloadRows | None = (
        None  # Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "copy_elements": "copy_elements",
            "element_identifiers": "element_identifiers",
            "fields": "fields",
            "folder_id": "folder_id",
            "hide_source_items": "hide_source_items",
            "history_id": "history_id",
            "instance_type": "instance_type",
            "name": "name",
            "rows": "rows",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "copy_elements": "copy_elements",
            "element_identifiers": "element_identifiers",
            "fields": "fields",
            "folder_id": "folder_id",
            "hide_source_items": "hide_source_items",
            "history_id": "history_id",
            "instance_type": "instance_type",
            "name": "name",
            "rows": "rows",
        }
