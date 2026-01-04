from dataclasses import dataclass

from .access_dataset_roles import AccessDatasetRoles
from .manage_dataset_roles import ManageDatasetRoles
from .modify_item_roles import ModifyItemRoles

__all__ = ["DatasetAssociationRoles"]


@dataclass
class DatasetAssociationRoles:
    """
    DatasetAssociationRoles dataclass.

    Args:
        access_dataset_roles (Optional[AccessDatasetRoles])
                                 : A list of roles that can access the dataset. The user has
                                   to **have all these roles** in order to access this
                                   dataset. Users without access permission **cannot** have
                                   other permissions on this dataset. If there are no access
                                   roles set on the dataset it is considered
                                   **unrestricted**.
        manage_dataset_roles (Optional[ManageDatasetRoles])
                                 : A list of roles that can manage permissions on the
                                   dataset. Users with **any** of these roles can manage
                                   permissions of this dataset. If you remove yourself you
                                   will lose the ability to manage this dataset unless you
                                   are an admin.
        modify_item_roles (Optional[ModifyItemRoles])
                                 : A list of roles that can modify the library item. This is
                                   a library related permission. User with **any** of these
                                   roles can modify name, metadata, and other information
                                   about this library item.
    """

    access_dataset_roles: AccessDatasetRoles | None = (
        None  # A list of roles that can access the dataset. The user has to **have all these roles** in order to access this dataset. Users without access permission **cannot** have other permissions on this dataset. If there are no access roles set on the dataset it is considered **unrestricted**.
    )
    manage_dataset_roles: ManageDatasetRoles | None = (
        None  # A list of roles that can manage permissions on the dataset. Users with **any** of these roles can manage permissions of this dataset. If you remove yourself you will lose the ability to manage this dataset unless you are an admin.
    )
    modify_item_roles: ModifyItemRoles | None = (
        None  # A list of roles that can modify the library item. This is a library related permission. User with **any** of these roles can modify name, metadata, and other information about this library item.
    )
