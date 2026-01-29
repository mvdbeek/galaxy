from dataclasses import dataclass

__all__ = ["UpdateLicenseAction"]


@dataclass
class UpdateLicenseAction:
    """
    UpdateLicenseAction dataclass.

    Args:
        action_type (str)        :
        license (str)            :
    """

    action_type: str
    license: str
