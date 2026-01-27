"""
Tool discovery utilities.

This module provides functions to discover tool files from Galaxy's tool configuration
without requiring a full ToolBox initialization. It can be used by scripts and the
ToolBox itself to find all tool XML/YAML files.
"""

import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import (
    Iterable,
    Iterator,
    List,
    Optional,
    TYPE_CHECKING,
)

from .parser import (
    get_toolbox_parser,
    ToolConfItem,
    ToolConfSection,
)

if TYPE_CHECKING:
    from galaxy.config import GalaxyAppConfiguration

log = logging.getLogger(__name__)


@dataclass
class DiscoveredTool:
    """Information about a discovered tool file."""

    path: str  # Absolute path to tool file
    tool_conf: str  # Path to the tool_conf file that referenced this tool
    tool_path: Optional[str]  # The tool_path from the tool_conf
    guid: Optional[str] = None  # GUID for shed tools
    is_shed_tool: bool = False


def get_tool_configs(config: "GalaxyAppConfiguration") -> List[str]:
    """
    Get all tool configuration file paths from Galaxy config.

    Args:
        config: Galaxy configuration object.

    Returns:
        List of tool configuration file paths (tool_conf.xml, shed_tool_conf.xml, etc.)
    """
    configs = []

    # Get main tool config files
    if hasattr(config, "tool_configs") and config.tool_configs:
        configs.extend(config.tool_configs)

    # Ensure shed_tool_config_file is included if not already
    if hasattr(config, "shed_tool_config_file") and config.shed_tool_config_file:
        if config.shed_tool_config_file not in configs:
            configs.append(config.shed_tool_config_file)

    # Include migrated_tools_config if present
    if hasattr(config, "migrated_tools_config") and config.migrated_tools_config:
        if config.migrated_tools_config not in configs:
            configs.append(config.migrated_tools_config)

    return configs


def _resolve_tool_path(tool_path: Optional[str], config_filename: str, root_dir: Optional[str] = None) -> str:
    """
    Resolve the tool_path to an absolute directory path.

    Args:
        tool_path: The tool_path from the tool_conf, may be None or relative.
        config_filename: The path to the tool_conf file.
        root_dir: Optional Galaxy root directory.

    Returns:
        Absolute path to the tool directory.
    """
    if tool_path is None:
        # Default to 'tools' relative to Galaxy root or config dir
        if root_dir:
            return os.path.join(root_dir, "tools")
        config_dir = os.path.dirname(os.path.abspath(config_filename))
        # Assume config is in config/ dir, tools is at same level
        return os.path.join(os.path.dirname(config_dir), "tools")

    if os.path.isabs(tool_path):
        return tool_path

    # tool_path is relative - resolve relative to config file location
    config_dir = os.path.dirname(os.path.abspath(config_filename))
    return os.path.abspath(os.path.join(config_dir, tool_path))


def _iter_tool_items(items: Iterable[ToolConfItem]) -> Iterator[ToolConfItem]:
    """
    Recursively iterate over all tool items, including those in sections.

    Args:
        items: Iterable of ToolConfItem objects.

    Yields:
        ToolConfItem objects of type 'tool'.
    """
    for item in items:
        if item.type == "tool":
            yield item
        elif isinstance(item, ToolConfSection):
            yield from _iter_tool_items(item.items)


def discover_tools_from_config(
    config_filename: str,
    root_dir: Optional[str] = None,
) -> Iterator[DiscoveredTool]:
    """
    Discover all tools from a single tool configuration file.

    Args:
        config_filename: Path to a tool_conf.xml or similar file.
        root_dir: Optional Galaxy root directory for resolving relative paths.

    Yields:
        DiscoveredTool objects for each tool found.
    """
    if not os.path.exists(config_filename):
        log.debug(f"Tool config file does not exist: {config_filename}")
        return

    try:
        tool_conf_source = get_toolbox_parser(config_filename)
    except Exception as e:
        log.warning(f"Failed to parse tool config {config_filename}: {e}")
        return

    tool_path = tool_conf_source.parse_tool_path()
    resolved_tool_path = _resolve_tool_path(tool_path, config_filename, root_dir)
    is_shed_conf = tool_conf_source.is_shed_tool_conf()

    for item in _iter_tool_items(tool_conf_source.parse_items()):
        tool_file = item.get("file")
        if not tool_file:
            continue

        # Resolve tool file path
        if os.path.isabs(tool_file):
            tool_path_abs = tool_file
        else:
            tool_path_abs = os.path.join(resolved_tool_path, tool_file)

        # Normalize path
        tool_path_abs = os.path.normpath(tool_path_abs)

        if not os.path.exists(tool_path_abs):
            log.debug(f"Tool file does not exist: {tool_path_abs}")
            continue

        yield DiscoveredTool(
            path=tool_path_abs,
            tool_conf=config_filename,
            tool_path=resolved_tool_path,
            guid=item.get("guid"),
            is_shed_tool=is_shed_conf,
        )


def discover_tools(
    config: "GalaxyAppConfiguration",
    include_bundled: bool = True,
) -> Iterator[DiscoveredTool]:
    """
    Discover all tools from Galaxy configuration.

    This reads all tool configuration files and yields information about
    each discovered tool file.

    Args:
        config: Galaxy configuration object.
        include_bundled: Whether to include bundled tools from lib/galaxy/tools/bundled.

    Yields:
        DiscoveredTool objects for each tool found.
    """
    root_dir = getattr(config, "root", None)
    seen_paths: set = set()

    # Discover from all tool config files
    for config_filename in get_tool_configs(config):
        for tool in discover_tools_from_config(config_filename, root_dir):
            if tool.path not in seen_paths:
                seen_paths.add(tool.path)
                yield tool

    # Include bundled tools if requested
    if include_bundled and root_dir:
        bundled_dir = Path(root_dir) / "lib" / "galaxy" / "tools" / "bundled"
        if bundled_dir.exists():
            for xml_file in bundled_dir.rglob("*.xml"):
                path_str = str(xml_file)
                # Skip macro files and already-seen files
                if path_str in seen_paths:
                    continue
                if "macro" in xml_file.name.lower():
                    continue
                # Quick check if it's a tool file
                try:
                    with open(xml_file) as f:
                        content = f.read(500)  # Read just enough to check
                    if "<tool" in content:
                        seen_paths.add(path_str)
                        yield DiscoveredTool(
                            path=path_str,
                            tool_conf="bundled",
                            tool_path=str(bundled_dir),
                            is_shed_tool=False,
                        )
                except Exception:
                    pass


def discover_tool_files(
    config: "GalaxyAppConfiguration",
    include_bundled: bool = True,
) -> List[str]:
    """
    Get a list of all tool file paths from Galaxy configuration.

    This is a convenience function that returns just the paths.

    Args:
        config: Galaxy configuration object.
        include_bundled: Whether to include bundled tools.

    Returns:
        List of absolute paths to tool files.
    """
    return [tool.path for tool in discover_tools(config, include_bundled)]


__all__ = (
    "DiscoveredTool",
    "discover_tools",
    "discover_tools_from_config",
    "discover_tool_files",
    "get_tool_configs",
)
