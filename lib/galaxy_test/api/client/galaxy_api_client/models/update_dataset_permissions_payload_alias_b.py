from dataclasses import dataclass

from .update_dataset_permissions_payload_alias_b_access import UpdateDatasetPermissionsPayloadAliasBAccess
from .update_dataset_permissions_payload_alias_b_action import UpdateDatasetPermissionsPayloadAliasBAction
from .update_dataset_permissions_payload_alias_b_manage import UpdateDatasetPermissionsPayloadAliasBManage
from .update_dataset_permissions_payload_alias_b_modify import UpdateDatasetPermissionsPayloadAliasBModify

__all__ = ["UpdateDatasetPermissionsPayloadAliasB"]


@dataclass
class UpdateDatasetPermissionsPayloadAliasB:
    """
    UpdateDatasetPermissionsPayloadAliasB dataclass

    Args:
        access (UpdateDatasetPermissionsPayloadAliasBAccess | None)
                                 : A list of role encoded IDs defining roles that should
                                   have access permission on the dataset.
        action (UpdateDatasetPermissionsPayloadAliasBAction | None)
                                 : Indicates what action should be performed on the dataset.
        manage (UpdateDatasetPermissionsPayloadAliasBManage | None)
                                 : A list of role encoded IDs defining roles that should
                                   have manage permission on the dataset.
        modify (UpdateDatasetPermissionsPayloadAliasBModify | None)
                                 : A list of role encoded IDs defining roles that should
                                   have modify permission on the dataset.
    """

    access: UpdateDatasetPermissionsPayloadAliasBAccess | None = (
        None  # A list of role encoded IDs defining roles that should have access permission on the dataset.
    )
    action: UpdateDatasetPermissionsPayloadAliasBAction | None = (
        "set_permissions"  # Indicates what action should be performed on the dataset.
    )
    manage: UpdateDatasetPermissionsPayloadAliasBManage | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the dataset.
    )
    modify: UpdateDatasetPermissionsPayloadAliasBModify | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the dataset.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access": "access",
            "action": "action",
            "manage": "manage",
            "modify": "modify",
        }
        key_transform_with_dump = {
            "access": "access",
            "action": "action",
            "manage": "manage",
            "modify": "modify",
        }
