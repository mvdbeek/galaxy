"""
Mock implementations for testing.

These mocks implement the Protocol contracts without requiring
network transport or authentication. Use them as base classes
in your tests.

Example:
    from myapi.mocks import MockAPIClient, MockPetsClient

    class TestPetsClient(MockPetsClient):
        async def list_pets(self, limit: int | None = None) -> list[Pet]:
            return [Pet(id=1, name='Test Pet')]

    client = MockAPIClient(pets=TestPetsClient())
"""

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
from .mock_client import MockAPIClient

__all__ = [
    "MockAPIClient",
    "MockAiClient",
    "MockAuthenticateClient",
    "MockChatClient",
    "MockConfigurationClient",
    "MockContextClient",
    "MockDataLibrariesFoldersClient",
    "MockDatasetCollectionsClient",
    "MockDatasetsClient",
    "MockDatatypesClient",
    "MockDisplayApplicationsClient",
    "MockDrsClient",
    "MockDynamicToolsClient",
    "MockFileSourcesClient",
    "MockFormsClient",
    "MockGenomesClient",
    "MockGroupRolesClient",
    "MockGroupUsersClient",
    "MockGroupsClient",
    "MockHelp_Client",
    "MockHistoriesClient",
    "MockJobLockClient",
    "MockJobsClient",
    "MockLibrariesClient",
    "MockLicensesClient",
    "MockMetricsClient",
    "MockNotificationsClient",
    "MockOauth2Client",
    "MockObjectStoresClient",
    "MockPagesClient",
    "MockQuotasClient",
    "MockRemoteFilesClient",
    "MockRolesClient",
    "MockShortTermStorageClient",
    "MockStorageManagementClient",
    "MockTagsClient",
    "MockTasksClient",
    "MockToolDataTablesClient",
    "MockToolShedRepositoriesClient",
    "MockToolsClient",
    "MockToursClient",
    "MockUsersClient",
    "MockUtilitiesClient",
    "MockVisualizationsClient",
    "MockWorkflowsClient",
]
