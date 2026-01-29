from dataclasses import dataclass

from .update_dataset_permissions_payload_access_ids import UpdateDatasetPermissionsPayloadAccessIds
from .update_dataset_permissions_payload_action import UpdateDatasetPermissionsPayloadAction
from .update_dataset_permissions_payload_manage_ids import UpdateDatasetPermissionsPayloadManageIds
from .update_dataset_permissions_payload_modify_ids import UpdateDatasetPermissionsPayloadModifyIds

__all__ = ["UpdateDatasetPermissionsPayload"]


@dataclass
class UpdateDatasetPermissionsPayload:
    """
    UpdateDatasetPermissionsPayload dataclass

    Args:
        access_ids (UpdateDatasetPermissionsPayloadAccessIds | None)
                                 : Maps from 'access_ids[]'
        action (UpdateDatasetPermissionsPayloadAction | None)
                                 : Indicates what action should be performed on the dataset.
        manage_ids (UpdateDatasetPermissionsPayloadManageIds | None)
                                 : Maps from 'manage_ids[]'
        modify_ids (UpdateDatasetPermissionsPayloadModifyIds | None)
                                 : Maps from 'modify_ids[]'
    """

    access_ids: UpdateDatasetPermissionsPayloadAccessIds | None = None  # Maps from 'access_ids[]'
    action: UpdateDatasetPermissionsPayloadAction | None = (
        "set_permissions"  # Indicates what action should be performed on the dataset.
    )
    manage_ids: UpdateDatasetPermissionsPayloadManageIds | None = None  # Maps from 'manage_ids[]'
    modify_ids: UpdateDatasetPermissionsPayloadModifyIds | None = None  # Maps from 'modify_ids[]'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_ids[]": "access_ids",
            "action": "action",
            "manage_ids[]": "manage_ids",
            "modify_ids[]": "modify_ids",
        }
        key_transform_with_dump = {
            "access_ids": "access_ids[]",
            "action": "action",
            "manage_ids": "manage_ids[]",
            "modify_ids": "modify_ids[]",
        }
