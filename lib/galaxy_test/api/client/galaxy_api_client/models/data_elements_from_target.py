from dataclasses import dataclass

from .destination import Destination
from .elements_from_type import ElementsFromType
from .ftp_path import FtpPath
from .items_from_src import ItemsFromSrc
from .path import Path
from .server_dir import ServerDir
from .url import Url

__all__ = ["DataElementsFromTarget"]


@dataclass
class DataElementsFromTarget:
    """
    DataElementsFromTarget dataclass.

    Args:
        destination (Destination):
        elements_from (ElementsFromType)
                                 :
        src (ItemsFromSrc)       :
        auto_decompress (Optional[bool])
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        ftp_path (Optional[FtpPath])
                                 :
        path (Optional[Path])    :
        server_dir (Optional[ServerDir])
                                 :
        url (Optional[Url])      : The relative URL to access this item.
    """

    destination: Destination
    elements_from: ElementsFromType
    src: ItemsFromSrc
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    ftp_path: FtpPath | None = None
    path: Path | None = None
    server_dir: ServerDir | None = ""
    url: Url | None = None  # The relative URL to access this item.
