"""Integration tests for tool source storage backends.

These tests configure Galaxy to use different tool source storage backends
and verify that tools work correctly through the API and can be executed.
"""

import os
import tempfile

from galaxy_test.base.populators import (
    DatasetPopulator,
    WorkflowPopulator,
)
from galaxy_test.driver import integration_util


class BaseToolSourceStorageIntegrationTestCase(integration_util.IntegrationTestCase):
    """Base class for tool source storage integration tests."""

    framework_tool_and_types = True
    dataset_populator: DatasetPopulator
    workflow_populator: WorkflowPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.workflow_populator = WorkflowPopulator(self.galaxy_interactor)

    def _test_api_tools_list(self):
        response = self._get("tools")
        self._assert_status_code_is(response, 200)
        tools = response.json()
        assert len(tools) > 0, "Expected at least one tool to be loaded"

    def _test_api_tools_show(self, tool_id: str = "cat1"):
        response = self._get(f"tools/{tool_id}")
        self._assert_status_code_is(response, 200)
        tool_info = response.json()
        assert tool_info["id"] == tool_id

    def _test_run_simple_tool(self):
        with self.dataset_populator.test_history() as history_id:
            hda = self.dataset_populator.new_dataset(history_id, content="test content\n")
            hda_id = hda["id"]

            inputs = {"input1": {"src": "hda", "id": hda_id}}
            run_response = self.dataset_populator.run_tool(
                tool_id="cat1",
                inputs=inputs,
                history_id=history_id,
            )

            assert "jobs" in run_response
            assert len(run_response["jobs"]) == 1

            job_id = run_response["jobs"][0]["id"]
            self.dataset_populator.wait_for_job(job_id)

            job_details = self.dataset_populator.get_job_details(job_id).json()
            assert job_details["state"] == "ok", f"Job failed: {job_details}"


class TestDatabaseToolSourceStorage(BaseToolSourceStorageIntegrationTestCase):
    """Integration tests with database tool source storage backend."""

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"

    def test_api_tools_list(self):
        self._test_api_tools_list()

    def test_api_tools_show(self):
        self._test_api_tools_show()

    def test_run_cat_tool(self):
        self._test_run_simple_tool()


class TestToolSourceStorageWorkflows(BaseToolSourceStorageIntegrationTestCase):
    """Integration tests for workflows with tool source storage."""

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"

    def test_simple_workflow_execution(self):
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
            workflow_id = self.workflow_populator.upload_yaml_workflow(workflow_str)
            hda = self.dataset_populator.new_dataset(history_id, content="workflow test\n")
            invocation_id = self.workflow_populator.invoke_workflow_and_assert_ok(
                workflow_id,
                inputs={"input_file": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )
            self.workflow_populator.wait_for_invocation_and_jobs(history_id, workflow_id, invocation_id)
            invocation_details = self.workflow_populator.get_invocation(invocation_id)
            assert invocation_details["state"] == "scheduled"


class TestCompositeToolSourceStorage(BaseToolSourceStorageIntegrationTestCase):
    """Galaxy boots with a default DB store + a per-conf read-only sqlite store.

    Verifies the composite wiring: a tool_conf carrying ``store="cvmfs_main"``
    plus ``use_lazy_toolbox: true`` causes ``build_tool_source_store`` to wrap
    the default backend in a composite. We exercise the wiring end-to-end by
    booting Galaxy and confirming /api/tools still serves the framework tools
    through the LazyToolBox.
    """

    _sqlite_path: str
    _conf_path: str
    _tmpdir: str

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        cls._tmpdir = tempfile.mkdtemp(prefix="composite_tss_")
        cls._sqlite_path = os.path.join(cls._tmpdir, "sources.sqlite")

        from galaxy.tool_source_store.sqlalchemy import SqlAlchemyToolSourceStore

        SqlAlchemyToolSourceStore(path=cls._sqlite_path).count()

        cls._conf_path = os.path.join(cls._tmpdir, "extra_tool_conf.xml")
        with open(cls._conf_path, "w") as f:
            f.write('<?xml version="1.0"?>\n<toolbox store="cvmfs_main"/>\n')

        config["tool_source_store"] = "database"
        config["use_lazy_toolbox"] = True
        existing_confs = config.get("tool_config_file") or "config/tool_conf.xml.sample"
        if isinstance(existing_confs, str):
            config["tool_config_file"] = f"{existing_confs},{cls._conf_path}"
        else:
            config["tool_config_file"] = list(existing_confs) + [cls._conf_path]
        config["tool_source_stores"] = {
            "cvmfs_main": {
                "backend": "sqlalchemy",
                "path": cls._sqlite_path,
                "read_only": True,
            }
        }

    def test_default_tools_still_listed(self):
        # Galaxy boots through the composite + LazyToolBox path; the
        # framework tools must still resolve from /api/tools.
        self._test_api_tools_list()


class TestToolSourceStorageMultipleVersions(BaseToolSourceStorageIntegrationTestCase):
    """Integration tests for tools with multiple versions."""

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["tool_source_store"] = "database"

    def test_multiple_versions_tool_available(self):
        response = self._get("tools")
        self._assert_status_code_is(response, 200)
        tools = response.json()

        tool_ids = []
        for section in tools:
            if "elems" in section:
                for elem in section["elems"]:
                    if isinstance(elem, dict) and "id" in elem:
                        tool_ids.append(elem["id"])
            elif "id" in section:
                tool_ids.append(section["id"])

        assert "multi_data_param" in tool_ids, f"multi_data_param not found in {tool_ids}"
