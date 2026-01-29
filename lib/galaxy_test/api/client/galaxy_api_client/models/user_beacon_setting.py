from dataclasses import dataclass

__all__ = ["UserBeaconSetting"]


@dataclass
class UserBeaconSetting:
    """
    UserBeaconSetting dataclass

    Args:
        enabled (bool)           : True if beacon sharing is enabled
    """

    enabled: bool  # True if beacon sharing is enabled

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "enabled": "enabled",
        }
        key_transform_with_dump = {
            "enabled": "enabled",
        }
