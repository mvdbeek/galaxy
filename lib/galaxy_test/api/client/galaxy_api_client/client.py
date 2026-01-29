from typing import Any

from galaxy_test.api.client.galaxy_api_client.core.config import ClientConfig
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport, HttpxTransport

from .endpoints.ai import AiClient
from .endpoints.authenticate import AuthenticateClient
from .endpoints.chat import ChatClient
from .endpoints.configuration import ConfigurationClient
from .endpoints.context import ContextClient
from .endpoints.data_libraries_folders import DataLibrariesFoldersClient
from .endpoints.dataset_collections import DatasetCollectionsClient
from .endpoints.datasets import DatasetsClient
from .endpoints.datatypes import DatatypesClient
from .endpoints.display_applications import DisplayApplicationsClient
from .endpoints.drs import DrsClient
from .endpoints.dynamic_tools import DynamicToolsClient
from .endpoints.file_sources import FileSourcesClient
from .endpoints.forms import FormsClient
from .endpoints.genomes import GenomesClient
from .endpoints.group_roles import GroupRolesClient
from .endpoints.group_users import GroupUsersClient
from .endpoints.groups import GroupsClient
from .endpoints.help_ import Help_Client
from .endpoints.histories import HistoriesClient
from .endpoints.job_lock import JobLockClient
from .endpoints.jobs import JobsClient
from .endpoints.libraries import LibrariesClient
from .endpoints.licenses import LicensesClient
from .endpoints.metrics import MetricsClient
from .endpoints.notifications import NotificationsClient
from .endpoints.oauth_2 import Oauth2Client
from .endpoints.object_stores import ObjectStoresClient
from .endpoints.oidc_tokens import OidcTokensClient
from .endpoints.pages import PagesClient
from .endpoints.quotas import QuotasClient
from .endpoints.remote_files import RemoteFilesClient
from .endpoints.roles import RolesClient
from .endpoints.short_term_storage import ShortTermStorageClient
from .endpoints.storage_management import StorageManagementClient
from .endpoints.tags import TagsClient
from .endpoints.tasks import TasksClient
from .endpoints.tool_data_tables import ToolDataTablesClient
from .endpoints.tool_shed_repositories import ToolShedRepositoriesClient
from .endpoints.tools import ToolsClient
from .endpoints.tours import ToursClient
from .endpoints.users import UsersClient
from .endpoints.utilities import UtilitiesClient
from .endpoints.visualizations import VisualizationsClient
from .endpoints.workflows import WorkflowsClient


class APIClient:
    """
    Galaxy API (version 0.1.0)


    Async API client with pluggable transport, tag-specific clients, and client-level
    headers.

    Args:
        config (ClientConfig)    : Client configuration object.
        transport (Optional[HttpTransport])
                                 : Custom HTTP transport (optional).
        ai (AiClient)            : Client for 'ai' endpoints.
        authenticate (AuthenticateClient)
                                 : Client for 'authenticate' endpoints.
        chat (ChatClient)        : Client for 'chat' endpoints.
        configuration (ConfigurationClient)
                                 : Client for 'configuration' endpoints.
        context (ContextClient)  : Client for 'context' endpoints.
        data_libraries_folders (DataLibrariesFoldersClient)
                                 : Client for 'data libraries folders' endpoints.
        dataset_collections (DatasetCollectionsClient)
                                 : Client for 'dataset collections' endpoints.
        datasets (DatasetsClient): Client for 'datasets' endpoints.
        datatypes (DatatypesClient)
                                 : Client for 'datatypes' endpoints.
        display_applications (DisplayApplicationsClient)
                                 : Client for 'display_applications' endpoints.
        drs (DrsClient)          : Client for 'drs' endpoints.
        dynamic_tools (DynamicToolsClient)
                                 : Client for 'dynamic_tools' endpoints.
        file_sources (FileSourcesClient)
                                 : Client for 'file_sources' endpoints.
        forms (FormsClient)      : Client for 'forms' endpoints.
        genomes (GenomesClient)  : Client for 'genomes' endpoints.
        group_roles (GroupRolesClient)
                                 : Client for 'group_roles' endpoints.
        groups (GroupsClient)    : Client for 'groups' endpoints.
        group_users (GroupUsersClient)
                                 : Client for 'group_users' endpoints.
        help_ (Help_Client)      : Client for 'help' endpoints.
        histories (HistoriesClient)
                                 : Client for 'histories' endpoints.
        job_lock (JobLockClient) : Client for 'job_lock' endpoints.
        jobs (JobsClient)        : Client for 'jobs' endpoints.
        libraries (LibrariesClient)
                                 : Client for 'libraries' endpoints.
        licenses (LicensesClient): Client for 'licenses' endpoints.
        metrics (MetricsClient)  : Client for 'metrics' endpoints.
        notifications (NotificationsClient)
                                 : Client for 'notifications' endpoints.
        oauth_2 (Oauth2Client)   : Client for 'oauth2' endpoints.
        object_stores (ObjectStoresClient)
                                 : Client for 'object_stores' endpoints.
        oidc_tokens (OidcTokensClient)
                                 : Client for 'oidc_tokens' endpoints.
        pages (PagesClient)      : Client for 'pages' endpoints.
        quotas (QuotasClient)    : Client for 'quotas' endpoints.
        remote_files (RemoteFilesClient)
                                 : Client for 'remote files' endpoints.
        roles (RolesClient)      : Client for 'roles' endpoints.
        short_term_storage (ShortTermStorageClient)
                                 : Client for 'short_term_storage' endpoints.
        storage_management (StorageManagementClient)
                                 : Client for 'storage management' endpoints.
        tags (TagsClient)        : Client for 'tags' endpoints.
        tasks (TasksClient)      : Client for 'tasks' endpoints.
        tool_data_tables (ToolDataTablesClient)
                                 : Client for 'tool data tables' endpoints.
        tools (ToolsClient)      : Client for 'tools' endpoints.
        tool_shed_repositories (ToolShedRepositoriesClient)
                                 : Client for 'tool_shed_repositories' endpoints.
        tours (ToursClient)      : Client for 'tours' endpoints.
        users (UsersClient)      : Client for 'users' endpoints.
        utilities (UtilitiesClient)
                                 : Client for 'utilities' endpoints.
        visualizations (VisualizationsClient)
                                 : Client for 'visualizations' endpoints.
        workflows (WorkflowsClient)
                                 : Client for 'workflows' endpoints.

    """

    def __init__(self, config: ClientConfig, transport: HttpTransport | None = None) -> None:
        self.config = config
        self.transport = transport if transport is not None else HttpxTransport(str(config.base_url), config.timeout)
        self._base_url: str = str(self.config.base_url)
        self._ai: AiClient | None = None
        self._authenticate: AuthenticateClient | None = None
        self._chat: ChatClient | None = None
        self._configuration: ConfigurationClient | None = None
        self._context: ContextClient | None = None
        self._data_libraries_folders: DataLibrariesFoldersClient | None = None
        self._dataset_collections: DatasetCollectionsClient | None = None
        self._datasets: DatasetsClient | None = None
        self._datatypes: DatatypesClient | None = None
        self._display_applications: DisplayApplicationsClient | None = None
        self._drs: DrsClient | None = None
        self._dynamic_tools: DynamicToolsClient | None = None
        self._file_sources: FileSourcesClient | None = None
        self._forms: FormsClient | None = None
        self._genomes: GenomesClient | None = None
        self._group_roles: GroupRolesClient | None = None
        self._groups: GroupsClient | None = None
        self._group_users: GroupUsersClient | None = None
        self._help_: Help_Client | None = None
        self._histories: HistoriesClient | None = None
        self._job_lock: JobLockClient | None = None
        self._jobs: JobsClient | None = None
        self._libraries: LibrariesClient | None = None
        self._licenses: LicensesClient | None = None
        self._metrics: MetricsClient | None = None
        self._notifications: NotificationsClient | None = None
        self._oauth_2: Oauth2Client | None = None
        self._object_stores: ObjectStoresClient | None = None
        self._oidc_tokens: OidcTokensClient | None = None
        self._pages: PagesClient | None = None
        self._quotas: QuotasClient | None = None
        self._remote_files: RemoteFilesClient | None = None
        self._roles: RolesClient | None = None
        self._short_term_storage: ShortTermStorageClient | None = None
        self._storage_management: StorageManagementClient | None = None
        self._tags: TagsClient | None = None
        self._tasks: TasksClient | None = None
        self._tool_data_tables: ToolDataTablesClient | None = None
        self._tools: ToolsClient | None = None
        self._tool_shed_repositories: ToolShedRepositoriesClient | None = None
        self._tours: ToursClient | None = None
        self._users: UsersClient | None = None
        self._utilities: UtilitiesClient | None = None
        self._visualizations: VisualizationsClient | None = None
        self._workflows: WorkflowsClient | None = None

    @property
    def ai(self) -> AiClient:
        """Client for 'ai' endpoints."""
        if self._ai is None:
            self._ai = AiClient(self.transport, self._base_url)
        return self._ai

    @property
    def authenticate(self) -> AuthenticateClient:
        """Client for 'authenticate' endpoints."""
        if self._authenticate is None:
            self._authenticate = AuthenticateClient(self.transport, self._base_url)
        return self._authenticate

    @property
    def chat(self) -> ChatClient:
        """Client for 'chat' endpoints."""
        if self._chat is None:
            self._chat = ChatClient(self.transport, self._base_url)
        return self._chat

    @property
    def configuration(self) -> ConfigurationClient:
        """Client for 'configuration' endpoints."""
        if self._configuration is None:
            self._configuration = ConfigurationClient(self.transport, self._base_url)
        return self._configuration

    @property
    def context(self) -> ContextClient:
        """Client for 'context' endpoints."""
        if self._context is None:
            self._context = ContextClient(self.transport, self._base_url)
        return self._context

    @property
    def data_libraries_folders(self) -> DataLibrariesFoldersClient:
        """Client for 'data libraries folders' endpoints."""
        if self._data_libraries_folders is None:
            self._data_libraries_folders = DataLibrariesFoldersClient(self.transport, self._base_url)
        return self._data_libraries_folders

    @property
    def dataset_collections(self) -> DatasetCollectionsClient:
        """Client for 'dataset collections' endpoints."""
        if self._dataset_collections is None:
            self._dataset_collections = DatasetCollectionsClient(self.transport, self._base_url)
        return self._dataset_collections

    @property
    def datasets(self) -> DatasetsClient:
        """Client for 'datasets' endpoints."""
        if self._datasets is None:
            self._datasets = DatasetsClient(self.transport, self._base_url)
        return self._datasets

    @property
    def datatypes(self) -> DatatypesClient:
        """Client for 'datatypes' endpoints."""
        if self._datatypes is None:
            self._datatypes = DatatypesClient(self.transport, self._base_url)
        return self._datatypes

    @property
    def display_applications(self) -> DisplayApplicationsClient:
        """Client for 'display_applications' endpoints."""
        if self._display_applications is None:
            self._display_applications = DisplayApplicationsClient(self.transport, self._base_url)
        return self._display_applications

    @property
    def drs(self) -> DrsClient:
        """Client for 'drs' endpoints."""
        if self._drs is None:
            self._drs = DrsClient(self.transport, self._base_url)
        return self._drs

    @property
    def dynamic_tools(self) -> DynamicToolsClient:
        """Client for 'dynamic_tools' endpoints."""
        if self._dynamic_tools is None:
            self._dynamic_tools = DynamicToolsClient(self.transport, self._base_url)
        return self._dynamic_tools

    @property
    def file_sources(self) -> FileSourcesClient:
        """Client for 'file_sources' endpoints."""
        if self._file_sources is None:
            self._file_sources = FileSourcesClient(self.transport, self._base_url)
        return self._file_sources

    @property
    def forms(self) -> FormsClient:
        """Client for 'forms' endpoints."""
        if self._forms is None:
            self._forms = FormsClient(self.transport, self._base_url)
        return self._forms

    @property
    def genomes(self) -> GenomesClient:
        """Client for 'genomes' endpoints."""
        if self._genomes is None:
            self._genomes = GenomesClient(self.transport, self._base_url)
        return self._genomes

    @property
    def group_roles(self) -> GroupRolesClient:
        """Client for 'group_roles' endpoints."""
        if self._group_roles is None:
            self._group_roles = GroupRolesClient(self.transport, self._base_url)
        return self._group_roles

    @property
    def groups(self) -> GroupsClient:
        """Client for 'groups' endpoints."""
        if self._groups is None:
            self._groups = GroupsClient(self.transport, self._base_url)
        return self._groups

    @property
    def group_users(self) -> GroupUsersClient:
        """Client for 'group_users' endpoints."""
        if self._group_users is None:
            self._group_users = GroupUsersClient(self.transport, self._base_url)
        return self._group_users

    @property
    def help_(self) -> Help_Client:
        """Client for 'help' endpoints."""
        if self._help_ is None:
            self._help_ = Help_Client(self.transport, self._base_url)
        return self._help_

    @property
    def histories(self) -> HistoriesClient:
        """Client for 'histories' endpoints."""
        if self._histories is None:
            self._histories = HistoriesClient(self.transport, self._base_url)
        return self._histories

    @property
    def job_lock(self) -> JobLockClient:
        """Client for 'job_lock' endpoints."""
        if self._job_lock is None:
            self._job_lock = JobLockClient(self.transport, self._base_url)
        return self._job_lock

    @property
    def jobs(self) -> JobsClient:
        """Client for 'jobs' endpoints."""
        if self._jobs is None:
            self._jobs = JobsClient(self.transport, self._base_url)
        return self._jobs

    @property
    def libraries(self) -> LibrariesClient:
        """Client for 'libraries' endpoints."""
        if self._libraries is None:
            self._libraries = LibrariesClient(self.transport, self._base_url)
        return self._libraries

    @property
    def licenses(self) -> LicensesClient:
        """Client for 'licenses' endpoints."""
        if self._licenses is None:
            self._licenses = LicensesClient(self.transport, self._base_url)
        return self._licenses

    @property
    def metrics(self) -> MetricsClient:
        """Client for 'metrics' endpoints."""
        if self._metrics is None:
            self._metrics = MetricsClient(self.transport, self._base_url)
        return self._metrics

    @property
    def notifications(self) -> NotificationsClient:
        """Client for 'notifications' endpoints."""
        if self._notifications is None:
            self._notifications = NotificationsClient(self.transport, self._base_url)
        return self._notifications

    @property
    def oauth_2(self) -> Oauth2Client:
        """Client for 'oauth2' endpoints."""
        if self._oauth_2 is None:
            self._oauth_2 = Oauth2Client(self.transport, self._base_url)
        return self._oauth_2

    @property
    def object_stores(self) -> ObjectStoresClient:
        """Client for 'object_stores' endpoints."""
        if self._object_stores is None:
            self._object_stores = ObjectStoresClient(self.transport, self._base_url)
        return self._object_stores

    @property
    def oidc_tokens(self) -> OidcTokensClient:
        """Client for 'oidc_tokens' endpoints."""
        if self._oidc_tokens is None:
            self._oidc_tokens = OidcTokensClient(self.transport, self._base_url)
        return self._oidc_tokens

    @property
    def pages(self) -> PagesClient:
        """Client for 'pages' endpoints."""
        if self._pages is None:
            self._pages = PagesClient(self.transport, self._base_url)
        return self._pages

    @property
    def quotas(self) -> QuotasClient:
        """Client for 'quotas' endpoints."""
        if self._quotas is None:
            self._quotas = QuotasClient(self.transport, self._base_url)
        return self._quotas

    @property
    def remote_files(self) -> RemoteFilesClient:
        """Client for 'remote files' endpoints."""
        if self._remote_files is None:
            self._remote_files = RemoteFilesClient(self.transport, self._base_url)
        return self._remote_files

    @property
    def roles(self) -> RolesClient:
        """Client for 'roles' endpoints."""
        if self._roles is None:
            self._roles = RolesClient(self.transport, self._base_url)
        return self._roles

    @property
    def short_term_storage(self) -> ShortTermStorageClient:
        """Client for 'short_term_storage' endpoints."""
        if self._short_term_storage is None:
            self._short_term_storage = ShortTermStorageClient(self.transport, self._base_url)
        return self._short_term_storage

    @property
    def storage_management(self) -> StorageManagementClient:
        """Client for 'storage management' endpoints."""
        if self._storage_management is None:
            self._storage_management = StorageManagementClient(self.transport, self._base_url)
        return self._storage_management

    @property
    def tags(self) -> TagsClient:
        """Client for 'tags' endpoints."""
        if self._tags is None:
            self._tags = TagsClient(self.transport, self._base_url)
        return self._tags

    @property
    def tasks(self) -> TasksClient:
        """Client for 'tasks' endpoints."""
        if self._tasks is None:
            self._tasks = TasksClient(self.transport, self._base_url)
        return self._tasks

    @property
    def tool_data_tables(self) -> ToolDataTablesClient:
        """Client for 'tool data tables' endpoints."""
        if self._tool_data_tables is None:
            self._tool_data_tables = ToolDataTablesClient(self.transport, self._base_url)
        return self._tool_data_tables

    @property
    def tools(self) -> ToolsClient:
        """Client for 'tools' endpoints."""
        if self._tools is None:
            self._tools = ToolsClient(self.transport, self._base_url)
        return self._tools

    @property
    def tool_shed_repositories(self) -> ToolShedRepositoriesClient:
        """Client for 'tool_shed_repositories' endpoints."""
        if self._tool_shed_repositories is None:
            self._tool_shed_repositories = ToolShedRepositoriesClient(self.transport, self._base_url)
        return self._tool_shed_repositories

    @property
    def tours(self) -> ToursClient:
        """Client for 'tours' endpoints."""
        if self._tours is None:
            self._tours = ToursClient(self.transport, self._base_url)
        return self._tours

    @property
    def users(self) -> UsersClient:
        """Client for 'users' endpoints."""
        if self._users is None:
            self._users = UsersClient(self.transport, self._base_url)
        return self._users

    @property
    def utilities(self) -> UtilitiesClient:
        """Client for 'utilities' endpoints."""
        if self._utilities is None:
            self._utilities = UtilitiesClient(self.transport, self._base_url)
        return self._utilities

    @property
    def visualizations(self) -> VisualizationsClient:
        """Client for 'visualizations' endpoints."""
        if self._visualizations is None:
            self._visualizations = VisualizationsClient(self.transport, self._base_url)
        return self._visualizations

    @property
    def workflows(self) -> WorkflowsClient:
        """Client for 'workflows' endpoints."""
        if self._workflows is None:
            self._workflows = WorkflowsClient(self.transport, self._base_url)
        return self._workflows

    async def request(self, method: str, url: str, **kwargs: Any) -> Any:
        """Send an HTTP request via the transport."""
        return await self.transport.request(method, url, **kwargs)

    async def close(self) -> None:
        """Close the underlying transport if supported."""
        if hasattr(self.transport, "close"):
            await self.transport.close()
        else:
            pass  # Or log a warning if close is expected but not found

    async def __aenter__(self) -> "APIClient":
        """Enter the async context manager. Returns self."""
        if hasattr(self.transport, "__aenter__"):
            await self.transport.__aenter__()
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: object | None
    ) -> None:
        """Exit the async context manager, ensuring transport is closed."""
        if hasattr(self.transport, "__aexit__"):
            await self.transport.__aexit__(exc_type, exc_val, exc_tb)
        else:
            await self.close()
