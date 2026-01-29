from typing import TypeAlias

from .data_elements_from_target import DataElementsFromTarget
from .data_elements_target import DataElementsTarget
from .ftp_import_target import FtpImportTarget
from .hdca_data_items_from_target import HdcaDataItemsFromTarget
from .hdca_data_items_target import HdcaDataItemsTarget

__all__ = ["FetchDataPayloadTargetsItem"]

FetchDataPayloadTargetsItem: TypeAlias = (
    DataElementsTarget | HdcaDataItemsTarget | DataElementsFromTarget | HdcaDataItemsFromTarget | FtpImportTarget
)
