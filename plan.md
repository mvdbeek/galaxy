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

The core issue is that `_handle_metadata_externally` with celery uses a synchronous `.get()` call that blocks the handler thread. If this is interrupted, there's no persistent record that metadata setting was in progress, and no mechanism to retry it on restart.

However, the **dataset-level** `SETTING_METADATA` state IS already persisted in the DB. When `setup_external_metadata` is called (line 453 in `runners/__init__.py`), it sets output datasets to `SETTING_METADATA` state before dispatching the celery task. If celery dies, those datasets remain in `SETTING_METADATA`. This state should be used for recovery — no marker files needed.

The fix should:
1. Make the metadata celery dispatch failure **not silently swallow the error** — at minimum, the job should be failed with a clear message rather than left in running state
2. Add a recovery mechanism: on startup, detect jobs in `RUNNING` state whose output datasets are in `SETTING_METADATA` state, and retry metadata or fail them cleanly
3. Add logging for celery set_meta dispatches (as noted in the issue)

## Implementation Plan

### Step 1: Write Integration Tests (test-first)

**File:** `test/integration/test_celery_metadata_recovery.py`

Create integration tests that verify:

1. **Test: Job recovery after handler restart during celery metadata** — Run a tool whose datatype has a slow `set_meta` (sleeps), restart Galaxy while metadata is being set, verify the job reaches a terminal state after recovery.

2. **Test: Job completes after celery metadata failure** — When celery metadata setting fails (e.g., task raises exception), the job should not be left in a non-terminal state.

**Test strategy — injecting a slow datatype:**
- Register a custom datatype (e.g., `SlowMetadata`) whose `set_meta` method sleeps for a configurable number of seconds. This guarantees the restart will always interrupt metadata setting.
- Use `handle_galaxy_config_kwds` to configure `metadata_strategy: directory_celery` and register the custom datatype.
- Run a tool that produces output with this datatype.
- While `set_meta` is sleeping (datasets in `SETTING_METADATA` state), call `self.restart()` to restart Galaxy.
- After restart, verify the job reaches a terminal state (either OK with re-run metadata, or ERROR/FAILED_METADATA).

**Slow datatype implementation:**
- Add a datatype class in the test file (or a test helper) that extends `Text` and overrides `set_meta` to sleep:
  ```python
  class SlowMetadata(Text):
      file_ext = "slow_metadata"
      def set_meta(self, dataset, **kwd):
          import time
          time.sleep(30)  # long enough to guarantee restart interrupts it
          super().set_meta(dataset, **kwd)
  ```
- Register it via `datatypes_conf_override` in the galaxy config or by dynamically adding it to the datatypes registry.

**Test abstractions to build:**
- A base test class `CeleryMetadataRecoveryTestCase` that:
  - Configures `metadata_strategy: directory_celery` (or `celery_extended`)
  - Registers the slow datatype
  - Provides a helper to run a tool that produces slow-metadata output
  - Provides a helper to wait until datasets are in `SETTING_METADATA` state
- Reuse `UsesCeleryTasks` mixin for celery setup
- Use the `restart()` infrastructure from `IntegrationTestCase`

### Step 2: Fix `_handle_metadata_externally` to not silently fail

**File:** `lib/galaxy/jobs/runners/__init__.py`

Changes:
- Add logging when dispatching celery metadata task (line ~468): `log.debug("dispatching set_job_metadata celery task for job %d", job_wrapper.job_id)`
- When the celery task raises an exception, instead of just `return`, **re-raise** the exception so the caller can handle it. The caller (`_finish_or_resubmit_job` / local runner) will then catch it and fail the job properly.

### Step 3: Add recovery for jobs stuck after celery metadata interruption

**File:** `lib/galaxy/jobs/handler.py` and/or `lib/galaxy/managers/jobs.py`

Use the existing `SETTING_METADATA` dataset state for recovery:

- When `_check_job_at_startup` finds a job in `RUNNING` state, check if any of its output datasets are in `SETTING_METADATA` state. If so, this job was interrupted during metadata setting.
- For these jobs, instead of dispatching to the runner's `recover()` method (which may not know how to handle this — e.g., local runner just errors, Pulsar tries to re-monitor a completed job), handle recovery directly:
  - Re-dispatch the celery metadata task, OR
  - Call `finish()` with `retry_metadata_internally=True`, OR
  - At minimum, fail the job with a clear error message instead of leaving it stuck.

The preferred approach is to attempt `finish()` again since the compute outputs are already available — this allows `retry_metadata_internally` (which defaults to `True`) to re-set metadata in-process.

### Step 4: Run and verify tests

Run with:
```bash
./run_tests.sh -integration test/integration/test_celery_metadata_recovery.py
```

## Files to Modify/Create

1. **`test/integration/test_celery_metadata_recovery.py`** (NEW) — Integration tests with slow datatype injection
2. **`lib/galaxy/jobs/runners/__init__.py`** — Fix `_handle_metadata_externally` to not silently swallow celery failures, add logging
3. **`lib/galaxy/jobs/handler.py`** — Enhance `_check_job_at_startup` to detect jobs interrupted during celery metadata (output datasets in `SETTING_METADATA`) and recover them
4. **`lib/galaxy/managers/jobs.py`** — Possibly extend `get_jobs_to_check_at_startup` if needed
