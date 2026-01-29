from dataclasses import dataclass

from .landing_uuid import LandingUuid
from .targets import Targets

__all__ = ["FetchDataPayload"]


@dataclass
class FetchDataPayload:
    """
    FetchDataPayload dataclass.

    Args:
        history_id (str)         :
        targets (Targets)        :
        landing_uuid (Optional[LandingUuid])
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
    """

    history_id: str
    targets: Targets
    landing_uuid: LandingUuid | None = None  # The UUID of the workflow landing request associated with this invocation.
