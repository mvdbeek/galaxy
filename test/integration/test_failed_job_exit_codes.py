"""Failed tools keep their stdout, stderr and exit code with and without job metrics."""

import os
from typing import (
    Any,
    ClassVar,
)

from galaxy_test.base.populators import (
    DatasetPopulator,
    skip_without_tool,
)
from galaxy_test.driver import integration_util

SCRIPT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
SIMPLE_JOB_CONFIG_FILE = os.path.join(SCRIPT_DIRECTORY, "simple_job_conf.xml")
EMBEDDED_PULSAR_JOB_CONFIG_FILE = os.path.join(SCRIPT_DIRECTORY, "embedded_pulsar_job_conf.yml")

CORE_JOB_METRICS = [{"type": "core"}]
NO_JOB_METRICS: list[dict[str, Any]] = []


def configure_job_metrics(config, job_metrics):
    config["job_metrics"] = job_metrics
    # Point away from the default file, which would take precedence over job_metrics.
    config["job_metrics_config_file"] = "job_metrics_conf_not_used.xml"


class FailedToolAssertions:
    dataset_populator: DatasetPopulator

    def _run_failing_tool(self):
        with self.dataset_populator.test_history() as history_id:
            response = self.dataset_populator.run_tool_raw(
                "job_properties", {"thebool": True, "failbool": True}, history_id
            )
            result = self.dataset_populator.wait_for_tool_run(
                run_response=response, history_id=history_id, assert_ok=False
            ).json()
            return self.dataset_populator.get_job_details(result["jobs"][0]["id"], full=True).json()

    def _assert_failed_tool_details(self, details):
        assert details["state"] == "error", details
        assert details["tool_stdout"] == "The bool is true\n", details
        assert details["tool_stderr"] == "The bool is really true\n", details
        assert details["exit_code"] == 127, details


class BaseFailedToolIntegrationTestCase(FailedToolAssertions, integration_util.IntegrationTestCase):
    framework_tool_and_types = True
    job_config_file: ClassVar[str]
    job_metrics: ClassVar[list[dict[str, Any]]]

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["job_config_file"] = cls.job_config_file
        configure_job_metrics(config, cls.job_metrics)

    @skip_without_tool("job_properties")
    def test_failed_tool_keeps_stdio_and_exit_code(self):
        self._assert_failed_tool_details(self._run_failing_tool())


class TestLocalFailedToolIntegration(BaseFailedToolIntegrationTestCase):
    job_config_file = SIMPLE_JOB_CONFIG_FILE
    job_metrics = CORE_JOB_METRICS


class TestLocalFailedToolWithoutMetricsIntegration(BaseFailedToolIntegrationTestCase):
    job_config_file = SIMPLE_JOB_CONFIG_FILE
    job_metrics = NO_JOB_METRICS


class TestEmbeddedPulsarFailedToolIntegration(BaseFailedToolIntegrationTestCase):
    job_config_file = EMBEDDED_PULSAR_JOB_CONFIG_FILE
    job_metrics = CORE_JOB_METRICS


class TestEmbeddedPulsarFailedToolWithoutMetricsIntegration(BaseFailedToolIntegrationTestCase):
    job_config_file = EMBEDDED_PULSAR_JOB_CONFIG_FILE
    job_metrics = NO_JOB_METRICS
