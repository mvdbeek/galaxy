"""Dispatch tool-template evaluation between Cheetah and CWL-style do_eval.

Legacy XML / YAML GalaxyTool wrappers use Cheetah (`fill_template`).
GalaxyUserTool wrappers (`tool_format == "GalaxyUserTool"`) are authored with
CWL-style `$(inputs.x)` expressions and must use `do_eval`.
"""

from collections.abc import Mapping
from typing import (
    Any,
    cast,
    Optional,
    Protocol,
    Union,
)

from cwl_utils.types import CWLObjectType
from packaging.version import Version

from galaxy.tool_util_models.tool_source import JavascriptRequirement
from galaxy.tools.expressions import do_eval
from galaxy.util.template import fill_template


class _HasToolFormat(Protocol):
    # Minimal duck-typed surface this dispatcher needs. Real `Tool` satisfies
    # it; tests can pass a SimpleNamespace(tool_format=...).
    tool_format: Optional[str]


def evaluate_tool_template(
    tool: Optional[_HasToolFormat],
    template_str: str,
    cheetah_context: Optional[dict[str, Any]] = None,
    *,
    cwl_inputs: Optional[Mapping[str, Any]] = None,
    outdir: Optional[str] = None,
    javascript_requirements: Optional[list[JavascriptRequirement]] = None,
    python_template_version: Optional[Union[Version, str]] = None,
) -> str:
    """Evaluate ``template_str`` against ``tool``'s expected templating engine.

    For ``tool.tool_format == "GalaxyUserTool"`` the expression is evaluated via
    ``do_eval`` against ``cwl_inputs`` (CWL-style ``$(inputs.x)`` references).
    Any other format (or ``tool is None``) falls back to Cheetah ``fill_template``
    against ``cheetah_context``.
    """
    if tool is not None and tool.tool_format == "GalaxyUserTool":
        return str(
            do_eval(
                template_str,
                cast(CWLObjectType, cwl_inputs or {}),
                javascript_requirements=javascript_requirements,
                outdir=outdir,
            )
        )
    return fill_template(
        template_str,
        context=cheetah_context or {},
        python_template_version=python_template_version,
    )


def project_wrapped_params_to_cwl_inputs(params: dict[str, Any]) -> dict[str, str]:
    """Project wrapped tool params to a flat CWL-shape inputs dict for ``do_eval``.

    Each value is ``str()``-coerced — primitive wrappers yield the value,
    ``DatasetFilenameWrapper`` yields the file path. Keys starting with ``__``
    (Galaxy-internal params) are filtered out so they don't pollute the
    ``inputs`` namespace seen by user expressions.
    """
    return {k: str(v) for k, v in params.items() if not k.startswith("__")}
