from dataclasses import dataclass

from .installed_tool_shed_repository_ctx_rev import InstalledToolShedRepositoryCtxRev
from .installed_tool_shed_repository_tool_shed_status import InstalledToolShedRepositoryToolShedStatus

__all__ = ["InstalledToolShedRepository"]


@dataclass
class InstalledToolShedRepository:
    """
    InstalledToolShedRepository dataclass

    Args:
        changeset_revision (str) : Changeset revision of the repository - a mercurial commit
                                   hash
        ctx_rev (InstalledToolShedRepositoryCtxRev)
                                 : The linearized 0-based index of the changeset on the tool
                                   shed (0, 1, 2,...)
        deleted (bool)           :
        dist_to_shed (bool)      :
        id_ (str)                : Encoded ID of the install tool shed repository. (maps
                                   from 'id')
        installed_changeset_revision (str)
                                 : Initially installed changeset revision. Used to construct
                                   path to repository within Galaxies filesystem. Does not
                                   change if a repository is updated.
        model_class (str)        : The name of the database model class.
        name (str)               : Name of repository
        owner (str)              : Owner of repository
        status (str)             :
        tool_shed (str)          : Hostname of the tool shed this was installed from
        uninstalled (bool)       :
        error_message (str | None):
        tool_shed_status (InstalledToolShedRepositoryToolShedStatus | None)
                                 :
    """

    changeset_revision: str  # Changeset revision of the repository - a mercurial commit hash
    ctx_rev: InstalledToolShedRepositoryCtxRev  # The linearized 0-based index of the changeset on the tool shed (0, 1, 2,...)
    deleted: bool
    dist_to_shed: bool
    id_: str  # Encoded ID of the install tool shed repository. (maps from 'id')
    installed_changeset_revision: str  # Initially installed changeset revision. Used to construct path to repository within Galaxies filesystem. Does not change if a repository is updated.
    model_class: str  # The name of the database model class.
    name: str  # Name of repository
    owner: str  # Owner of repository
    status: str
    tool_shed: str  # Hostname of the tool shed this was installed from
    uninstalled: bool
    error_message: str | None = "Installation error message, the empty string means no error was recorded"
    tool_shed_status: InstalledToolShedRepositoryToolShedStatus | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "changeset_revision": "changeset_revision",
            "ctx_rev": "ctx_rev",
            "deleted": "deleted",
            "dist_to_shed": "dist_to_shed",
            "error_message": "error_message",
            "id": "id_",
            "installed_changeset_revision": "installed_changeset_revision",
            "model_class": "model_class",
            "name": "name",
            "owner": "owner",
            "status": "status",
            "tool_shed": "tool_shed",
            "tool_shed_status": "tool_shed_status",
            "uninstalled": "uninstalled",
        }
        key_transform_with_dump = {
            "changeset_revision": "changeset_revision",
            "ctx_rev": "ctx_rev",
            "deleted": "deleted",
            "dist_to_shed": "dist_to_shed",
            "error_message": "error_message",
            "id_": "id",
            "installed_changeset_revision": "installed_changeset_revision",
            "model_class": "model_class",
            "name": "name",
            "owner": "owner",
            "status": "status",
            "tool_shed": "tool_shed",
            "tool_shed_status": "tool_shed_status",
            "uninstalled": "uninstalled",
        }
