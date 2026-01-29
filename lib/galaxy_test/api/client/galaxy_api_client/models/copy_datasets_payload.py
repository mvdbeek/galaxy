from dataclasses import dataclass

from .copy_datasets_payload_source_entry import CopyDatasetsPayloadSourceEntry
from .copy_datasets_payload_target_history_ids import CopyDatasetsPayloadTargetHistoryIds
from .copy_datasets_payload_target_history_name import CopyDatasetsPayloadTargetHistoryName

__all__ = ["CopyDatasetsPayload"]


@dataclass
class CopyDatasetsPayload:
    """
    CopyDatasetsPayload dataclass

    Args:
        source_content (List[CopyDatasetsPayloadSourceEntry])
                                 :
        target_history_ids (CopyDatasetsPayloadTargetHistoryIds | None)
                                 :
        target_history_name (CopyDatasetsPayloadTargetHistoryName | None)
                                 :
    """

    source_content: list[CopyDatasetsPayloadSourceEntry]
    target_history_ids: CopyDatasetsPayloadTargetHistoryIds | None = None
    target_history_name: CopyDatasetsPayloadTargetHistoryName | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "source_content": "source_content",
            "target_history_ids": "target_history_ids",
            "target_history_name": "target_history_name",
        }
        key_transform_with_dump = {
            "source_content": "source_content",
            "target_history_ids": "target_history_ids",
            "target_history_name": "target_history_name",
        }
