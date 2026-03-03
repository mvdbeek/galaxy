from unittest.mock import (
    MagicMock,
    patch,
)

import pytest

from galaxy.celery import (
    celery_app,
    DEFAULT_TASK_QUEUE,
    GalaxyCelery,
    get_or_raise_if_workers_lost,
    TASKS_MODULES,
    WorkersLostError,
)
from galaxy.config import GalaxyAppConfiguration


def test_default_configuration():
    conf = celery_app.conf
    galaxy_conf = GalaxyAppConfiguration(override_tempdir=False)

    assert conf.task_default_queue == DEFAULT_TASK_QUEUE
    assert conf.include == TASKS_MODULES
    assert conf.task_create_missing_queues is True
    assert conf.timezone == "UTC"
    assert conf.broker_url == galaxy_conf.amqp_internal_connection
    assert conf.task_routes["galaxy.fetch_data"] == "galaxy.external"
    assert conf.task_routes["galaxy.set_job_metadata"] == "galaxy.external"
    assert conf.beat_schedule["prune-history-audit-table"] == {
        "task": "galaxy.prune_history_audit_table",
        "schedule": galaxy_conf.history_audit_table_prune_interval,
    }
    assert conf.beat_schedule["cleanup-short-term-storage"] == {
        "task": "galaxy.cleanup_short_term_storage",
        "schedule": galaxy_conf.short_term_storage_cleanup_interval,
    }


def test_galaxycelery_trim_module_name():
    gc = GalaxyCelery()
    assert gc.trim_module_name("notgalaxy.celery.tasks") == "notgalaxy.celery.tasks"
    assert gc.trim_module_name("galaxy.notcelery.tasks") == "galaxy.notcelery.tasks"
    assert gc.trim_module_name("galaxy.celery.tasks") == "galaxy"
    assert gc.trim_module_name("galaxy.celery.tasks.nextlevel") == "galaxy.nextlevel"


class TestGetOrRaiseIfWorkersLost:
    def test_returns_result_on_success(self):
        async_result = MagicMock()
        async_result.get.return_value = "metadata_set"
        assert get_or_raise_if_workers_lost(async_result, poll_interval=1) == "metadata_set"
        async_result.get.assert_called_once_with(timeout=1)

    def test_propagates_task_exception(self):
        async_result = MagicMock()
        async_result.get.side_effect = ValueError("task failed")
        with pytest.raises(ValueError, match="task failed"):
            get_or_raise_if_workers_lost(async_result, poll_interval=1)

    @patch("galaxy.celery.celery_app")
    def test_raises_workers_lost_when_no_workers(self, mock_app):
        from celery.exceptions import TimeoutError as CeleryTimeoutError

        async_result = MagicMock()
        async_result.id = "test-task-id"
        async_result.get.side_effect = CeleryTimeoutError("timed out")
        mock_app.control.ping.return_value = []

        with pytest.raises(WorkersLostError, match="no workers responded to ping"):
            get_or_raise_if_workers_lost(async_result, poll_interval=1)

    @patch("galaxy.celery.celery_app")
    def test_retries_when_workers_alive(self, mock_app):
        from celery.exceptions import TimeoutError as CeleryTimeoutError

        async_result = MagicMock()
        # First call times out, second returns result
        async_result.get.side_effect = [CeleryTimeoutError("timed out"), "done"]
        mock_app.control.ping.return_value = [{"worker1": {"ok": "pong"}}]

        assert get_or_raise_if_workers_lost(async_result, poll_interval=1) == "done"
        assert async_result.get.call_count == 2
        mock_app.control.ping.assert_called_once_with(timeout=2.0)
