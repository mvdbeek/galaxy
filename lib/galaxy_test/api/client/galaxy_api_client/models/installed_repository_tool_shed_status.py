from dataclasses import dataclass

from .latest_installable_revision import LatestInstallableRevision
from .repository_deprecated import RepositoryDeprecated
from .revision_upgrade import RevisionUpgrade

__all__ = ["InstalledRepositoryToolShedStatus"]


@dataclass
class InstalledRepositoryToolShedStatus:
    """
    InstalledRepositoryToolShedStatus dataclass.

    Args:
        revision_update (str)    :
        latest_installable_revision (Optional[LatestInstallableRevision])
                                 : Most recent version available on the tool shed
        repository_deprecated (Optional[RepositoryDeprecated])
                                 : Repository has been depreciated on the tool shed
        revision_upgrade (Optional[RevisionUpgrade])
                                 :
    """

    revision_update: str
    latest_installable_revision: LatestInstallableRevision | None = (
        None  # Most recent version available on the tool shed
    )
    repository_deprecated: RepositoryDeprecated | None = None  # Repository has been depreciated on the tool shed
    revision_upgrade: RevisionUpgrade | None = None
