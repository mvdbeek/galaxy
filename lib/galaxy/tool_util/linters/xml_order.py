"""This module contains a linter for tool XML block order.

For more information on the IUC standard for XML block order see -
https://github.com/galaxy-iuc/standards.
"""

from typing import (
    Dict,
    Optional,
    TYPE_CHECKING,
)

from galaxy.tool_util.lint import Linter
from ._util import (
    apply_staged,
    get_or_load_staged_tree,
    is_datasource,
    source_file_for_node,
)

if TYPE_CHECKING:
    from galaxy.tool_util.lint import LintContext
    from galaxy.tool_util.parser.interface import ToolSource
    from galaxy.util import ElementTree

# https://github.com/galaxy-iuc/standards
# https://github.com/galaxy-iuc/standards/pull/7/files
TAG_ORDER = [
    "description",
    "macros",
    "options",
    "edam_topics",
    "edam_operations",
    "xrefs",
    "parallelism",
    "requirements",
    "required_files",
    "code",
    "stdio",
    "version_command",
    "command",
    "environment_variables",
    "configfiles",
    "inputs",
    "outputs",
    "tests",
    "help",
    "citations",
]

DATASOURCE_TAG_ORDER = [
    "description",
    "macros",
    "requirements",
    "command",
    "configfiles",
    "inputs",
    "request_param_translation",
    "uihints",
    "outputs",
    "options",
    "help",
    "citations",
]


class XMLOrder(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml = getattr(tool_source, "xml_tree", None)
        if not tool_xml:
            return
        tool_root = tool_xml.getroot()

        if is_datasource(tool_xml):
            tag_ordering = DATASOURCE_TAG_ORDER
        else:
            tag_ordering = TAG_ORDER
        last_tag = None
        last_key: Optional[int] = None
        for elem in tool_root:
            tag = elem.tag
            if tag not in tag_ordering:
                continue
            key = tag_ordering.index(tag)
            if last_key:
                if last_key > key:
                    lint_ctx.warn(
                        f"Best practice violation [{tag}] elements should come before [{last_tag}]",
                        linter=cls.name(),
                        node=elem,
                    )
            last_tag = tag
            last_key = key

    @classmethod
    def fix(
        cls,
        tool_source: "ToolSource",
        lint_ctx: "LintContext",
        staged: Optional[Dict[str, "ElementTree"]] = None,
    ) -> bool:
        tool_xml = getattr(tool_source, "xml_tree", None)
        if not tool_xml:
            return False
        tag_ordering = DATASOURCE_TAG_ORDER if is_datasource(tool_xml) else TAG_ORDER
        tool_root = tool_xml.getroot()

        # Check if reordering is needed.
        ordered_tags = [c.tag for c in tool_root if c.tag in tag_ordering]
        expected = sorted(ordered_tags, key=tag_ordering.index)
        if ordered_tags == expected:
            return False

        path = source_file_for_node(tool_root, tool_source)
        if not path:
            return False
        _staged = staged if staged is not None else {}
        tree = get_or_load_staged_tree(_staged, path)
        raw_root = tree.getroot()

        # Stable reorder: collect all children, sort known-tag children by
        # desired order, splice back in at their original positions.
        children = list(raw_root)
        known = [(i, c) for i, c in enumerate(children) if c.tag in tag_ordering]
        sorted_known = sorted(known, key=lambda x: tag_ordering.index(x[1].tag))

        # Build new child list: fill known slots with sorted elements.
        new_children = list(children)
        for slot, (_, sorted_child) in zip(known, sorted_known):
            new_children[slot[0]] = sorted_child

        for child in list(raw_root):
            raw_root.remove(child)
        for child in new_children:
            raw_root.append(child)

        apply_staged(staged, path, tree)
        return True
