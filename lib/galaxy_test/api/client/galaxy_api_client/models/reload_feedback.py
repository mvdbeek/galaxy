from dataclasses import dataclass

from .failed import Failed
from .reloaded import Reloaded

__all__ = ["ReloadFeedback"]


@dataclass
class ReloadFeedback:
    """
    ReloadFeedback dataclass.

    Args:
        failed (Failed)          :
        message (str)            :
        reloaded (Reloaded)      :
    """

    failed: Failed
    message: str
    reloaded: Reloaded
