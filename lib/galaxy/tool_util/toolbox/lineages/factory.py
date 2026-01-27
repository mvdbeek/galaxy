from typing import (
    Dict,
    Optional,
    TYPE_CHECKING,
    Union,
)

from galaxy.util.tool_version import remove_version_from_guid

from .interface import (
    IndexToolLineage,
    ToolLineage,
)

if TYPE_CHECKING:
    from galaxy.tool_source_store.index import ToolIndex
    from galaxy.tools import Tool


class LineageMap:
    """Map each unique tool id to a lineage object."""

    def __init__(self, app):
        self.lineage_map: Dict[str, ToolLineage] = {}
        self.app = app

    def register(self, tool: "Tool") -> ToolLineage:
        tool_id = tool.id
        assert tool_id
        versionless_tool_id = remove_version_from_guid(tool_id)
        lineage: ToolLineage
        if versionless_tool_id not in self.lineage_map:
            lineage = ToolLineage.from_tool(tool)
        else:
            lineage = self.lineage_map[versionless_tool_id]
            # A lineage for a tool with the same versionless_tool_id exists,
            # but this lineage may not have the current tools' version,
            # so we add tool.version to the lineage
            lineage.register_version(tool.version)
        if versionless_tool_id and versionless_tool_id not in self.lineage_map:
            self.lineage_map[versionless_tool_id] = lineage
        if tool_id not in self.lineage_map:
            self.lineage_map[tool_id] = lineage
        return self.lineage_map[tool_id]

    def get(self, tool_id: str) -> Optional[ToolLineage]:
        """
        Get lineage for `tool_id`.

        By preference the lineage for a version-agnostic tool_id is returned.
        Falls back to fetching the lineage only when this fails.
        This happens when the tool_id does not contain a version.
        """
        lineage = self._get_versionless(tool_id)
        if lineage:
            return lineage
        if tool_id not in self.lineage_map:
            toolbox = None
            try:
                toolbox = self.app.toolbox
            except AttributeError:
                # We're building the lineage map while building the toolbox,
                # so app.toolbox may not be available.
                # TODO: is the fallback really needed / can it be fixed by improving _get_versionless ?
                pass
            tool = toolbox and toolbox._tools_by_id.get(tool_id)
            if tool:
                lineage = ToolLineage.from_tool(tool)
                self.lineage_map[tool_id] = lineage
        return self.lineage_map.get(tool_id)

    def _get_versionless(self, tool_id: str) -> Optional[ToolLineage]:
        versionless_tool_id = remove_version_from_guid(tool_id)
        if not versionless_tool_id:
            return None
        return self.lineage_map.get(versionless_tool_id)


class LazyLineageMap(LineageMap):
    """
    LineageMap that uses index data for unloaded tools.

    Extends LineageMap to support lazy-loaded toolboxes. When a lineage
    is requested for a tool that hasn't been loaded yet, falls back to
    creating an IndexToolLineage from the tool index.
    """

    def __init__(self, app, tool_index: Optional["ToolIndex"] = None):
        super().__init__(app)
        self._tool_index = tool_index
        self._index_lineages: Dict[str, IndexToolLineage] = {}

    def set_tool_index(self, tool_index: "ToolIndex") -> None:
        """Set or update the tool index."""
        self._tool_index = tool_index
        self._index_lineages.clear()  # Clear cached index lineages

    def get(self, tool_id: str) -> Optional[Union[ToolLineage, IndexToolLineage]]:
        """
        Get lineage for `tool_id`.

        First tries the regular lineage map (for loaded tools),
        then falls back to index-based lineage for unloaded tools.
        """
        # Try regular lineage first (for loaded tools)
        lineage = super().get(tool_id)
        if lineage is not None:
            return lineage

        # Fall back to index-based lineage
        return self._get_index_lineage(tool_id)

    def _get_index_lineage(self, tool_id: str) -> Optional[IndexToolLineage]:
        """Get or create an IndexToolLineage for the given tool ID."""
        if self._tool_index is None:
            return None

        # Check cache first
        versionless = remove_version_from_guid(tool_id)
        cache_key = versionless if versionless else tool_id

        if cache_key in self._index_lineages:
            return self._index_lineages[cache_key]

        # Create from index
        lineage = IndexToolLineage.from_index(tool_id, self._tool_index)
        if lineage:
            self._index_lineages[cache_key] = lineage
            # Also cache by full tool_id for faster subsequent lookups
            if tool_id != cache_key:
                self._index_lineages[tool_id] = lineage

        return lineage

    def get_lineage_tool_ids(self, tool_id: str) -> list[str]:
        """
        Get all tool IDs in the lineage for the given tool.

        Returns tool IDs from both loaded tools and the index.
        """
        lineage = self.get(tool_id)
        if lineage:
            return lineage.tool_ids
        return []

    def has_lineage(self, tool_id: str) -> bool:
        """Check if a lineage exists for the given tool ID."""
        return self.get(tool_id) is not None


__all__ = ("LazyLineageMap", "LineageMap")
