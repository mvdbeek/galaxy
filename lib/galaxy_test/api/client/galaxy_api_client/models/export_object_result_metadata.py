from dataclasses import dataclass

from .error import Error
from .uri import Uri

__all__ = ["ExportObjectResultMetadata"]


@dataclass
class ExportObjectResultMetadata:
    """
    ExportObjectResultMetadata dataclass.

    Args:
        success (bool)           :
        error (Optional[Error])  :
        uri (Optional[Uri])      :
    """

    success: bool
    error: Error | None = None
    uri: Uri | None = None
