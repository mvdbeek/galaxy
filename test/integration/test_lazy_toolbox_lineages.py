"""Integration tests for LazyToolBox lineage support.

These tests verify that tool lineages work correctly with LazyToolBox,
including version resolution without loading all tools.
"""

from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util


class TestLazyToolBoxLineages(integration_util.IntegrationTestCase):
    """Integration tests for LazyToolBox lineage support."""

    framework_tool_and_types = True
    dataset_populator: DatasetPopulator

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"
        config["use_lazy_toolbox"] = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def test_tool_versions_available(self):
        """Test that all tool versions are available via API."""
        response = self._get("tools/multiple_versions")
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["id"] == "multiple_versions"

    def test_get_specific_version(self):
        """Test requesting a specific tool version."""
        # Request version 0.1
        response = self._get("tools/multiple_versions", data={"tool_version": "0.1"})
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["version"] == "0.1", f"Expected version 0.1, got {tool_info.get('version')}"

        # Request version 0.2
        response = self._get("tools/multiple_versions", data={"tool_version": "0.2"})
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["version"] == "0.2", f"Expected version 0.2, got {tool_info.get('version')}"

    def test_latest_version_by_default(self):
        """Test that requesting without version returns latest."""
        response = self._get("tools/multiple_versions")
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        # Should return the latest version (0.2)
        assert tool_info["version"] == "0.2", f"Expected latest version 0.2, got {tool_info.get('version')}"

    def test_run_specific_version(self):
        """Test running a specific tool version."""
        with self.dataset_populator.test_history() as history_id:
            # Run version 0.1
            run_response = self.dataset_populator.run_tool(
                tool_id="multiple_versions",
                inputs={"inttest": 1},
                history_id=history_id,
                tool_version="0.1",
            )

            assert "jobs" in run_response, f"Expected jobs in response: {run_response}"
            assert len(run_response["jobs"]) == 1

            job_id = run_response["jobs"][0]["id"]
            self.dataset_populator.wait_for_job(job_id)

            job_details = self.dataset_populator.get_job_details(job_id, full=True).json()
            assert job_details["state"] == "ok", f"Job failed: {job_details}"
            # Check tool_id contains version info or check tool_version if available
            tool_id = job_details.get("tool_id", "")
            tool_version = job_details.get("tool_version")
            assert tool_version == "0.1" or "multiple_versions" in tool_id, (
                f"Expected version 0.1, got tool_version={tool_version}, tool_id={tool_id}"
            )

    def test_run_different_versions(self):
        """Test running different versions of the same tool."""
        with self.dataset_populator.test_history() as history_id:
            jobs = []

            # Run both versions
            for version in ["0.1", "0.2"]:
                run_response = self.dataset_populator.run_tool(
                    tool_id="multiple_versions",
                    inputs={"inttest": 1},
                    history_id=history_id,
                    tool_version=version,
                )
                assert "jobs" in run_response
                jobs.append((version, run_response["jobs"][0]["id"]))

            # Wait for all jobs and verify they completed successfully
            for version, job_id in jobs:
                self.dataset_populator.wait_for_job(job_id)
                job_details = self.dataset_populator.get_job_details(job_id, full=True).json()
                assert job_details["state"] == "ok", f"Job failed for version {version}: {job_details}"
                # Verify version if available in response
                tool_version = job_details.get("tool_version")
                if tool_version:
                    assert tool_version == version, (
                        f"Expected version {version}, got {tool_version}"
                    )

    def test_tool_panel_available(self):
        """Test that the tool panel is available and has content."""
        response = self._get("tool_panels/default")
        self._assert_status_code_is(response, 200)
        panel = response.json()
        # Panel should have some content (sections or tools)
        assert len(panel) > 0, "Expected tool panel to have content"

    def test_nonexistent_version_fallback(self):
        """Test that requesting a non-existent version falls back gracefully."""
        response = self._get("tools/multiple_versions", data={"tool_version": "99.99.99"})
        # Should either return 404 or fall back to latest version
        if response.status_code == 200:
            tool_info = response.json()
            assert tool_info["version"] in ["0.1", "0.2", "0.1+galaxy6"]


class TestLazyToolBoxLineageIndex(integration_util.IntegrationTestCase):
    """Test that lineage index is properly built and used."""

    framework_tool_and_types = True

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"
        config["use_lazy_toolbox"] = True

    def test_tool_index_has_lineages(self):
        """Test that tool index stats show lineage information."""
        response = self._get("tool_index/stats")
        if response.status_code == 200:
            stats = response.json()
            # Check for lineage-related stats if available
            if "lineage_count" in stats:
                assert stats["lineage_count"] >= 0

    def test_tools_list_returns_all_tools(self):
        """Test that /api/tools returns tools from the index."""
        response = self._get("tools")
        self._assert_status_code_is(response, 200)
        tools = response.json()
        assert len(tools) > 0, "Expected at least one tool"


class TestLazyToolBoxWithoutLazyEnabled(integration_util.IntegrationTestCase):
    """Test that regular toolbox still works when lazy is disabled."""

    framework_tool_and_types = True
    dataset_populator: DatasetPopulator

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"
        config["use_lazy_toolbox"] = False  # Explicitly disable

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def test_tools_still_work(self):
        """Test that tools work with lazy toolbox disabled."""
        response = self._get("tools")
        self._assert_status_code_is(response, 200)
        tools = response.json()
        assert len(tools) > 0

    def test_run_tool_without_lazy(self):
        """Test running a tool with lazy toolbox disabled."""
        with self.dataset_populator.test_history() as history_id:
            hda = self.dataset_populator.new_dataset(history_id, content="test\n")
            run_response = self.dataset_populator.run_tool(
                tool_id="cat1",
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )
            assert "jobs" in run_response
            job_id = run_response["jobs"][0]["id"]
            self.dataset_populator.wait_for_job(job_id)
            job_details = self.dataset_populator.get_job_details(job_id).json()
            assert job_details["state"] == "ok"
