from dataclasses import dataclass

from .export_object_request_metadata import ExportObjectRequestMetadata
from .result_data import ResultData

__all__ = ["ExportObjectMetadata"]


@dataclass
class ExportObjectMetadata:
    """
    ExportObjectMetadata dataclass.

    Args:
        request_data (ExportObjectRequestMetadata)
                                 :
        result_data (Optional[ResultData])
                                 :
    """

    request_data: ExportObjectRequestMetadata
    result_data: ResultData | None = None
