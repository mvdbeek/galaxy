from typing import Optional

from galaxy_test.base.populators import (
    DatasetCollectionPopulator,
    DatasetPopulator,
)
from galaxy_test.driver import integration_util


class TestDefaultPermissionsIntegration(integration_util.IntegrationTestCase):
    dataset_populator: DatasetPopulator
    dataset_collection_populator: DatasetCollectionPopulator
    framework_tool_and_types = True
    new_user_dataset_access_role_default_private: Optional[bool] = None
    metadata_strategy: Optional[str] = None
    expected_access_status_code = 200

    def setUp(self) -> None:
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.dataset_collection_populator = DatasetCollectionPopulator(self.galaxy_interactor)

    @classmethod
    def handle_galaxy_config_kwds(cls, config) -> None:
        super().handle_galaxy_config_kwds(config)
        if cls.new_user_dataset_access_role_default_private is not None:
            config["new_user_dataset_access_role_default_private"] = cls.new_user_dataset_access_role_default_private
        if cls.metadata_strategy is not None:
            config["metadata_strategy"] = cls.metadata_strategy

    def test_setting(self, history_id: str) -> None:
        hda = self.dataset_populator.new_dataset(history_id, wait=True)
        with self._different_user():
            details_response = self.dataset_populator.get_history_dataset_details_raw(
                history_id=history_id, dataset_id=hda["id"]
            )
            assert details_response.status_code == self.expected_access_status_code, details_response.content

    def test_setting_uploaded_collection_elements(self, history_id: str) -> None:
        fetch_response = self.dataset_collection_populator.create_list_in_history(
            history_id, contents=["one", "two"], direct_upload=True
        )
        hdca = self.dataset_collection_populator.wait_for_fetched_collection(fetch_response.json())
        self._assert_access_as_different_user(history_id, [element["object"]["id"] for element in hdca["elements"]])

    def test_setting_discovered_outputs(self, history_id: str) -> None:
        run = self.dataset_populator.run_tool("multi_output", {"input": 7}, history_id)
        job_id = run["jobs"][0]["id"]
        self.dataset_populator.wait_for_job(job_id, assert_ok=True)
        outputs = self._get(f"jobs/{job_id}/outputs").json()
        discovered_ids = [o["dataset"]["id"] for o in outputs if o["name"].startswith("__new_primary_file")]

        hda = self.dataset_populator.new_dataset(history_id, content="a\t1\nb\t2\n", file_type="tabular", wait=True)
        split = self.dataset_populator.run_tool(
            "collection_split_on_column", {"input1": {"src": "hda", "id": hda["id"]}}, history_id
        )
        self.dataset_populator.wait_for_job(split["jobs"][0]["id"], assert_ok=True)
        hdca = self.dataset_populator.get_history_collection_details(
            history_id, content_id=split["output_collections"][0]["id"]
        )
        element_ids = [element["object"]["id"] for element in hdca["elements"]]
        assert len(discovered_ids) == 1 and len(element_ids) == 2
        self._assert_access_as_different_user(history_id, discovered_ids + element_ids)

    def test_setting_discovered_outputs_of_public_input(self, history_id: str) -> None:
        # Explicit outputs keep the history's default access restriction when the inputs are
        # public; discovered outputs have to follow the same rule.
        hda = self.dataset_populator.new_dataset(history_id, content="a\t1\nb\t2\n", file_type="tabular", wait=True)
        self.dataset_populator.make_dataset_public_raw(history_id, hda["id"]).raise_for_status()
        split = self.dataset_populator.run_tool(
            "collection_split_on_column", {"input1": {"src": "hda", "id": hda["id"]}}, history_id
        )
        self.dataset_populator.wait_for_job(split["jobs"][0]["id"], assert_ok=True)
        hdca = self.dataset_populator.get_history_collection_details(
            history_id, content_id=split["output_collections"][0]["id"]
        )
        self._assert_access_as_different_user(history_id, [element["object"]["id"] for element in hdca["elements"]])

    def test_setting_archive_expanded_into_history(self, history_id: str) -> None:
        with open(self.test_data_resolver.get_filename("testdir1.zip"), "rb") as archive:
            payload = {
                "history_id": history_id,
                "targets": [{"destination": {"type": "hdas"}, "elements_from": "archive", "src": "files"}],
                "__files": {"files_0|file_data": archive},
            }
            self.dataset_populator.fetch(payload, wait=True)
        dataset_ids = [content["id"] for content in self.dataset_populator.get_history_contents(history_id)]
        assert len(dataset_ids) == 3
        self._assert_access_as_different_user(history_id, dataset_ids)

    def _assert_access_as_different_user(self, history_id: str, dataset_ids: list[str]) -> None:
        assert dataset_ids
        with self._different_user():
            for dataset_id in dataset_ids:
                details_response = self.dataset_populator.get_history_dataset_details_raw(
                    history_id=history_id, dataset_id=dataset_id
                )
                assert details_response.status_code == self.expected_access_status_code, details_response.content


class TestPrivateDefaultPermissionsIntegration(TestDefaultPermissionsIntegration):
    new_user_dataset_access_role_default_private = True
    expected_access_status_code = 403


class TestPrivateDefaultPermissionsExtendedMetadataIntegration(TestPrivateDefaultPermissionsIntegration):
    metadata_strategy = "extended"


class TestPublicDefaultPermissionsIntegration(TestDefaultPermissionsIntegration):
    new_user_dataset_access_role_default_private = False
    expected_access_status_code = 200
