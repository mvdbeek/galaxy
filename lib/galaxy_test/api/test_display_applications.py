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

    def test_rapid_create_link_does_not_create_excessive_duplicate_conversions(self):
        """Test that rapid create_link requests don't create excessive duplicate implicit conversions.

        Regression test for: https://github.com/galaxyproject/galaxy/issues/21573

        The issue was that without flushing the session after creating an ICDA
        (ImplicitlyConvertedDatasetAssociation), requests would not see the pending
        conversion and would trigger duplicate conversions.

        The fix adds a session.flush() after ICDA creation. This helps reduce but may
        not completely eliminate duplicates with SQLite (which doesn't support row-level
        locking). With PostgreSQL in production, the fix should be more effective.

        This test makes rapid sequential requests and verifies that we don't see excessive
        duplicates (the original issue reported "hundreds" of duplicate conversions).
        """
        test_file = self.get_filename("1.interval")
        with self.dataset_populator.test_history() as history_id:
            ds = self.dataset_populator.new_dataset(
                history_id,
                content=open(test_file, "rb"),
                file_type="auto",
                wait=True,
            )
            payload = {
                "app_name": "igv_interval_as_bed",
                "dataset_id": ds["id"],
                "link_name": "local_default",
            }

            # Make rapid sequential requests to simulate user clicking multiple times
            num_requests = 5
            responses = []
            for _ in range(num_requests):
                response = self._post("display_applications/create_link", data=payload, json=True)
                responses.append(response)
                # Small delay to allow flush to take effect
                time.sleep(0.1)

            # All requests should succeed
            for response in responses:
                self._assert_status_code_is(response, 200)

            # Wait for conversion to complete
            for _ in range(20):
                response = self._post("display_applications/create_link", data=payload, json=True)
                self._assert_status_code_is(response, 200)
                if response.json()["refresh"] is False:
                    break
                time.sleep(1)

            # Get all datasets in the history
            # First get all visible datasets
            visible_contents = self.dataset_populator.get_history_contents(history_id)

            # Then get hidden datasets by filtering for visible=False
            hidden_contents = self.dataset_populator.get_history_contents(
                history_id, data={"visible": "false"}
            )

            # Combine both lists to get all datasets
            all_contents = visible_contents + hidden_contents

            # Filter to get only the converted datasets (bedstrict files - interval->bed conversion produces bedstrict)
            converted_datasets = [
                item for item in all_contents
                if item.get("history_content_type") == "dataset"
                and item.get("extension") == "bedstrict"
                and not item.get("deleted", False)
            ]

            # With the flush fix, we should ideally have just 1 conversion.
            # Allow up to 2 due to potential race conditions with the test server's thread pool.
            assert len(converted_datasets) <= 2, (
                f"Expected at most 2 BED conversions but found {len(converted_datasets)}. "
                f"This indicates the race condition fix is not working effectively. "
                f"Converted datasets: {[{'id': c.get('id'), 'create_time': c.get('create_time')} for c in converted_datasets]}"
            )
