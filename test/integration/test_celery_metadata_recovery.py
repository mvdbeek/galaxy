"""Integration tests for recovery of jobs interrupted during celery metadata setting."""

import os

from sqlalchemy import select

from galaxy import model
from galaxy.model.orm.util import ensure_object_added_to_session
from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util

SCRIPT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
SIMPLE_JOB_CONFIG_FILE = os.path.join(SCRIPT_DIRECTORY, "simple_job_conf.xml")


class TestCeleryMetadataJobRecovery(integration_util.IntegrationTestCase):
    """Test that a job stuck in RUNNING with outputs in SETTING_METADATA
    recovers to a terminal state after a Galaxy restart.

    Simulates the scenario where Galaxy is restarted while blocked on
    ``get_or_raise_if_workers_lost`` waiting for celery metadata setting.
    """

    dataset_populator: DatasetPopulator
    framework_tool_and_types = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["metadata_strategy"] = "directory_celery"
        config["job_config_file"] = SIMPLE_JOB_CONFIG_FILE

    def test_recovery_from_interrupted_celery_metadata(self):
        """Job in RUNNING + outputs in SETTING_METADATA should reach a
        terminal state after restart, not stay stuck forever."""
        sa_session = self._app.model.session
        history = sa_session.scalars(select(model.History)).first()
        user = sa_session.scalars(select(model.User)).first()
        if not user:
            # Create a user and history if none exist yet
            history_id = self.dataset_populator.new_history()
            sa_session.expire_all()
            history = sa_session.scalars(select(model.History)).first()
            user = sa_session.scalars(select(model.User)).first()

        # Create output HDA with its underlying dataset in SETTING_METADATA
        output_hda = model.HistoryDatasetAssociation(history=history, create_dataset=True, flush=False)
        output_hda.hid = 99
        sa_session.add(output_hda)
        sa_session.flush()
        output_hda.dataset.state = model.Dataset.states.SETTING_METADATA

        # Create a job that looks like it was mid-execution when the server died:
        # - state=RUNNING (handler will try to recover it)
        # - job_runner_name + job_runner_external_id + destination_id set
        #   (so _check_job_at_startup hits the "already dispatched" branch)
        # - handler="main" (matches server_name after restart)
        # - tool_id points to a real tool so recovery doesn't bail out
        job = model.Job()
        job.history = history
        ensure_object_added_to_session(job, object_in_session=history)
        job.user = user
        job.tool_id = "exit_code_oom"
        job.tool_version = "0.1.1"
        job.state = model.Job.states.RUNNING
        job.handler = "main"
        job.job_runner_name = "local:///"
        job.job_runner_external_id = "0"
        job.destination_id = "local_dest"
        sa_session.add(job)
        job.add_output_dataset("out_file1", output_hda)
        sa_session.commit()

        # Create the job working directory so the runner doesn't crash
        self._app.object_store.create(job, base_dir="job_work", dir_only=True, obj_dir=True)

        # Restart Galaxy — _check_job_at_startup will find this RUNNING job
        # and call LocalJobRunner.recover(), which sets it to ERROR.
        self.restart()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

        # Verify the job reached a terminal state (ERROR for local runner recovery)
        sa_session = self._app.model.session
        recovered_job = sa_session.get(model.Job, job.id)
        assert recovered_job.state in model.Job.terminal_states, (
            f"Expected job to be in a terminal state after restart, got {recovered_job.state}"
        )
