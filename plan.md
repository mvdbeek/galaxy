# Plan: Fix Interrupted Celery set_meta Causes Stuck Non-Terminal Jobs (#20186)

## Problem Analysis

When `metadata_strategy: directory_celery` (or `celery_extended`) is configured, if the Celery process is interrupted (OOM killed, process restart, etc.) while executing a `set_job_metadata` task, jobs become permanently stuck in a non-terminal state (`running`) with no recovery mechanism.

### Root Cause

**The handler blocks forever on `.get()` when a worker dies.**

The handler calls `set_job_metadata.delay(...).get()` which blocks indefinitely. If the worker is OOM-killed, no result is ever written to the backend, so `.get()` hangs forever. The handler thread is stuck, and the job stays in `RUNNING`.

Note: when the celery task raises a normal exception (not worker death), `.get()` does propagate it. The `except Exception` on line 473 catches it and returns, but execution continues to `_finish_or_resubmit_job` → `finish()` which retries metadata internally (via `retry_metadata_internally`, default `True`). So **normal task failures are already handled** — the problem is specifically worker death causing `.get()` to hang forever.

Additionally, there's no logging when the celery metadata task is dispatched, making troubleshooting difficult.

### Approaches considered and rejected

**`acks_late=True` + `reject_on_worker_lost=True`**: Would automatically requeue the task when a worker dies, giving it a chance to succeed on another worker. However, broker-level requeue bypasses Celery's `max_retries` entirely (the broker sees a fresh message), creating an infinite death loop if the task consistently OOMs. This is a [known Celery issue](https://github.com/celery/celery/issues/9082) with no clean solution — workarounds require broker-specific features (RabbitMQ DLX) that aren't portable.

## Implementation Plan

### Step 1: Write Integration Tests (test-first)

**File:** `test/integration/test_celery_metadata_recovery.py`

Create integration tests that verify:

1. **Test: Job recovery after handler restart during celery metadata** — Run a tool whose datatype has a slow `set_meta` (sleeps), restart Galaxy while metadata is being set, verify the job reaches a terminal state after recovery.

2. **Test: Job reaches terminal state when celery worker dies** — Verify the polling loop detects dead workers and the job is failed/recovered.

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
- Normal task exceptions from `.get()` propagate up naturally (they already did — `finish()` handles them via `retry_metadata_internally`)
- When all workers are dead, raises an exception; the caller proceeds to `finish()` which retries metadata internally
- Adds dispatch logging for troubleshooting

### Step 3: Add recovery for jobs stuck after handler restart (defense-in-depth)

**File:** `lib/galaxy/jobs/handler.py`

Use the existing `SETTING_METADATA` dataset state for recovery on startup:

- When `_check_job_at_startup` finds a job in `RUNNING` state, check if any of its output datasets are in `SETTING_METADATA` state. If so, this job was interrupted during metadata setting (the handler restarted while blocked on `.get()`).
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
