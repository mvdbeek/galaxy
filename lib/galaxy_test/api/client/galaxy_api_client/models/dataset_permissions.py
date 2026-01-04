from dataclasses import dataclass

from .access import Access
from .manage import Manage

__all__ = ["DatasetPermissions"]


@dataclass
class DatasetPermissions:
    """
    Role-based permissions for accessing and managing a dataset.

    Args:
        access (Optional[Access]): The set of roles (encoded IDs) that can access this
                                   dataset.
        manage (Optional[Manage]): The set of roles (encoded IDs) that can manage this
                                   dataset.
    """

    access: Access | None = None  # The set of roles (encoded IDs) that can access this dataset.
    manage: Manage | None = None  # The set of roles (encoded IDs) that can manage this dataset.
