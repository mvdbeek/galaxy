"""
Lazy ToolBox - On-demand tool loading with LRU caching.

This module provides a LazyToolBox that extends ToolBox but keeps only a
lightweight index in memory and loads full Tool objects on-demand with
LRU eviction.
"""

import logging
import os
import string
import threading
from typing import (
    Any,
    Dict,
    List,
    Optional,
    TYPE_CHECKING,
    Union,
)
from uuid import UUID

from cachetools import LRUCache

from galaxy.tool_source_store import (
    StoredToolSource,
    ToolSourceStore,
)
from galaxy.tool_source_store.index import (
    ToolIndex,
    ToolIndexEntry,
)
from galaxy.tool_util.parser import get_tool_source
from galaxy.tool_util.toolbox.base import DynamicToolConfDict
from galaxy.tool_util.toolbox.filters import FilterFactory
from galaxy.tool_util.toolbox.lineages import LineageMap
from galaxy.tool_util.toolbox.panel import (
    ToolPanelElements,
    ToolSection,
)
from galaxy.tool_util.toolbox.views.edam import (
    EdamPanelMode,
    EdamToolPanelView,
)
from galaxy.tool_util.toolbox.views.interface import (
    ToolPanelView,
    ToolPanelViewModel,
    ToolPanelViewModelType,
)
from galaxy.tool_util.toolbox.views.sources import StaticToolBoxViewSources
from galaxy.util import listify

from . import (
    create_tool_from_source,
    PersistentToolTagManager,
    ToolBox,
)

if TYPE_CHECKING:
    from galaxy.app import UniverseApplication
    from galaxy.model import User
    from galaxy.tools import Tool

log = logging.getLogger(__name__)


class LazyToolBox(ToolBox):
    """
    ToolBox that loads tools on-demand from the tool source store.

    Extends ToolBox but overrides initialization to avoid loading all tools
    at startup. Keeps a lightweight index in memory for API responses,
    but only loads full Tool objects when needed for execution or form building.
    """

    def __init__(
        self,
        config_filenames: List[str],
        tool_root_dir: str,
        app: "UniverseApplication",
        tool_source_store: ToolSourceStore,
        cache_size: int = 500,
        save_integrated_tool_panel: bool = True,
    ) -> None:
        """
        Initialize the lazy toolbox.

        Args:
            config_filenames: Tool configuration files (used for panel structure).
            tool_root_dir: Root directory for tools.
            app: Galaxy application instance.
            tool_source_store: The tool source store to load from.
            cache_size: Maximum number of Tool objects to cache in memory.
            save_integrated_tool_panel: Whether to save integrated tool panel.
        """
        # Store references before any initialization
        self._store = tool_source_store
        self._tool_object_cache: LRUCache = LRUCache(maxsize=cache_size)
        self._cache_lock = threading.RLock()
        self._reload_count = 0

        # Initialize core attributes that AbstractToolBox.__init__ would set
        # We do this manually to avoid loading all tools
        self._init_lazy_toolbox(
            config_filenames=config_filenames,
            tool_root_dir=tool_root_dir,
            app=app,
            save_integrated_tool_panel=save_integrated_tool_panel,
        )

        # Load tool index from store
        self._tool_index: Optional[ToolIndex] = None
        self._load_index_from_store()

        # Populate _tools_by_id with stub entries from index
        # This allows has_tool() and similar checks to work without loading
        self._populate_tool_registry_from_index()

        log.info(
            f"LazyToolBox initialized with {len(self._tools_by_id)} tools "
            f"(cache_size={cache_size})"
        )

    def _init_lazy_toolbox(
        self,
        config_filenames: List[str],
        tool_root_dir: str,
        app: "UniverseApplication",
        save_integrated_tool_panel: bool,
    ) -> None:
        """
        Initialize toolbox attributes without loading tools.

        This replicates the essential parts of AbstractToolBox.__init__
        without calling _init_tools_from_configs which loads all tools.
        """
        # From ToolBox.__init__
        from galaxy.tool_util.fetcher import ToolLocationFetcher

        self.tool_location_fetcher = ToolLocationFetcher()
        self._tools_loaded_from_store = 0
        self._tools_parsed_from_file = 0

        # From AbstractToolBox.__init__
        self._dynamic_tool_confs: List[DynamicToolConfDict] = []
        self._tools_by_id: Dict[str, "Tool"] = {}
        self._tools_by_uuid: Dict[UUID, "Tool"] = {}
        self._tool_versions_by_id: Dict[str, Dict[Union[str, None], "Tool"]] = {}
        self._tools_by_old_id: Dict[str, List["Tool"]] = {}
        self._workflows_by_id: Dict[str, Any] = {}
        self._tool_to_dict_cache: Dict[str, Dict[str, Any]] = {}
        self._tool_to_dict_cache_admin: Dict[str, Dict[str, Any]] = {}
        self._tool_panel = ToolPanelElements()
        self._index = 0
        self.data_manager_tools: Dict[str, "Tool"] = {}
        self._lineage_map = LineageMap(app)

        # Tool root dir handling from ToolBox
        if tool_root_dir == "./tools":
            tool_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "bundled"))
        self._tool_root_dir = tool_root_dir
        self.app = app

        # Initialize integrated tool panel (from ManagesIntegratedToolPanelMixin)
        self._init_integrated_tool_panel(app.config)

        # Watchers and filters
        self._tool_watcher = self.app.watchers.tool_watcher
        self._tool_config_watcher = self.app.watchers.tool_config_watcher
        self._filter_factory = FilterFactory(self)
        self._tool_tag_manager = self.tool_tag_manager()

        # Initialize panel views
        view_sources = StaticToolBoxViewSources(
            view_directories=app.config.panel_views_dir,
            view_dicts=app.config.panel_views,
        )
        # Note: AbstractToolBox uses name-mangled __default_panel_view
        self._AbstractToolBox__default_panel_view = app.config.default_panel_view
        self._setup_panel_views(view_sources)

        # Initialize dependency manager
        self._init_dependency_manager()

        # Load panel structure from config files (sections, labels)
        # but don't load the actual tools
        self._init_panel_structure_from_configs(config_filenames)

        # Load tool panel views (required for panel_has_tool checks)
        if self.app.name == "galaxy":
            self._load_tool_panel_views()

        if save_integrated_tool_panel:
            self._save_integrated_tool_panel()

    def _setup_panel_views(self, view_sources) -> None:
        """Set up tool panel views."""
        toolbox = self

        class DefaultToolPanelView(ToolPanelView):
            def apply_view(self, base_tool_panel, toolbox_registry):
                return toolbox._tool_panel

            def to_model(self) -> ToolPanelViewModel:
                return ToolPanelViewModel(
                    id="default",
                    name="Full Tool Panel",
                    description="Galaxy's fully configured toolbox panel.",
                    model_class="DefaultToolPanelView",
                    view_type=ToolPanelViewModelType.default_type,
                    searchable=True,
                )

        tool_panel_views_list: List[ToolPanelView] = [DefaultToolPanelView()]

        for edam_view in listify(self.app.config.edam_panel_views):
            mode = EdamPanelMode[edam_view]
            tool_panel_views_list.append(
                EdamToolPanelView(self.app.datatypes_registry.edam, mode=mode)
            )

        if view_sources is not None:
            from galaxy.tool_util.toolbox.views.static import StaticToolPanelView
            for definition in view_sources.get_definitions():
                tool_panel_views_list.append(StaticToolPanelView(definition))

        self._tool_panel_views = {}
        for tool_panel_view in tool_panel_views_list:
            self._tool_panel_views[tool_panel_view.to_model().id] = tool_panel_view

        self._tool_panel_view_rendered: Dict[str, ToolPanelElements] = {}

    def _init_panel_structure_from_configs(self, config_filenames: List[str]) -> None:
        """
        Load panel structure (sections, labels) from config files.

        This parses the tool configs to get the panel layout and builds
        a mapping of tool_id -> section info for use with the index.
        """
        from galaxy.tool_util.toolbox.parser import get_toolbox_parser

        # Map tool_id -> (section_id, section_name)
        self._tool_section_map: Dict[str, tuple] = {}

        config_filenames = listify(config_filenames)

        for config_filename in config_filenames:
            if not self.can_load_config_file(config_filename):
                continue
            try:
                tool_conf_source = get_toolbox_parser(config_filename)
                tool_path = tool_conf_source.parse_tool_path()
                if not tool_path:
                    tool_path = self._tool_root_dir
                else:
                    tool_conf_dir = os.path.dirname(config_filename)
                    tool_path_vars = {"tool_conf_dir": tool_conf_dir}
                    tool_path = string.Template(tool_path).safe_substitute(tool_path_vars)

                parsing_shed_tool_conf = tool_conf_source.is_shed_tool_conf()

                for item in tool_conf_source.parse_items():
                    try:
                        item_type = getattr(item, 'type', None)
                        if item_type == "section":
                            section_id = item.get("id")
                            section_name = item.get("name", section_id)
                            section_dict = {
                                "id": section_id,
                                "name": section_name,
                                "version": item.get("version", ""),
                            }
                            if section_id and section_id not in self._tool_panel:
                                section = ToolSection(section_dict)
                                self._tool_panel.append_section(section_id, section)

                            # Extract tools in this section
                            if section_id:
                                self._extract_tools_from_section(item, section_id, section_name, tool_path)

                        elif item_type == "label":
                            label_id = item.get("id")
                            label_text = item.get("text", "")
                            if label_id and label_id not in self._tool_panel:
                                from galaxy.tool_util.toolbox.panel import ToolSectionLabel
                                label = ToolSectionLabel({"id": label_id, "text": label_text})
                                self._tool_panel[f"label_{label_id}"] = label

                        elif item_type == "tool":
                            # Tool at root level (no section)
                            tool_id = self._extract_tool_id_from_item(item, tool_path)
                            if tool_id:
                                self._tool_section_map[tool_id] = (None, None)
                    except Exception as e:
                        log.debug(f"Error processing item in {config_filename}: {e}")

                if parsing_shed_tool_conf:
                    if os.access(config_filename, os.W_OK):
                        shed_tool_conf_dict = dict(
                            config_filename=config_filename,
                            tool_path=tool_path,
                            config_elems=[],
                        )
                        self._dynamic_tool_confs.append(shed_tool_conf_dict)

            except FileNotFoundError:
                log.debug(f"Tool config file not found: {config_filename}")
            except Exception as e:
                log.warning(f"Error parsing tool config {config_filename}: {e}")

        log.info(f"Built tool section map with {len(self._tool_section_map)} entries")
        # Log some sample entries for debugging
        sample_entries = list(self._tool_section_map.items())[:5]
        for tool_id, (section_id, section_name) in sample_entries:
            log.debug(f"  Section map sample: {tool_id} -> {section_id}")

    def _extract_tools_from_section(self, section_item, section_id: str, section_name: str, tool_path: str) -> None:
        """Extract tool IDs from a section and add to section map."""
        if not hasattr(section_item, 'items'):
            return

        for sub_item in section_item.items:
            try:
                item_type = getattr(sub_item, 'type', None)
                if item_type == "tool":
                    tool_id = self._extract_tool_id_from_item(sub_item, tool_path)
                    if tool_id:
                        self._tool_section_map[tool_id] = (section_id, section_name)
            except Exception as e:
                log.debug(f"Error extracting tool from section {section_id}: {e}")

    def _extract_tool_id_from_item(self, item, tool_path: str) -> Optional[str]:
        """Extract tool ID from a tool item - either from guid or by parsing the file."""
        # For shed tools, use the guid directly
        guid = item.get("guid")
        if guid:
            return guid

        # For regular tools, we need to get the ID from the file attribute
        # and optionally parse the tool XML to get the actual ID
        tool_file = item.get("file")
        if not tool_file:
            return None

        # Try to extract tool ID from file path or by quick parsing
        tool_path_full = os.path.join(tool_path, tool_file)
        try:
            # Quick regex extraction of tool ID from XML
            import re
            with open(tool_path_full, 'r') as f:
                content = f.read(2000)
            match = re.search(r'<tool[^>]+id=["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
        except Exception:
            pass

        # Fall back to using filename without extension as ID hint
        return os.path.splitext(os.path.basename(tool_file))[0]

    def _load_index_from_store(self) -> None:
        """Load the tool index from store."""
        log.debug("Loading tool index from store...")
        self._tool_index = self._store.load_index()

        if self._tool_index is None or len(self._tool_index.entries) == 0:
            # Check if store has tools but index is missing/empty
            stored_hashes = list(self._store.list_all())
            if stored_hashes:
                log.info(f"Index empty but store has {len(stored_hashes)} tools - rebuilding index...")
                self._rebuild_index_from_store(stored_hashes)
            else:
                log.info("No tool index found in store and store is empty")
                self._tool_index = ToolIndex()
        else:
            log.info(f"Loaded tool index with {len(self._tool_index.entries)} entries")

    def _rebuild_index_from_store(self, stored_hashes: List[str]) -> None:
        """Rebuild the index from stored tool sources."""
        import hashlib
        from datetime import datetime

        entries: Dict[str, ToolIndexEntry] = {}

        for source_hash in stored_hashes:
            stored = self._store.get(source_hash)
            if stored:
                try:
                    entry = self._build_index_entry_from_stored(stored)
                    if entry and entry.id:
                        entries[entry.id] = entry
                except Exception as e:
                    log.warning(f"Error building index entry for {source_hash}: {e}")

        self._tool_index = ToolIndex(
            entries=entries,
            by_section={},
            version=hashlib.md5(str(sorted(entries.keys())).encode()).hexdigest()[:8],
            built_at=datetime.utcnow(),
        )

        # Save the rebuilt index
        try:
            self._store.store_index(self._tool_index)
            log.info(f"Rebuilt and saved tool index with {len(entries)} entries")
        except Exception as e:
            log.warning(f"Could not save rebuilt index: {e}")

    def _build_index_entry_from_stored(self, stored: StoredToolSource) -> Optional[ToolIndexEntry]:
        """Build an index entry from a stored tool source."""
        from datetime import datetime

        try:
            tool_source = get_tool_source(
                raw_tool_source=stored.raw_source,
                tool_source_class=stored.tool_source_class,
            )

            tool_id = tool_source.parse_id() or stored.tool_id
            if not tool_id:
                return None

            # Safely get optional attributes
            uuid_val = None
            if hasattr(tool_source, "parse_uuid"):
                try:
                    parsed_uuid = tool_source.parse_uuid()
                    uuid_val = str(parsed_uuid) if parsed_uuid else None
                except Exception:
                    pass

            hidden = False
            if hasattr(tool_source, "parse_hidden"):
                try:
                    hidden = tool_source.parse_hidden()
                except Exception:
                    pass

            return ToolIndexEntry(
                id=tool_id,
                uuid=uuid_val,
                version=tool_source.parse_version(),
                name=tool_source.parse_name() or "",
                description=tool_source.parse_description() or "",
                source_hash=stored.hash,
                source_class=stored.tool_source_class,
                hidden=hidden,
                indexed_at=datetime.utcnow(),
            )
        except Exception as e:
            log.debug(f"Error parsing tool source for index: {e}")
            return None

    def _populate_tool_registry_from_index(self) -> None:
        """
        Populate _tools_by_id with None placeholders from index.

        This allows has_tool() checks to work without loading Tool objects.
        The actual Tool objects are loaded on-demand in get_tool().
        """
        if self._tool_index is None:
            return

        # Update index entries with section info from tool_conf.xml
        # Build reverse map: short_id -> section_info for faster lookup
        if hasattr(self, "_tool_section_map"):
            short_id_to_section: Dict[str, tuple] = {}
            for map_tool_id, section_info in self._tool_section_map.items():
                # Store exact ID
                short_id_to_section[map_tool_id] = section_info
                # For guids, also store the short tool ID
                if "/" in map_tool_id:
                    parts = map_tool_id.split("/")
                    if len(parts) >= 2:
                        # Short ID is second-to-last part (before version)
                        short_id = parts[-2]
                        if short_id not in short_id_to_section:
                            short_id_to_section[short_id] = section_info
        else:
            short_id_to_section = {}

        section_updates = 0
        for tool_id, entry in self._tool_index.entries.items():
            section_info = None

            # Try exact match first
            if tool_id in short_id_to_section:
                section_info = short_id_to_section[tool_id]

            if section_info:
                section_id, section_name = section_info
                if section_id and not entry.panel_section_id:
                    entry.panel_section_id = section_id
                    entry.panel_section_name = section_name
                    section_updates += 1

            # Store None as placeholder - actual Tool loaded on demand
            self._tools_by_id[tool_id] = None  # type: ignore[assignment]

            # Initialize version tracking
            if tool_id not in self._tool_versions_by_id:
                self._tool_versions_by_id[tool_id] = {}
            if entry.version:
                self._tool_versions_by_id[tool_id][entry.version] = None  # type: ignore[assignment]

            # Add to panel if section info available
            if entry.panel_section_id and entry.panel_section_id in self._tool_panel:
                section = self._tool_panel[entry.panel_section_id]
                if isinstance(section, ToolSection):
                    self._tool_panel.record_section_for_tool_id(
                        tool_id, entry.panel_section_id, section.name or ""
                    )

        # Debug: check for mismatches
        index_ids = set(self._tool_index.entries.keys()) if self._tool_index else set()
        map_ids = set(self._tool_section_map.keys()) if hasattr(self, "_tool_section_map") else set()
        matched = index_ids & map_ids
        log.info(f"Section map has {len(map_ids)} entries, index has {len(index_ids)} entries, {len(matched)} matched, {section_updates} updated")
        if map_ids and index_ids:
            # Show sample IDs from each for comparison
            log.info(f"  Sample index IDs: {list(index_ids)[:3]}")
            log.info(f"  Sample map IDs: {list(map_ids)[:3]}")

    # === Override get_tool for lazy loading ===

    def get_tool(
        self,
        tool_id: Optional[str] = None,
        tool_version: Optional[str] = None,
        tool_uuid: Optional[Union[UUID, str]] = None,
        get_all_versions: Optional[bool] = False,
        exact: Optional[bool] = False,
        user: Optional["User"] = None,
    ) -> Union[Optional["Tool"], List["Tool"]]:
        """
        Get a tool, loading from store on-demand if needed.

        Overrides ToolBox.get_tool to implement lazy loading.
        """
        from galaxy.exceptions import ObjectNotFound, RequestParameterInvalidException

        if tool_id is None and tool_uuid is None:
            raise RequestParameterInvalidException(
                "get_tool cannot be called with both tool_id and tool_uuid as None"
            )

        # Handle UUID lookup
        if tool_uuid:
            if user:
                unprivileged_tool = self.get_unprivileged_tool_or_none(user, tool_uuid=tool_uuid)
                if unprivileged_tool:
                    return unprivileged_tool
            tool_uuid = tool_uuid if isinstance(tool_uuid, UUID) else UUID(tool_uuid)
            tool_from_uuid = self._get_tool_by_uuid(tool_uuid)
            if tool_from_uuid is None:
                raise ObjectNotFound(f"Failed to find a tool with uuid [{tool_uuid}]")
            tool_id = tool_from_uuid.id

        assert tool_id

        if tool_version:
            tool_version = str(tool_version)

        if get_all_versions and exact:
            raise RequestParameterInvalidException(
                "get_tool cannot be called with both get_all_versions and exact as True"
            )

        # Check if we have this tool in our index
        if self._tool_index and tool_id in self._tool_index.entries:
            tool = self._load_tool_on_demand(tool_id, tool_version)
            if tool:
                if get_all_versions:
                    return [tool]  # TODO: support multiple versions
                return tool

        # Fall back to parent implementation for tools not in our index
        # (dynamic tools, data manager tools, etc.)
        return super().get_tool(
            tool_id=tool_id,
            tool_version=tool_version,
            tool_uuid=tool_uuid,
            get_all_versions=get_all_versions,
            exact=exact,
            user=user,
        )

    def _load_tool_on_demand(
        self, tool_id: str, tool_version: Optional[str] = None
    ) -> Optional["Tool"]:
        """
        Load a tool from the store on-demand.

        Uses LRU cache to avoid reloading frequently used tools.
        """
        cache_key = f"{tool_id}:{tool_version or 'latest'}"

        # Check cache first
        with self._cache_lock:
            if cache_key in self._tool_object_cache:
                return self._tool_object_cache[cache_key]

        # Check if already loaded in _tools_by_id
        existing = self._tools_by_id.get(tool_id)
        if existing is not None:
            with self._cache_lock:
                self._tool_object_cache[cache_key] = existing
            return existing

        # Get entry from index
        if self._tool_index is None:
            return None

        entry = self._tool_index.get(tool_id)
        if not entry:
            return None

        # Load source from store
        stored = self._store.get(entry.source_hash)
        if not stored:
            log.warning(f"Tool source not found for {tool_id} (hash: {entry.source_hash})")
            return None

        # Create Tool object
        try:
            tool = self._create_tool_from_stored_source(stored)
            log.debug(f"Lazy-loaded tool: {tool_id}")
        except Exception as e:
            log.error(f"Error creating tool {tool_id}: {e}")
            return None

        # Register the tool
        self._register_loaded_tool(tool)

        # Add to cache
        with self._cache_lock:
            self._tool_object_cache[cache_key] = tool

        return tool

    def _create_tool_from_stored_source(self, stored: StoredToolSource) -> "Tool":
        """Create a Tool object from stored source."""
        tool_source = get_tool_source(
            raw_tool_source=stored.raw_source,
            tool_source_class=stored.tool_source_class,
        )
        return create_tool_from_source(
            self.app,
            tool_source,
            tool_dir=stored.tool_dir,
        )

    def _register_loaded_tool(self, tool: "Tool") -> None:
        """Register a lazily-loaded tool in the toolbox registries."""
        tool_id = tool.id
        if not tool_id:
            return

        self._tools_by_id[tool_id] = tool

        version = tool.version
        if tool_id not in self._tool_versions_by_id:
            self._tool_versions_by_id[tool_id] = {}
        self._tool_versions_by_id[tool_id][version] = tool

        # Tool uses 'guid' not 'uuid'
        if hasattr(tool, "uuid") and tool.uuid:
            self._tools_by_uuid[tool.uuid] = tool

        # Update lineage
        self._lineage_map.register(tool)

    # === Override has_tool to check index ===

    def has_tool(
        self,
        tool_id: Optional[str],
        tool_version: Optional[str] = None,
        tool_uuid: Optional[Union[UUID, str]] = None,
        exact: bool = False,
        user: Optional["User"] = None,
    ) -> bool:
        """Check if tool exists, using index for fast lookup."""
        if tool_id and self._tool_index and tool_id in self._tool_index.entries:
            return True
        # Fall back to parent for UUID lookups and edge cases
        return super().has_tool(
            tool_id=tool_id,
            tool_version=tool_version,
            tool_uuid=tool_uuid,
            exact=exact,
            user=user,
        )

    # === Override tools() to iterate loaded tools ===

    def tools(self):
        """
        Return loaded tools.

        Note: This only returns tools that have been loaded on-demand.
        For a full list, use the index.
        """
        return {
            k: v for k, v in self._tools_by_id.items() if v is not None
        }.items()

    # === Index access methods ===

    @property
    def tool_index(self) -> Optional[ToolIndex]:
        """Get the tool index."""
        return self._tool_index

    def get_tool_ids(self) -> List[str]:
        """Get all tool IDs from index."""
        if self._tool_index:
            return list(self._tool_index.entries.keys())
        return []

    def get_index_entry(self, tool_id: str) -> Optional[ToolIndexEntry]:
        """Get index entry for a tool without loading it."""
        if self._tool_index:
            return self._tool_index.get(tool_id)
        return None

    # === Cache management ===

    def cache_stats(self) -> Dict[str, Any]:
        """Return cache statistics."""
        return {
            "tool_cache_size": len(self._tool_object_cache),
            "tool_cache_maxsize": self._tool_object_cache.maxsize,
            "tools_loaded": sum(1 for v in self._tools_by_id.values() if v is not None),
            "tools_indexed": len(self._tool_index.entries) if self._tool_index else 0,
        }

    def clear_tool_cache(self) -> None:
        """Clear the tool object cache."""
        with self._cache_lock:
            self._tool_object_cache.clear()

    def evict_tool_from_cache(self, tool_id: str) -> None:
        """Evict a specific tool from cache."""
        with self._cache_lock:
            keys_to_remove = [
                k for k in self._tool_object_cache if k.startswith(f"{tool_id}:")
            ]
            for key in keys_to_remove:
                del self._tool_object_cache[key]

    # === Required property overrides ===

    @property
    def all_requirements(self):
        """Get all tool requirements from index (no tool loading needed)."""
        if self._tool_index:
            requirements = set()
            for entry in self._tool_index.entries.values():
                for req in entry.requirements:
                    # Convert dict to hashable tuple
                    req_tuple = (req.get("name"), req.get("version"), req.get("type"))
                    requirements.add(req_tuple)
            return [
                {"name": r[0], "version": r[1], "type": r[2]}
                for r in requirements
                if r[0]  # Filter out empty names
            ]
        return []

    # === Override to_dict for API responses ===

    def to_dict(
        self, trans, in_panel: bool = True, tool_help: bool = False, view: Optional[str] = None, **kwds
    ) -> List[Dict[str, Any]]:
        """
        Create a dictionary representation of the toolbox.

        For LazyToolBox, this returns lightweight data directly from the index
        without loading full Tool objects. This is much faster and uses less memory.

        Note: tool_help is ignored since we don't load the full tool.
        """
        if self._tool_index is None:
            return []

        rval = []

        # Return data directly from index - no tool loading needed!
        for tool_id, entry in self._tool_index.entries.items():
            # Skip hidden tools unless requested
            if entry.hidden and not kwds.get("include_hidden", False):
                continue

            # Convert index entry to API dict format
            tool_dict = self._index_entry_to_api_dict(entry)
            rval.append(tool_dict)

        log.debug(f"LazyToolBox.to_dict: returning {len(rval)} tools from index (no loading)")
        return rval

    def _index_entry_to_api_dict(self, entry: ToolIndexEntry) -> Dict[str, Any]:
        """Convert an index entry to the format expected by /api/tools."""
        return {
            "id": entry.id,
            "name": entry.name,
            "version": entry.version,
            "description": entry.description,
            "labels": entry.labels if entry.labels else [],
            "edam_operations": entry.edam_operations if entry.edam_operations else [],
            "edam_topics": entry.edam_topics if entry.edam_topics else [],
            "hidden": entry.hidden,
            "model_class": "Tool",
            "panel_section_id": entry.panel_section_id,
            "panel_section_name": entry.panel_section_name,
            # Minimal fields that indicate this is from index
            "link": f"/api/tools/{entry.id}",
            "min_width": -1,
            "target": "galaxy_main",
        }

    def to_panel_view(self, trans, view="default_panel_view", **kwds) -> Dict[str, Dict]:
        """
        Create a panel view representation of the toolbox.

        For LazyToolBox, returns tools from index organized by section.
        """
        if self._tool_index is None:
            return {}

        view_contents: Dict[str, Dict] = {}

        # Group tools by section from index
        sections: Dict[str, Dict[str, Any]] = {}
        uncategorized_tools: List[Dict[str, Any]] = []

        for tool_id, entry in self._tool_index.entries.items():
            if entry.hidden and not kwds.get("include_hidden", False):
                continue

            tool_dict = self._index_entry_to_api_dict(entry)

            section_id = entry.panel_section_id
            if section_id:
                if section_id not in sections:
                    sections[section_id] = {
                        "id": section_id,
                        "name": entry.panel_section_name or section_id,
                        "model_class": "ToolSection",
                        "elems": [],
                    }
                sections[section_id]["elems"].append(tool_dict)
            else:
                uncategorized_tools.append(tool_dict)

        # Add sections to view_contents
        for section_id, section_dict in sections.items():
            view_contents[section_id] = section_dict

        # Add uncategorized tools directly
        for tool_dict in uncategorized_tools:
            view_contents[tool_dict["id"]] = tool_dict

        return view_contents
