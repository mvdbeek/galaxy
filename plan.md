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

### Step 2: Add an integration test

**File:** `lib/galaxy_test/api/test_workflows.py`

Add an integration test that launches a real workflow with a dataset collection whose elements have `ext: "auto"`. This exercises the full code path: the workflow scheduler picks up the invocation, the tool step tries to validate the collection's extensions, encounters `auto`, and should delay (not fail) until the extensions are resolved by the upload/sniff job.

**Test design:**

```python
@skip_without_tool("multi_data_optional")
def test_workflow_run_collection_with_auto_extension(self):
    """Test that a workflow with a collection input whose datasets have ext='auto' delays and succeeds."""
    with self.dataset_populator.test_history() as history_id:
        workflow_id = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input:
    type: collection
    collection_type: "list"
steps:
  multi_data_optional:
    tool_id: multi_data_optional
    in:
      input1: input
        """)
        input_b64 = base64.b64encode(b"1 2 3").decode("utf-8")
        inputs = {
            "input": {
                "class": "Collection",
                "collection_type": "list",
                "elements": [
                    {
                        "class": "File",
                        "identifier": "auto_element",
                        "url": f"base64://{input_b64}",
                        "ext": "auto",
                        "deferred": False,
                    }
                ],
            },
        }
        workflow_request = dict(
            history=f"hist_id={history_id}",
        )
        workflow_request["inputs"] = json.dumps(inputs)
        workflow_request["inputs_by"] = "name"
        invocation_id = self.workflow_populator.invoke_workflow_and_wait(
            workflow_id, request=workflow_request
        ).json()["id"]
        invocation = self.workflow_populator.wait_for_invocation_and_completion(invocation_id)
        assert invocation["state"] == "completed", invocation
```

**What this tests:**
1. Creates a collection with `ext: "auto"` — the upload/fetch job will need to sniff the type
2. Invokes a workflow that takes the collection as input
3. The workflow scheduler encounters the `auto` extension during step scheduling
4. **Before fix:** `RequestParameterInvalidException` fails the workflow
5. **After fix:** `ToolInputsNotReadyException` delays the step; once sniffing completes, the step retries and succeeds
6. Asserts the invocation reaches `"completed"` state

This pattern mirrors the existing `test_run_workflow_with_url_collection` test but uses `ext: "auto"` instead of `ext: "txt"`.

### Step 3: Verification

1. Run `make setup-venv`
2. Run `make format` and `ruff`
3. Run `tox -e mypy`
4. Run relevant tests via `run_tests.sh`

## Files to Modify

| File | Change |
|------|--------|
| `lib/galaxy/tools/actions/__init__.py` | Check for `auto`/`_sniff_` before datatype lookup; raise `ToolInputsNotReadyException` instead of `RequestParameterInvalidException` |
| `lib/galaxy_test/api/test_workflows.py` | Add `test_workflow_run_collection_with_auto_extension` integration test |

## Risk Assessment

- **Low risk**: The change is narrowly scoped — it only affects the case where extension is literally `auto` or `_sniff_`, which are never valid registered extensions.
- **Backward compatible**: No API or behavior changes for resolved extensions. Workflows that previously failed will now delay and succeed once extensions are resolved.
- **Consistent with existing patterns**: Uses the same `ToolInputsNotReadyException` mechanism already in place for unpopulated collections.
