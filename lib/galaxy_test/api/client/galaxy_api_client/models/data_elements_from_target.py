from dataclasses import dataclass

from .data_elements_from_target_destination import DataElementsFromTargetDestination
from .data_elements_from_target_ftp_path import DataElementsFromTargetFtpPath
from .data_elements_from_target_path import DataElementsFromTargetPath
from .data_elements_from_target_server_dir import DataElementsFromTargetServerDir
from .data_elements_from_target_url import DataElementsFromTargetUrl
from .elements_from_type import ElementsFromType
from .items_from_src import ItemsFromSrc

__all__ = ["DataElementsFromTarget"]


@dataclass
class DataElementsFromTarget:
    """
    DataElementsFromTarget dataclass

    Args:
        destination (DataElementsFromTargetDestination)
                                 :
        elements_from (ElementsFromType)
                                 :
        src (ItemsFromSrc)       :
        auto_decompress (bool | None)
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        ftp_path (DataElementsFromTargetFtpPath | None)
                                 :
        path (DataElementsFromTargetPath | None)
                                 :
        server_dir (DataElementsFromTargetServerDir | None)
                                 :
        url (DataElementsFromTargetUrl | None)
                                 :
    """

    destination: DataElementsFromTargetDestination
    elements_from: ElementsFromType
    src: ItemsFromSrc
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    ftp_path: DataElementsFromTargetFtpPath | None = None
    path: DataElementsFromTargetPath | None = None
    server_dir: DataElementsFromTargetServerDir | None = None
    url: DataElementsFromTargetUrl | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "auto_decompress": "auto_decompress",
            "destination": "destination",
            "elements_from": "elements_from",
            "ftp_path": "ftp_path",
            "path": "path",
            "server_dir": "server_dir",
            "src": "src",
            "url": "url",
        }
        key_transform_with_dump = {
            "auto_decompress": "auto_decompress",
            "destination": "destination",
            "elements_from": "elements_from",
            "ftp_path": "ftp_path",
            "path": "path",
            "server_dir": "server_dir",
            "src": "src",
            "url": "url",
        }
