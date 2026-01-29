from dataclasses import dataclass

from .ftp_import_target_collection_type import FtpImportTargetCollectionType
from .ftp_import_target_column_definitions import FtpImportTargetColumnDefinitions
from .ftp_import_target_items_from import FtpImportTargetItemsFrom
from .ftp_import_target_name import FtpImportTargetName
from .ftp_import_target_tags import FtpImportTargetTags
from .hdca_destination import HdcaDestination

__all__ = ["FtpImportTarget"]


@dataclass
class FtpImportTarget:
    """
    FtpImportTarget dataclass

    Args:
        destination (HdcaDestination)
                                 :
        ftp_path (str)           :
        src (str)                :
        auto_decompress (bool | None)
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        collection_type (FtpImportTargetCollectionType | None)
                                 :
        column_definitions (FtpImportTargetColumnDefinitions | None)
                                 :
        items_from (FtpImportTargetItemsFrom | None)
                                 :
        name (FtpImportTargetName | None)
                                 :
        tags (FtpImportTargetTags | None)
                                 :
    """

    destination: HdcaDestination
    ftp_path: str
    src: str
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    collection_type: FtpImportTargetCollectionType | None = None
    column_definitions: FtpImportTargetColumnDefinitions | None = None
    items_from: FtpImportTargetItemsFrom | None = None
    name: FtpImportTargetName | None = None
    tags: FtpImportTargetTags | None = None

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
            "src": "src",
            "tags": "tags",
        }
        key_transform_with_dump = {
            "auto_decompress": "auto_decompress",
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "destination": "destination",
            "ftp_path": "ftp_path",
            "items_from": "items_from",
            "name": "name",
            "src": "src",
            "tags": "tags",
        }
