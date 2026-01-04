from dataclasses import dataclass

__all__ = ["UserBeaconSetting"]


@dataclass
class UserBeaconSetting:
    """
    UserBeaconSetting dataclass.

    Args:
        enabled (bool)           : True if beacon sharing is enabled
    """

    enabled: bool  # True if beacon sharing is enabled
