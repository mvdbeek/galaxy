from dataclasses import dataclass

from .hdca_data_items_target_collection_type import HdcaDataItemsTargetCollectionType
from .hdca_data_items_target_column_definitions import HdcaDataItemsTargetColumnDefinitions
from .hdca_data_items_target_elements import HdcaDataItemsTargetElements
from .hdca_data_items_target_name import HdcaDataItemsTargetName
from .hdca_data_items_target_tags import HdcaDataItemsTargetTags
from .hdca_destination import HdcaDestination

__all__ = ["HdcaDataItemsTarget"]


@dataclass
class HdcaDataItemsTarget:
    """
    HdcaDataItemsTarget dataclass

    Args:
        destination (HdcaDestination)
                                 :
        elements (HdcaDataItemsTargetElements)
                                 :
        auto_decompress (bool | None)
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        collection_type (HdcaDataItemsTargetCollectionType | None)
                                 :
        column_definitions (HdcaDataItemsTargetColumnDefinitions | None)
                                 :
        name (HdcaDataItemsTargetName | None)
                                 :
        tags (HdcaDataItemsTargetTags | None)
                                 :
    """

    destination: HdcaDestination
    elements: HdcaDataItemsTargetElements
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    collection_type: HdcaDataItemsTargetCollectionType | None = None
    column_definitions: HdcaDataItemsTargetColumnDefinitions | None = None
    name: HdcaDataItemsTargetName | None = None
    tags: HdcaDataItemsTargetTags | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "auto_decompress": "auto_decompress",
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "destination": "destination",
            "elements": "elements",
            "name": "name",
            "tags": "tags",
        }
        key_transform_with_dump = {
            "auto_decompress": "auto_decompress",
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "destination": "destination",
            "elements": "elements",
            "name": "name",
            "tags": "tags",
        }
