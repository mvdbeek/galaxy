"""Zarr datasets created before store_root was removed must keep working after a metadata reset."""

from galaxy.model import HistoryDatasetAssociation
from galaxy.tool_util.verify.test_data import TestDataResolver
from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver.integration_util import IntegrationTestCase


class TestZarrStoreRootMetadataResetIntegration(IntegrationTestCase):
    dataset_populator: DatasetPopulator
    framework_tool_and_types = True

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["metadata_strategy"] = "directory"

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def test_reset_metadata_clears_store_root_of_moved_store(self, history_id):
        dataset_id = self._create_historical_zarr_dataset(history_id)

        self._put(f"histories/{history_id}/contents/{dataset_id}/validate").raise_for_status()
        self.dataset_populator.wait_for_history(history_id, assert_ok=True)

        hda = self._get_hda(dataset_id)
        assert "store_root" not in (hda._metadata or {})
        assert str(hda.metadata.zarr_format) == "2"
        # Published wrappers read $input.extra_files_path/$input.metadata.store_root.
        response = self.dataset_populator.run_tool(
            "zarr_store_root_compat", {"input": {"src": "hda", "id": dataset_id}}, history_id
        )
        self.dataset_populator.wait_for_job(response["jobs"][0]["id"], assert_ok=True)
        listing = self.dataset_populator.get_history_dataset_content(
            history_id, dataset_id=response["outputs"][0]["id"]
        )
        assert ".zgroup" in listing.splitlines()

    def _create_historical_zarr_dataset(self, history_id: str) -> str:
        # A plain directory keeps the wrapper folder, which is how older Galaxy stored a zarr
        # dataset; mark it as such a dataset, with store_root naming the wrapper.
        with open(TestDataResolver().get_filename("wrapped_store.zarr.zip"), "rb") as archive:
            payload = {
                "history_id": history_id,
                "targets": [
                    {
                        "destination": {"type": "hdas"},
                        "items": [
                            {
                                "src": "pasted",
                                "paste_content": "",
                                "ext": "directory",
                                "extra_files": {"items_from": "archive", "src": "files", "fuzzy_root": False},
                            }
                        ],
                    }
                ],
                "__files": {"files_0|file_data": archive},
            }
            fetch_response = self.dataset_populator.fetch(payload)
        fetch_response.raise_for_status()
        dataset_id = fetch_response.json()["outputs"][0]["id"]
        self.dataset_populator.wait_for_history(history_id, assert_ok=True)

        hda = self._get_hda(dataset_id)
        hda.extension = "zarr"
        hda._metadata = {**(hda._metadata or {}), "store_root": "wrapped.zarr", "zarr_format": "2"}
        self._app.model.session.commit()
        return dataset_id

    def _get_hda(self, dataset_id: str) -> HistoryDatasetAssociation:
        session = self._app.model.session
        session.expire_all()
        hda = session.get(HistoryDatasetAssociation, self._decode_id(dataset_id))
        assert hda
        return hda


class TestZarrStoreRootMetadataResetExtendedIntegration(TestZarrStoreRootMetadataResetIntegration):
    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["metadata_strategy"] = "extended"
