from dataclasses import dataclass

from .data_landing_request_state_targets import DataLandingRequestStateTargets

__all__ = ["DataLandingRequestState"]


@dataclass
class DataLandingRequestState:
    """
    DataLandingRequestState dataclass

    Args:
        targets (DataLandingRequestStateTargets)
                                 :
    """

    targets: DataLandingRequestStateTargets

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "targets": "targets",
        }
        key_transform_with_dump = {
            "targets": "targets",
        }
