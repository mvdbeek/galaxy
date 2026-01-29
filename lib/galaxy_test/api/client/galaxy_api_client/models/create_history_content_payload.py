from dataclasses import dataclass

from .create_history_content_payload_collection_type import CreateHistoryContentPayloadCollectionType
from .create_history_content_payload_column_definitions import CreateHistoryContentPayloadColumnDefinitions
from .create_history_content_payload_content import CreateHistoryContentPayloadContent
from .create_history_content_payload_copy_elements import CreateHistoryContentPayloadCopyElements
from .create_history_content_payload_dbkey import CreateHistoryContentPayloadDbkey
from .create_history_content_payload_element_identifiers import CreateHistoryContentPayloadElementIdentifiers
from .create_history_content_payload_fields import CreateHistoryContentPayloadFields
from .create_history_content_payload_folder_id import CreateHistoryContentPayloadFolderId
from .create_history_content_payload_hide_source_items import CreateHistoryContentPayloadHideSourceItems
from .create_history_content_payload_history_id import CreateHistoryContentPayloadHistoryId
from .create_history_content_payload_instance_type import CreateHistoryContentPayloadInstanceType
from .create_history_content_payload_name import CreateHistoryContentPayloadName
from .create_history_content_payload_rows import CreateHistoryContentPayloadRows
from .create_history_content_payload_source import CreateHistoryContentPayloadSource
from .type__5 import Type5

__all__ = ["CreateHistoryContentPayload"]


@dataclass
class CreateHistoryContentPayload:
    """
    CreateHistoryContentPayload dataclass

    Args:
        collection_type (CreateHistoryContentPayloadCollectionType | None)
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (CreateHistoryContentPayloadColumnDefinitions | None)
                                 : Specify definitions for row data if collection_type is
                                   sample_sheet
        content (CreateHistoryContentPayloadContent | None)
                                 : Depending on the `source` it can be: - The encoded id
                                   from the library dataset - The encoded id from the
                                   library folder - The encoded id from the HDA - The
                                   encoded id from the HDCA
        copy_elements (CreateHistoryContentPayloadCopyElements | None)
                                 : If the source is a collection, whether to copy child HDAs
                                   into the target history as well. Prior to the galaxy
                                   release 23.1 this defaulted to false.
        dbkey (CreateHistoryContentPayloadDbkey | None)
                                 : TODO
        element_identifiers (CreateHistoryContentPayloadElementIdentifiers | None)
                                 : List of elements that should be in the new collection.
        fields (CreateHistoryContentPayloadFields | None)
                                 : List of fields to create for this collection. Set to
                                   'auto' to guess fields from identifiers.
        folder_id (CreateHistoryContentPayloadFolderId | None)
                                 : The ID of the library folder that will contain the
                                   collection. Required if `instance_type=library`.
        hide_source_items (CreateHistoryContentPayloadHideSourceItems | None)
                                 : Whether to mark the original HDAs as hidden.
        history_id (CreateHistoryContentPayloadHistoryId | None)
                                 : The ID of the history that will contain the collection.
                                   Required if `instance_type=history`.
        instance_type (CreateHistoryContentPayloadInstanceType | None)
                                 : The type of the instance, either `history` (default) or
                                   `library`.
        name (CreateHistoryContentPayloadName | None)
                                 : The name of the new collection.
        rows (CreateHistoryContentPayloadRows | None)
                                 : Specify rows of metadata data corresponding to an
                                   identifier if collection_type is sample_sheet
        source (CreateHistoryContentPayloadSource | None)
                                 : The source of the content. Can be other history element
                                   to be copied or library elements.
        type_ (Type5 | None)     : The type of content to be created in the history. (maps
                                   from 'type')
    """

    collection_type: CreateHistoryContentPayloadCollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    column_definitions: CreateHistoryContentPayloadColumnDefinitions | None = (
        None  # Specify definitions for row data if collection_type is sample_sheet
    )
    content: CreateHistoryContentPayloadContent | None = (
        None  # Depending on the `source` it can be: - The encoded id from the library dataset - The encoded id from the library folder - The encoded id from the HDA - The encoded id from the HDCA
    )
    copy_elements: CreateHistoryContentPayloadCopyElements | None = (
        True  # If the source is a collection, whether to copy child HDAs into the target history as well. Prior to the galaxy release 23.1 this defaulted to false.
    )
    dbkey: CreateHistoryContentPayloadDbkey | None = None  # TODO
    element_identifiers: CreateHistoryContentPayloadElementIdentifiers | None = (
        None  # List of elements that should be in the new collection.
    )
    fields: CreateHistoryContentPayloadFields | None = (
        None  # List of fields to create for this collection. Set to 'auto' to guess fields from identifiers.
    )
    folder_id: CreateHistoryContentPayloadFolderId | None = (
        None  # The ID of the library folder that will contain the collection. Required if `instance_type=library`.
    )
    hide_source_items: CreateHistoryContentPayloadHideSourceItems | None = (
        False  # Whether to mark the original HDAs as hidden.
    )
    history_id: CreateHistoryContentPayloadHistoryId | None = (
        None  # The ID of the history that will contain the collection. Required if `instance_type=history`.
    )
    instance_type: CreateHistoryContentPayloadInstanceType | None = (
        "history"  # The type of the instance, either `history` (default) or `library`.
    )
    name: CreateHistoryContentPayloadName | None = None  # The name of the new collection.
    rows: CreateHistoryContentPayloadRows | None = (
        None  # Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet
    )
    source: CreateHistoryContentPayloadSource | None = (
        None  # The source of the content. Can be other history element to be copied or library elements.
    )
    type_: Type5 | None = "dataset"  # The type of content to be created in the history. (maps from 'type')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "content": "content",
            "copy_elements": "copy_elements",
            "dbkey": "dbkey",
            "element_identifiers": "element_identifiers",
            "fields": "fields",
            "folder_id": "folder_id",
            "hide_source_items": "hide_source_items",
            "history_id": "history_id",
            "instance_type": "instance_type",
            "name": "name",
            "rows": "rows",
            "source": "source",
            "type": "type_",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "content": "content",
            "copy_elements": "copy_elements",
            "dbkey": "dbkey",
            "element_identifiers": "element_identifiers",
            "fields": "fields",
            "folder_id": "folder_id",
            "hide_source_items": "hide_source_items",
            "history_id": "history_id",
            "instance_type": "instance_type",
            "name": "name",
            "rows": "rows",
            "source": "source",
            "type_": "type",
        }
