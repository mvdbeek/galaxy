from dataclasses import dataclass, field

from .galaxy_tool_parameter_model_output_2 import GalaxyToolParameterModelOutput2
from .help__43 import Help43
from .user_tool_source_output_citations import UserToolSourceOutputCitations
from .user_tool_source_output_configfiles import UserToolSourceOutputConfigfiles
from .user_tool_source_output_description import UserToolSourceOutputDescription
from .user_tool_source_output_edam_operations import UserToolSourceOutputEdamOperations
from .user_tool_source_output_edam_topics import UserToolSourceOutputEdamTopics
from .user_tool_source_output_license import UserToolSourceOutputLicense
from .user_tool_source_output_outputs import UserToolSourceOutputOutputs
from .user_tool_source_output_requirements import UserToolSourceOutputRequirements
from .user_tool_source_output_xrefs import UserToolSourceOutputXrefs

__all__ = ["UserToolSourceOutput"]


@dataclass
class UserToolSourceOutput:
    """
    UserToolSourceOutput dataclass

    Args:
        class_ (str)             : Maps from 'class'
        container (str)          : Container image to use for this tool.
        id_ (str)                : Unique identifier for the tool. Should be all lower-case
                                   and should not include whitespace. (maps from 'id')
        name (str)               : The name of the tool, displayed in the tool menu. This is
                                   not the same as the tool id, which is a unique identifier
                                   for the tool.
        shell_command (str)      : A string that contains the command to be executed.
                                   Parameters can be referenced inside $().
        version (str)            : Version for the tool.
        citations (UserToolSourceOutputCitations | None)
                                 :
        configfiles (UserToolSourceOutputConfigfiles | None)
                                 : A list of config files for this tool.
        description (UserToolSourceOutputDescription | None)
                                 : The description is displayed in the tool menu immediately
                                   following the hyperlink for the tool.
        edam_operations (UserToolSourceOutputEdamOperations | None)
                                 :
        edam_topics (UserToolSourceOutputEdamTopics | None)
                                 :
        help_ (Help43 | None)    : Help text shown below the tool interface. (maps from
                                   'help')
        inputs (List[GalaxyToolParameterModelOutput2] | None)
                                 :
        license (UserToolSourceOutputLicense | None)
                                 : A full URI or a a short
                                   [SPDX](https://spdx.org/licenses/) identifier for a
                                   license for this tool wrapper. The tool wrapper license
                                   can be independent of the underlying tool license. This
                                   license covers the tool yaml and associated scripts
                                   shipped with the tool.
        outputs (UserToolSourceOutputOutputs | None)
                                 :
        requirements (UserToolSourceOutputRequirements | None)
                                 : A list of requirements needed to execute this tool. These
                                   can be javascript expressions, resource requirements or
                                   container images.
        xrefs (UserToolSourceOutputXrefs | None)
                                 :
    """

    class_: str  # Maps from 'class'
    container: str  # Container image to use for this tool.
    id_: str  # Unique identifier for the tool. Should be all lower-case and should not include whitespace. (maps from 'id')
    name: str  # The name of the tool, displayed in the tool menu. This is not the same as the tool id, which is a unique identifier for the tool.
    shell_command: str  # A string that contains the command to be executed. Parameters can be referenced inside $().
    version: str  # Version for the tool.
    citations: UserToolSourceOutputCitations | None = None
    configfiles: UserToolSourceOutputConfigfiles | None = None  # A list of config files for this tool.
    description: UserToolSourceOutputDescription | None = (
        None  # The description is displayed in the tool menu immediately following the hyperlink for the tool.
    )
    edam_operations: UserToolSourceOutputEdamOperations | None = None
    edam_topics: UserToolSourceOutputEdamTopics | None = None
    help_: Help43 | None = None  # Help text shown below the tool interface. (maps from 'help')
    inputs: list[GalaxyToolParameterModelOutput2] | None = field(default_factory=list)
    license: UserToolSourceOutputLicense | None = (
        None  # A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool.
    )
    outputs: UserToolSourceOutputOutputs | None = None
    requirements: UserToolSourceOutputRequirements | None = (
        None  # A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images.
    )
    xrefs: UserToolSourceOutputXrefs | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "citations": "citations",
            "class": "class_",
            "configfiles": "configfiles",
            "container": "container",
            "description": "description",
            "edam_operations": "edam_operations",
            "edam_topics": "edam_topics",
            "help": "help_",
            "id": "id_",
            "inputs": "inputs",
            "license": "license",
            "name": "name",
            "outputs": "outputs",
            "requirements": "requirements",
            "shell_command": "shell_command",
            "version": "version",
            "xrefs": "xrefs",
        }
        key_transform_with_dump = {
            "citations": "citations",
            "class_": "class",
            "configfiles": "configfiles",
            "container": "container",
            "description": "description",
            "edam_operations": "edam_operations",
            "edam_topics": "edam_topics",
            "help_": "help",
            "id_": "id",
            "inputs": "inputs",
            "license": "license",
            "name": "name",
            "outputs": "outputs",
            "requirements": "requirements",
            "shell_command": "shell_command",
            "version": "version",
            "xrefs": "xrefs",
        }
