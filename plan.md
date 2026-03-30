# Plan: Fix Workflow Scheduling Failure with 'auto' Extension on Dataset Collections

## Issue
galaxyproject/galaxy#22261 — Workflow invocation fails with `RequestParameterInvalidException: Extension 'auto' unknown, cannot use dataset collection as input` when a dataset collection contains datasets whose extension hasn't been resolved yet (still `auto` or `_sniff_`).

## Root Cause

In `lib/galaxy/tools/actions/__init__.py:306-315`, `_collect_input_datasets()` retrieves the `dataset_states_and_extensions_summary` for a collection and validates each extension against the datatypes registry. The extension `auto` (and `_sniff_`) are placeholder values used while a dataset's type is still being detected — they are not registered datatypes, so `get_datatype_by_extension('auto')` returns `None`, causing the `RequestParameterInvalidException`.

The workflow scheduler should **delay** this step (like it does for other not-yet-ready inputs) instead of failing. There's already a precedent: `datatype_for_extension()` in `lib/galaxy/model/__init__.py:5098-5107` treats `auto` and `_sniff_` as equivalent to `data`. But in the workflow context, the correct behavior is to wait for the real extension to be determined.

### Why existing safeguards don't catch this

In `lib/galaxy/workflow/run.py:557-589`, pending dataset checks for HDCA collections only run when `is_data=False`. When `is_data=True` (the default for data inputs), the collection passes through `replacement_for_connection()` without checking whether its datasets are still pending. So the collection with unresolved `auto` extensions reaches `_collect_input_datasets()` and fails.

## Implementation Plan

### Step 1: Handle 'auto'/'_sniff_' extensions in `_collect_input_datasets`

**File:** `lib/galaxy/tools/actions/__init__.py` (~line 309-315)

In the loop that validates extensions from `dataset_states_and_extensions_summary`, treat `auto` and `_sniff_` as unresolved placeholder extensions. Instead of raising `RequestParameterInvalidException`, raise `ToolInputsNotReadyException` (which is already defined and handled by the tool execution framework).

**Current code (lines 308-315):**
```python
conversion_required = False
for ext in extensions:
    if ext:
        datatype = trans.app.datatypes_registry.get_datatype_by_extension(ext)
        if not datatype:
            raise RequestParameterInvalidException(
                f"Extension '{ext}' unknown, cannot use dataset collection as input"
            )
```

**Changed code:**
```python
conversion_required = False
for ext in extensions:
    if ext:
        if ext in ("auto", "_sniff_"):
            raise ToolInputsNotReadyException(
                f"Extension '{ext}' not yet resolved, cannot use dataset collection as input"
            )
        datatype = trans.app.datatypes_registry.get_datatype_by_extension(ext)
        if not datatype:
            raise RequestParameterInvalidException(
                f"Extension '{ext}' unknown, cannot use dataset collection as input"
            )
```

**Why this works:** `ToolInputsNotReadyException` is already caught at two levels:
1. In `lib/galaxy/tools/__init__.py:2480-2481` (`handle_single_execution`), it returns `(False, e)` which marks the execution as incomplete.
2. In `lib/galaxy/tools/execute.py:275-276` (`check_inputs_ready` for model operations), it's recorded as an error.
3. When `handle_single_execution` returns `(False, e)`, the `execution_tracker.record_error(result)` is called, and the step is not marked complete — leading the workflow scheduler to retry later.

**Import needed:** Add `ToolInputsNotReadyException` to the imports in `lib/galaxy/tools/actions/__init__.py` (from `galaxy.exceptions`).

### Step 2: Add a test

**File:** Add a test case (likely in `test/unit/tool_util/` or `test/unit/workflows/`) that verifies:
- A dataset collection with `auto` extension raises `ToolInputsNotReadyException` (not `RequestParameterInvalidException`)
- This confirms the workflow scheduler can delay and retry

### Step 3: Verification

1. Run `make setup-venv`
2. Run `make format` and `ruff`
3. Run `tox -e mypy`
4. Run relevant unit tests via `run_tests.sh`

## Files to Modify

| File | Change |
|------|--------|
| `lib/galaxy/tools/actions/__init__.py` | Check for `auto`/`_sniff_` before datatype lookup; raise `ToolInputsNotReadyException` instead of `RequestParameterInvalidException` |

## Risk Assessment

- **Low risk**: The change is narrowly scoped — it only affects the case where extension is literally `auto` or `_sniff_`, which are never valid registered extensions.
- **Backward compatible**: No API or behavior changes for resolved extensions. Workflows that previously failed will now delay and succeed once extensions are resolved.
- **Consistent with existing patterns**: Uses the same `ToolInputsNotReadyException` mechanism already in place for unpopulated collections.
