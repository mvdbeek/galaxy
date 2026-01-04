from dataclasses import dataclass

from .ctx_rev import CtxRev
from .tool_shed_status import ToolShedStatus

__all__ = ["InstalledToolShedRepository"]


@dataclass
class InstalledToolShedRepository:
    """
    InstalledToolShedRepository dataclass.

    Args:
        changeset_revision (str) : Changeset revision of the repository - a mercurial commit
                                   hash
        ctx_rev (Optional[CtxRev]): The linearized 0-based index of the changeset on the
                                    tool shed (0, 1, 2,...)
        deleted (bool)           :
        dist_to_shed (bool)      :
        id_ (str)                : Encoded ID of the install tool shed repository.
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
        error_message (Optional[str])
                                 :
        tool_shed_status (Optional[ToolShedStatus])
                                 :
    """

    changeset_revision: str  # Changeset revision of the repository - a mercurial commit hash
    ctx_rev: CtxRev | None  # The linearized 0-based index of the changeset on the tool shed (0, 1, 2,...)
    deleted: bool
    dist_to_shed: bool
    id_: str  # Encoded ID of the install tool shed repository.
    installed_changeset_revision: str  # Initially installed changeset revision. Used to construct path to repository within Galaxies filesystem. Does not change if a repository is updated.
    model_class: str  # The name of the database model class.
    name: str  # Name of repository
    owner: str  # Owner of repository
    status: str
    tool_shed: str  # Hostname of the tool shed this was installed from
    uninstalled: bool
    error_message: str | None = "Installation error message, the empty string means no error was recorded"
    tool_shed_status: ToolShedStatus | None = None
