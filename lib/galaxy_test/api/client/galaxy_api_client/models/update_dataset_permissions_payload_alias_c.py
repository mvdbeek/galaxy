from dataclasses import dataclass

from .update_dataset_permissions_payload_alias_c_access_ids import UpdateDatasetPermissionsPayloadAliasCAccessIds
from .update_dataset_permissions_payload_alias_c_action import UpdateDatasetPermissionsPayloadAliasCAction
from .update_dataset_permissions_payload_alias_c_manage_ids import UpdateDatasetPermissionsPayloadAliasCManageIds
from .update_dataset_permissions_payload_alias_c_modify_ids import UpdateDatasetPermissionsPayloadAliasCModifyIds

__all__ = ["UpdateDatasetPermissionsPayloadAliasC"]


@dataclass
class UpdateDatasetPermissionsPayloadAliasC:
    """
    UpdateDatasetPermissionsPayloadAliasC dataclass

    Args:
        access_ids (UpdateDatasetPermissionsPayloadAliasCAccessIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have access permission on the dataset.
        action (UpdateDatasetPermissionsPayloadAliasCAction | None)
                                 : Indicates what action should be performed on the dataset.
        manage_ids (UpdateDatasetPermissionsPayloadAliasCManageIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have manage permission on the dataset.
        modify_ids (UpdateDatasetPermissionsPayloadAliasCModifyIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have modify permission on the dataset.
    """

    access_ids: UpdateDatasetPermissionsPayloadAliasCAccessIds | None = (
        None  # A list of role encoded IDs defining roles that should have access permission on the dataset.
    )
    action: UpdateDatasetPermissionsPayloadAliasCAction | None = (
        "set_permissions"  # Indicates what action should be performed on the dataset.
    )
    manage_ids: UpdateDatasetPermissionsPayloadAliasCManageIds | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the dataset.
    )
    modify_ids: UpdateDatasetPermissionsPayloadAliasCModifyIds | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the dataset.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_ids": "access_ids",
            "action": "action",
            "manage_ids": "manage_ids",
            "modify_ids": "modify_ids",
        }
        key_transform_with_dump = {
            "access_ids": "access_ids",
            "action": "action",
            "manage_ids": "manage_ids",
            "modify_ids": "modify_ids",
        }
