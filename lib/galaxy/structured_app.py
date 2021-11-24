"""Typed description of Galaxy's app object."""
from typing import Any, Optional, TYPE_CHECKING

from kombu import Connection

from galaxy.auth import AuthManager
from galaxy.datatypes.registry import Registry
from galaxy.di import Container
from galaxy.files import ConfiguredFileSources
from galaxy.job_metrics import JobMetrics
from galaxy.model.base import ModelMapping, SharedModelMapping
from galaxy.model.mapping import GalaxyModelMapping
from galaxy.model.security import GalaxyRBACAgent
from galaxy.model.security import HostAgent
from galaxy.model.tags import GalaxyTagHandler
from galaxy.objectstore import ObjectStore
from galaxy.quota import QuotaAgent
from galaxy.security.idencoding import IdEncodingHelper
from galaxy.tool_util.deps.views import DependencyResolversView
from galaxy.tool_util.verify import test_data
from galaxy.util.dbkeys import GenomeBuilds
from galaxy.web_stack import ApplicationStack
from galaxy.webhooks import WebhooksRegistry
from galaxy.workflow.trs_proxy import TrsProxy

if TYPE_CHECKING:
    from galaxy.config import (
        BaseAppConfiguration,
        GalaxyAppConfiguration,
    )
    from galaxy.config_watchers import ConfigWatchers
    from galaxy.jobs import JobConfiguration
    from galaxy.jobs.manager import JobManager
    from galaxy.managers.api_keys import ApiKeyManager
    from galaxy.managers.collections import DatasetCollectionManager
    from galaxy.managers.folders import FolderManager
    from galaxy.managers.hdas import HDAManager
    from galaxy.managers.histories import HistoryManager
    from galaxy.managers.interactivetool import InteractiveToolManager
    from galaxy.managers.libraries import LibraryManager
    from galaxy.managers.roles import RoleManager
    from galaxy.managers.tools import DynamicToolManager
    from galaxy.managers.users import UserManager
    from galaxy.managers.workflows import (
        WorkflowsManager,
        WorkflowContentsManager,
    )
    from galaxy.queue_worker import GalaxyQueueWorker
    from galaxy.tool_shed.galaxy_install.installed_repository_manager import InstalledRepositoryManager
    from galaxy.tools import ToolBox
    from galaxy.tools.cache import (
        ToolCache,
        ToolShedRepositoryCache,
    )
    from galaxy.tools.data import ToolDataTableManager
    from galaxy.tools.error_reports import ErrorReports
    from galaxy.workflow.scheduling_manager import WorkflowSchedulingManager
    from galaxy.visualization.data_providers.registry import DataProviderRegistry
    from galaxy.visualization.genomes import Genomes
    from galaxy.visualization.plugins.registry import VisualizationsRegistry

class BasicApp(Container):
    """Stripped down version of the ``app`` shared between Galaxy and ToolShed.

    Code that is shared between Galaxy and the Tool Shed should be annotated as
    using BasicApp instead of StructuredApp below.
    """
    name: str
    config: Any
    application_stack: ApplicationStack
    model: SharedModelMapping
    security: IdEncodingHelper
    auth_manager: AuthManager
    toolbox: 'ToolBox'
    security_agent: Any
    quota_agent: QuotaAgent
    datatypes_registry: Registry


class MinimalApp(BasicApp):
    config: 'GalaxyAppConfiguration'
    is_webapp: bool  # is_webapp will be set to true when building WSGI app
    new_installation: bool
    tag_handler: GalaxyTagHandler
    model: GalaxyModelMapping
    install_model: ModelMapping
    security_agent: GalaxyRBACAgent
    host_security_agent: HostAgent
    object_store: ObjectStore


class MinimalManagerApp(MinimalApp):
    file_sources: ConfiguredFileSources
    genome_builds: GenomeBuilds
    dataset_collection_manager: 'DatasetCollectionManager'
    history_manager: 'HistoryManager'
    hda_manager: 'HDAManager'
    workflow_manager: 'WorkflowsManager'
    workflow_contents_manager: 'WorkflowContentsManager'
    library_folder_manager: 'FolderManager'
    library_manager: 'LibraryManager'
    role_manager: 'RoleManager'
    installed_repository_manager: 'InstalledRepositoryManager'
    user_manager: 'UserManager'
    job_config: 'JobConfiguration'
    job_manager: 'JobManager'

    @property
    def is_job_handler(self) -> bool:
        pass


class StructuredApp(MinimalManagerApp):
    """Interface defining typed description of the Galaxy UniverseApplication.

    Ideally nothing that depends on StructuredApp should require
    StructuredApp so we can have a clean import dag. This will
    require setting up a lot more distinction between interfaces
    and implementations in Galaxy though. In the meantime, for
    imports that would bring in StructuredApp if properly type
    (cyclical imports), we're just setting the class attributes to
    Any.
    """
    is_webapp: bool  # is_webapp will be set to true when building WSGI app
    new_installation: bool
    tag_handler: GalaxyTagHandler
    amqp_internal_connection_obj: Optional[Connection]
    dependency_resolvers_view: DependencyResolversView
    test_data_resolver: test_data.TestDataResolver
    file_sources: ConfiguredFileSources
    genome_builds: GenomeBuilds
    job_metrics: JobMetrics
    model: GalaxyModelMapping
    install_model: ModelMapping
    security_agent: GalaxyRBACAgent
    host_security_agent: HostAgent
    trs_proxy: TrsProxy
    webhooks_registry: WebhooksRegistry

    queue_worker: 'GalaxyQueueWorker'
    history_manager: 'HistoryManager'
    hda_manager: 'HDAManager'
    workflow_manager: 'WorkflowsManager'
    workflow_contents_manager: 'WorkflowContentsManager'
    library_folder_manager: 'FolderManager'
    library_manager: 'LibraryManager'
    role_manager: 'RoleManager'
    dynamic_tool_manager: 'DynamicToolManager'
    data_provider_registry: 'DataProviderRegistry'
    tool_data_tables: 'ToolDataTableManager'
    genomes: 'Genomes'
    error_reports: 'ErrorReports'
    tool_cache: 'ToolCache'
    tool_shed_repository_cache: 'ToolShedRepositoryCache'
    watchers: 'ConfigWatchers'
    installed_repository_manager: 'InstalledRepositoryManager'
    workflow_scheduling_manager: 'WorkflowSchedulingManager'
    interactivetool_manager: 'InteractiveToolManager'
    job_config: 'JobConfiguration'
    job_manager: 'JobManager'
    user_manager: 'UserManager'
    api_keys_manager: 'ApiKeyManager'
    visualizations_registry: 'VisualizationsRegistry'