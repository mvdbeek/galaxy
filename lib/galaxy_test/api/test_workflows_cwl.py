"""Test CWL workflow functionality."""
import os
import re
from typing import Optional

from galaxy_test.api.test_workflows import BaseWorkflowsApiTestCase
from galaxy_test.base.populators import (
    CWL_TOOL_DIRECTORY,
    CwlPopulator,
    CwlWorkflowRun,
)


def resolve_path(rel_path):
    return os.path.join(CWL_TOOL_DIRECTORY, rel_path)


class BaseCwlWorkflowsApiTestCase(BaseWorkflowsApiTestCase):
    allow_path_paste = True
    require_admin_user = True

    def setUp(self):
        super().setUp()
        self.cwl_populator = CwlPopulator(self.dataset_populator, self.workflow_populator)


class TestCwlWorkflows(BaseCwlWorkflowsApiTestCase):
    """Test case encompassing CWL workflow tests."""

    history_id: str

    def setUp(self):
        super().setUp()
        self.history_id = self.dataset_populator.new_history()

    def test_simplest_wf(self):
        """Test simplest workflow."""
        workflow_id = self._load_workflow("v1.0_custom/just-wc-wf.cwl")
        workflow_content = self._download_workflow(workflow_id)
        for step in workflow_content["steps"].values():
            if "tool_representation" in step:
                del step["tool_representation"]

        hda1 = self.dataset_populator.new_dataset(
            self.history_id, content="hello world\nhello all\nhello all in world\nhello"
        )
        inputs_map = {"file1": {"src": "hda", "id": hda1["id"]}}
        invocation_id = self._invoke(inputs_map, workflow_id)
        self.workflow_populator.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        output = self.dataset_populator.get_history_dataset_content(self.history_id, hid=2)
        assert re.search(r"\s+4\s+9\s+47\s+", output)

    def test_load_ids(self):
        workflow_id = self._load_workflow("v1.0/v1.0/search.cwl#main")
        workflow_content = self._download_workflow(workflow_id)
        for step in workflow_content["steps"].values():
            if "tool_representation" in step:
                del step["tool_representation"]

        print(workflow_content)
        steps = workflow_content["steps"]
        step_3 = steps["3"]
        step_4 = steps["4"]

        assert step_3["label"] == "index", step_3
        assert step_4["label"] == "search", step_4

        print(step_3)
        print(step_4)

    def test_count_line1_v1(self):
        """Test simple workflow v1.0/v1.0/count-lines1-wf.cwl."""
        self._run_count_lines_wf("v1.0/v1.0/count-lines1-wf.cwl")

    def test_count_line1_v1_json(self):
        run_object = self.cwl_populator.run_cwl_job(
            resolve_path("v1.0/v1.0/count-lines1-wf.cwl"),
            resolve_path("v1.0/v1.0/wc-job.json"),
            history_id=self.history_id,
        )
        assert isinstance(run_object, CwlWorkflowRun)
        self._check_countlines_wf(run_object.invocation_id, run_object.workflow_id, expected_count=16)

    def test_count_line2_v1(self):
        """Test simple workflow v1.0/v1.0/count-lines2-wf.cwl."""
        self._run_count_lines_wf("v1.0/v1.0/count-lines2-wf.cwl")

    def test_count_lines3_v1(self):
        workflow_id = self._load_workflow("v1.0/v1.0/count-lines3-wf.cwl")
        fetch_response = self.dataset_collection_populator.create_list_in_history(self.history_id).json()
        hdca = self.dataset_collection_populator.wait_for_fetched_collection(fetch_response)
        inputs_map = {"file1": {"src": "hdca", "id": hdca["id"]}}
        invocation_id = self._invoke(inputs_map, workflow_id)
        self.workflow_populator.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        hdca = self.dataset_populator.get_history_collection_details(self.history_id, hid=5)
        assert hdca["collection_type"] == "list"
        elements = hdca["elements"]
        assert len(elements) == 3
        element0 = elements[0]["object"]
        assert element0["history_content_type"] == "dataset"
        assert element0["state"] == "ok"
        assert element0["file_ext"] == "expression.json"
        # TODO: ensure this looks like an int[] - it doesn't currently...

    def test_count_lines4_v1(self):
        workflow_id = self._load_workflow("v1.0/v1.0/count-lines4-wf.cwl")
        hda1 = self.dataset_populator.new_dataset(
            self.history_id, content="hello world\nhello all\nhello all in world\nhello"
        )
        hda2 = self.dataset_populator.new_dataset(self.history_id, content="moo\ncow\nthat\nis\nall")
        inputs_map = {"file1": {"src": "hda", "id": hda1["id"]}, "file2": {"src": "hda", "id": hda2["id"]}}
        invocation_id = self._invoke(inputs_map, workflow_id)
        self.workflow_populator.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        self.dataset_populator.get_history_collection_details(self.history_id, hid=4)

    def test_count_lines4_json(self):
        self.cwl_populator.run_cwl_job(
            resolve_path("v1.0/v1.0/count-lines4-wf.cwl"),
            resolve_path("v1.0/v1.0/count-lines4-job.json"),
            history_id=self.history_id,
        )
        self.dataset_populator.get_history_collection_details(self.history_id, hid=4)

    def test_scatter_wf1_v1(self):
        self.cwl_populator.run_cwl_job(
            resolve_path("v1.0/v1.0/scatter-wf1.cwl"),
            resolve_path("v1.0/v1.0/scatter-job1.json"),
            history_id=self.history_id,
        )
        self.dataset_populator.get_history_collection_details(self.history_id, hid=5)

    def _run_count_lines_wf(self, wf_path: str):
        workflow_id = self._load_workflow(wf_path)
        hda1 = self.dataset_populator.new_dataset(
            self.history_id, content="hello world\nhello all\nhello all in world\nhello"
        )
        inputs_map = {"file1": {"src": "hda", "id": hda1["id"]}}
        invocation_id = self._invoke(inputs_map, workflow_id)
        self._check_countlines_wf(invocation_id, workflow_id)

    def _check_countlines_wf(self, invocation_id: str, workflow_id: str, expected_count: int = 4):
        self.workflow_populator.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        output = self.dataset_populator.get_history_dataset_content(self.history_id, hid=3)
        assert int(output) == expected_count, output

    def _invoke(self, inputs: Optional[dict], workflow_id: str) -> str:
        return self.workflow_populator.invoke_workflow_and_assert_ok(
            workflow_id, self.history_id, inputs, inputs_by="name"
        )

    def _load_workflow(self, rel_path: str) -> str:
        rel_path = rel_path.split("#", 1)[0]
        path = resolve_path(rel_path)
        data = dict(
            from_path=path,
        )
        route = "workflows"
        upload_response = self._post(route, data=data)
        self._assert_status_code_is(upload_response, 200)
        workflow = upload_response.json()
        workflow_id = workflow["id"]
        return workflow_id
