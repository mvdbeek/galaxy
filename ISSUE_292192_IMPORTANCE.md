# Sentry Issue GALAXY-MAIN-4KSCZZZ0014M9 (#292192) -- Importance Assessment

## Issue Summary

N+1 query on `POST /api/tools/__FILTER_EMPTY_DATASETS__/build`. When building the tool form, the `dataset_states_and_extensions_summary` property on `DatasetCollection` executes a separate DB query for each sub-collection within a nested collection (e.g., each pair in a `list:paired`). In this case, 12 sub-collections produce 12 individual queries totaling ~200ms of DB time out of ~502ms total.

---

## 1. Severity: **Low**

- This is a performance issue, not a crash, data loss, or correctness bug. The endpoint returns the correct result.
- The extra DB time is ~200ms. While noticeable, this is within acceptable latency for a form-building endpoint that is not called in tight loops.
- The N+1 scales linearly with the number of sub-collections. A collection with 100 pairs could push the overhead to ~1.5-2 seconds, but such large collections are uncommon in interactive form-building contexts.
- The endpoint still completes in ~500ms, which is within typical web application response time expectations.

## 2. Blast Radius: **Narrow**

- **Tool specificity**: The `__FILTER_EMPTY_DATASETS__` tool is a built-in collection operation tool (`lib/galaxy/tools/filter_empty_collection.xml`). It filters empty datasets from `list` or `list:paired` collections. It is a utility tool, not a core analysis tool -- it is used when downstream tools would fail on empty inputs.
- **Trigger condition**: The N+1 only fires on the `/build` endpoint, which is called when a user opens the tool form in the UI or when a tool form parameter changes. It is NOT called during workflow execution or tool execution itself.
- **Broader pattern**: However, the root cause is in `DatasetCollection.dataset_states_and_extensions_summary` (`lib/galaxy/model/__init__.py:7308`) and the `SummarizedCollectionDatasetMatch.hdca_match` method (`lib/galaxy/tools/parameters/dataset_matcher.py:210`). These are called for ALL tools that accept `data_collection` parameters during form building. The N+1 is not unique to `__FILTER_EMPTY_DATASETS__` -- it affects any tool with a collection input when the user's history contains nested collections. The Sentry event happened to capture it on this tool, but the same pattern would occur on tools like Map Over, Flatten, Filter Failed, or any third-party tool accepting collection inputs.
- **User scope**: Only users who have nested collections (e.g., `list:paired`) in their active history AND open a collection-accepting tool form will experience this. This is a subset of all Galaxy users, but it includes many bioinformatics workflows that work with paired-end sequencing data.

## 3. Workaround Existence: **Yes (trivial)**

- Users are not blocked. The tool form loads, just slightly slower.
- If a user wanted to avoid the delay, they could reduce the number of visible collections in their history (e.g., hide old collections), though this is not a realistic expectation.
- No configuration-level workaround exists on the admin side.

## 4. Regression Status: **Long-standing, not a regression in 26.0.rc1**

- The `dataset_states_and_extensions_summary` property and the `_build_nested_collection_attributes_stmt` method have existed in `lib/galaxy/model/__init__.py` for multiple releases. The `SummarizedCollectionDatasetMatch` matcher class in `dataset_matcher.py` uses this property and has been the matching strategy for collection parameters across many versions.
- The `__FILTER_EMPTY_DATASETS__` tool itself dates back to at least Galaxy 18.09 (referenced in `doc/source/releases/18.09.rst`).
- Git history shows no recent changes to the core matching or summary logic that would have introduced this as a new regression. The N+1 pattern is inherent to how collection metadata summaries are computed -- one query per `DatasetCollection` object.
- The codebase does contain an optimization for PostgreSQL using `ARRAY(subquery)` patterns in `_build_nested_collection_attributes_stmt` (line 7100-7125), which is used when `collection_attributes` are not needed. This optimization exists but does not prevent the per-sub-collection query pattern when the matcher iterates over candidate collections.

## 5. User Impact Signals: **None found**

- No GitHub issues were found in the repository referencing N+1 queries on the tool build endpoint or performance problems with `__FILTER_EMPTY_DATASETS__`.
- No related issues found in the `mvdbeek/galaxy` fork.
- The `doc/source/dev/finding_and_improving_slow_code.rst` file exists, indicating the project is aware of performance optimization as a concern, but no specific tracking of this issue was found.
- The absence of user reports is consistent with the low severity: ~200ms extra latency on a form load is unlikely to generate bug reports.

## 6. Recommendation: **Backlog**

**Rationale:**

- **Not a hotfix**: The issue does not cause errors, data loss, or broken functionality. The ~200ms overhead is below the threshold users would typically report. No users have complained.
- **Not next-release priority**: While the fix (eager-loading or batching collection metadata summaries) would be a clean improvement, it is not urgent enough to justify inclusion in a release candidate patch.
- **Backlog with context**: This should be filed as a backlog performance improvement ticket with the following notes:
  - The root cause is broader than `__FILTER_EMPTY_DATASETS__` -- it affects all collection-accepting tools during form building.
  - The fix would involve either (a) batch-loading `dataset_states_and_extensions_summary` for all candidate collections in a single query, or (b) using SQLAlchemy eager loading / subquery loading when fetching history collections for the matcher.
  - Priority should increase if Sentry shows this pattern recurring at higher N values (e.g., collections with 50+ sub-collections) or if it appears on more frequently used endpoints.
  - The existing `_build_nested_collection_attributes_stmt` already has PostgreSQL-specific optimizations; a batch variant could build on that work.

**Classification**: Low-severity performance debt. Appropriate for a future optimization pass, not for immediate action.

---

## Key Files

| File | Relevance |
|------|-----------|
| `lib/galaxy/model/__init__.py:7308` | `dataset_states_and_extensions_summary` -- property that issues the per-collection query |
| `lib/galaxy/model/__init__.py:7065` | `_build_nested_collection_attributes_stmt` -- builds the SQL statement |
| `lib/galaxy/tools/parameters/dataset_matcher.py:210` | `SummarizedCollectionDatasetMatch.hdca_match` -- calls the summary for each candidate collection |
| `lib/galaxy/tools/parameters/dataset_matcher.py:261` | `DatasetCollectionMatcher.hdca_match` -- alternative matcher that iterates elements individually |
| `lib/galaxy/tools/parameters/basic.py:2680` | `DataCollectionToolParameter.to_dict` -- iterates over matching collections, triggering the N+1 |
| `lib/galaxy/tools/filter_empty_collection.xml` | Tool definition for `__FILTER_EMPTY_DATASETS__` |
| `lib/galaxy/tools/__init__.py:4374` | `FilterEmptyDatasetsTool` class |
