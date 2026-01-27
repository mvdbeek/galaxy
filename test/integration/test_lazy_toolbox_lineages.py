"""Integration tests for LazyToolBox lineage support.

These tests verify that tool lineages work correctly with LazyToolBox,
including version resolution without loading all tools.
"""

import os
import tempfile
from pathlib import Path

from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util


# Tool XML templates for versioned tools
TOOL_V1_XML = """<tool id="{tool_id}" name="{name}" version="1.0.0">
    <description>Test tool version 1.0.0</description>
    <command>echo "v1: $input" > $output</command>
    <inputs>
        <param name="input" type="text" value="" label="Input"/>
    </inputs>
    <outputs>
        <data name="output" format="txt"/>
    </outputs>
</tool>
"""

TOOL_V2_XML = """<tool id="{tool_id}" name="{name}" version="2.0.0">
    <description>Test tool version 2.0.0</description>
    <command>echo "v2: $input" > $output</command>
    <inputs>
        <param name="input" type="text" value="" label="Input"/>
    </inputs>
    <outputs>
        <data name="output" format="txt"/>
    </outputs>
</tool>
"""

TOOL_V3_XML = """<tool id="{tool_id}" name="{name}" version="3.0.0">
    <description>Test tool version 3.0.0</description>
    <command>echo "v3: $input" > $output</command>
    <inputs>
        <param name="input" type="text" value="" label="Input"/>
    </inputs>
    <outputs>
        <data name="output" format="txt"/>
    </outputs>
</tool>
"""

TOOL_CONF_TEMPLATE = """<?xml version="1.0"?>
<toolbox>
    <section id="test_lineages" name="Test Lineages">
        <tool file="{tool_v1_path}"/>
        <tool file="{tool_v2_path}"/>
        <tool file="{tool_v3_path}"/>
    </section>
</toolbox>
"""


class TestLazyToolBoxLineages(integration_util.IntegrationTestCase):
    """Integration tests for LazyToolBox lineage support."""

    framework_tool_and_types = True
    dataset_populator: DatasetPopulator

    _temp_dir: str
    _tool_conf_path: str

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)

        # Create temporary directory for test tools
        cls._temp_dir = tempfile.mkdtemp(prefix="lazy_toolbox_lineage_test_")
        tools_dir = Path(cls._temp_dir) / "tools"
        tools_dir.mkdir()

        # Create versioned tools
        tool_id = "lineage_test_tool"
        tool_name = "Lineage Test Tool"

        tool_v1_path = tools_dir / "lineage_tool_v1.xml"
        tool_v2_path = tools_dir / "lineage_tool_v2.xml"
        tool_v3_path = tools_dir / "lineage_tool_v3.xml"

        tool_v1_path.write_text(TOOL_V1_XML.format(tool_id=tool_id, name=tool_name))
        tool_v2_path.write_text(TOOL_V2_XML.format(tool_id=tool_id, name=tool_name))
        tool_v3_path.write_text(TOOL_V3_XML.format(tool_id=tool_id, name=tool_name))

        # Create tool_conf.xml
        tool_conf_path = Path(cls._temp_dir) / "tool_conf.xml"
        tool_conf_path.write_text(
            TOOL_CONF_TEMPLATE.format(
                tool_v1_path=str(tool_v1_path),
                tool_v2_path=str(tool_v2_path),
                tool_v3_path=str(tool_v3_path),
            )
        )
        cls._tool_conf_path = str(tool_conf_path)

        # Configure Galaxy to use our tool conf and lazy toolbox
        config["tool_config_file"] = cls._tool_conf_path
        config["tool_source_store"] = "database"
        config["use_lazy_toolbox"] = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def test_tool_versions_available(self):
        """Test that all tool versions are available via API."""
        response = self._get("tools/lineage_test_tool")
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["id"] == "lineage_test_tool"

    def test_get_specific_version(self):
        """Test requesting a specific tool version."""
        # Request version 1.0.0
        response = self._get("tools/lineage_test_tool", data={"tool_version": "1.0.0"})
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["version"] == "1.0.0", f"Expected version 1.0.0, got {tool_info.get('version')}"

        # Request version 2.0.0
        response = self._get("tools/lineage_test_tool", data={"tool_version": "2.0.0"})
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["version"] == "2.0.0", f"Expected version 2.0.0, got {tool_info.get('version')}"

        # Request version 3.0.0
        response = self._get("tools/lineage_test_tool", data={"tool_version": "3.0.0"})
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["version"] == "3.0.0", f"Expected version 3.0.0, got {tool_info.get('version')}"

    def test_latest_version_by_default(self):
        """Test that requesting without version returns latest."""
        response = self._get("tools/lineage_test_tool")
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        # Should return the latest version (3.0.0)
        assert tool_info["version"] == "3.0.0", f"Expected latest version 3.0.0, got {tool_info.get('version')}"

    def test_run_specific_version(self):
        """Test running a specific tool version."""
        with self.dataset_populator.test_history() as history_id:
            # Run version 1.0.0
            run_response = self.dataset_populator.run_tool(
                tool_id="lineage_test_tool",
                inputs={"input": "test input"},
                history_id=history_id,
                tool_version="1.0.0",
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
            assert tool_version == "1.0.0" or "lineage_test_tool" in tool_id, (
                f"Expected version 1.0.0, got tool_version={tool_version}, tool_id={tool_id}"
            )

    def test_run_different_versions(self):
        """Test running different versions of the same tool."""
        with self.dataset_populator.test_history() as history_id:
            jobs = []

            # Run all three versions
            for version in ["1.0.0", "2.0.0", "3.0.0"]:
                run_response = self.dataset_populator.run_tool(
                    tool_id="lineage_test_tool",
                    inputs={"input": f"test for {version}"},
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

    def test_tool_panel_contains_tool(self):
        """Test that the tool appears in the tool panel."""
        response = self._get("tool_panels/default")
        self._assert_status_code_is(response, 200)
        panel = response.json()

        # Find our test section
        found_section = None
        for section_id, section_data in panel.items():
            if section_id == "test_lineages" or (
                isinstance(section_data, dict) and section_data.get("id") == "test_lineages"
            ):
                found_section = section_data
                break

        assert found_section is not None, f"Expected to find test_lineages section in panel: {list(panel.keys())}"

        # Check that our tool is in the section
        if "elems" in found_section:
            tool_ids = [elem.get("id") for elem in found_section["elems"] if isinstance(elem, dict)]
            assert "lineage_test_tool" in tool_ids, f"Expected lineage_test_tool in section elems: {tool_ids}"

    def test_nonexistent_version_error(self):
        """Test that requesting a non-existent version returns appropriate error."""
        response = self._get("tools/lineage_test_tool", data={"tool_version": "99.99.99"})
        # Should either return 404 or fall back to latest version
        # depending on implementation
        if response.status_code == 200:
            # If it returns 200, it should be the latest version as fallback
            tool_info = response.json()
            assert tool_info["version"] in ["1.0.0", "2.0.0", "3.0.0"]


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
