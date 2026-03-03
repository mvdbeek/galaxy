# Plan: Fix Interrupted Celery set_meta Causes Stuck Non-Terminal Jobs (#20186)

## Problem Analysis

When `metadata_strategy: directory_celery` (or `celery_extended`) is configured, if the Celery process is interrupted (OOM killed, process restart, etc.) while executing a `set_job_metadata` task, jobs become permanently stuck in a non-terminal state (`running`) with no recovery mechanism.

### Root Causes

**Problem 1: Worker death is undetectable**
The handler calls `set_job_metadata.delay(...).get()` which blocks forever. If the worker is OOM-killed, no result is ever written to the backend, so `.get()` hangs indefinitely. The handler thread is stuck, the job stays in `RUNNING`, and there's no way to detect this without restarting Galaxy.

**Problem 2: Silent error swallowing**
In `lib/galaxy/jobs/runners/__init__.py:473-475`, when the celery task does raise an exception (normal failure, not worker death), it's caught with a bare `except Exception` that logs and **returns early**. No job state update occurs.

**Problem 3: No logging on dispatch**
There's no log message when the celery metadata task is dispatched, making troubleshooting difficult.

### Key insight for the fix

Replace the blocking `.get()` with a **`.get(timeout=N)` polling loop** that periodically checks celery worker liveness via `celery_app.control.ping()`. If all workers are dead, the task will never complete — fail immediately instead of hanging forever. This detects worker death in real-time without requiring a Galaxy restart.

Additionally, use the existing **dataset-level** `SETTING_METADATA` state as defense-in-depth for handler restarts. When `setup_external_metadata` is called, it sets output datasets to `SETTING_METADATA` before dispatching. On handler startup, detect jobs with outputs stuck in this state and recover them.

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
- Add a datatype class that extends `Text` and overrides `set_meta` to sleep:
  ```python
  class SlowMetadata(Text):
      file_ext = "slow_metadata"
      def set_meta(self, dataset, **kwd):
          import time
          time.sleep(30)  # long enough to guarantee restart interrupts it
          super().set_meta(dataset, **kwd)
  ```
- Register it via `datatypes_conf_override` in the galaxy config.

**Test abstractions to build:**
- A base test class `CeleryMetadataRecoveryTestCase` that:
  - Configures `metadata_strategy: directory_celery`
  - Registers the slow datatype
  - Provides a helper to run a tool that produces slow-metadata output
  - Provides a helper to wait until datasets are in `SETTING_METADATA` state
- Reuse `UsesCeleryTasks` mixin for celery setup
- Use the `restart()` infrastructure from `IntegrationTestCase`

### Step 2: Replace blocking `.get()` with polling loop + worker health check

**File:** `lib/galaxy/jobs/runners/__init__.py`

Replace:
```python
try:
    set_job_metadata.delay(...).get()
except Exception:
    log.exception("Metadata task failed")
    return
```

With:
```python
from galaxy.celery import celery_app

result = set_job_metadata.delay(...)
log.debug("Dispatched set_job_metadata celery task %s for job %d", result.id, job_wrapper.job_id)
while True:
    try:
        result.get(timeout=CELERY_POLL_INTERVAL)
        break
    except TimeoutError:
        if not celery_app.control.ping(timeout=2.0):
            raise Exception(
                f"No celery workers available to complete metadata task for job {job_wrapper.job_id}"
            )
```

This:
- Detects worker death within one poll interval (no hanging forever)
- `control.ping()` returns an empty list if no workers respond
- Normal task exceptions from `.get()` propagate up (no more silent swallowing)
- The caller (`_finish_or_resubmit_job` / local runner) handles the exception by failing the job

### Step 3: Add recovery for jobs stuck after handler restart (defense-in-depth)

**File:** `lib/galaxy/jobs/handler.py`

Use the existing `SETTING_METADATA` dataset state for recovery on startup:

- When `_check_job_at_startup` finds a job in `RUNNING` state, check if any of its output datasets are in `SETTING_METADATA` state. If so, this job was interrupted during metadata setting.
- For these jobs, instead of dispatching to the runner's `recover()` method, handle recovery directly by calling `finish()` which will retry metadata internally (via `retry_metadata_internally` which defaults to `True`).

This is defense-in-depth for the handler-restart case, which can't be handled by the polling loop since the polling thread itself is gone.

### Step 4: Run and verify tests

Run with:
```bash
./run_tests.sh -integration test/integration/test_celery_metadata_recovery.py
```

## Files to Modify/Create

1. **`test/integration/test_celery_metadata_recovery.py`** (NEW) — Integration tests with slow datatype injection
2. **`lib/galaxy/jobs/runners/__init__.py`** — Replace blocking `.get()` with polling loop + worker health check, add logging
3. **`lib/galaxy/jobs/handler.py`** — Enhance `_check_job_at_startup` to detect jobs with `SETTING_METADATA` outputs and recover them
