import random
import time
from typing import Optional

from galaxy.util import UNKNOWN
from galaxy_test.base.decorators import requires_admin
from galaxy_test.base.populators import DatasetPopulator
from ._framework import ApiTestCase


class TestDisplayApplicationsApi(ApiTestCase):
    dataset_populator: DatasetPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def test_index(self):
        response = self._get("display_applications")
        self._assert_status_code_is(response, 200)
        as_list = response.json()
        assert isinstance(as_list, list)
        assert len(as_list) > 0
        for display_app in as_list:
            self._assert_has_keys(display_app, "id", "name", "version", "filename_", "links")

    @requires_admin
    def test_reload_as_admin(self):
        response = self._post("display_applications/reload", admin=True)
        self._assert_status_code_is(response, 200)

    @requires_admin
    def test_reload_with_some_ids(self):
        response = self._get("display_applications")
        self._assert_status_code_is(response, 200)
        display_apps = response.json()
        all_ids = [display_app["id"] for display_app in display_apps]
        input_ids = self._get_half_random_items(all_ids)
        payload = {"ids": input_ids}
        response = self._post("display_applications/reload", payload, admin=True, json=True)
        self._assert_status_code_is(response, 200)
        reloaded = response.json()["reloaded"]
        assert len(reloaded) == len(input_ids)
        assert all(elem in reloaded for elem in input_ids)

    @requires_admin
    def test_reload_unknown_returns_as_failed(self):
        unknown_id = UNKNOWN
        payload = {"ids": [unknown_id]}
        response = self._post("display_applications/reload", payload, admin=True, json=True)
        self._assert_status_code_is(response, 200)
        reloaded = response.json()["reloaded"]
        failed = response.json()["failed"]
        assert len(reloaded) == 0
        assert len(failed) == 1
        assert unknown_id in failed

    def test_reload_as_non_admin_returns_403(self):
        response = self._post("display_applications/reload")
        self._assert_status_code_is(response, 403)

    def test_create_link(self):
        cases: list[dict[str, Optional[str]]] = [
            {"file": "1.interval", "app": "igv_interval_as_bed", "step": "bed_file"},
            {"file": "1.bam", "app": "igv_bam", "step": None},
            {"file": "test.vcf", "app": "igv_vcf", "step": "bgzip_file"},
            {"file": "test.vcf.gz", "app": "igv_vcf", "step": None},
            {"file": "5.gff", "app": "igv_gff", "step": None},
            {"file": "1.bigwig", "app": "igv_bigwig", "step": None},
            {"file": "1.fasta", "app": "igv_fasta", "step": "fasta_file"},
        ]
        for case in cases:
            test_file = self.get_filename(str(case["file"]))
            with self.dataset_populator.test_history() as history_id:
                ds = self.dataset_populator.new_dataset(
                    history_id,
                    content=open(test_file, "rb"),
                    file_type="auto",
                    wait=True,
                )
                payload = {
                    "app_name": case["app"],
                    "dataset_id": ds["id"],
                    "link_name": "local_default",
                }
                response = self._post("display_applications/create_link", data=payload, json=True)
                self._assert_status_code_is(response, 200)
                response_json = response.json()
                step = case["step"]
                if step is not None:
                    assert response_json["refresh"]
                    assert response_json["preparable_steps"][0]["name"] == step
                    assert "required additional datasets" in response_json["messages"][0][0]
                    if step == "bed_file":
                        for _ in range(10):
                            response = self._post("display_applications/create_link", data=payload, json=True)
                            self._assert_status_code_is(response, 200)
                            response_json = response.json()
                            if response_json["refresh"] is False:
                                break
                            time.sleep(2)
                        assert response_json["refresh"] is False
                else:
                    assert response_json["refresh"] is False
                    assert "http://localhost:60151/load?file=http" in response_json["resource"]
                    assert "name=Test_Dataset" in response_json["resource"]

    def _get_half_random_items(self, collection: list[str]) -> list[str]:
        half_num_items = int(len(collection) / 2)
        rval = random.sample(collection, half_num_items)
        return rval

    def test_sequential_requests_do_not_create_duplicate_conversions(self):
        """Test that sequential display application requests don't create duplicate conversions.

        Regression test for: https://github.com/galaxyproject/galaxy/issues/21573

        The issue was that without flushing the session after creating an ICDA
        (ImplicitlyConvertedDatasetAssociation), the implicitly_converted_datasets
        relationship could be cached and subsequent checks might not see the newly
        created ICDA, causing duplicate conversions.

        The fix adds session.flush() and session.expire() after ICDA creation to ensure
        subsequent queries in the same session see the new ICDA.

        This test uses interval→bedstrict conversion which doesn't require external tools.
        """
        test_file = self.get_filename("1.interval")
        with self.dataset_populator.test_history() as history_id:
            ds = self.dataset_populator.new_dataset(
                history_id,
                content=open(test_file, "rb"),
                file_type="interval",
                wait=True,
            )
            payload = {
                "app_name": "igv_interval_as_bed",
                "dataset_id": ds["id"],
                "link_name": "local_default",
            }

            # Make the initial request to trigger conversion
            response = self._post("display_applications/create_link", data=payload, json=True)
            self._assert_status_code_is(response, 200)

            # Wait for conversion to complete, polling with multiple requests
            # Each request should detect the in-progress conversion and NOT create a duplicate
            for _ in range(20):
                response = self._post("display_applications/create_link", data=payload, json=True)
                self._assert_status_code_is(response, 200)
                if response.json()["refresh"] is False:
                    break
                time.sleep(1)

            # Get all datasets in the history including hidden ones
            visible_contents = self.dataset_populator.get_history_contents(history_id)
            hidden_contents = self.dataset_populator.get_history_contents(
                history_id, data={"visible": "false"}
            )
            all_contents = visible_contents + hidden_contents

            # Check for bedstrict conversions (interval→bed produces bedstrict)
            bedstrict_datasets = [
                item for item in all_contents
                if item.get("history_content_type") == "dataset"
                and item.get("extension") == "bedstrict"
                and not item.get("deleted", False)
            ]

            # There should be exactly ONE bedstrict conversion
            # With the fix (flush + expire), subsequent requests should see the existing
            # conversion and not create duplicates
            assert len(bedstrict_datasets) == 1, (
                f"Expected exactly 1 bedstrict conversion but found {len(bedstrict_datasets)}. "
                f"This indicates duplicate conversions are being created. "
                f"bedstrict datasets: {[{'id': c.get('id'), 'create_time': c.get('create_time')} for c in bedstrict_datasets]}"
            )
