from dataclasses import dataclass, field

from .galaxy_tool_parameter_model_input_2 import GalaxyToolParameterModelInput2
from .help__36 import Help36
from .user_tool_source_input_citations import UserToolSourceInputCitations
from .user_tool_source_input_configfiles import UserToolSourceInputConfigfiles
from .user_tool_source_input_description import UserToolSourceInputDescription
from .user_tool_source_input_edam_operations import UserToolSourceInputEdamOperations
from .user_tool_source_input_edam_topics import UserToolSourceInputEdamTopics
from .user_tool_source_input_license import UserToolSourceInputLicense
from .user_tool_source_input_outputs import UserToolSourceInputOutputs
from .user_tool_source_input_requirements import UserToolSourceInputRequirements
from .user_tool_source_input_xrefs import UserToolSourceInputXrefs

__all__ = ["UserToolSourceInput2"]


@dataclass
class UserToolSourceInput2:
    """
    UserToolSourceInput2 dataclass

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
        citations (UserToolSourceInputCitations | None)
                                 :
        configfiles (UserToolSourceInputConfigfiles | None)
                                 : A list of config files for this tool.
        description (UserToolSourceInputDescription | None)
                                 : The description is displayed in the tool menu immediately
                                   following the hyperlink for the tool.
        edam_operations (UserToolSourceInputEdamOperations | None)
                                 :
        edam_topics (UserToolSourceInputEdamTopics | None)
                                 :
        help_ (Help36 | None)    : Help text shown below the tool interface. (maps from
                                   'help')
        inputs (List[GalaxyToolParameterModelInput2] | None)
                                 :
        license (UserToolSourceInputLicense | None)
                                 : A full URI or a a short
                                   [SPDX](https://spdx.org/licenses/) identifier for a
                                   license for this tool wrapper. The tool wrapper license
                                   can be independent of the underlying tool license. This
                                   license covers the tool yaml and associated scripts
                                   shipped with the tool.
        outputs (UserToolSourceInputOutputs | None)
                                 :
        requirements (UserToolSourceInputRequirements | None)
                                 : A list of requirements needed to execute this tool. These
                                   can be javascript expressions, resource requirements or
                                   container images.
        xrefs (UserToolSourceInputXrefs | None)
                                 :
    """

    class_: str  # Maps from 'class'
    container: str  # Container image to use for this tool.
    id_: str  # Unique identifier for the tool. Should be all lower-case and should not include whitespace. (maps from 'id')
    name: str  # The name of the tool, displayed in the tool menu. This is not the same as the tool id, which is a unique identifier for the tool.
    shell_command: str  # A string that contains the command to be executed. Parameters can be referenced inside $().
    version: str  # Version for the tool.
    citations: UserToolSourceInputCitations | None = None
    configfiles: UserToolSourceInputConfigfiles | None = None  # A list of config files for this tool.
    description: UserToolSourceInputDescription | None = (
        None  # The description is displayed in the tool menu immediately following the hyperlink for the tool.
    )
    edam_operations: UserToolSourceInputEdamOperations | None = None
    edam_topics: UserToolSourceInputEdamTopics | None = None
    help_: Help36 | None = None  # Help text shown below the tool interface. (maps from 'help')
    inputs: list[GalaxyToolParameterModelInput2] | None = field(default_factory=list)
    license: UserToolSourceInputLicense | None = (
        None  # A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool.
    )
    outputs: UserToolSourceInputOutputs | None = None
    requirements: UserToolSourceInputRequirements | None = (
        None  # A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images.
    )
    xrefs: UserToolSourceInputXrefs | None = None

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
