"""This module contains linting functions for general aspects of the tool."""

import re
from typing import (
    Dict,
    Optional,
    Tuple,
    TYPE_CHECKING,
)

from packaging.version import Version

from galaxy.tool_util.biotools.source import ApiBiotoolsMetadataSource
from galaxy.tool_util.edam_util import load_edam_tree
from galaxy.tool_util.lint import Linter
from galaxy.tool_util.version import (
    LegacyVersion,
    parse_version,
)
from ._util import (
    apply_staged,
    get_or_load_staged_tree,
    source_file_for_node,
)

if TYPE_CHECKING:
    from galaxy.tool_util.lint import LintContext
    from galaxy.tool_util.parser.interface import ToolSource
    from galaxy.util import ElementTree
    from galaxy.util.etree import (
        Element,
    )

PROFILE_PATTERN = re.compile(r"^[12]\d\.\d{1,2}$")


lint_tool_types = ["*"]


def _tool_xml_and_root(tool_source: "ToolSource") -> Tuple[Optional["ElementTree"], Optional["Element"]]:
    tool_xml = getattr(tool_source, "xml_tree", None)
    if tool_xml:
        tool_node = tool_xml.getroot()
    else:
        tool_node = None
    return tool_xml, tool_node


class ToolVersionMissing(Linter):
    """
    Tools must have a version
    """

    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml, tool_node = _tool_xml_and_root(tool_source)
        version = tool_source.parse_version() or ""
        if not version:
            lint_ctx.error("Tool version is missing or empty.", linter=cls.name(), node=tool_node)


class ToolVersionPEP404(Linter):
    """
    Tools should have a PEP404 compliant version.
    """

    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml, tool_node = _tool_xml_and_root(tool_source)
        version = tool_source.parse_version() or ""
        parsed_version = parse_version(version)
        if version and isinstance(parsed_version, LegacyVersion):
            lint_ctx.warn(f"Tool version [{version}] is not compliant with PEP 440.", linter=cls.name(), node=tool_node)


class ToolVersionWhitespace(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml, tool_node = _tool_xml_and_root(tool_source)
        version = tool_source.parse_version() or ""
        if version != version.strip():
            lint_ctx.warn(
                f"Tool version is pre/suffixed by whitespace, this may cause errors: [{version}].",
                linter=cls.name(),
                node=tool_node,
            )


class ToolVersionValid(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml, tool_node = _tool_xml_and_root(tool_source)
        version = tool_source.parse_version() or ""
        parsed_version = parse_version(version)
        if version and not isinstance(parsed_version, LegacyVersion) and version == version.strip():
            lint_ctx.valid(f"Tool defines a version [{version}].", linter=cls.name(), node=tool_node)


class ToolNameMissing(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        name = tool_source.parse_name()
        if not name:
            lint_ctx.error("Tool name is missing or empty.", linter=cls.name(), node=tool_node)


class ToolNameWhitespace(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        name = tool_source.parse_name()
        if name and name != name.strip():
            lint_ctx.warn(
                f"Tool name is pre/suffixed by whitespace, this may cause errors: [{name}].",
                linter=cls.name(),
                node=tool_node,
            )

    @classmethod
    def fix(
        cls,
        tool_source: "ToolSource",
        lint_ctx: "LintContext",
        staged: Optional[Dict[str, "ElementTree"]] = None,
    ) -> bool:
        _, tool_node = _tool_xml_and_root(tool_source)
        if tool_node is None:
            return False
        name = tool_node.get("name", "")
        stripped = name.strip()
        if name == stripped:
            return False
        path = source_file_for_node(tool_node, tool_source)
        if not path:
            return False
        tree = get_or_load_staged_tree(staged if staged is not None else {}, path)
        tree.getroot().set("name", stripped)
        apply_staged(staged, path, tree)
        return True


class ToolNameValid(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        name = tool_source.parse_name()
        if name and name == name.strip():
            lint_ctx.valid(f"Tool defines a name [{name}].", linter=cls.name(), node=tool_node)


class ToolIDMissing(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        tool_id = tool_source.parse_id()
        if not tool_id:
            lint_ctx.error("Tool does not define an id attribute.", linter=cls.name(), node=tool_node)


class ToolIDWhitespace(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        tool_id = tool_source.parse_id()
        if tool_id and re.search(r"\s", tool_id):
            lint_ctx.warn(
                f"Tool ID contains whitespace - this is discouraged: [{tool_id}].", linter=cls.name(), node=tool_node
            )


class ToolIDValid(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        tool_id = tool_source.parse_id()
        if tool_id and not re.search(r"\s", tool_id):
            lint_ctx.valid(f"Tool defines an id [{tool_id}].", linter=cls.name(), node=tool_node)


class ToolProfileInvalid(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        profile = tool_source.parse_profile()
        profile_valid = PROFILE_PATTERN.match(profile) is not None
        if not profile_valid:
            lint_ctx.error(f"Tool specifies an invalid profile version [{profile}].", linter=cls.name(), node=tool_node)


class ToolProfileLegacy(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        profile = tool_source.parse_profile()
        profile_valid = PROFILE_PATTERN.match(profile) is not None
        if profile_valid and Version(profile) == Version("16.01"):
            lint_ctx.valid("Tool targets 16.01 Galaxy profile.", linter=cls.name(), node=tool_node)


class ToolProfileValid(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        profile = tool_source.parse_profile()
        profile_valid = PROFILE_PATTERN.match(profile) is not None
        if profile_valid and Version(profile) != Version("16.01"):
            lint_ctx.valid(f"Tool specifies profile version [{profile}].", linter=cls.name(), node=tool_node)


class RequirementNameMissing(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        requirements, *_ = tool_source.parse_requirements()
        for r in requirements:
            if r.type != "package":
                continue
            if not r.name:
                lint_ctx.error("Requirement without name found", linter=cls.name(), node=tool_node)


class RequirementVersionMissing(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        requirements, *_ = tool_source.parse_requirements()
        for r in requirements:
            if r.type != "package":
                continue
            if not r.version:
                lint_ctx.warn(f"Requirement {r.name} defines no version", linter=cls.name(), node=tool_node)


class RequirementVersionWhitespace(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        requirements, *_ = tool_source.parse_requirements()
        for r in requirements:
            if r.type != "package":
                continue
            if r.version and r.version != r.version.strip():
                lint_ctx.warn(
                    f"Requirement version contains whitespace, this may cause errors: [{r.version}].",
                    linter=cls.name(),
                    node=tool_node,
                )

    @classmethod
    def fix(
        cls,
        tool_source: "ToolSource",
        lint_ctx: "LintContext",
        staged: Optional[Dict[str, "ElementTree"]] = None,
    ) -> bool:
        tool_xml = getattr(tool_source, "xml_tree", None)
        if tool_xml is None:
            return False
        _staged = staged if staged is not None else {}
        changed = False
        for req_el in tool_xml.findall(".//requirements/requirement"):
            version = req_el.get("version", "")
            stripped = version.strip()
            if version == stripped or req_el.get("type", "package") != "package":
                continue
            path = source_file_for_node(req_el, tool_source)
            if not path:
                continue
            tree = get_or_load_staged_tree(_staged, path)
            # Use .//requirement (not .//requirements/requirement) so the
            # search also finds elements nested inside macro definitions.
            for raw_req in tree.findall(".//requirement"):
                if raw_req.get("name") == req_el.get("name") and raw_req.get("version") == version:
                    raw_req.set("version", stripped)
                    apply_staged(staged, path, tree)
                    changed = True
                    break
        return changed


class ResourceRequirementExpression(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        requirements, containers, resource_requirements, *_ = tool_source.parse_requirements()
        for rr in resource_requirements:
            if rr.runtime_required:
                lint_ctx.warn(
                    "Expressions in resource requirement not supported yet", linter=cls.name(), node=tool_node
                )


class BioToolsValid(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        xrefs = tool_source.parse_xrefs()
        for xref in xrefs:
            if xref["type"] != "bio.tools":
                continue
            metadata_source = ApiBiotoolsMetadataSource()
            if not metadata_source.get_biotools_metadata(xref["value"]):
                lint_ctx.warn(f'No entry {xref["value"]} in bio.tools.', linter=cls.name(), node=tool_node)


class EDAMTermsValid(Linter):
    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        _, tool_node = _tool_xml_and_root(tool_source)
        edam = load_edam_tree(None, "operation_", "topic_")
        terms = tool_source.parse_edam_operations() + tool_source.parse_edam_topics()
        for term in terms:
            if term not in edam:
                lint_ctx.warn(f"No entry '{term}' in EDAM.", linter=cls.name(), node=tool_node)


# Non-canonical boolean values accepted by Galaxy's string_as_bool() but
# rejected by xs:boolean — canonical form is "true" / "false".
_NONCANONICAL_BOOLEANS = {"True", "False", "Yes", "No", "On", "Off"}
_CANONICAL_REMAP = {
    "True": "true",
    "False": "false",
    "Yes": "true",
    "No": "false",
    "On": "true",
    "Off": "false",
}


class BooleanValues(Linter):
    """Warn when attributes contain non-canonical boolean values (True/False/Yes/No/On/Off).

    Galaxy's ``string_as_bool()`` accepts these at runtime, but XSD schemas
    only accept ``true`` / ``false`` / ``1`` / ``0``.
    """

    @classmethod
    def lint(cls, tool_source: "ToolSource", lint_ctx: "LintContext"):
        tool_xml = getattr(tool_source, "xml_tree", None)
        if tool_xml is None:
            return
        for el in tool_xml.iter():
            for attr, val in el.attrib.items():
                if val in _NONCANONICAL_BOOLEANS:
                    lint_ctx.warn(
                        f"Non-canonical boolean value '{val}' on <{el.tag}> @{attr};"
                        f" use '{_CANONICAL_REMAP[val]}' instead.",
                        linter=cls.name(),
                        node=el,
                    )
                    return  # one message per tool per lint run

    @classmethod
    def fix(
        cls,
        tool_source: "ToolSource",
        lint_ctx: "LintContext",
        staged: Optional[Dict[str, "ElementTree"]] = None,
    ) -> bool:
        tool_xml = getattr(tool_source, "xml_tree", None)
        if tool_xml is None:
            return False
        _staged = staged if staged is not None else {}
        changed = False
        for el in tool_xml.iter():
            for attr, val in list(el.attrib.items()):
                if val not in _NONCANONICAL_BOOLEANS:
                    continue
                path = source_file_for_node(el, tool_source)
                if not path:
                    continue
                tree = get_or_load_staged_tree(_staged, path)
                # Match raw element by tag + all attribute names present in expanded el.
                # This is a best-effort match; it fails if the same tag/attrib combo
                # appears multiple times with different boolean values.
                for raw_el in tree.iter(el.tag):
                    if raw_el.get(attr) == val:
                        raw_el.set(attr, _CANONICAL_REMAP[val])
                        apply_staged(staged, path, tree)
                        changed = True
                        break
        return changed
