from typing import (
    Callable,
    Dict,
    Iterable,
    Optional,
    TYPE_CHECKING,
)

from galaxy.util.tool_version import remove_version_from_guid
from .interface import ToolLineage

if TYPE_CHECKING:
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
    """Lineage map that derives versions from a callable on first access.

    Used by ``galaxy.tools.lazy_toolbox.LazyToolBox`` so the lineage view
    over ``ToolIndex.entries_by_version`` doesn't need a boot-time pass to
    seed every tool's version set into ``ToolLineage.tool_versions``.
    Lineage data is already serialised inside the index
    (``ToolIndex.to_dict``); this class just exposes it as a ``LineageMap``
    on demand.
    """

    def __init__(self, app, versions_for: Optional[Callable[[str], Iterable[str]]] = None):
        super().__init__(app)
        self._versions_for = versions_for

    def get(self, tool_id: str) -> Optional[ToolLineage]:
        # Always source versions from the index when available — the parent's
        # fallback path builds a lineage from a single ``Tool`` object's
        # version (via ``ToolLineage.from_tool``) and memoises it, which
        # would freeze ``tool_versions`` at ``[just-loaded version]`` and
        # hide every other version present in the index. That breaks
        # ``get_safe_version`` (used by ``ToolModule.__init__`` at workflow
        # upload to map a pinned-but-missing tool_version onto the nearest
        # safe-upgrade version, e.g. ``__BUILD_LIST__`` 1.0.0 → 1.1.0): it
        # walks ``tool.lineage.tool_versions`` and only finds candidates
        # within ``WORKFLOW_SAFE_TOOL_VERSION_UPDATES``' bounds, so a
        # one-element ``[1.2.0]`` lineage misses 1.1.0 and the workflow
        # ends up bound to 1.2.0 with state shaped for 1.0.0.
        if self._versions_for is not None:
            try:
                versions = list(self._versions_for(tool_id))
            except Exception:
                versions = []
            if versions:
                lineage = self.lineage_map.get(tool_id)
                if lineage is None:
                    lineage = ToolLineage(tool_id)
                    self.lineage_map[tool_id] = lineage
                    versionless = remove_version_from_guid(tool_id)
                    if versionless and versionless not in self.lineage_map:
                        self.lineage_map[versionless] = lineage
                for version in versions:
                    if version:
                        lineage.register_version(version)
                return lineage
        # Index has no entry for this tool_id — fall back to whatever the
        # parent class can derive (a registered Tool, etc.).
        return super().get(tool_id)


__all__ = ("LazyLineageMap", "LineageMap")
