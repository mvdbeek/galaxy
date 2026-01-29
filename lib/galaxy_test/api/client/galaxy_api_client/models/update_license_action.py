from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["UpdateLicenseAction"]


@dataclass
class UpdateLicenseAction:
    """
    UpdateLicenseAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        license (str)            :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    license: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "license": "license",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "license": "license",
        }
