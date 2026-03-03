# Plan: Fix Interrupted Celery set_meta Causes Stuck Non-Terminal Jobs (#20186)

## Problem Analysis

When `metadata_strategy: directory_celery` (or `celery_extended`) is configured, if the Celery process is interrupted (OOM killed, process restart, etc.) while executing a `set_job_metadata` task, jobs become permanently stuck in a non-terminal state (`running`) with no recovery mechanism.

### Root Causes

There are two related problems:

**Problem 1: Celery failure during `_handle_metadata_externally`**
In `lib/galaxy/jobs/runners/__init__.py:467-475`, the celery task failure is caught with a bare `except Exception` that logs the error and **returns early** without any state update. For the local runner, `_finish_or_resubmit_job` is still called afterward, so the job will still finish (with potentially bad metadata). But if the Galaxy handler itself restarts while blocked on `.get()`, the thread is killed and the job stays in RUNNING forever.

**Problem 2: Handler restart during Celery metadata wait (especially with Pulsar)**
When a handler restarts while its thread is blocked on `set_job_metadata.delay().get()`:
- For Pulsar + MQ: The completion message was already acknowledged but job state was never updated. On restart, Pulsar recovery puts the job back in the monitor queue, but Pulsar already considers it complete. The job is stuck in RUNNING forever.
- For local runner: `recover()` sets jobs to ERROR ("killed when Galaxy restarted"), which works but is a poor experience since the job actually completed successfully — only metadata setting was interrupted.

**Missing:** `get_jobs_to_check_at_startup` in `lib/galaxy/managers/jobs.py:2077-2092` only checks `QUEUED`, `RUNNING`, `STOPPED` states. There is no special handling to detect jobs that were in the middle of Celery metadata setting and retry/complete them.

### Key insight for the fix

The core issue is that `_handle_metadata_externally` with celery uses a synchronous `.get()` call that blocks the handler thread. If this is interrupted, there's no persistent record that metadata setting was in progress, and no mechanism to retry it on restart. The fix should:

1. Make the metadata celery dispatch failure **not silently swallow the error** — at minimum, the job should be failed with a clear message rather than left in running state
2. Add a recovery mechanism for jobs that were in the middle of celery metadata setting when Galaxy restarted
3. Add logging for celery set_meta dispatches (as noted in the issue)

## Implementation Plan

### Step 1: Write Integration Tests (test-first)

**File:** `test/integration/test_celery_metadata_recovery.py`

Create integration tests that verify:

1. **Test: Job completes after celery metadata failure** — When celery metadata setting fails (e.g., task raises exception), the job should not be left in a non-terminal state. It should either retry metadata internally or be set to an error/failed_metadata state.

2. **Test: Job recovery after handler restart during celery metadata** — Simulate a handler restart while a job's metadata is being set via celery. After restart, the job should be recovered (either re-run metadata or fail cleanly).

The test strategy:
- Use `handle_galaxy_config_kwds` to configure `metadata_strategy: celery_extended`
- Run a tool that produces output
- Before the celery metadata task completes, simulate the failure scenario
- Verify the job reaches a terminal state after recovery/restart

To simulate celery metadata failure without actually killing celery, we can:
- Use a mock/monkeypatch approach on `set_job_metadata` to raise an exception
- Or use the `restart()` test infrastructure to restart Galaxy while a job is in progress

Following the pattern from `test_job_recovery.py`, the restart-based test is the most realistic integration test approach.

**Test abstractions to build:**
- A base class `CeleryMetadataRecoveryTestCase` that configures `metadata_strategy: celery_extended` and provides helper methods
- Helper to set a job to the state where it's post-execution but metadata hasn't been set

### Step 2: Fix `_handle_metadata_externally` to not silently fail

**File:** `lib/galaxy/jobs/runners/__init__.py`

Changes:
- Add logging when dispatching celery metadata task (line ~468): `log.debug("dispatching set_job_metadata celery task for job %d", job_wrapper.job_id)`
- When the celery task raises an exception, instead of just `return`, **re-raise** the exception or set a flag so the caller knows metadata failed. The caller (`_finish_or_resubmit_job` / local runner) should then handle it appropriately (fail the job or retry metadata internally).

### Step 3: Add recovery for jobs stuck after celery metadata interruption

**File:** `lib/galaxy/jobs/handler.py` and/or `lib/galaxy/managers/jobs.py`

The `_check_job_at_startup` method needs to handle the case where a job is in RUNNING state but its compute job already completed (external job finished), and it was interrupted during metadata setting.

Two approaches:
- **Approach A (preferred):** Modify `_handle_metadata_externally` to record the celery task state (e.g., via a flag on the job or a marker file in the working directory). On recovery, detect this and re-dispatch the celery metadata task or retry internally.
- **Approach B:** On recovery, if the working directory still exists and has compute outputs but metadata wasn't finalized, attempt to re-run `finish()` for the job.

The simplest approach: when `_handle_metadata_externally` dispatches a celery task, write a marker file. When recovery runs and finds a job in RUNNING state whose external job is complete but has this marker, re-attempt metadata setting or just call `finish()` which will retry metadata internally.

### Step 4: Run and verify tests

Run with:
```bash
./run_tests.sh -integration test/integration/test_celery_metadata_recovery.py
```

## Files to Modify

1. **`test/integration/test_celery_metadata_recovery.py`** (NEW) — Integration tests
2. **`lib/galaxy/jobs/runners/__init__.py`** — Fix `_handle_metadata_externally` to not silently swallow celery failures, add logging
3. **`lib/galaxy/jobs/handler.py`** — Enhance `_check_job_at_startup` to handle post-compute-pre-metadata jobs
4. **`lib/galaxy/managers/jobs.py`** — Possibly extend `get_jobs_to_check_at_startup` if needed
