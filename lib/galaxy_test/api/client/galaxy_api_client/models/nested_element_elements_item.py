from typing import TypeAlias

from .composite_data_element import CompositeDataElement
from .file_data_element import FileDataElement
from .ftp_import_element import FtpImportElement
from .nested_element import NestedElement
from .pasted_data_element import PastedDataElement
from .path_data_element import PathDataElement
from .server_dir_element import ServerDirElement
from .url_data_element import UrlDataElement

__all__ = ["NestedElementElementsItem"]

NestedElementElementsItem: TypeAlias = (
    FileDataElement
    | PastedDataElement
    | UrlDataElement
    | PathDataElement
    | ServerDirElement
    | FtpImportElement
    | CompositeDataElement
    | NestedElement
)
