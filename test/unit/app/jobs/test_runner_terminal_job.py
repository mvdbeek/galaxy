import subprocess
from queue import Queue
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from galaxy.jobs.command_factory import CommandsBuilder
from galaxy.jobs.runners import (
    AsynchronousJobRunner,
    AsynchronousJobState,
    BaseJobRunner,
    cli as cli_runner,
    drmaa as drmaa_runner,
    slurm as slurm_runner,
)
from galaxy.jobs.runners.util.job_script import (
    EXIT_WITH_TOOL_EXIT_CODE,
    EXIT_WITH_ZERO,
    job_script,
)
from galaxy.util import commands

DRMAA_JOB_STATES = SimpleNamespace(DONE="done", FAILED="failed")


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


@pytest.fixture
def runner(monkeypatch):
    runner = object.__new__(AsynchronousJobRunner)
    runner.app = Mock()
    runner.app.config.retry_job_output_collection = 0
    runner.work_queue = Queue()
    monkeypatch.setattr(runner, "finish_job", Mock())
    monkeypatch.setattr(runner, "fail_job", Mock())
    return runner


@pytest.fixture
def slurm(monkeypatch):
    monkeypatch.setattr(drmaa_runner, "drmaa", SimpleNamespace(JobState=DRMAA_JOB_STATES))
    runner = object.__new__(slurm_runner.SlurmJobRunner)
    runner.drmaa_job_states = DRMAA_JOB_STATES
    runner.work_queue = Queue()

    def reports(slurm_state):
        monkeypatch.setattr(commands, "execute", lambda cmd: f"JobId=1234 JobState={slurm_state} Reason=None")
        return runner

    return reports


def queued(runner):
    items = []
    while not runner.work_queue.empty():
        method, arg = runner.work_queue.get_nowait()
        items.append((method.__name__, arg))
    return items


@pytest.mark.parametrize("exit_code", [0, 1, 137])
def test_recorded_exit_code_finishes_job(runner, job_state, exit_code):
    with open(job_state.exit_code_file, "w") as f:
        f.write(f"{exit_code}\n")

    runner.finish_or_fail_job(job_state)

    runner.finish_job.assert_called_once_with(job_state)
    runner.fail_job.assert_not_called()


def test_empty_exit_code_file_fails_job(runner, job_state):
    open(job_state.exit_code_file, "w").close()

    runner.finish_or_fail_job(job_state)

    runner.fail_job.assert_called_once_with(job_state)
    runner.finish_job.assert_not_called()


def test_missing_exit_code_fails_job(runner, job_state):
    runner.finish_or_fail_job(job_state)

    runner.fail_job.assert_called_once_with(job_state)
    runner.finish_job.assert_not_called()
    assert job_state.stop_job is False


def test_slurm_failed_is_decided_by_tool_exit_code(slurm, job_state):
    runner = slurm("FAILED")

    runner._complete_terminal_job(job_state, drmaa_state=DRMAA_JOB_STATES.FAILED)

    assert queued(runner) == [("finish_or_fail_job", job_state)]
    assert job_state.stop_job is False


@pytest.mark.parametrize(
    "slurm_state, runner_state",
    [
        ("OUT_OF_MEMORY", AsynchronousJobState.runner_states.MEMORY_LIMIT_REACHED),
        ("TIMEOUT", AsynchronousJobState.runner_states.WALLTIME_REACHED),
    ],
)
def test_slurm_limit_reached_fails_job(slurm, job_state, slurm_state, runner_state):
    runner = slurm(slurm_state)

    runner._complete_terminal_job(job_state, drmaa_state=DRMAA_JOB_STATES.FAILED)

    assert queued(runner) == [("fail_job", job_state)]
    assert job_state.runner_state == runner_state


def test_drmaa_failed_is_decided_by_tool_exit_code(slurm, job_state):
    runner = slurm("FAILED")

    drmaa_runner.DRMAAJobRunner._complete_terminal_job(runner, job_state, drmaa_state=DRMAA_JOB_STATES.FAILED)

    assert queued(runner) == [("finish_or_fail_job", job_state)]


def test_drmaa_failed_with_drm_reason_fails_job(slurm, job_state):
    runner = slurm("FAILED")
    job_state.runner_state = job_state.runner_states.MEMORY_LIMIT_REACHED

    drmaa_runner.DRMAAJobRunner._complete_terminal_job(runner, job_state, drmaa_state=DRMAA_JOB_STATES.FAILED)

    assert queued(runner) == [("fail_job", job_state)]


@pytest.mark.parametrize("instrument_post_commands", ["", "date +%s > __instrument_core_epoch_end"])
@pytest.mark.parametrize(
    "exit_statement, tool_exit_code, script_exit_code",
    [
        (EXIT_WITH_TOOL_EXIT_CODE, 0, 0),
        (EXIT_WITH_TOOL_EXIT_CODE, 3, 3),
        (EXIT_WITH_ZERO, 3, 0),
    ],
)
def test_job_script_exit_code(tmp_path, instrument_post_commands, exit_statement, tool_exit_code, script_exit_code):
    exit_code_file = tmp_path / "galaxy_1.ec"
    builder = CommandsBuilder(f"exit_with() {{ return $1; }}; exit_with {tool_exit_code}")
    builder.capture_return_code(str(exit_code_file))
    script = tmp_path / "galaxy_1.sh"
    script.write_text(
        job_script(
            working_directory=str(tmp_path),
            command=builder.build(),
            instrument_post_commands=instrument_post_commands,
            exit_statement=exit_statement,
            integrity_injection="",
        )
    )

    result = subprocess.run(["/bin/bash", str(script)], cwd=tmp_path)

    assert result.returncode == script_exit_code
    assert exit_code_file.read_text().strip() == str(tool_exit_code)


@pytest.mark.parametrize(
    "runner_state, method",
    [
        (None, "finish_or_fail_job"),
        (AsynchronousJobState.runner_states.MEMORY_LIMIT_REACHED, "mark_as_failed"),
    ],
)
def test_cli_error_is_decided_by_tool_exit_code(monkeypatch, job_state, runner_state, method):
    runner = object.__new__(cli_runner.ShellJobRunner)
    runner.work_queue = Queue()
    job_state.old_state = "running"
    runner.watched = [job_state]
    job_interface = Mock()
    job_interface.parse_failure_reason.return_value = runner_state
    monkeypatch.setattr(runner, "_ShellJobRunner__get_job_states", lambda: {"1234": "error"})
    monkeypatch.setattr(runner, "parse_destination_params", lambda params: ({}, {}))
    monkeypatch.setattr(runner, "get_cli_plugins", lambda shell_params, job_params: (Mock(), job_interface))

    runner.check_watched_items()

    assert queued(runner) == [(method, job_state)]
    assert runner.watched == []
