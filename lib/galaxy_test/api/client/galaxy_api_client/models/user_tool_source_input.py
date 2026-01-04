from dataclasses import dataclass, field

from .citations import Citations
from .configfiles import Configfiles
from .description import Description
from .edam_operations import EdamOperations
from .edam_topics import EdamTopics
from .galaxy_tool_parameter_model_input_4 import GalaxyToolParameterModelInput4
from .help_ import Help_
from .license import License
from .outputs import Outputs
from .requirements import Requirements
from .xrefs import Xrefs

__all__ = ["UserToolSourceInput"]


@dataclass
class UserToolSourceInput:
    """
    UserToolSourceInput dataclass.

    Args:
        class_ (str)             :
        container (str)          : Container image to use for this tool.
        id_ (str)                : Unique identifier for the tool. Should be all lower-case
                                   and should not include whitespace.
        name (str)               : The name of the tool, displayed in the tool menu. This is
                                   not the same as the tool id, which is a unique identifier
                                   for the tool.
        shell_command (str)      : A string that contains the command to be executed.
                                   Parameters can be referenced inside $().
        version (str)            : Version for the tool.
        citations (Optional[Citations])
                                 :
        configfiles (Optional[Configfiles])
                                 : A list of config files for this tool.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        edam_operations (Optional[EdamOperations])
                                 :
        edam_topics (Optional[EdamTopics])
                                 :
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        inputs (Optional[List[GalaxyToolParameterModelInput4]])
                                 :
        license (Optional[License])
                                 : A full URI or a a short
                                   [SPDX](https://spdx.org/licenses/) identifier for a
                                   license for this tool wrapper. The tool wrapper license
                                   can be independent of the underlying tool license. This
                                   license covers the tool yaml and associated scripts
                                   shipped with the tool.
        outputs (Optional[Outputs])
                                 :
        requirements (Optional[Requirements])
                                 : A list of requirements needed to execute this tool. These
                                   can be javascript expressions, resource requirements or
                                   container images.
        xrefs (Optional[Xrefs])  :
    """

    class_: str
    container: str  # Container image to use for this tool.
    id_: str  # Unique identifier for the tool. Should be all lower-case and should not include whitespace.
    name: str  # The name of the tool, displayed in the tool menu. This is not the same as the tool id, which is a unique identifier for the tool.
    shell_command: str  # A string that contains the command to be executed. Parameters can be referenced inside $().
    version: str  # Version for the tool.
    citations: Citations | None = None
    configfiles: Configfiles | None = None  # A list of config files for this tool.
    description: Description | None = ""  # Detailed text description for this Quota.
    edam_operations: EdamOperations | None = None
    edam_topics: EdamTopics | None = None
    help_: Help_ | None = None  # Help text shown below the tool interface.
    inputs: list[GalaxyToolParameterModelInput4] | None = field(default_factory=list)
    license: License | None = (
        None  # A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool.
    )
    outputs: Outputs | None = None
    requirements: Requirements | None = (
        None  # A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images.
    )
    xrefs: Xrefs | None = None
