from dataclasses import dataclass, field

from .admin_tool_source_citations import AdminToolSourceCitations
from .admin_tool_source_container import AdminToolSourceContainer
from .admin_tool_source_description import AdminToolSourceDescription
from .admin_tool_source_edam_operations import AdminToolSourceEdamOperations
from .admin_tool_source_edam_topics import AdminToolSourceEdamTopics
from .admin_tool_source_license import AdminToolSourceLicense
from .admin_tool_source_name import AdminToolSourceName
from .admin_tool_source_outputs import AdminToolSourceOutputs
from .admin_tool_source_profile import AdminToolSourceProfile
from .admin_tool_source_requirements import AdminToolSourceRequirements
from .admin_tool_source_version import AdminToolSourceVersion
from .admin_tool_source_xrefs import AdminToolSourceXrefs
from .dynamic_tool_create_payload_representation_class_enum import DynamicToolCreatePayloadRepresentationClassEnum
from .galaxy_tool_parameter_model_input_2 import GalaxyToolParameterModelInput2
from .help_ import Help_
from .id_ import Id_

__all__ = ["AdminToolSource"]


@dataclass
class AdminToolSource:
    """
    AdminToolSource dataclass

    Args:
        class_ (DynamicToolCreatePayloadRepresentationClassEnum)
                                 : Maps from 'class'
        command (str)            :
        citations (AdminToolSourceCitations | None)
                                 :
        container (AdminToolSourceContainer | None)
                                 :
        description (AdminToolSourceDescription | None)
                                 :
        edam_operations (AdminToolSourceEdamOperations | None)
                                 :
        edam_topics (AdminToolSourceEdamTopics | None)
                                 :
        help_ (Help_ | None)     : Maps from 'help'
        id_ (Id_ | None)         : Maps from 'id'
        inputs (List[GalaxyToolParameterModelInput2] | None)
                                 :
        license (AdminToolSourceLicense | None)
                                 :
        name (AdminToolSourceName | None)
                                 :
        outputs (AdminToolSourceOutputs | None)
                                 :
        profile (AdminToolSourceProfile | None)
                                 :
        requirements (AdminToolSourceRequirements | None)
                                 :
        version (AdminToolSourceVersion | None)
                                 :
        xrefs (AdminToolSourceXrefs | None)
                                 :
    """

    class_: DynamicToolCreatePayloadRepresentationClassEnum  # Maps from 'class'
    command: str
    citations: AdminToolSourceCitations | None = None
    container: AdminToolSourceContainer | None = None
    description: AdminToolSourceDescription | None = None
    edam_operations: AdminToolSourceEdamOperations | None = None
    edam_topics: AdminToolSourceEdamTopics | None = None
    help_: Help_ | None = None  # Maps from 'help'
    id_: Id_ | None = None  # Maps from 'id'
    inputs: list[GalaxyToolParameterModelInput2] | None = field(default_factory=list)
    license: AdminToolSourceLicense | None = None
    name: AdminToolSourceName | None = None
    outputs: AdminToolSourceOutputs | None = None
    profile: AdminToolSourceProfile | None = None
    requirements: AdminToolSourceRequirements | None = None
    version: AdminToolSourceVersion | None = "1.0"
    xrefs: AdminToolSourceXrefs | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "citations": "citations",
            "class": "class_",
            "command": "command",
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
            "profile": "profile",
            "requirements": "requirements",
            "version": "version",
            "xrefs": "xrefs",
        }
        key_transform_with_dump = {
            "citations": "citations",
            "class_": "class",
            "command": "command",
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
            "profile": "profile",
            "requirements": "requirements",
            "version": "version",
            "xrefs": "xrefs",
        }
