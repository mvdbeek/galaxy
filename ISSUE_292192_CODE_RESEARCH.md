# Sentry Issue GALAXY-MAIN-4KSCZZZ0014M9 (#292192) - N+1 Query Research

## Summary

**Endpoint**: `POST /api/tools/__FILTER_EMPTY_DATASETS__/build`  
**Problem**: When building the tool form for `__FILTER_EMPTY_DATASETS__`, the code fires one SQL query per dataset collection in the user's history to check whether each collection is compatible with the tool's input parameter. For a history with 12 collections, this results in 12 individual queries (plus a "cause" query for nested collections).

## Code Path Trace

### 1. Entry Point: Tool Form Build

**File**: `lib/galaxy/webapps/galaxy/api/tools.py`, line 546-560

The `build` endpoint calls `tool.to_json(trans, kwd.get("inputs", kwd), history=history)`.

### 2. `Tool.to_json` Triggers Collection Matching

**File**: `lib/galaxy/tools/__init__.py`, lines 3079-3160

`to_json` does two things that trigger collection queries:

1. **Line 3129-3133**: `set_dataset_matcher_factory` then `populate_state` which calls `get_initial_value` on the `data_collection` parameter.
2. **Line 3136-3138**: `populate_model` which calls `DataCollectionToolParameter.to_dict`, building the list of compatible collections for the form dropdown.

### 3. `DataCollectionToolParameter.to_dict` - The Main N+1 Source

**File**: `lib/galaxy/tools/parameters/basic.py`, lines 2644-2723

This method builds the options for the collection parameter dropdown. It does two passes over history collections:

- **Line 2680**: `match_collections(trans, history, dataset_collection_matcher)` - checks all HDCAs that directly match the parameter's collection types (`list` or `list:paired`)
- **Line 2696**: `match_multirun_collections(trans, history, dataset_collection_matcher)` - checks all HDCAs that can be mapped over

Both call `dataset_collection_matcher.hdca_match(hdca)` on each candidate HDCA.

### 4. `SummaryDatasetCollectionMatcher.hdca_match` - Where Queries Fire

**File**: `lib/galaxy/tools/parameters/dataset_matcher.py`, lines 204-237

For `__FILTER_EMPTY_DATASETS__`, the matcher factory determines `_can_process_summary = True` (line 41-46 of the same file) because the tool's `data_collection` input has no `<options>` filter. This means `SummaryDatasetCollectionMatcher` is used (line 84-85).

Each `hdca_match` call accesses two properties on the `DatasetCollection`:

1. **Line 213**: `dataset_collection.populated_optimized` - For simple `list` collections (no ":" in type), this just checks `populated_state == OK` with no DB query. For nested collections like `list:paired`, this fires a DB query.

2. **Line 216**: `dataset_collection.dataset_states_and_extensions_summary` - This ALWAYS fires a DB query (per collection) the first time it's accessed.

### 5. `DatasetCollection.dataset_states_and_extensions_summary` - The Query

**File**: `lib/galaxy/model/__init__.py`, lines 7308-7345

This property calls `_build_nested_collection_attributes_stmt` (line 7315) with `hda_attributes=("_metadata", "extension", "deleted"), dataset_attributes=("state",)`. The result is cached on the Python object via `_dataset_states_and_extensions_summary`, but each distinct `DatasetCollection` object fires its own query.

### 6. `_build_nested_collection_attributes_stmt` - The Query Builder

**File**: `lib/galaxy/model/__init__.py`, lines 7065-7260

For a simple `list` collection (no ":" in collection_type), this generates the exact query from the Sentry issue (lines 7200-7213):

```sql
SELECT hda._metadata, hda.extension, hda.deleted, dataset.state
FROM dataset_collection dc
JOIN dataset_collection_element dce ON dce.dataset_collection_id = dc.id
JOIN history_dataset_association hda ON hda.id = dce.hda_id
JOIN dataset ON dataset.id = hda.dataset_id
WHERE dc.id = :id_1
ORDER BY dce.element_index
```

### 7. `match_collections` - How Collections Are Fetched

**File**: `lib/galaxy/tools/parameters/basic.py`, line 2545-2559

Calls `trans.app.dataset_collection_manager.history_dataset_collections(history, self._history_query(trans))`.

**File**: `lib/galaxy/managers/collections.py`, lines 564-567

This fetches `history.active_dataset_collections` and filters by `query.direct_match` (checking collection type compatibility).

### 8. `match_multirun_collections`

**File**: `lib/galaxy/tools/parameters/basic.py`, lines 2561-2568

Iterates `history.active_visible_dataset_collections` and checks `can_map_over` for each HDCA.

**File**: `lib/galaxy/model/__init__.py`, lines 3966-3981

`active_visible_dataset_collections` uses `joinedload` for `collection` and `tags`, avoiding N+1 on those relationships.

### 9. `get_initial_value` - Additional Collection Iteration

**File**: `lib/galaxy/tools/parameters/basic.py`, lines 1915-1932

Before `to_dict` runs, `get_initial_value` also iterates `active_visible_dataset_collections` calling `hdca_match` on each, stopping at the first match. This may fire 1 or more queries before the `to_dict` phase.

## Tool Definition

**File**: `lib/galaxy/tools/filter_empty_collection.xml`

The tool accepts `collection_type="list,list:paired"` on its single `data_collection` input parameter.

**File**: `lib/galaxy/tools/__init__.py`, line 4374-4388

`FilterEmptyDatasetsTool` extends `FilterDatasetsTool` with `require_dataset_ok = True`.

## The N+1 Pattern

The N+1 pattern occurs because:

1. The tool form build needs to find all compatible collections in the user's history to populate the input dropdown.
2. For each candidate HDCA, `SummaryDatasetCollectionMatcher.hdca_match` is called.
3. Each `hdca_match` call accesses `dataset_states_and_extensions_summary` on the collection, which fires a separate SQL query.
4. The result is cached per Python object, but each distinct collection in history requires its own query.
5. With 12 collections in the history, this produces 12 individual queries.

The "cause" query mentioned in the Sentry issue is likely the `dataset_states_and_extensions_summary` call on a `list:paired` collection, which generates a more complex nested query. The 12 repeating queries are for 12 simple `list` collections (or other single-level collections) in the same history.

## Relevant File Paths and Line Numbers

| File | Lines | Purpose |
|------|-------|---------|
| `lib/galaxy/webapps/galaxy/api/tools.py` | 546-560 | `build` endpoint handler |
| `lib/galaxy/tools/__init__.py` | 3079-3160 | `Tool.to_json` - form build orchestration |
| `lib/galaxy/tools/__init__.py` | 4374-4388 | `FilterEmptyDatasetsTool` class |
| `lib/galaxy/tools/filter_empty_collection.xml` | 1-56 | Tool XML definition |
| `lib/galaxy/tools/parameters/basic.py` | 2511-2723 | `DataCollectionToolParameter` - `to_dict` builds options |
| `lib/galaxy/tools/parameters/basic.py` | 1915-1932 | `get_initial_value` - initial collection selection |
| `lib/galaxy/tools/parameters/dataset_matcher.py` | 21-87 | `DatasetMatcherFactory` - decides Summary vs Full matcher |
| `lib/galaxy/tools/parameters/dataset_matcher.py` | 204-237 | `SummaryDatasetCollectionMatcher.hdca_match` - fires query |
| `lib/galaxy/model/__init__.py` | 7308-7345 | `DatasetCollection.dataset_states_and_extensions_summary` |
| `lib/galaxy/model/__init__.py` | 7065-7260 | `_build_nested_collection_attributes_stmt` - query builder |
| `lib/galaxy/model/__init__.py` | 7363-7423 | `populated_optimized` property |
| `lib/galaxy/managers/collections.py` | 564-567 | `history_dataset_collections` |

## Theories About the Root Cause

### Theory 1: Per-Collection Summary Query is Unavoidable in Current Architecture (Most Likely)

The `SummaryDatasetCollectionMatcher` was designed as an optimization over the `DatasetCollectionMatcher` (which iterates individual elements). However, it still fires one query per collection to get the summary (states, extensions, deleted count). The summary query uses `_build_nested_collection_attributes_stmt` which is efficient for a single collection but becomes an N+1 problem when checking many collections.

**Fix approach**: Batch the summary queries. Instead of calling `dataset_states_and_extensions_summary` per collection, pre-fetch summaries for all candidate collections in a single query before the matching loop. This could be done by:
- Adding a class method to `DatasetCollection` that accepts multiple collection IDs and returns summaries for all of them.
- Pre-populating `_dataset_states_and_extensions_summary` on all collection objects before entering the matching loop.

### Theory 2: Redundant Collection Iteration Across Multiple Code Paths

The tool form build checks collections in up to three places:
1. `get_initial_value` (line 1930) - iterates `active_visible_dataset_collections`
2. `match_collections` in `to_dict` (line 2680) - iterates `active_dataset_collections` filtered by type
3. `match_multirun_collections` in `to_dict` (line 2696) - iterates `active_visible_dataset_collections`

While SQLAlchemy identity map means the same objects are reused (and summaries cached), the collections checked in `match_multirun_collections` that were not in `match_collections` (those that can be mapped over but don't directly match) will still fire new queries.

**Fix approach**: Pre-fetch all collection summaries before any matching begins, e.g., in `set_dataset_matcher_factory` or at the start of `to_dict`.

### Theory 3: Lack of Eager Loading for Collection State Summaries

The `active_visible_dataset_collections` relationship (line 3966-3981) eagerly loads the `collection` and `tags` relationships, but the `dataset_states_and_extensions_summary` is computed lazily. This property could be pre-computed or cached at the history level.

**Fix approach**: Add a history-level method that fetches all collection summaries in a single query (e.g., using UNION ALL or a single query that groups by collection ID), then populates the `_dataset_states_and_extensions_summary` cache on each `DatasetCollection` object. This would turn N+1 queries into 1 query regardless of how many collections are in the history.
