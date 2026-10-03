from galaxy.util import requests
from galaxy_test.base.populators import WorkflowPopulator
from galaxy_test.driver import integration_util


class TestWorkflowExport(integration_util.IntegrationTestCase):
    framework_tool_and_types = True

    def setUp(self):
        super().setUp()
        self.workflow_populator = WorkflowPopulator(self.galaxy_interactor)

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["default_workflow_export_format"] = "format2"

    def test_default_format2_download(self):
        workflow_id = self.workflow_populator.simple_workflow("format2_export")
        self._assert_downloads(workflow_id, "gxwf.json")

    def test_default_download_falls_back_to_native(self):
        workflow = self.workflow_populator.load_workflow("native_fallback")
        for i in ("0", "1"):
            workflow["steps"][i]["workflow_outputs"] = [{"output_name": "output", "label": "duplicate"}]
        workflow_id = self.workflow_populator.create_workflow(workflow)
        self._assert_downloads(workflow_id, "ga")
        explicit = self._get(f"workflows/{workflow_id}/download", data={"style": "format2"})
        self._assert_status_code_is(explicit, 500)

    def _assert_downloads(self, workflow_id, extension):
        self.workflow_populator.make_public(workflow_id)
        workflow = self._get(f"workflows/{workflow_id}").json()
        api_download = self._get(f"workflows/{workflow_id}/download", data={"format": "json-download"})
        legacy_download = requests.get(
            f"{self.url}u/{workflow['owner']}/w/{workflow['slug']}/json-download", timeout=30
        )
        for response in (api_download, legacy_download):
            self._assert_status_code_is(response, 200)
            assert response.headers["Content-Disposition"].endswith(f'.{extension}"')
            exported = response.json()
            if extension == "ga":
                assert exported["format-version"] == "0.1"
                assert [
                    output["label"] for step in exported["steps"].values() for output in step["workflow_outputs"]
                ] == ["duplicate", "duplicate"]
            else:
                assert exported["class"] == "GalaxyWorkflow"
