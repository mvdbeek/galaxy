from galaxy_test.api.test_histories import ImportExportHistory
from galaxy_test.base.populators import (
    DatasetCollectionPopulator,
    DatasetPopulator,
)
from galaxy_test.driver import integration_util


class ImportExportHistoryOutputsToWorkingDirTestCase(integration_util.IntegrationTestCase, ImportExportHistory):

    framework_tool_and_types = True

    def setUp(self):
        super(ImportExportHistoryOutputsToWorkingDirTestCase, self).setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.dataset_collection_populator = DatasetCollectionPopulator(self.galaxy_interactor)

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        config['outputs_to_working_directory'] = True
