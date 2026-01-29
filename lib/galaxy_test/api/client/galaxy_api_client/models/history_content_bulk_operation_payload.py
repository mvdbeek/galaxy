from dataclasses import dataclass

from .history_content_item_operation import HistoryContentItemOperation
from .items import Items
from .params import Params

__all__ = ["HistoryContentBulkOperationPayload"]


@dataclass
class HistoryContentBulkOperationPayload:
    """
    HistoryContentBulkOperationPayload dataclass.

    Args:
        operation (HistoryContentItemOperation)
                                 :
        items (Optional[Items])  :
        params (Optional[Params]): Object containing all the parameters of the tool
                                   associated with this job. The specific parameters depend
                                   on the tool itself.
    """

    operation: HistoryContentItemOperation
    items: Items | None = None
    params: Params | None = (
        None  # Object containing all the parameters of the tool associated with this job. The specific parameters depend on the tool itself.
    )
