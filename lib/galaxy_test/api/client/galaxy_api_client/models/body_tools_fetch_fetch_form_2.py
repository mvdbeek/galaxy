from dataclasses import dataclass

from .body_tools_fetch_fetch_form_files import BodyToolsFetchFetchFormFiles
from .body_tools_fetch_fetch_form_history_id import BodyToolsFetchFetchFormHistoryId
from .body_tools_fetch_fetch_form_landing_uuid import BodyToolsFetchFetchFormLandingUuid
from .body_tools_fetch_fetch_form_targets import BodyToolsFetchFetchFormTargets

__all__ = ["BodyToolsFetchFetchForm2"]


@dataclass
class BodyToolsFetchFetchForm2:
    """
    BodyToolsFetchFetchForm2 dataclass

    Args:
        history_id (BodyToolsFetchFetchFormHistoryId)
                                 :
        targets (BodyToolsFetchFetchFormTargets)
                                 :
        files (BodyToolsFetchFetchFormFiles | None)
                                 :
        landing_uuid (BodyToolsFetchFetchFormLandingUuid | None)
                                 :
    """

    history_id: BodyToolsFetchFetchFormHistoryId
    targets: BodyToolsFetchFetchFormTargets
    files: BodyToolsFetchFetchFormFiles | None = None
    landing_uuid: BodyToolsFetchFetchFormLandingUuid | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "files": "files",
            "history_id": "history_id",
            "landing_uuid": "landing_uuid",
            "targets": "targets",
        }
        key_transform_with_dump = {
            "files": "files",
            "history_id": "history_id",
            "landing_uuid": "landing_uuid",
            "targets": "targets",
        }
