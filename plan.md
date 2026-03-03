# Plan: Fix Interrupted Celery set_meta Causes Stuck Non-Terminal Jobs (#20186)

## Problem Analysis

When `metadata_strategy: directory_celery` (or `celery_extended`) is configured, if the Celery process is interrupted (OOM killed, process restart, etc.) while executing a `set_job_metadata` task, jobs become permanently stuck in a non-terminal state (`running`) with no recovery mechanism.

### Root Causes

There are two related problems:

**Problem 1: Celery worker dies during `set_job_metadata` task**
The `set_job_metadata` task has no `acks_late` or `reject_on_worker_lost` settings. By default, Celery acks the message as soon as the worker **starts** the task. If the worker is OOM-killed mid-task, the message is already gone from the broker. The handler thread blocked on `.get()` will either hang forever or eventually get an error, which is silently swallowed (line 473-475 of `runners/__init__.py`).

**Problem 2: Galaxy handler restarts while blocked on `.get()`**
When a handler restarts while its thread is blocked on `set_job_metadata.delay().get()`:
- For Pulsar + MQ: The completion message was already acknowledged but job state was never updated. On restart, Pulsar recovery puts the job back in the monitor queue, but Pulsar already considers it complete. The job is stuck in RUNNING forever.
- For local runner: `recover()` sets jobs to ERROR ("killed when Galaxy restarted"), which works but is a poor experience since the job actually completed successfully — only metadata setting was interrupted.

**Problem 3: Silent error swallowing**
In `lib/galaxy/jobs/runners/__init__.py:473-475`, the celery task failure is caught with a bare `except Exception` that logs and **returns early**. No state update occurs. There's also no logging when the celery task is dispatched, making troubleshooting difficult.

### Key insight for the fix

There are two complementary solutions:

1. **Celery-native**: Add `acks_late=True` + `reject_on_worker_lost=True` to `set_job_metadata`. This makes Celery automatically requeue the task when a worker dies. The handler's `.get()` will eventually succeed when another worker picks it up. This handles the "celery worker dies" case without Galaxy needing to do anything.

2. **Galaxy recovery**: For the "handler restarts" case, use the existing **dataset-level** `SETTING_METADATA` state for recovery. When `setup_external_metadata` is called (line 453 in `runners/__init__.py`), it sets output datasets to `SETTING_METADATA` state before dispatching the celery task. If Galaxy restarts, those datasets remain in `SETTING_METADATA`. On startup, detect these jobs and recover them.

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

### Step 2: Add `acks_late` + `reject_on_worker_lost` to `set_job_metadata`

**File:** `lib/galaxy/celery/tasks.py`

Change the task decorator:
```python
@galaxy_task(action="set metadata for job", acks_late=True, reject_on_worker_lost=True)
def set_job_metadata(...):
```

This is the Celery-native fix for the "worker dies" case:
- `acks_late=True`: Message is acked only after the task completes successfully, not when the worker starts it.
- `reject_on_worker_lost=True`: If the worker connection drops (OOM kill, crash), the message is explicitly rejected and requeued by the broker.
- The handler's `.get()` call will eventually return when another worker (or the restarted worker) picks up the requeued task.

This handles the primary issue scenario (celery OOM killed) entirely within Celery's broker mechanism — no Galaxy restart or recovery logic needed.

### Step 3: Fix `_handle_metadata_externally` to not silently fail

**File:** `lib/galaxy/jobs/runners/__init__.py`

Changes:
- Add logging when dispatching celery metadata task: `log.debug("dispatching set_job_metadata celery task for job %d", job_wrapper.job_id)`
- When the celery task raises an exception, instead of just `return`, **re-raise** the exception so the caller can handle it. The caller (`_finish_or_resubmit_job` / local runner) will catch it and fail the job properly.

### Step 4: Add recovery for jobs stuck after handler restart during celery metadata

**File:** `lib/galaxy/jobs/handler.py` and/or `lib/galaxy/managers/jobs.py`

Use the existing `SETTING_METADATA` dataset state for recovery:

- When `_check_job_at_startup` finds a job in `RUNNING` state, check if any of its output datasets are in `SETTING_METADATA` state. If so, this job was interrupted during metadata setting (the handler restarted while blocked on `.get()`).
- For these jobs, instead of dispatching to the runner's `recover()` method (which may not know how to handle this — e.g., local runner just errors, Pulsar tries to re-monitor a completed job), handle recovery directly:
  - Re-dispatch the celery metadata task and call `finish()`, OR
  - Call `finish()` which will retry metadata internally (via `retry_metadata_internally` which defaults to `True`), OR
  - At minimum, fail the job with a clear error message instead of leaving it stuck.

The preferred approach is to attempt `finish()` again since the compute outputs are already available — this allows `retry_metadata_internally` (which defaults to `True`) to re-set metadata in-process.

### Step 5: Run and verify tests

Run with:
```bash
./run_tests.sh -integration test/integration/test_celery_metadata_recovery.py
```

## Files to Modify/Create

1. **`test/integration/test_celery_metadata_recovery.py`** (NEW) — Integration tests with slow datatype injection
2. **`lib/galaxy/celery/tasks.py`** — Add `acks_late=True` + `reject_on_worker_lost=True` to `set_job_metadata`
3. **`lib/galaxy/jobs/runners/__init__.py`** — Fix `_handle_metadata_externally` to not silently swallow celery failures, add logging
4. **`lib/galaxy/jobs/handler.py`** — Enhance `_check_job_at_startup` to detect jobs interrupted during celery metadata (output datasets in `SETTING_METADATA`) and recover them
5. **`lib/galaxy/managers/jobs.py`** — Possibly extend `get_jobs_to_check_at_startup` if needed
