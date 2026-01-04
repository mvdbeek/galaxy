from dataclasses import dataclass

from .collection_type import CollectionType
from .column_definitions import ColumnDefinitions
from .content import Content
from .copy_elements import CopyElements
from .dbkey import Dbkey
from .element_identifiers import ElementIdentifiers
from .fields import Fields
from .folder_id import FolderId
from .hide_source_items import HideSourceItems
from .history_id import HistoryId
from .instance_type import InstanceType
from .name import Name
from .rows import Rows
from .source import Source
from .type_ import Type_

__all__ = ["CreateHistoryContentPayload"]


@dataclass
class CreateHistoryContentPayload:
    """
    CreateHistoryContentPayload dataclass.

    Args:
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (Optional[ColumnDefinitions])
                                 : Column data associated with each element of this
                                   collection.
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        copy_elements (Optional[CopyElements])
                                 : Whether to create a copy of the source HDAs for the new
                                   collection.
        dbkey (Optional[Dbkey])  : The database key of the visualization.
        element_identifiers (Optional[ElementIdentifiers])
                                 : List of elements that should be in the new collection.
        fields (Optional[Fields]):
        folder_id (Optional[FolderId])
                                 : The ID of the library folder that will contain the
                                   collection. Required if `instance_type=library`.
        hide_source_items (Optional[HideSourceItems])
                                 : Whether to mark the original HDAs as hidden.
        history_id (Optional[HistoryId])
                                 : The encoded ID of the history associated with this item.
        instance_type (Optional[InstanceType])
                                 : The type of the instance, either `history` (default) or
                                   `library`.
        name (Optional[Name])    : The name of the creator.
        rows (Optional[Rows])    : Specify rows of metadata data corresponding to an
                                   identifier if collection_type is sample_sheet
        source (Optional[Source]): The source of the notification. Represents the agent that
                                   created the notification.
        type_ (Optional[Type_])  : The type of content to be created in the history.
    """

    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    column_definitions: ColumnDefinitions | None = None  # Column data associated with each element of this collection.
    content: Content | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    copy_elements: CopyElements | None = True  # Whether to create a copy of the source HDAs for the new collection.
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
    element_identifiers: ElementIdentifiers | None = None  # List of elements that should be in the new collection.
    fields: Fields | None = None
    folder_id: FolderId | None = (
        None  # The ID of the library folder that will contain the collection. Required if `instance_type=library`.
    )
    hide_source_items: HideSourceItems | None = False  # Whether to mark the original HDAs as hidden.
    history_id: HistoryId | None = None  # The encoded ID of the history associated with this item.
    instance_type: InstanceType | None = "history"  # The type of the instance, either `history` (default) or `library`.
    name: Name | None = None  # The name of the creator.
    rows: Rows | None = (
        None  # Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet
    )
    source: Source | None = None  # The source of the notification. Represents the agent that created the notification.
    type_: Type_ | None = "dataset"  # The type of content to be created in the history.
