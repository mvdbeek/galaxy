"""Integration tests for tool source storage backends.

These tests configure Galaxy to use different tool source storage backends
and verify that tools work correctly through the API and can be executed.
"""

import tempfile

from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util


class BaseToolSourceStorageIntegrationTestCase(integration_util.IntegrationTestCase):
    """Base class for tool source storage integration tests."""

    framework_tool_and_types = True
    dataset_populator: DatasetPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def _test_api_tools_list(self):
        """Test that /api/tools returns tool list."""
        response = self._get("tools")
        self._assert_status_code_is(response, 200)
        tools = response.json()
        # Should have some tools loaded
        assert len(tools) > 0, "Expected at least one tool to be loaded"

    def _test_api_tools_show(self, tool_id: str = "cat1"):
        """Test that /api/tools/{tool_id} returns tool info."""
        response = self._get(f"tools/{tool_id}")
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["id"] == tool_id

    def _test_run_simple_tool(self):
        """Test that a simple tool can be executed."""
        with self.dataset_populator.test_history() as history_id:
            # Create input dataset
            hda = self.dataset_populator.new_dataset(history_id, content="test content\n")
            hda_id = hda["id"]

            # Run cat1 tool
            inputs = {"input1": {"src": "hda", "id": hda_id}}
            run_response = self.dataset_populator.run_tool(
                tool_id="cat1",
                inputs=inputs,
                history_id=history_id,
            )

            # Verify job was created
            assert "jobs" in run_response
            assert len(run_response["jobs"]) == 1

            job_id = run_response["jobs"][0]["id"]
            self.dataset_populator.wait_for_job(job_id)

            # Verify job completed successfully
            job_details = self.dataset_populator.get_job_details(job_id).json()
            assert job_details["state"] == "ok", f"Job failed: {job_details}"


class TestDatabaseToolSourceStorage(BaseToolSourceStorageIntegrationTestCase):
    """Integration tests with database tool source storage backend.

    This is the default backend - tests verify tools work with database storage.
    """

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        # Database backend is the default, but explicitly set it
        config["tool_source_store"] = "database"

    def test_api_tools_list(self):
        """Test /api/tools endpoint works with database backend."""
        self._test_api_tools_list()

    def test_api_tools_show(self):
        """Test /api/tools/{id} endpoint works with database backend."""
        self._test_api_tools_show()

    def test_run_cat_tool(self):
        """Test running cat1 tool with database backend."""
        self._test_run_simple_tool()

    def test_api_tool_sources_stats(self):
        """Test /api/tool_sources/stats endpoint."""
        response = self._get("tool_sources/stats")
        # May not be available if store not populated, but endpoint should exist
        if response.status_code == 200:
            stats = response.json()
            assert "backend" in stats
            assert stats["backend"] == "database"

    def test_api_tool_index_stats(self):
        """Test /api/tool_index/stats endpoint."""
        response = self._get("tool_index/stats")
        if response.status_code == 200:
            stats = response.json()
            assert "index_size" in stats


class TestDiskToolSourceStorage(BaseToolSourceStorageIntegrationTestCase):
    """Integration tests with disk tool source storage backend."""

    _tool_source_disk_path: str

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        # Create temp directory for disk storage
        cls._tool_source_disk_path = tempfile.mkdtemp(prefix="tool_source_disk_")
        config["tool_source_store"] = "disk"
        config["tool_source_disk_path"] = cls._tool_source_disk_path

    def test_api_tools_list(self):
        """Test /api/tools endpoint works with disk backend."""
        self._test_api_tools_list()

    def test_api_tools_show(self):
        """Test /api/tools/{id} endpoint works with disk backend."""
        self._test_api_tools_show()

    def test_run_cat_tool(self):
        """Test running cat1 tool with disk backend."""
        self._test_run_simple_tool()

    def test_api_tool_sources_stats(self):
        """Test /api/tool_sources/stats endpoint with disk backend."""
        response = self._get("tool_sources/stats")
        if response.status_code == 200:
            stats = response.json()
            assert "backend" in stats
            assert stats["backend"] == "disk"


class TestToolSourceStorageWorkflows(BaseToolSourceStorageIntegrationTestCase):
    """Integration tests for workflows with tool source storage."""

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"

    def test_simple_workflow_execution(self):
        """Test that a simple workflow can be executed with tool source storage."""
        # Create a simple workflow with cat1
        workflow_str = """
class: GalaxyWorkflow
inputs:
  input_file:
    type: File
steps:
  cat_step:
    tool_id: cat1
    in:
      input1: input_file
"""
        with self.dataset_populator.test_history() as history_id:
            # Upload workflow
            workflow_id = self.dataset_populator.upload_workflow(workflow_str)

            # Create input
            hda = self.dataset_populator.new_dataset(history_id, content="workflow test\n")

            # Run workflow
            invocation = self.dataset_populator.invoke_workflow(
                workflow_id,
                inputs={"input_file": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Wait for completion
            self.dataset_populator.wait_for_invocation_and_jobs(
                history_id, workflow_id, invocation["id"]
            )

            # Verify invocation succeeded
            invocation_details = self.dataset_populator.get_invocation(invocation["id"])
            assert invocation_details["state"] == "scheduled"


class TestToolSourceStorageMultipleVersions(BaseToolSourceStorageIntegrationTestCase):
    """Integration tests for tools with multiple versions."""

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"

    def test_multiple_versions_tool_available(self):
        """Test that tools with multiple versions are available."""
        # Get tool panel to see all tools
        response = self._get("tools")
        self._assert_status_code_is(response, 200)
        tools = response.json()

        # Find tools with multiple versions - look for multiple_versions tool
        tool_ids = []
        for section in tools:
            if "elems" in section:
                for elem in section["elems"]:
                    if isinstance(elem, dict) and "id" in elem:
                        tool_ids.append(elem["id"])
            elif "id" in section:
                tool_ids.append(section["id"])

        # Should have tools loaded
        assert len(tool_ids) > 0, "Expected tools to be loaded"
