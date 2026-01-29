from dataclasses import dataclass

from .installed_repository_tool_shed_status_latest_installable_revision import (
    InstalledRepositoryToolShedStatusLatestInstallableRevision,
)
from .installed_repository_tool_shed_status_repository_deprecated import (
    InstalledRepositoryToolShedStatusRepositoryDeprecated,
)
from .installed_repository_tool_shed_status_revision_upgrade import InstalledRepositoryToolShedStatusRevisionUpgrade

__all__ = ["InstalledRepositoryToolShedStatus"]


@dataclass
class InstalledRepositoryToolShedStatus:
    """
    InstalledRepositoryToolShedStatus dataclass

    Args:
        revision_update (str)    :
        latest_installable_revision (InstalledRepositoryToolShedStatusLatestInstallableRevision | None)
                                 : Most recent version available on the tool shed
        repository_deprecated (InstalledRepositoryToolShedStatusRepositoryDeprecated | None)
                                 : Repository has been depreciated on the tool shed
        revision_upgrade (InstalledRepositoryToolShedStatusRevisionUpgrade | None)
                                 :
    """

    revision_update: str
    latest_installable_revision: InstalledRepositoryToolShedStatusLatestInstallableRevision | None = (
        None  # Most recent version available on the tool shed
    )
    repository_deprecated: InstalledRepositoryToolShedStatusRepositoryDeprecated | None = (
        None  # Repository has been depreciated on the tool shed
    )
    revision_upgrade: InstalledRepositoryToolShedStatusRevisionUpgrade | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "latest_installable_revision": "latest_installable_revision",
            "repository_deprecated": "repository_deprecated",
            "revision_update": "revision_update",
            "revision_upgrade": "revision_upgrade",
        }
        key_transform_with_dump = {
            "latest_installable_revision": "latest_installable_revision",
            "repository_deprecated": "repository_deprecated",
            "revision_update": "revision_update",
            "revision_upgrade": "revision_upgrade",
        }
