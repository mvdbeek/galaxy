"""This module contains linters for a tool's command description.

A command description describes how to build the command-line to execute
from supplied inputs.
"""

from typing import (
    Dict,
    Optional,
    TYPE_CHECKING,
)

from lxml import etree

from galaxy.tool_util.lint import Linter
from ._util import (
    apply_staged,
    get_or_load_staged_tree,
    source_file_for_node,
)

if TYPE_CHECKING:
    from galaxy.tool_util.lint import LintContext
    from galaxy.tool_util.parser.interface import ToolSource
    from galaxy.util import ElementTree


def _element_has_cdata(el) -> bool:
    """Return True if *el* already has CDATA-wrapped text when serialised.

    Requires the owning tree to have been parsed with ``preserve_cdata=True``
    (the default for :func:`~galaxy.util.xml_macros.raw_xml_tree`).
    """
    return "<![CDATA[" in etree.tostring(el, encoding="unicode")


class CommandMissing(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml = getattr(tool_source, "xml_tree", None)
        if not tool_xml:
            return
        root = tool_xml.find("./command")
        if root is None:
            root = tool_xml.getroot()
        command = tool_xml.find("./command")
        if command is None:
            lint_ctx.error(
                "No command tag found, must specify a command template to execute.", linter=cls.name(), node=root
            )


class CommandEmpty(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml = getattr(tool_source, "xml_tree", None)
        if not tool_xml:
            return
        root = tool_xml.find("./command")
        if root is None:
            root = tool_xml.getroot()
        command = tool_xml.find("./command")
        if command is not None and command.text is None:
            lint_ctx.error("Command is empty.", linter=cls.name(), node=root)


class CommandTODO(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml = getattr(tool_source, "xml_tree", None)
        if not tool_xml:
            return
        command = tool_xml.find("./command")
        if command is not None and command.text is not None and "TODO" in command.text:
            lint_ctx.warn("Command template contains TODO text.", linter=cls.name(), node=command)


class CommandInterpreterDeprecated(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml = getattr(tool_source, "xml_tree", None)
        if not tool_xml:
            return
        command = tool_xml.find("./command")
        if command is None:
            return
        interpreter_type = command.attrib.get("interpreter", None)
        if interpreter_type is not None:
            lint_ctx.warn("Command uses deprecated 'interpreter' attribute.", linter=cls.name(), node=command)


class CommandInfo(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml = getattr(tool_source, "xml_tree", None)
        if not tool_xml:
            return
        command = tool_xml.find("./command")
        if command is None:
            return
        interpreter_type = command.attrib.get("interpreter", None)
        interpreter_info = ""
        if interpreter_type:
            interpreter_info = f" with interpreter of type [{interpreter_type}]"
        lint_ctx.info(f"Tool contains a command{interpreter_info}.", linter=cls.name(), node=command)


def _lint_cdata(el_tag: str, tool_source: "ToolSource", lint_ctx: "LintContext", linter_name: str) -> None:
    """Shared lint logic for CDATA-wrapping checks.

    When the tool is file-backed (has a source_path) the expanded tree is
    loaded with CDATA preserved, so we can check directly without a second
    disk read.  In-memory tools may have been parsed without CDATA preservation,
    so we skip the check for them.
    """
    tool_xml = getattr(tool_source, "xml_tree", None)
    if tool_xml is None:
        return
    if not getattr(tool_source, "source_path", None):
        return  # in-memory tool — CDATA may have been stripped during parsing
    el = tool_xml.find(f"./{el_tag}")
    if el is None or not (el.text or "").strip() or len(el):
        return  # empty or has child elements — skip
    if not _element_has_cdata(el):
        lint_ctx.warn(
            f"<{el_tag}> block should use CDATA to protect special characters from XML escaping.",
            linter=linter_name,
            node=el,
        )


def _fix_cdata(
    el_tag: str,
    tool_source: "ToolSource",
    staged: Optional[Dict[str, "ElementTree"]],
) -> bool:
    """Shared fix logic for CDATA-wrapping."""
    tool_xml = getattr(tool_source, "xml_tree", None)
    if tool_xml is None:
        return False
    el = tool_xml.find(f"./{el_tag}")
    if el is None or not (el.text or "").strip() or len(el):
        return False
    if _element_has_cdata(el):
        return False  # already wrapped — check on the CDATA-preserving expanded tree
    path = source_file_for_node(el, tool_source)
    if not path:
        return False
    _staged = staged if staged is not None else {}
    tree = get_or_load_staged_tree(_staged, path)
    raw_el = tree.find(f"./{el_tag}")
    if raw_el is None or not raw_el.text:
        return False
    raw_el.text = etree.CDATA(raw_el.text)
    apply_staged(staged, path, tree)
    return True


class CommandCdata(Linter):
    """Warn when the <command> block is not wrapped in CDATA."""

    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _lint_cdata("command", tool_source, lint_ctx, cls.name())

    @classmethod
    def fix(
        cls,
        tool_source: "ToolSource",
        lint_ctx: "LintContext",
        staged: Optional[Dict[str, "ElementTree"]] = None,
    ) -> bool:
        return _fix_cdata("command", tool_source, staged)


class HelpCdata(Linter):
    """Warn when the <help> block is not wrapped in CDATA."""

    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _lint_cdata("help", tool_source, lint_ctx, cls.name())

    @classmethod
    def fix(
        cls,
        tool_source: "ToolSource",
        lint_ctx: "LintContext",
        staged: Optional[Dict[str, "ElementTree"]] = None,
    ) -> bool:
        return _fix_cdata("help", tool_source, staged)
