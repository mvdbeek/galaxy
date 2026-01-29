from typing import TypeAlias

from .change_datatype_operation_params import ChangeDatatypeOperationParams
from .change_dbkey_operation_params import ChangeDbkeyOperationParams
from .tag_operation_params import TagOperationParams

__all__ = ["HistoryContentBulkOperationPayloadParams"]

HistoryContentBulkOperationPayloadParams: TypeAlias = (
    ChangeDatatypeOperationParams | ChangeDbkeyOperationParams | TagOperationParams | None
)
