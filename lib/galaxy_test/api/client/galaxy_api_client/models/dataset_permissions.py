from dataclasses import dataclass, field

__all__ = ["DatasetPermissions"]


@dataclass
class DatasetPermissions:
    """
    Role-based permissions for accessing and managing a dataset.

    Args:
        access (List[str] | None): The set of roles (encoded IDs) that can access this
                                   dataset.
        manage (List[str] | None): The set of roles (encoded IDs) that can manage this
                                   dataset.
    """

    access: list[str] | None = field(
        default_factory=list
    )  # The set of roles (encoded IDs) that can access this dataset.
    manage: list[str] | None = field(
        default_factory=list
    )  # The set of roles (encoded IDs) that can manage this dataset.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access": "access",
            "manage": "manage",
        }
        key_transform_with_dump = {
            "access": "access",
            "manage": "manage",
        }
