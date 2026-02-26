"""Integration tests for quota enforcement during data upload.

Verifies that when a user is over their disk quota, upload jobs
are correctly paused both with and without Celery-based data fetch.
"""

from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util


class BaseUploadQuotaTestCase(integration_util.IntegrationTestCase):
    dataset_populator: DatasetPopulator
    require_admin_user = True

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["enable_quotas"] = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def _assert_upload_paused_when_over_quota(self):
        with self.dataset_populator.test_history() as history_id:
            # Upload an initial dataset so the user has some disk usage
            self.dataset_populator.new_dataset(history_id, content="initial content", wait=True)

            # Set a very low quota (1 byte) so the user is over quota
            self.dataset_populator.create_quota(
                {
                    "name": "default-upload-quota",
                    "description": "very low default quota for testing",
                    "amount": "1 bytes",
                    "operation": "=",
                    "default": "registered",
                }
            )

            # Now try to upload another dataset - should be paused due to quota
            hda = self.dataset_populator.new_dataset(history_id, content="more data", wait=False)
            self.dataset_populator.wait_for_history(history_id, assert_ok=False)

            details = self.dataset_populator.get_history_dataset_details(
                history_id, dataset=hda, wait=False, assert_ok=False
            )
            assert details["state"] == "paused", f"Expected dataset state 'paused', got '{details['state']}'"


class TestUploadQuotaWithCeleryFetch(BaseUploadQuotaTestCase):
    """Quota enforced when data fetch goes through the Celery task chain."""

    def test_fetch_paused_when_over_quota(self):
        self._assert_upload_paused_when_over_quota()


class TestUploadQuotaWithoutCeleryFetch(BaseUploadQuotaTestCase):
    """Quota enforced when data fetch goes through the standard job handler."""

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        celery_conf = config.get("celery_conf", {})
        task_routes = celery_conf.get("task_routes", {})
        task_routes["galaxy.fetch_data"] = "disabled"
        celery_conf["task_routes"] = task_routes
        config["celery_conf"] = celery_conf

    def test_fetch_paused_when_over_quota(self):
        self._assert_upload_paused_when_over_quota()
