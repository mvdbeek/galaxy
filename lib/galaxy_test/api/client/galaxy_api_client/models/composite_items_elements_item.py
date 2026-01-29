from typing import TypeAlias

from .file_data_element import FileDataElement
from .ftp_import_element import FtpImportElement
from .pasted_data_element import PastedDataElement
from .path_data_element import PathDataElement
from .server_dir_element import ServerDirElement
from .url_data_element import UrlDataElement

__all__ = ["CompositeItemsElementsItem"]

CompositeItemsElementsItem: TypeAlias = (
    FileDataElement | PastedDataElement | UrlDataElement | PathDataElement | ServerDirElement | FtpImportElement
)
