# Code Review: Workflow Invocation Output Queuing Feature

**Review Date**: 2026-02-05
**Reviewed Commits**: HEAD~3 to HEAD
**Reviewer**: Claude Code

---

## Overview

This feature adds the ability for workflow invocations to use outputs from other (potentially still running) invocations as inputs. The implementation introduces:

- New `WorkflowInvocationInputDependency` model
- New `WAITING_FOR_INPUT` invocation state
- New src types: `invocation_output` and `invocation_step_output`
- Dependency resolution logic in the scheduling manager

---

## Critical Issues

### 1. Placeholder Migration Revision ID

**File**: `lib/galaxy/model/migrations/alembic/versions_gxy/a1b2c3d4e5f6_add_workflow_invocation_input_dependency.py`

The revision ID `a1b2c3d4e5f6` is a placeholder pattern, not a properly generated Alembic revision. Regenerate using:

```bash
alembic revision --autogenerate -m "add workflow_invocation_input_dependency table"
```

### 2. Debug Statement Left in Code

**File**: `lib/galaxy/workflow/run.py:641`

```python
log.info("ADDING INPUT FOR STEP %s: %s", step.id, content, exc_info=True)
```

This will print a stack trace on every input addition. Remove or change to `log.debug` without `exc_info`.

### 3. Missing ON DELETE CASCADE in Migration

**File**: Migration file

The foreign keys should include cascade behavior:

```python
ForeignKey("workflow_invocation.id", onupdate="CASCADE", ondelete="CASCADE")
```

---

## High Priority Issues

### 4. Duplicate Output Resolution Logic (DRY Violation)

**Files**: `run_request.py` (lines 371-412) and `scheduling_manager.py` (lines 519-565)

The same logic for iterating through `output_datasets` and `output_dataset_collections` appears in both files. Extract to a shared utility function.

### 5. Silent Failure on Missing Source Invocation

**File**: `lib/galaxy/workflow/scheduling_manager.py:451-454`

When source invocation is None, the code logs a warning and continues. This represents a data integrity issue and should fail the invocation with a clear error message.

### 6. Missing Cross-User Access Control Tests

The implementation has access checks but no tests verify:

- User A cannot reference user B's invocation outputs
- Admin users CAN access other users' invocations

---

## Medium Priority Issues

### 7. No Circular Dependency Detection

The implementation doesn't prevent:

- Self-references (invocation referencing itself)
- Circular chains (A → B → A)

### 8. Missing Test Coverage for `invocation_step_output`

Only `invocation_output` src type is tested. The `invocation_step_output` path has no test coverage.

### 9. Missing Collection Output Tests

The implementation supports collection outputs but no tests verify this works.

### 10. Large Function Needs Refactoring

**File**: `lib/galaxy/workflow/run_request.py:306-414`

The `_resolve_invocation_output_reference` function is 108 lines. Consider extracting helpers for `_resolve_labeled_output` and `_resolve_step_output`.

### 11. N+1 Query Risk in `to_dict()`

**File**: `lib/galaxy/model/__init__.py`

Accessing `dep.source_invocation.state` in a loop may cause N+1 queries. Consider eager loading the relationship.

---

## Low Priority Issues

### 12. Type Hint Inconsistency for Timestamps

```python
# Current:
create_time: Mapped[datetime] = mapped_column(default=now, nullable=True)
# Should be:
create_time: Mapped[Optional[datetime]] = mapped_column(default=now, nullable=True)
```

### 13. Verbose Debug Logging

**File**: `lib/galaxy/workflow/scheduling_manager.py:526-539`

Consider using `log.trace` or making verbose logging configurable.

### 14. Missing `Dictifiable` Inheritance

The `WorkflowInvocationInputDependency` model defines `dict_collection_visible_keys` but doesn't inherit from `Dictifiable`.

---

## Missing Test Cases

| Test Case                                         | Priority |
| ------------------------------------------------- | -------- |
| Cancelled source invocation propagation           | High     |
| Cross-user access control tests                   | High     |
| `invocation_step_output` src type                 | High     |
| Collection output references                      | Medium   |
| Multiple inputs from different invocations        | Medium   |
| Circular dependency handling                      | Medium   |
| Source invocation deleted after dependent created | Medium   |
| Invalid step_id for step output reference         | Low      |

---

## Session Management Observations

1. **Inconsistent patterns**: Some code uses context managers (`with app.model.context() as session:`), some doesn't
2. **Direct commits in managers**: Consider adding `flush` parameters to let callers control transaction boundaries
3. **Potential lost commits**: In `__attempt_resolve_input_dependencies`, if `all_resolved` is False but some dependencies were resolved, those changes might not be committed

---

## Summary

The overall architecture is sound and follows Galaxy patterns. The main concerns are:

1. **Migration needs regeneration** with proper revision ID and cascade behavior
2. **Remove debug statement** in `run.py`
3. **Improve test coverage** especially for error paths and access control
4. **DRY refactoring** for duplicate resolution logic
