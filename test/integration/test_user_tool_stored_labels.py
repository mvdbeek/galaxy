import copy
from typing import Any
from uuid import UUID

from sqlalchemy import select

from galaxy.model import DynamicTool
from galaxy.tool_util_models import UserToolSource
from galaxy_test.base.populators import (
    DatasetPopulator,
    TOOL_WITH_SHELL_COMMAND,
    user_defined_tool_run_workflow_dict,
    WorkflowPopulator,
)
from galaxy_test.driver import integration_util

# Stored before the label rules existed; current validation refuses it when a tool is saved.
STORED_CHEETAH_LABEL = "${on_string} from $(inputs.input.name)"
LIFTED_LABEL = "\\${on_string} from $(inputs.input.name)"


class TestUserToolStoredLabels(integration_util.IntegrationTestCase):
    dataset_populator: DatasetPopulator
    workflow_populator: WorkflowPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.workflow_populator = WorkflowPopulator(self.galaxy_interactor)

    def test_stored_label_fills_in_what_it_can(self):
        with (
            self.dataset_populator.test_history() as history_id,
            self.dataset_populator.user_tool_execute_permissions(),
        ):
            dynamic_tool = self._stored_tool()
            dataset = self.dataset_populator.new_dataset(history_id=history_id, content="abc", name="reads.txt")
            response = self.dataset_populator.run_tool_raw(
                tool_id=None,
                tool_uuid=dynamic_tool["uuid"],
                inputs={"input": {"src": "hda", "id": dataset["id"]}},
                history_id=history_id,
            )
            self._assert_status_code_is(response, 200)
            listed = next(
                tool for tool in self.dataset_populator.get_unprivileged_tools() if tool["uuid"] == dynamic_tool["uuid"]
            )
        assert response.json()["outputs"][0]["name"] == "${on_string} from reads.txt"
        assert listed["representation_status"] == "lifted"
        assert listed["representation"]["outputs"][0]["label"] == LIFTED_LABEL

    def test_workflow_with_stored_label_copied_for_another_user(self):
        with self.dataset_populator.user_tool_execute_permissions():
            dynamic_tool = self._stored_tool()
            workflow_id = self.workflow_populator.create_workflow(
                user_defined_tool_run_workflow_dict("basecommand", dynamic_tool["uuid"]), publish=True
            )
            export = self.workflow_populator.download_workflow(workflow_id, style="ga")
        with self._different_user(), self.dataset_populator.user_tool_execute_permissions():
            shared_import = self._post("workflows", {"shared_workflow_id": workflow_id})
            self._assert_status_code_is(shared_import, 200)
            export_import = self.workflow_populator.import_workflow(export)
            copied_uuids = [
                self.workflow_populator.download_workflow(imported_id, style="instance")["steps"]["1"]["tool_uuid"]
                for imported_id in (shared_import.json()["id"], export_import["id"])
            ]
            copies = [tool for tool in self.dataset_populator.get_unprivileged_tools() if tool["uuid"] in copied_uuids]
        assert [tool["representation"]["outputs"][0]["label"] for tool in copies] == [LIFTED_LABEL, LIFTED_LABEL]

    def _stored_tool(self) -> dict[str, Any]:
        dynamic_tool = self.dataset_populator.create_unprivileged_tool(UserToolSource(**TOOL_WITH_SHELL_COMMAND))
        session = self._app.model.session
        stored = session.scalars(select(DynamicTool).where(DynamicTool.uuid == UUID(dynamic_tool["uuid"]))).one()
        value = copy.deepcopy(stored.value)
        value["outputs"][0]["label"] = STORED_CHEETAH_LABEL
        stored.value = value
        session.commit()
        return dynamic_tool
