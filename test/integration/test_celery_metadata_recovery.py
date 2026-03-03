"""Integration tests for recovery of jobs interrupted during celery metadata setting."""

import os

from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util

SCRIPT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
SIMPLE_JOB_CONFIG_FILE = os.path.join(SCRIPT_DIRECTORY, "simple_job_conf.xml")


class TestCeleryMetadataJobRecovery(integration_util.IntegrationTestCase):
    """Test that jobs interrupted during celery metadata setting recover after restart.

    Uses the server_name trick: start Galaxy with server_name="moo" so the
    handler doesn't pick up jobs, then restart with server_name="main" to
    trigger recovery via ``_check_job_at_startup``.
    """

    dataset_populator: DatasetPopulator
    framework_tool_and_types = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["metadata_strategy"] = "directory_celery"
        config["job_config_file"] = SIMPLE_JOB_CONFIG_FILE
        config["server_name"] = "moo"

    def handle_reconfigure_galaxy_config_kwds(self, config):
        config["server_name"] = "main"

    def test_recovery(self):
        history_id = self.dataset_populator.new_history()
        self.dataset_populator.run_tool_raw(
            "exit_code_oom",
            {},
            history_id,
        )
        self.restart(handle_reconfig=self.handle_reconfigure_galaxy_config_kwds)
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.dataset_populator.wait_for_history(history_id, assert_ok=True)
