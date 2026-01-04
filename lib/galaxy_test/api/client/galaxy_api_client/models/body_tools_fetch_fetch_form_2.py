from dataclasses import dataclass

from .files import Files
from .history_id import HistoryId
from .landing_uuid import LandingUuid
from .targets import Targets

__all__ = ["BodyToolsFetchFetchForm2"]


@dataclass
class BodyToolsFetchFetchForm2:
    """
    BodyToolsFetchFetchForm2 dataclass.

    Args:
        history_id (HistoryId)   : The encoded ID of the history associated with this item.
        targets (Targets)        :
        files (Optional[Files])  :
        landing_uuid (Optional[LandingUuid])
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
    """

    history_id: HistoryId  # The encoded ID of the history associated with this item.
    targets: Targets
    files: Files | None = None
    landing_uuid: LandingUuid | None = None  # The UUID of the workflow landing request associated with this invocation.
