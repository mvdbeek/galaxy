import threading
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    TYPE_CHECKING,
)

from sortedcontainers import SortedSet

from galaxy.tool_util.version import parse_version
from galaxy.util.tool_version import remove_version_from_guid

if TYPE_CHECKING:
    from galaxy.tool_source_store.index import ToolIndex
    from galaxy.tools import Tool


class ToolLineageVersion:
    """Represents a single tool in a lineage. If lineage is based
    around GUIDs that somehow encode the version (either using GUID
    or a simple tool id and a version)."""

    def __init__(self, id: str, version: str) -> None:
        self.id = id
        self.version = version

    @property
    def id_based(self) -> bool:
        """Return True if the lineage is defined by GUIDs (in this
        case the indexer of the tools (i.e. the ToolBox) should ignore
        the tool_version (because it is encoded in the GUID and managed
        externally).
        """
        return self.version is None

    def to_dict(self) -> Dict[str, str]:
        return dict(
            id=self.id,
            version=self.version,
        )


class ToolLineage:
    """Simple tool's loaded directly from file system with lineage
    determined solely by PEP 440 versioning scheme.
    """

    lineages_by_id: Dict[str, "ToolLineage"] = {}
    lock = threading.Lock()

    def __init__(self, tool_id: str) -> None:
        self.tool_id = tool_id
        self.tool_versions = SortedSet(key=parse_version)

    @property
    def tool_ids(self) -> List[str]:
        versionless_tool_id = remove_version_from_guid(self.tool_id)
        tool_id = versionless_tool_id or self.tool_id
        return [f"{tool_id}/{version}" for version in self.tool_versions]

    @classmethod
    def from_tool(cls, tool: "Tool") -> "ToolLineage":
        tool_id = tool.id
        assert tool_id is not None
        lineages_by_id = cls.lineages_by_id
        with cls.lock:
            if tool_id not in lineages_by_id:
                lineages_by_id[tool_id] = ToolLineage(tool_id)
        lineage = lineages_by_id[tool_id]
        lineage.register_version(tool.version)
        return lineage

    def register_version(self, tool_version: str) -> None:
        self.tool_versions.add(tool_version)

    def get_versions(self) -> List[ToolLineageVersion]:
        """
        Return an ordered list of lineages (ToolLineageVersion) in this
        chain, from oldest to newest.
        """
        return [
            ToolLineageVersion(tool_id, tool_version)
            for tool_id, tool_version in zip(self.tool_ids, self.tool_versions)
        ]

    def get_version_ids(self, reverse: bool = False) -> List[str]:
        if reverse:
            return list(reversed(self.tool_ids))
        return self.tool_ids

    def to_dict(self) -> Dict[str, Any]:
        return dict(
            tool_id=self.tool_id,
            tool_versions=list(self.tool_versions),
            lineage_type="stock",
        )


class IndexToolLineage:
    """
    ToolLineage built from index data without requiring loaded Tool objects.

    This provides the same interface as ToolLineage but is constructed from
    pre-indexed tool metadata, enabling lineage queries without loading tools.
    """

    def __init__(
        self,
        tool_id: str,
        versions: List[Tuple[str, Optional[str]]],
    ) -> None:
        """
        Initialize an index-based lineage.

        Args:
            tool_id: The base/versionless tool ID for this lineage.
            versions: List of (full_tool_id, version_string) tuples,
                     sorted from oldest to newest.
        """
        self.tool_id = tool_id
        self._versions = versions  # Already sorted
        self.tool_versions = SortedSet(
            [v for _, v in versions if v],
            key=parse_version,
        )

    @classmethod
    def from_index(
        cls,
        tool_id: str,
        tool_index: "ToolIndex",
    ) -> Optional["IndexToolLineage"]:
        """
        Create an IndexToolLineage from a ToolIndex.

        Args:
            tool_id: Any tool ID (full or versionless).
            tool_index: The ToolIndex to look up lineage data from.

        Returns:
            IndexToolLineage if found, None otherwise.
        """
        lineage_ids = tool_index.get_lineage_tool_ids(tool_id)
        if not lineage_ids:
            return None

        # Build versions list
        versions: List[Tuple[str, Optional[str]]] = []
        for lid in lineage_ids:
            entry = tool_index.entries.get(lid)
            if entry:
                versions.append((lid, entry.version))

        if not versions:
            return None

        # Get the versionless ID for this lineage
        versionless = remove_version_from_guid(lineage_ids[0])
        base_id = versionless if versionless else tool_id

        return cls(base_id, versions)

    @property
    def tool_ids(self) -> List[str]:
        """Return all tool IDs in this lineage."""
        return [tid for tid, _ in self._versions]

    def register_version(self, tool_version: str) -> None:
        """
        Register a new version in this lineage.

        Note: This is typically not called for IndexToolLineage since
        versions are pre-populated from the index.
        """
        if tool_version:
            self.tool_versions.add(tool_version)

    def get_versions(self) -> List[ToolLineageVersion]:
        """
        Return an ordered list of lineages (ToolLineageVersion) in this
        chain, from oldest to newest.
        """
        return [
            ToolLineageVersion(tool_id, version)
            for tool_id, version in self._versions
        ]

    def get_version_ids(self, reverse: bool = False) -> List[str]:
        """Return tool IDs in version order."""
        ids = self.tool_ids
        if reverse:
            return list(reversed(ids))
        return ids

    def to_dict(self) -> Dict[str, Any]:
        return dict(
            tool_id=self.tool_id,
            tool_versions=list(self.tool_versions),
            lineage_type="index",
        )
