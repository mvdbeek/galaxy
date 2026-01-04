from dataclasses import dataclass, field

from .citations import Citations
from .container import Container
from .description import Description
from .edam_operations import EdamOperations
from .edam_topics import EdamTopics
from .galaxy_tool_parameter_model_input_4 import GalaxyToolParameterModelInput4
from .help_ import Help_
from .id_ import Id_
from .license import License
from .name import Name
from .outputs import Outputs
from .profile import Profile
from .requirements import Requirements
from .version import Version
from .xrefs import Xrefs

__all__ = ["AdminToolSource"]


@dataclass
class AdminToolSource:
    """
    AdminToolSource dataclass.

    Args:
        class_ (str)             :
        command (str)            :
        citations (Optional[Citations])
                                 :
        container (Optional[Container])
                                 :
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        edam_operations (Optional[EdamOperations])
                                 :
        edam_topics (Optional[EdamTopics])
                                 :
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        id_ (Optional[Id_])      : The encoded ID of the dataset/dataset collection.
        inputs (Optional[List[GalaxyToolParameterModelInput4]])
                                 :
        license (Optional[License])
                                 : A full URI or a a short
                                   [SPDX](https://spdx.org/licenses/) identifier for a
                                   license for this tool wrapper. The tool wrapper license
                                   can be independent of the underlying tool license. This
                                   license covers the tool yaml and associated scripts
                                   shipped with the tool.
        name (Optional[Name])    : The name of the creator.
        outputs (Optional[Outputs])
                                 :
        profile (Optional[Profile])
                                 :
        requirements (Optional[Requirements])
                                 : A list of requirements needed to execute this tool. These
                                   can be javascript expressions, resource requirements or
                                   container images.
        version (Optional[Version])
                                 : The version of the workflow to invoke.
        xrefs (Optional[Xrefs])  :
    """

    class_: str
    command: str
    citations: Citations | None = None
    container: Container | None = None
    description: Description | None = ""  # Detailed text description for this Quota.
    edam_operations: EdamOperations | None = None
    edam_topics: EdamTopics | None = None
    help_: Help_ | None = None  # Help text shown below the tool interface.
    id_: Id_ | None = None  # The encoded ID of the dataset/dataset collection.
    inputs: list[GalaxyToolParameterModelInput4] | None = field(default_factory=list)
    license: License | None = (
        None  # A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool.
    )
    name: Name | None = None  # The name of the creator.
    outputs: Outputs | None = None
    profile: Profile | None = None
    requirements: Requirements | None = (
        None  # A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images.
    )
    version: Version | None = "1.0"  # The version of the workflow to invoke.
    xrefs: Xrefs | None = None
