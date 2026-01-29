from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import APIClientProtocol
    from ..endpoints.ai import AiClientProtocol
    from ..endpoints.authenticate import AuthenticateClientProtocol
    from ..endpoints.chat import ChatClientProtocol
    from ..endpoints.configuration import ConfigurationClientProtocol
    from ..endpoints.context import ContextClientProtocol
    from ..endpoints.data_libraries_folders import DataLibrariesFoldersClientProtocol
    from ..endpoints.dataset_collections import DatasetCollectionsClientProtocol
    from ..endpoints.datasets import DatasetsClientProtocol
    from ..endpoints.datatypes import DatatypesClientProtocol
    from ..endpoints.display_applications import DisplayApplicationsClientProtocol
    from ..endpoints.drs import DrsClientProtocol
    from ..endpoints.dynamic_tools import DynamicToolsClientProtocol
    from ..endpoints.file_sources import FileSourcesClientProtocol
    from ..endpoints.forms import FormsClientProtocol
    from ..endpoints.genomes import GenomesClientProtocol
    from ..endpoints.group_roles import GroupRolesClientProtocol
    from ..endpoints.group_users import GroupUsersClientProtocol
    from ..endpoints.groups import GroupsClientProtocol
    from ..endpoints.help_ import Help_ClientProtocol
    from ..endpoints.histories import HistoriesClientProtocol
    from ..endpoints.job_lock import JobLockClientProtocol
    from ..endpoints.jobs import JobsClientProtocol
    from ..endpoints.libraries import LibrariesClientProtocol
    from ..endpoints.licenses import LicensesClientProtocol
    from ..endpoints.metrics import MetricsClientProtocol
    from ..endpoints.notifications import NotificationsClientProtocol
    from ..endpoints.oauth_2 import Oauth2ClientProtocol
    from ..endpoints.object_stores import ObjectStoresClientProtocol
    from ..endpoints.pages import PagesClientProtocol
    from ..endpoints.quotas import QuotasClientProtocol
    from ..endpoints.remote_files import RemoteFilesClientProtocol
    from ..endpoints.roles import RolesClientProtocol
    from ..endpoints.short_term_storage import ShortTermStorageClientProtocol
    from ..endpoints.storage_management import StorageManagementClientProtocol
    from ..endpoints.tags import TagsClientProtocol
    from ..endpoints.tasks import TasksClientProtocol
    from ..endpoints.tool_data_tables import ToolDataTablesClientProtocol
    from ..endpoints.tool_shed_repositories import ToolShedRepositoriesClientProtocol
    from ..endpoints.tools import ToolsClientProtocol
    from ..endpoints.tours import ToursClientProtocol
    from ..endpoints.users import UsersClientProtocol
    from ..endpoints.utilities import UtilitiesClientProtocol
    from ..endpoints.visualizations import VisualizationsClientProtocol
    from ..endpoints.workflows import WorkflowsClientProtocol

from .endpoints.mock_ai import MockAiClient
from .endpoints.mock_authenticate import MockAuthenticateClient
from .endpoints.mock_chat import MockChatClient
from .endpoints.mock_configuration import MockConfigurationClient
from .endpoints.mock_context import MockContextClient
from .endpoints.mock_data_libraries_folders import MockDataLibrariesFoldersClient
from .endpoints.mock_dataset_collections import MockDatasetCollectionsClient
from .endpoints.mock_datasets import MockDatasetsClient
from .endpoints.mock_datatypes import MockDatatypesClient
from .endpoints.mock_display_applications import MockDisplayApplicationsClient
from .endpoints.mock_drs import MockDrsClient
from .endpoints.mock_dynamic_tools import MockDynamicToolsClient
from .endpoints.mock_file_sources import MockFileSourcesClient
from .endpoints.mock_forms import MockFormsClient
from .endpoints.mock_genomes import MockGenomesClient
from .endpoints.mock_group_roles import MockGroupRolesClient
from .endpoints.mock_group_users import MockGroupUsersClient
from .endpoints.mock_groups import MockGroupsClient
from .endpoints.mock_help_ import MockHelp_Client
from .endpoints.mock_histories import MockHistoriesClient
from .endpoints.mock_job_lock import MockJobLockClient
from .endpoints.mock_jobs import MockJobsClient
from .endpoints.mock_libraries import MockLibrariesClient
from .endpoints.mock_licenses import MockLicensesClient
from .endpoints.mock_metrics import MockMetricsClient
from .endpoints.mock_notifications import MockNotificationsClient
from .endpoints.mock_oauth_2 import MockOauth2Client
from .endpoints.mock_object_stores import MockObjectStoresClient
from .endpoints.mock_pages import MockPagesClient
from .endpoints.mock_quotas import MockQuotasClient
from .endpoints.mock_remote_files import MockRemoteFilesClient
from .endpoints.mock_roles import MockRolesClient
from .endpoints.mock_short_term_storage import MockShortTermStorageClient
from .endpoints.mock_storage_management import MockStorageManagementClient
from .endpoints.mock_tags import MockTagsClient
from .endpoints.mock_tasks import MockTasksClient
from .endpoints.mock_tool_data_tables import MockToolDataTablesClient
from .endpoints.mock_tool_shed_repositories import MockToolShedRepositoriesClient
from .endpoints.mock_tools import MockToolsClient
from .endpoints.mock_tours import MockToursClient
from .endpoints.mock_users import MockUsersClient
from .endpoints.mock_utilities import MockUtilitiesClient
from .endpoints.mock_visualizations import MockVisualizationsClient
from .endpoints.mock_workflows import MockWorkflowsClient


class MockAPIClient:
    """
    Mock implementation of APIClient for testing.

    Auto-creates default mock implementations for all tag-based endpoint clients.
    You can override specific tag clients by passing them to the constructor.

    Example:
        # Use all defaults
        client = MockAPIClient()

        # Override specific tag client
        class MyAiClientMock(MockAiClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data

        client = MockAPIClient(ai=MyAiClientMock())
    """

    def __init__(
        self,
        ai: "AiClientProtocol | None" = None,
        authenticate: "AuthenticateClientProtocol | None" = None,
        chat: "ChatClientProtocol | None" = None,
        configuration: "ConfigurationClientProtocol | None" = None,
        tools: "ToolsClientProtocol | None" = None,
        dataset_collections: "DatasetCollectionsClientProtocol | None" = None,
        histories: "HistoriesClientProtocol | None" = None,
        datasets: "DatasetsClientProtocol | None" = None,
        jobs: "JobsClientProtocol | None" = None,
        datatypes: "DatatypesClientProtocol | None" = None,
        display_applications: "DisplayApplicationsClientProtocol | None" = None,
        drs: "DrsClientProtocol | None" = None,
        dynamic_tools: "DynamicToolsClientProtocol | None" = None,
        file_sources: "FileSourcesClientProtocol | None" = None,
        data_libraries_folders: "DataLibrariesFoldersClientProtocol | None" = None,
        forms: "FormsClientProtocol | None" = None,
        remote_files: "RemoteFilesClientProtocol | None" = None,
        genomes: "GenomesClientProtocol | None" = None,
        groups: "GroupsClientProtocol | None" = None,
        group_roles: "GroupRolesClientProtocol | None" = None,
        group_users: "GroupUsersClientProtocol | None" = None,
        help_: "Help_ClientProtocol | None" = None,
        workflows: "WorkflowsClientProtocol | None" = None,
        job_lock: "JobLockClientProtocol | None" = None,
        libraries: "LibrariesClientProtocol | None" = None,
        licenses: "LicensesClientProtocol | None" = None,
        metrics: "MetricsClientProtocol | None" = None,
        notifications: "NotificationsClientProtocol | None" = None,
        object_stores: "ObjectStoresClientProtocol | None" = None,
        pages: "PagesClientProtocol | None" = None,
        utilities: "UtilitiesClientProtocol | None" = None,
        quotas: "QuotasClientProtocol | None" = None,
        roles: "RolesClientProtocol | None" = None,
        short_term_storage: "ShortTermStorageClientProtocol | None" = None,
        storage_management: "StorageManagementClientProtocol | None" = None,
        tags: "TagsClientProtocol | None" = None,
        tasks: "TasksClientProtocol | None" = None,
        tool_data_tables: "ToolDataTablesClientProtocol | None" = None,
        tool_shed_repositories: "ToolShedRepositoriesClientProtocol | None" = None,
        tours: "ToursClientProtocol | None" = None,
        users: "UsersClientProtocol | None" = None,
        visualizations: "VisualizationsClientProtocol | None" = None,
        context: "ContextClientProtocol | None" = None,
        oauth_2: "Oauth2ClientProtocol | None" = None,
    ) -> None:
        self._ai = ai if ai is not None else MockAiClient()
        self._authenticate = authenticate if authenticate is not None else MockAuthenticateClient()
        self._chat = chat if chat is not None else MockChatClient()
        self._configuration = configuration if configuration is not None else MockConfigurationClient()
        self._tools = tools if tools is not None else MockToolsClient()
        self._dataset_collections = (
            dataset_collections if dataset_collections is not None else MockDatasetCollectionsClient()
        )
        self._histories = histories if histories is not None else MockHistoriesClient()
        self._datasets = datasets if datasets is not None else MockDatasetsClient()
        self._jobs = jobs if jobs is not None else MockJobsClient()
        self._datatypes = datatypes if datatypes is not None else MockDatatypesClient()
        self._display_applications = (
            display_applications if display_applications is not None else MockDisplayApplicationsClient()
        )
        self._drs = drs if drs is not None else MockDrsClient()
        self._dynamic_tools = dynamic_tools if dynamic_tools is not None else MockDynamicToolsClient()
        self._file_sources = file_sources if file_sources is not None else MockFileSourcesClient()
        self._data_libraries_folders = (
            data_libraries_folders if data_libraries_folders is not None else MockDataLibrariesFoldersClient()
        )
        self._forms = forms if forms is not None else MockFormsClient()
        self._remote_files = remote_files if remote_files is not None else MockRemoteFilesClient()
        self._genomes = genomes if genomes is not None else MockGenomesClient()
        self._groups = groups if groups is not None else MockGroupsClient()
        self._group_roles = group_roles if group_roles is not None else MockGroupRolesClient()
        self._group_users = group_users if group_users is not None else MockGroupUsersClient()
        self._help_ = help_ if help_ is not None else MockHelp_Client()
        self._workflows = workflows if workflows is not None else MockWorkflowsClient()
        self._job_lock = job_lock if job_lock is not None else MockJobLockClient()
        self._libraries = libraries if libraries is not None else MockLibrariesClient()
        self._licenses = licenses if licenses is not None else MockLicensesClient()
        self._metrics = metrics if metrics is not None else MockMetricsClient()
        self._notifications = notifications if notifications is not None else MockNotificationsClient()
        self._object_stores = object_stores if object_stores is not None else MockObjectStoresClient()
        self._pages = pages if pages is not None else MockPagesClient()
        self._utilities = utilities if utilities is not None else MockUtilitiesClient()
        self._quotas = quotas if quotas is not None else MockQuotasClient()
        self._roles = roles if roles is not None else MockRolesClient()
        self._short_term_storage = (
            short_term_storage if short_term_storage is not None else MockShortTermStorageClient()
        )
        self._storage_management = (
            storage_management if storage_management is not None else MockStorageManagementClient()
        )
        self._tags = tags if tags is not None else MockTagsClient()
        self._tasks = tasks if tasks is not None else MockTasksClient()
        self._tool_data_tables = tool_data_tables if tool_data_tables is not None else MockToolDataTablesClient()
        self._tool_shed_repositories = (
            tool_shed_repositories if tool_shed_repositories is not None else MockToolShedRepositoriesClient()
        )
        self._tours = tours if tours is not None else MockToursClient()
        self._users = users if users is not None else MockUsersClient()
        self._visualizations = visualizations if visualizations is not None else MockVisualizationsClient()
        self._context = context if context is not None else MockContextClient()
        self._oauth_2 = oauth_2 if oauth_2 is not None else MockOauth2Client()

    @property
    def ai(self) -> "AiClientProtocol":
        return self._ai

    @property
    def authenticate(self) -> "AuthenticateClientProtocol":
        return self._authenticate

    @property
    def chat(self) -> "ChatClientProtocol":
        return self._chat

    @property
    def configuration(self) -> "ConfigurationClientProtocol":
        return self._configuration

    @property
    def tools(self) -> "ToolsClientProtocol":
        return self._tools

    @property
    def dataset_collections(self) -> "DatasetCollectionsClientProtocol":
        return self._dataset_collections

    @property
    def histories(self) -> "HistoriesClientProtocol":
        return self._histories

    @property
    def datasets(self) -> "DatasetsClientProtocol":
        return self._datasets

    @property
    def jobs(self) -> "JobsClientProtocol":
        return self._jobs

    @property
    def datatypes(self) -> "DatatypesClientProtocol":
        return self._datatypes

    @property
    def display_applications(self) -> "DisplayApplicationsClientProtocol":
        return self._display_applications

    @property
    def drs(self) -> "DrsClientProtocol":
        return self._drs

    @property
    def dynamic_tools(self) -> "DynamicToolsClientProtocol":
        return self._dynamic_tools

    @property
    def file_sources(self) -> "FileSourcesClientProtocol":
        return self._file_sources

    @property
    def data_libraries_folders(self) -> "DataLibrariesFoldersClientProtocol":
        return self._data_libraries_folders

    @property
    def forms(self) -> "FormsClientProtocol":
        return self._forms

    @property
    def remote_files(self) -> "RemoteFilesClientProtocol":
        return self._remote_files

    @property
    def genomes(self) -> "GenomesClientProtocol":
        return self._genomes

    @property
    def groups(self) -> "GroupsClientProtocol":
        return self._groups

    @property
    def group_roles(self) -> "GroupRolesClientProtocol":
        return self._group_roles

    @property
    def group_users(self) -> "GroupUsersClientProtocol":
        return self._group_users

    @property
    def help_(self) -> "Help_ClientProtocol":
        return self._help_

    @property
    def workflows(self) -> "WorkflowsClientProtocol":
        return self._workflows

    @property
    def job_lock(self) -> "JobLockClientProtocol":
        return self._job_lock

    @property
    def libraries(self) -> "LibrariesClientProtocol":
        return self._libraries

    @property
    def licenses(self) -> "LicensesClientProtocol":
        return self._licenses

    @property
    def metrics(self) -> "MetricsClientProtocol":
        return self._metrics

    @property
    def notifications(self) -> "NotificationsClientProtocol":
        return self._notifications

    @property
    def object_stores(self) -> "ObjectStoresClientProtocol":
        return self._object_stores

    @property
    def pages(self) -> "PagesClientProtocol":
        return self._pages

    @property
    def utilities(self) -> "UtilitiesClientProtocol":
        return self._utilities

    @property
    def quotas(self) -> "QuotasClientProtocol":
        return self._quotas

    @property
    def roles(self) -> "RolesClientProtocol":
        return self._roles

    @property
    def short_term_storage(self) -> "ShortTermStorageClientProtocol":
        return self._short_term_storage

    @property
    def storage_management(self) -> "StorageManagementClientProtocol":
        return self._storage_management

    @property
    def tags(self) -> "TagsClientProtocol":
        return self._tags

    @property
    def tasks(self) -> "TasksClientProtocol":
        return self._tasks

    @property
    def tool_data_tables(self) -> "ToolDataTablesClientProtocol":
        return self._tool_data_tables

    @property
    def tool_shed_repositories(self) -> "ToolShedRepositoriesClientProtocol":
        return self._tool_shed_repositories

    @property
    def tours(self) -> "ToursClientProtocol":
        return self._tours

    @property
    def users(self) -> "UsersClientProtocol":
        return self._users

    @property
    def visualizations(self) -> "VisualizationsClientProtocol":
        return self._visualizations

    @property
    def context(self) -> "ContextClientProtocol":
        return self._context

    @property
    def oauth_2(self) -> "Oauth2ClientProtocol":
        return self._oauth_2

    async def request(self, method: str, url: str, **kwargs: Any) -> Any:
        """
        Mock request method - raises NotImplementedError.

        This is a low-level method - consider using tag-specific methods instead.
        """
        raise NotImplementedError("MockAPIClient.request() not implemented. Use tag-specific methods instead.")

    async def close(self) -> None:
        """Mock close method - no-op for testing."""
        pass  # No cleanup needed for mocks

    async def __aenter__(self) -> "APIClientProtocol":
        """Enter async context manager."""
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: object | None
    ) -> None:
        """Exit async context manager - no-op for mocks."""
        pass  # No cleanup needed for mocks
