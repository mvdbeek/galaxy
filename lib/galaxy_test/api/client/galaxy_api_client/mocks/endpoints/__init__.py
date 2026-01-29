"""
Mock endpoint clients for testing.

Import mock classes to use as base classes for your test doubles.
"""

from .mock_ai import MockAiClient
from .mock_authenticate import MockAuthenticateClient
from .mock_chat import MockChatClient
from .mock_configuration import MockConfigurationClient
from .mock_context import MockContextClient
from .mock_data_libraries_folders import MockDataLibrariesFoldersClient
from .mock_dataset_collections import MockDatasetCollectionsClient
from .mock_datasets import MockDatasetsClient
from .mock_datatypes import MockDatatypesClient
from .mock_display_applications import MockDisplayApplicationsClient
from .mock_drs import MockDrsClient
from .mock_dynamic_tools import MockDynamicToolsClient
from .mock_file_sources import MockFileSourcesClient
from .mock_forms import MockFormsClient
from .mock_genomes import MockGenomesClient
from .mock_group_roles import MockGroupRolesClient
from .mock_group_users import MockGroupUsersClient
from .mock_groups import MockGroupsClient
from .mock_help_ import MockHelp_Client
from .mock_histories import MockHistoriesClient
from .mock_job_lock import MockJobLockClient
from .mock_jobs import MockJobsClient
from .mock_libraries import MockLibrariesClient
from .mock_licenses import MockLicensesClient
from .mock_metrics import MockMetricsClient
from .mock_notifications import MockNotificationsClient
from .mock_oauth_2 import MockOauth2Client
from .mock_object_stores import MockObjectStoresClient
from .mock_pages import MockPagesClient
from .mock_quotas import MockQuotasClient
from .mock_remote_files import MockRemoteFilesClient
from .mock_roles import MockRolesClient
from .mock_short_term_storage import MockShortTermStorageClient
from .mock_storage_management import MockStorageManagementClient
from .mock_tags import MockTagsClient
from .mock_tasks import MockTasksClient
from .mock_tool_data_tables import MockToolDataTablesClient
from .mock_tool_shed_repositories import MockToolShedRepositoriesClient
from .mock_tools import MockToolsClient
from .mock_tours import MockToursClient
from .mock_users import MockUsersClient
from .mock_utilities import MockUtilitiesClient
from .mock_visualizations import MockVisualizationsClient
from .mock_workflows import MockWorkflowsClient

__all__ = [
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
