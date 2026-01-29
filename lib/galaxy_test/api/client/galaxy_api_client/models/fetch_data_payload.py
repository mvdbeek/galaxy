from dataclasses import dataclass

from .fetch_data_payload_landing_uuid import FetchDataPayloadLandingUuid
from .fetch_data_payload_targets import FetchDataPayloadTargets

__all__ = ["FetchDataPayload"]


@dataclass
class FetchDataPayload:
    """
    FetchDataPayload dataclass

    Args:
        history_id (str)         :
        targets (FetchDataPayloadTargets)
                                 :
        landing_uuid (FetchDataPayloadLandingUuid | None)
                                 :
    """

    history_id: str
    targets: FetchDataPayloadTargets
    landing_uuid: FetchDataPayloadLandingUuid | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_id": "history_id",
            "landing_uuid": "landing_uuid",
            "targets": "targets",
        }
        key_transform_with_dump = {
            "history_id": "history_id",
            "landing_uuid": "landing_uuid",
            "targets": "targets",
        }
