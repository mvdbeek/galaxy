import re
from typing import (
    Dict,
    Optional,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from galaxy.util import ElementTree


def is_datasource(tool_xml):
    """Returns true if the tool is a datasource tool"""
    return tool_xml.getroot().attrib.get("tool_type", "") in ["data_source", "data_source_async"]


def is_valid_cheetah_placeholder(name):
    """Returns true if name is a valid Cheetah placeholder"""
    return re.match(r"^[a-zA-Z_]\w*$", name) is not None


def source_file_for_node(node, tool_source) -> Optional[str]:
    """Return the source file path for *node* in the post-expansion tree.

    Consults the ``_source_map`` stored on *tool_source* (populated when the
    tool was loaded via :func:`~galaxy.util.xml_macros.load_with_source_map`).
    Falls back to ``tool_source.source_path`` for main-file nodes.
    """
    source_map: Dict[str, str] = getattr(tool_source, "_source_map", {})
    if source_map:
        try:
            xpath = node.getroottree().getpath(node)
            src = source_map.get(xpath)
            if src:
                return src
        except Exception:
            pass
    return getattr(tool_source, "source_path", None)


def get_or_load_staged_tree(staged: Dict[str, "ElementTree"], path: str) -> "ElementTree":
    """Return the staged tree for *path*, loading (CDATA-preserving) on first access."""
    if path not in staged:
        from galaxy.util.xml_macros import raw_xml_tree

        staged[path] = raw_xml_tree(path, preserve_cdata=True)
    return staged[path]


def apply_staged(staged: Optional[Dict[str, "ElementTree"]], path: str, tree: "ElementTree") -> None:
    """Write *tree* to disk when *staged* is None (standalone fix call)."""
    if staged is None:
        tree.write(path, pretty_print=True, xml_declaration=True, encoding="UTF-8")
