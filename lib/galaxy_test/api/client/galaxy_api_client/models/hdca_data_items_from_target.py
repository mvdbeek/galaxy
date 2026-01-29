from dataclasses import dataclass

from .elements_from_type import ElementsFromType
from .hdca_data_items_from_target_collection_type import HdcaDataItemsFromTargetCollectionType
from .hdca_data_items_from_target_column_definitions import HdcaDataItemsFromTargetColumnDefinitions
from .hdca_data_items_from_target_ftp_path import HdcaDataItemsFromTargetFtpPath
from .hdca_data_items_from_target_name import HdcaDataItemsFromTargetName
from .hdca_data_items_from_target_path import HdcaDataItemsFromTargetPath
from .hdca_data_items_from_target_server_dir import HdcaDataItemsFromTargetServerDir
from .hdca_data_items_from_target_tags import HdcaDataItemsFromTargetTags
from .hdca_data_items_from_target_url import HdcaDataItemsFromTargetUrl
from .hdca_destination import HdcaDestination
from .items_from_src import ItemsFromSrc

__all__ = ["HdcaDataItemsFromTarget"]


@dataclass
class HdcaDataItemsFromTarget:
    """
    HdcaDataItemsFromTarget dataclass

    Args:
        destination (HdcaDestination)
                                 :
        items_from (ElementsFromType)
                                 :
        src (ItemsFromSrc)       :
        auto_decompress (bool | None)
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        collection_type (HdcaDataItemsFromTargetCollectionType | None)
                                 :
        column_definitions (HdcaDataItemsFromTargetColumnDefinitions | None)
                                 :
        ftp_path (HdcaDataItemsFromTargetFtpPath | None)
                                 :
        name (HdcaDataItemsFromTargetName | None)
                                 :
        path (HdcaDataItemsFromTargetPath | None)
                                 :
        server_dir (HdcaDataItemsFromTargetServerDir | None)
                                 :
        tags (HdcaDataItemsFromTargetTags | None)
                                 :
        url (HdcaDataItemsFromTargetUrl | None)
                                 :
    """

    destination: HdcaDestination
    items_from: ElementsFromType
    src: ItemsFromSrc
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    collection_type: HdcaDataItemsFromTargetCollectionType | None = None
    column_definitions: HdcaDataItemsFromTargetColumnDefinitions | None = None
    ftp_path: HdcaDataItemsFromTargetFtpPath | None = None
    name: HdcaDataItemsFromTargetName | None = None
    path: HdcaDataItemsFromTargetPath | None = None
    server_dir: HdcaDataItemsFromTargetServerDir | None = None
    tags: HdcaDataItemsFromTargetTags | None = None
    url: HdcaDataItemsFromTargetUrl | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "auto_decompress": "auto_decompress",
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "destination": "destination",
            "ftp_path": "ftp_path",
            "items_from": "items_from",
            "name": "name",
            "path": "path",
            "server_dir": "server_dir",
            "src": "src",
            "tags": "tags",
            "url": "url",
        }
        key_transform_with_dump = {
            "auto_decompress": "auto_decompress",
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "destination": "destination",
            "ftp_path": "ftp_path",
            "items_from": "items_from",
            "name": "name",
            "path": "path",
            "server_dir": "server_dir",
            "src": "src",
            "tags": "tags",
            "url": "url",
        }
