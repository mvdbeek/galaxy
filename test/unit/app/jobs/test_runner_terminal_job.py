from unittest.mock import Mock

import pytest

from galaxy.jobs.runners import (
    AsynchronousJobState,
    BaseJobRunner,
)


@pytest.fixture
def job_state(tmp_path):
    wrapper = Mock()
    wrapper.working_directory = str(tmp_path)
    wrapper.get_id_tag.return_value = "1"
    wrapper.get_state.return_value = "running"
    wrapper.app.config.redact_email_in_job_name = True
    return AsynchronousJobState(wrapper, wrapper.job_destination, job_id="1234")


def test_fail_job_keeps_tool_output(tmp_path, job_state):
    outputs = tmp_path / "outputs"
    outputs.mkdir()
    (outputs / "tool_stdout").write_text("tool stdout")
    (outputs / "tool_stderr").write_text("slurmstepd: error: Detected 1 oom_kill event")
    job_state.output_file = str(tmp_path / "galaxy_1.o")
    job_state.error_file = str(tmp_path / "galaxy_1.e")
    (tmp_path / "galaxy_1.o").write_text("job stdout")
    (tmp_path / "galaxy_1.e").write_text("job stderr")
    with open(job_state.exit_code_file, "w") as f:
        f.write("137")
    job_state.stop_job = False
    job_state.fail_message = "This job was terminated because it used more memory than it was allocated."
    runner = object.__new__(BaseJobRunner)
    runner.runner_state_handlers = {}

    runner.fail_job(job_state)

    job_state.job_wrapper.fail.assert_called_once_with(
        job_state.fail_message,
        tool_stdout="tool stdout",
        tool_stderr="slurmstepd: error: Detected 1 oom_kill event",
        exit_code=137,
        job_stdout="job stdout",
        job_stderr="job stderr",
        exception=False,
    )


def test_fail_job_before_job_started(job_state):
    job_state.stop_job = False
    runner = object.__new__(BaseJobRunner)
    runner.runner_state_handlers = {}

    runner.fail_job(job_state, message="Cluster could not complete job")

    job_state.job_wrapper.fail.assert_called_once_with(
        "Cluster could not complete job",
        tool_stdout="",
        tool_stderr="",
        exit_code=None,
        job_stdout=None,
        job_stderr=None,
        exception=False,
    )


def test_fail_job_prefers_remote_status(tmp_path, job_state):
    outputs = tmp_path / "outputs"
    outputs.mkdir()
    (outputs / "tool_stdout").write_text("stale local stdout")
    job_state.stop_job = False
    runner = object.__new__(BaseJobRunner)
    runner.runner_state_handlers = {}
    full_status = {
        "stdout": "remote stdout",
        "stderr": "remote stderr",
        "job_stdout": "remote job stdout",
        "job_stderr": "remote job stderr",
        "returncode": 3,
    }

    runner.fail_job(job_state, message="Remote job failed", full_status=full_status)

    job_state.job_wrapper.fail.assert_called_once_with(
        "Remote job failed",
        tool_stdout="remote stdout",
        tool_stderr="remote stderr",
        exit_code=3,
        job_stdout="remote job stdout",
        job_stderr="remote job stderr",
        exception=False,
    )
