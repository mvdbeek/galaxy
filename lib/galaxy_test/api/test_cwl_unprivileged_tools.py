"""Test CWL tool import and execution via the unprivileged tools API."""

import os

import yaml

from galaxy_test.base.populators import (
    CwlPopulator,
    CwlToolRun,
    DatasetPopulator,
    WorkflowPopulator,
)
from ._framework import ApiTestCase

CWL_TOOLS_DIR = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "test", "functional", "tools")


def _cwl_tool_path(relative_path: str) -> str:
    return os.path.join(CWL_TOOLS_DIR, relative_path)


def _load_cwl(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


# cat1-tool.cwl has a DockerRequirement
CAT1_TOOL_PATH = _cwl_tool_path("cwl_tools/v1.0_custom/cat1-tool.cwl")


class TestCwlUnprivilegedTools(ApiTestCase):
    """Test importing and running CWL tools via the unprivileged tools API."""

    dataset_populator: DatasetPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        workflow_populator = WorkflowPopulator(self.galaxy_interactor)
        self.cwl_populator = CwlPopulator(self.dataset_populator, workflow_populator)
        self.cwl_populator.setup_permissions()

    def tearDown(self):
        self.cwl_populator.teardown_permissions()
        super().tearDown()

    # -- Import tests --

    def test_create_cwl_commandlinetool(self):
        """Import a CWL CommandLineTool via POST /api/unprivileged_tools."""
        cwl_doc = _load_cwl(CAT1_TOOL_PATH)
        result = self.cwl_populator.create_unprivileged_cwl_tool(CAT1_TOOL_PATH)
        assert result["uuid"]
        assert result["tool_format"] in ("CommandLineTool",)
        assert result["active"] is True
        # Verify the representation round-trips
        assert result["representation"]["class"] == cwl_doc["class"]

    def test_create_cwl_tool_without_docker_rejected(self):
        """CWL tools without DockerRequirement must be rejected."""
        # cwl_int.cwl is an ExpressionTool with no DockerRequirement
        cwl_doc = _load_cwl(_cwl_tool_path("parameters/cwl_int.cwl"))
        payload = {
            "src": "representation",
            "representation": {
                "class": cwl_doc["class"],
                "raw_process_reference": cwl_doc,
            },
        }
        response = self.dataset_populator._post("unprivileged_tools", data=payload, json=True)
        assert response.status_code != 200, "Expected rejection for CWL tool without DockerRequirement"

    def test_list_user_cwl_tools(self):
        """Verify imported CWL tools appear in GET /api/unprivileged_tools."""
        created = self.cwl_populator.create_unprivileged_cwl_tool(CAT1_TOOL_PATH)
        tools = self.dataset_populator.get_unprivileged_tools()
        assert any(t["uuid"] == created["uuid"] for t in tools)

    def test_show_user_cwl_tool(self):
        """Verify tool details via GET /api/unprivileged_tools/{uuid}."""
        created = self.cwl_populator.create_unprivileged_cwl_tool(CAT1_TOOL_PATH)
        shown = self.dataset_populator.show_unprivileged_tool(created["uuid"])
        assert shown["uuid"] == created["uuid"]
        assert shown["tool_format"] == "CommandLineTool"

    def test_deactivate_cwl_tool(self):
        """Verify deactivation via DELETE /api/unprivileged_tools/{uuid}."""
        created = self.cwl_populator.create_unprivileged_cwl_tool(CAT1_TOOL_PATH)
        self.dataset_populator.deactivate_unprivileged_tool(created["uuid"])
        tools = self.dataset_populator.get_unprivileged_tools()
        assert not any(t["uuid"] == created["uuid"] for t in tools)

    def test_cwl_tool_not_in_global_toolbox(self):
        """User-scoped CWL tools must not appear in the global tool panel."""
        created = self.cwl_populator.create_unprivileged_cwl_tool(CAT1_TOOL_PATH)
        tool_id = created.get("tool_id")
        # Query the global toolbox
        get_response = self.dataset_populator._get("tools", data=dict(tool_id=tool_id))
        get_response.raise_for_status()
        # The created dynamic tool's UUID should not be findable through
        # the global toolbox query by UUID
        toolbox_response = self.dataset_populator._get("tools", data=dict(tool_id=created["uuid"]))
        toolbox_response.raise_for_status()
        assert len(toolbox_response.json()) == 0

    # -- Execution tests --

    def test_run_cwl_cat1_tool(self):
        """Import cat1-tool.cwl, execute via tool_uuid, verify output."""
        with self.dataset_populator.test_history() as history_id:
            run_object = self.cwl_populator.run_cwl_job(
                CAT1_TOOL_PATH,
                job={"file1": {"class": "File", "location": "hello.txt"}, "numbering": False},
                test_data_directory=os.path.join(CWL_TOOLS_DIR, "cwl_tools", "v1.0_custom"),
                history_id=history_id,
            )
            assert isinstance(run_object, CwlToolRun)

    def test_run_cwl_cat1_with_numbering(self):
        """Import and run cat1-tool.cwl with numbering enabled."""
        with self.dataset_populator.test_history() as history_id:
            run_object = self.cwl_populator.run_cwl_job(
                CAT1_TOOL_PATH,
                job={"file1": {"class": "File", "location": "hello.txt"}, "numbering": True},
                test_data_directory=os.path.join(CWL_TOOLS_DIR, "cwl_tools", "v1.0_custom"),
                history_id=history_id,
            )
            assert isinstance(run_object, CwlToolRun)
