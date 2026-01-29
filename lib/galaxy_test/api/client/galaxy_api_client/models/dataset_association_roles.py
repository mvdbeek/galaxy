from dataclasses import dataclass

from .dataset_association_roles_access_dataset_roles import DatasetAssociationRolesAccessDatasetRoles
from .dataset_association_roles_manage_dataset_roles import DatasetAssociationRolesManageDatasetRoles
from .dataset_association_roles_modify_item_roles import DatasetAssociationRolesModifyItemRoles

__all__ = ["DatasetAssociationRoles"]


@dataclass
class DatasetAssociationRoles:
    """
    DatasetAssociationRoles dataclass

    Args:
        access_dataset_roles (DatasetAssociationRolesAccessDatasetRoles | None)
                                 : A list of roles that can access the dataset. The user has
                                   to **have all these roles** in order to access this
                                   dataset. Users without access permission **cannot** have
                                   other permissions on this dataset. If there are no access
                                   roles set on the dataset it is considered
                                   **unrestricted**.
        manage_dataset_roles (DatasetAssociationRolesManageDatasetRoles | None)
                                 : A list of roles that can manage permissions on the
                                   dataset. Users with **any** of these roles can manage
                                   permissions of this dataset. If you remove yourself you
                                   will lose the ability to manage this dataset unless you
                                   are an admin.
        modify_item_roles (DatasetAssociationRolesModifyItemRoles | None)
                                 : A list of roles that can modify the library item. This is
                                   a library related permission. User with **any** of these
                                   roles can modify name, metadata, and other information
                                   about this library item.
    """

    access_dataset_roles: DatasetAssociationRolesAccessDatasetRoles | None = (
        None  # A list of roles that can access the dataset. The user has to **have all these roles** in order to access this dataset. Users without access permission **cannot** have other permissions on this dataset. If there are no access roles set on the dataset it is considered **unrestricted**.
    )
    manage_dataset_roles: DatasetAssociationRolesManageDatasetRoles | None = (
        None  # A list of roles that can manage permissions on the dataset. Users with **any** of these roles can manage permissions of this dataset. If you remove yourself you will lose the ability to manage this dataset unless you are an admin.
    )
    modify_item_roles: DatasetAssociationRolesModifyItemRoles | None = (
        None  # A list of roles that can modify the library item. This is a library related permission. User with **any** of these roles can modify name, metadata, and other information about this library item.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_dataset_roles": "access_dataset_roles",
            "manage_dataset_roles": "manage_dataset_roles",
            "modify_item_roles": "modify_item_roles",
        }
        key_transform_with_dump = {
            "access_dataset_roles": "access_dataset_roles",
            "manage_dataset_roles": "manage_dataset_roles",
            "modify_item_roles": "modify_item_roles",
        }
