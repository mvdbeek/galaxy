# Plan: Improve Handling of Non-Terminal Workflow Invocations (#21978)

## Problem Statement

On production Galaxy instances, workflow invocations accumulate in non-terminal states (NEW, READY, CANCELLING) and never progress to completion. The scheduler must iterate over all of them every loop, causing the loop execution time to grow (reported as ~10 minutes). The default `maximum_workflow_invocation_duration` is 31 days, meaning these invocations sit there for a month before being discarded.

## Investigation: How Invocations Get Stuck

After thorough code analysis, here are the scenarios where invocations remain in non-terminal states indefinitely. Critically, **a job in error state does NOT prevent scheduling** — it's properly handled by `FailWorkflowEvaluation`. The real problems are jobs or collections that never reach any terminal state, and design-level choices about when to fail the whole invocation vs. continue scheduling independent branches.

### Scenario 1: Pause Steps Awaiting User Action (Most Likely Dominant Cause)

**Files:** `lib/galaxy/workflow/modules.py:1903-1936`, `lib/galaxy/workflow/run.py:259-261`

A `PauseModule.execute()` marks step outputs as delayed and returns `None`. On subsequent scheduling iterations, `recover_mapping()` checks `invocation_step.action`. If the user never provides an action (True to approve, False to cancel), `DelayedWorkflowEvaluation` is raised every time. The invocation stays in READY indefinitely until `maximum_workflow_invocation_duration` expires (31 days by default).

**Key insight:** This is by design — pause steps are meant to wait for user input. But users abandon workflows, and these accumulate. The scheduler re-evaluates each one every 5 minutes (backfill timeout) to check if the user acted.

### Scenario 2: Dataset Collection Never Populated

**File:** `lib/galaxy/workflow/run.py:531-551`

When a step produces a `HistoryDatasetCollectionAssociation` that has `populated=False` and `waiting_for_elements=True`, the downstream step raises `DelayedWorkflowEvaluation`. If the job producing the collection elements is stuck (never reaches a terminal state), the collection never populates and the workflow waits forever.

Note: If the producing job errors and the collection gets `waiting_for_elements=False` while still `populated=False`, the code correctly raises `FailWorkflowEvaluation` (line 541). The problem is specifically when the job is stuck, not when it errors.

### Scenario 3: Implicitly Dependent Step's Job Never Finishes

**File:** `lib/galaxy/workflow/run.py:346-352`

For non-data connections (e.g., parameter connections), `__check_implicitly_dependent_step` checks if the upstream step's jobs have all finished. If a job is stuck in a non-terminal state (NEW, QUEUED, RUNNING) due to infrastructure issues, the workflow delays indefinitely.

**When jobs DO error:** If the job reaches ERROR state, `FailWorkflowEvaluation` is raised (lines 354-362), which correctly transitions the invocation to FAILED. So **job errors terminate the invocation promptly** — it's jobs that never reach ANY terminal state that cause stuck invocations.

### Scenario 4: Data-Connected Step with Pending Input

**File:** `lib/galaxy/workflow/run.py:555-587`

For non-data connections that consume dataset values (parameter connections using HDA values), if `replacement.is_pending` returns True, `DelayedWorkflowEvaluation` is raised. The `is_pending` property checks for states (NEW, UPLOAD, QUEUED, RUNNING, SETTING_METADATA). If the producing job is stuck and never completes, the dataset stays pending forever.

For **data** connections, the check happens later at job creation time via `check_inputs_ready()` (`lib/galaxy/tools/__init__.py:3844-3862`). If an input dataset is not OK, `ToolInputsNotOKException` is raised, which is caught in `modules.py:2596` and raises `FailWorkflowEvaluation`. If the input is pending (non-ready state), `ToolInputsNotReadyException` is raised, caught in `modules.py:2564`, and raises `DelayedWorkflowEvaluation`.

### Scenario 5: Subworkflow Stuck in READY State

**File:** `lib/galaxy/workflow/modules.py:840-914`, `lib/galaxy/model/__init__.py:10265-10288`

When a subworkflow invocation gets stuck (due to any of the above reasons), the parent workflow can't complete. The subworkflow invocation is independently polled by `poll_active_workflow_ids` (since it's in READY state). The parent's step for this subworkflow was marked "scheduled" when the subworkflow was initially created, but the completion monitor sees the subworkflow as incomplete via `_is_subworkflow_step_complete()`.

### Scenario 6: CANCELLING State Sticks

**File:** `lib/galaxy/workflow/scheduling_manager.py:441-446`

The CANCELLING handler at line 441-446 runs `cancel_invocation_steps()` → `mark_cancelled()` → `session.commit()`. If `cancel_invocation_steps()` raises an exception (e.g., during subworkflow cascade at `model/__init__.py:9542-9548`), the exception bubbles up to the outer `except` at line 463, and `mark_cancelled()` never runs. The invocation stays CANCELLING.

On the next iteration, the scheduler loads it again, sees it's CANCELLING, and tries again — potentially hitting the same exception repeatedly. The 34 CANCELLING invocations in the issue likely represent this case.

There's also a subtle inefficiency: `poll_active_workflow_ids` returns CANCELLING invocations, but `__attempt_schedule` checks `workflow_invocation.active` (which only considers NEW and READY). For CANCELLING invocations, the cancellation block (line 441) runs before the active check (line 448), so this isn't a problem IF the cancellation succeeds. It's only a problem when cancellation throws.

### Scenario 7: History Update Time Optimization (Performance Context)

**File:** `lib/galaxy/workflow/scheduling_manager.py:339-360`

The `ready_to_schedule_more` optimization prevents re-scheduling unless something changed:
- `history.update_time` changed since last schedule, OR
- A `WorkflowInvocationStep.update_time` changed, OR
- 5 minutes have passed (backfill timeout, `DEFAULT_SCHEDULER_BACKFILL_SECONDS = 300`)

This means stuck invocations are re-evaluated every ~5 minutes, not every second. With 1,931 invocations, each 5-minute backfill cycle processes many of them just to conclude "still stuck." The `poll_active_workflow_ids` query runs every second though, loading all 1,931 IDs from the DB each time.

### What DOESN'T Cause Stuck States

- **Jobs in ERROR state:** `__check_implicitly_dependent_step` correctly raises `FailWorkflowEvaluation`, and `schedule()` catches this and calls `workflow_invocation.fail()`. The invocation transitions to FAILED promptly.
- **Data connections to errored datasets:** The tool's `check_inputs_ready()` raises `ToolInputsNotOKException` when datasets aren't OK, which propagates to `FailWorkflowEvaluation` via `modules.py:2596`.
- **`when` expression evaluation failures:** These correctly raise `FailWorkflowEvaluation` via `modules.py:286`.
- **Expired invocations:** `invoke()` checks `maximum_workflow_invocation_duration` at `run.py:204-209` and fails expired invocations. But this only runs when the invocation is actually scheduled (not during the polling/load phase).

## Proposed Changes

### Change 1: Filter Expired Invocations at Query Level (High Impact, Low Risk)

**File:** `lib/galaxy/model/__init__.py`, `poll_active_workflow_ids` (line 9596)

Currently, `maximum_workflow_invocation_duration` is only checked inside `invoke()` (run.py:204-209). This means expired invocations are still returned by the poll query, loaded by `Session.get()`, evaluated by `ready_to_schedule_more()`, then finally failed inside `invoke()`. With 1,000+ old invocations, this is extremely wasteful.

**Implementation:** Pass `maximum_workflow_invocation_duration` to `poll_active_workflow_ids` and add a filter: `WorkflowInvocation.create_time > func.now() - timedelta(seconds=duration)`. Invocations past the duration limit will be excluded from the scheduler loop entirely.

Note: We still need a mechanism to transition these to FAILED (see Change 4). But removing them from the hot loop is the immediate win.

### Change 2: Fix CANCELLING State Exception Handling (Bug Fix)

**Files:** `lib/galaxy/workflow/scheduling_manager.py`

**Problem:** If `cancel_invocation_steps()` raises, the invocation stays CANCELLING forever.

**Fix:** Wrap the cancellation logic in try/except. If `cancel_invocation_steps()` fails, still call `mark_cancelled()` and commit. Log the error but don't let it prevent the state transition. A best-effort cancellation is better than a permanently stuck CANCELLING invocation.

```python
if workflow_invocation.state == workflow_invocation.states.CANCELLING:
    try:
        workflow_invocation.cancel_invocation_steps()
    except Exception:
        log.exception("Failed to cancel invocation steps for %s, marking cancelled anyway", invocation_id)
    workflow_invocation.mark_cancelled()
    session.commit()
    self.update_time_tracking_dict.pop(invocation_id, None)
    return False
```

### Change 3: Batch-Fail Expired Invocations (Complements Change 1)

**File:** `lib/galaxy/workflow/scheduling_manager.py`

After Change 1 removes expired invocations from the scheduler loop, we need a mechanism to actually transition them to FAILED. Add a periodic batch operation (e.g., once per scheduler loop) that runs a single SQL UPDATE to fail all invocations past `maximum_workflow_invocation_duration`.

**Implementation:** In `__monitor()`, before the scheduler loop, execute:
```sql
UPDATE workflow_invocation SET state = 'failed'
WHERE state IN ('new', 'ready', 'requires_materialization')
AND create_time < now() - interval 'maximum_workflow_invocation_duration seconds'
```
Also add an appropriate `InvocationFailure` message.

### Change 4: Exponential Backoff for No-Progress Invocations (Performance)

**File:** `lib/galaxy/workflow/scheduling_manager.py`

**Problem:** `ready_to_schedule_more` returns True every 5 minutes for all stuck invocations, even if no progress has been made in weeks.

**Implementation:** Track a per-invocation `no_progress_count` alongside `update_time_tracking_dict`. When scheduling runs and produces no state changes (the invocation is still in the same state with the same step states), increment the counter. Use it to exponentially increase the backfill timeout for that invocation:

```python
effective_backfill = self.timedelta * (2 ** min(self.no_progress_count.get(invocation_id, 0), 6))
# Cap at ~5 hours (300s * 64 = 19200s). Reset on any progress.
```

This means:
- First evaluation: 5 minutes
- After 1 no-progress evaluation: 10 minutes
- After 2: 20 minutes
- After 6+: ~5 hours

### Change 5: Consider Not Failing Entire Invocation on Step Dependency Error

**Files:** `lib/galaxy/workflow/run.py`

**Current behavior:** When `__check_implicitly_dependent_step` finds a dependent job in ERROR (line 354), it raises `FailWorkflowEvaluation`, which fails the **entire** invocation. This means if step A errors and step B depends on A via a non-data connection, all other independent branches (steps C, D, E...) are also killed.

**The user's note ("do not assume that a job in error means we can't schedule more") points to this:** A job in error should potentially allow independent branches to continue rather than failing the whole invocation.

This is a larger design change that requires careful consideration:
- For **non-data connections** where the dependent step has a `when` expression that could evaluate to False on error → the step should be skipped rather than failing the invocation.
- For **data connections** where the downstream tool requires OK inputs → the step can't run, but independent branches should proceed.
- The current `FailWorkflowEvaluation` propagation model is all-or-nothing. Changing to per-step failure requires a new mechanism to mark individual steps as failed while continuing to schedule others.

**Possible implementation approach:**
1. Instead of raising `FailWorkflowEvaluation` from `__check_implicitly_dependent_step`, treat it like `DelayedWorkflowEvaluation` with an error marker.
2. Mark the dependent step as failed/skipped and continue iterating through remaining steps.
3. At the end of the scheduling loop, if ALL remaining steps are either completed or failed, transition to SCHEDULED (allowing completion monitor to detect it).
4. Only fail the entire invocation if a critical invariant is violated.

This change needs careful design to avoid running steps that shouldn't run and to correctly propagate error state through the dependency graph.

### Change 6: Admin Observability for Stuck Invocations

**File:** `lib/galaxy/workflow/scheduling_manager.py`

Add WARNING-level logging when:
- An invocation has been in READY state for more than 24 hours
- The scheduler loop takes more than a configurable threshold (e.g., 60 seconds)
- The number of active invocations exceeds a threshold

This helps admins catch accumulation before it becomes a performance problem.

## Implementation Order

1. **Change 1** (Filter expired at query level) — Immediate, high-impact performance improvement
2. **Change 2** (Fix CANCELLING exception handling) — Simple bug fix
3. **Change 3** (Batch-fail expired invocations) — Completes Change 1, clears accumulated debris
4. **Change 4** (Exponential backoff) — Performance improvement for the steady-state
5. **Change 6** (Admin observability) — Low effort, high value for operators
6. **Change 5** (Per-step failure instead of invocation failure) — Larger design change, separate PR

## Files to Modify

- `lib/galaxy/model/__init__.py` — `poll_active_workflow_ids` query optimization (add duration filter)
- `lib/galaxy/workflow/scheduling_manager.py` — CANCELLING fix, batch-fail, exponential backoff, logging
- `lib/galaxy/workflow/run.py` — Per-step failure handling (Change 5, separate PR)
- `lib/galaxy/config/schemas/config_schema.yml` — New config options if needed
- `lib/galaxy/config/sample/galaxy.yml.sample` — Document new options
- `test/integration/test_workflow_scheduling_options.py` — Tests for new behavior

## Summary of Root Causes (Ranked by Likely Impact)

| Cause | Invocations in Issue | State | Why It Persists |
|-------|---------------------|-------|-----------------|
| Pause steps without user action | ~1,673 (NEW) + ~224 (READY) | READY | By design; 31-day timeout |
| Stuck jobs (never reach terminal) | Subset of READY | READY | No job-level timeout exists |
| Failed cancellation cascade | 34 | CANCELLING | Exception prevents state transition |
| Subworkflow stuck → parent stuck | Subset of READY | READY | Recursive; child stuck = parent stuck |
| Collection never populated | Subset of READY | READY | Producing job stuck |

The 1,673 NEW invocations may also include invocations that were never assigned to a handler, or ones that need materialization but are stuck — worth investigating further with actual database queries on the production instance.
