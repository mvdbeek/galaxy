from dataclasses import dataclass

from .copy_datasets_payload_source_entry import CopyDatasetsPayloadSourceEntry
from .target_history_ids import TargetHistoryIds
from .target_history_name import TargetHistoryName

__all__ = ["CopyDatasetsPayload"]


@dataclass
class CopyDatasetsPayload:
    """
    CopyDatasetsPayload dataclass.

    Args:
        source_content (List[CopyDatasetsPayloadSourceEntry])
                                 :
        target_history_ids (Optional[TargetHistoryIds])
                                 :
        target_history_name (Optional[TargetHistoryName])
                                 :
    """

    source_content: list[CopyDatasetsPayloadSourceEntry]
    target_history_ids: TargetHistoryIds | None = None
    target_history_name: TargetHistoryName | None = None
