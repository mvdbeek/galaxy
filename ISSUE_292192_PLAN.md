# Fix Plan: N+1 Query in `POST /api/tools/__FILTER_EMPTY_DATASETS__/build`

**Sentry Issue:** GALAXY-MAIN-4KSCZZZ0014M9 (#292192)

## Problem

When building tool forms for `DataCollectionToolParameter`, the method `to_dict()` (at `lib/galaxy/tools/parameters/basic.py:2644`) iterates over all candidate dataset collections in the user's history via two loops:

1. `match_collections()` (line 2680) -- iterates collections returned by `history_dataset_collections()`
2. `match_multirun_collections()` (line 2696) -- iterates `history.active_visible_dataset_collections`

Each iteration calls `dataset_collection_matcher.hdca_match()` (`lib/galaxy/tools/parameters/dataset_matcher.py:210`), which accesses `dataset_collection.dataset_states_and_extensions_summary` (line 216). This property (`lib/galaxy/model/__init__.py:7308`) executes a separate SQL query per collection via `_build_nested_collection_attributes_stmt()`. The result is cached per Python object instance, but each distinct `DatasetCollection` still requires its own query.

For a history with N collections, this produces N+1 queries (1 to load collections + N summary queries).

## Solution: Batch-Fetch Collection Summaries

Pre-compute `dataset_states_and_extensions_summary` for all candidate collections in a single SQL query before the matching loops begin, then inject the cached results onto each `DatasetCollection` object so the per-object property never hits the database.

---

## Detailed Implementation Plan

### Step 1: Create a Batch Summary Fetch Function

**File:** `lib/galaxy/model/__init__.py`
**Location:** After the `CollectionStateSummary` class (after line 7013), or as a module-level function / classmethod on `DatasetCollection`.

Add a new classmethod on `DatasetCollection`:

```python
@classmethod
def batch_fetch_dataset_states_and_extensions_summary(
    cls,
    session,
    collection_ids: list[int],
) -> dict[int, "CollectionStateSummary"]:
    """
    Fetch dataset_states_and_extensions_summary for multiple collections
    in a single query. Returns a dict mapping collection_id -> CollectionStateSummary.
    """
```

**Logic:**

For **flat collections** (collection_type without `:`), the query is straightforward -- a single join from `dataset_collection_element` -> `history_dataset_association` -> `dataset` with a `WHERE dataset_collection_id IN (:ids)` clause, grouped by `dataset_collection_id`.

For **nested collections** (collection_type with `:`), we need the recursive walk. Since collections in a single history can have mixed types (list, list:paired, etc.), the most pragmatic approach is:

1. Separate the collection IDs by collection type (using `DatasetCollection.collection_type`).
2. For flat collections, use a single efficient batched query.
3. For nested collections, use a single batched query that walks the nesting tree for all collections of the same type simultaneously.

**SQL design for flat collections (single query):**

```sql
SELECT
    dce.dataset_collection_id,
    hda._metadata,
    hda.extension,
    hda.deleted,
    d.state
FROM dataset_collection_element dce
JOIN history_dataset_association hda ON hda.id = dce.hda_id
JOIN dataset d ON d.id = hda.dataset_id
WHERE dce.dataset_collection_id IN (:collection_ids)
```

Results are grouped in Python by `dataset_collection_id` to build per-collection `CollectionStateSummary` objects.

**SQL design for nested collections (e.g., list:paired):**

For PostgreSQL, use the ARRAY-walk pattern already present in `_build_nested_collection_attributes_stmt` (lines 7124-7199), but parameterize the root collection ID as a list:

```sql
-- For list:paired (1 level of nesting):
SELECT
    outer_dce.dataset_collection_id AS root_collection_id,
    hda._metadata,
    hda.extension,
    hda.deleted,
    d.state
FROM dataset_collection_element outer_dce
JOIN dataset_collection_element inner_dce
    ON inner_dce.dataset_collection_id = outer_dce.child_collection_id
JOIN history_dataset_association hda ON hda.id = inner_dce.hda_id
JOIN dataset d ON d.id = hda.dataset_id
WHERE outer_dce.dataset_collection_id IN (:collection_ids)
```

For deeper nesting, add additional joins per nesting level. Since the nesting depth is known from `collection_type`, construct the appropriate number of joins.

For SQLite, use the same outerjoin-chain pattern from the existing code but with `IN (:ids)` instead of `= :id`.

**Return value:** `dict[int, CollectionStateSummary]` mapping each `collection_id` to its summary.

### Step 2: Create a Cache-Injection Helper

**File:** `lib/galaxy/model/__init__.py`
**Location:** As a classmethod on `DatasetCollection` or standalone function near `batch_fetch_dataset_states_and_extensions_summary`.

```python
@classmethod
def prefill_dataset_states_and_extensions_summary(
    cls,
    collections: list["DatasetCollection"],
    summaries: dict[int, "CollectionStateSummary"],
) -> None:
    """
    Inject pre-fetched summaries into collection objects so the
    dataset_states_and_extensions_summary property uses the cache.
    """
    for collection in collections:
        if collection.id in summaries:
            collection._dataset_states_and_extensions_summary = summaries[collection.id]
```

This works because `dataset_states_and_extensions_summary` (line 7313) checks `hasattr(self, "_dataset_states_and_extensions_summary")` before querying. By setting the attribute, the property short-circuits and returns the cached value.

### Step 3: Integrate Batch Fetch Before Matching Loops

**File:** `lib/galaxy/tools/parameters/basic.py`
**Location:** In `DataCollectionToolParameter.to_dict()`, after line 2664 (after `dataset_collection_matcher` is created), before line 2680 (the first `match_collections` loop).

Add:

```python
# Batch-prefetch collection summaries to avoid N+1 queries
from galaxy.model import DatasetCollection

# Collect all candidate collections from both match paths
all_candidate_hdcas = []

# Collections from match_collections path
direct_collections = trans.app.dataset_collection_manager.history_dataset_collections(
    history, self._history_query(trans)
)
all_candidate_hdcas.extend(direct_collections)

# Collections from match_multirun_collections path
multirun_collections = history.active_visible_dataset_collections
all_candidate_hdcas.extend(multirun_collections)

# Deduplicate by collection_id and batch fetch
seen_collection_ids = set()
collections_to_fetch = []
for hdca in all_candidate_hdcas:
    cid = hdca.collection.id
    if cid not in seen_collection_ids:
        seen_collection_ids.add(cid)
        collections_to_fetch.append(hdca.collection)

if collections_to_fetch:
    collection_ids = [c.id for c in collections_to_fetch]
    summaries = DatasetCollection.batch_fetch_dataset_states_and_extensions_summary(
        trans.sa_session, collection_ids
    )
    DatasetCollection.prefill_dataset_states_and_extensions_summary(
        collections_to_fetch, summaries
    )
```

**Important:** The `history_dataset_collections()` call (line 2546) and `active_visible_dataset_collections` property (line 3967) both cache their results, so calling them once here and again in the match loops does NOT trigger extra DB queries.

However, this approach computes the candidate lists twice. A cleaner alternative is to modify `match_collections` and `match_multirun_collections` to accept pre-fetched collection lists, or to perform the prefetch inside `SummaryDatasetCollectionMatcher` itself.

**Alternative (preferred): Prefetch inside `SummaryDatasetCollectionMatcher`**

**File:** `lib/galaxy/tools/parameters/dataset_matcher.py`
**Location:** Modify `SummaryDatasetCollectionMatcher` to accept and prefetch summaries.

Add a method:

```python
class SummaryDatasetCollectionMatcher:
    def __init__(self, dataset_matcher_factory, trans, dataset_matcher):
        self.dataset_matcher_factory = dataset_matcher_factory
        self._trans = trans
        self.dataset_matcher = dataset_matcher

    def prefetch_summaries(self, hdcas):
        """Batch-fetch summaries for all candidate HDCAs to avoid N+1 queries."""
        from galaxy.model import DatasetCollection

        collections = []
        seen = set()
        for hdca in hdcas:
            collection = hdca.collection
            if collection.id not in seen:
                seen.add(collection.id)
                collections.append(collection)

        if collections:
            collection_ids = [c.id for c in collections]
            summaries = DatasetCollection.batch_fetch_dataset_states_and_extensions_summary(
                object_session(collections[0]), collection_ids
            )
            DatasetCollection.prefill_dataset_states_and_extensions_summary(
                collections, summaries
            )
```

Then in `DataCollectionToolParameter.to_dict()` (line 2664, after creating `dataset_collection_matcher`):

```python
# Prefetch summaries if using SummaryDatasetCollectionMatcher
if hasattr(dataset_collection_matcher, 'prefetch_summaries'):
    all_hdcas = list(trans.app.dataset_collection_manager.history_dataset_collections(
        history, self._history_query(trans)
    )) + list(history.active_visible_dataset_collections)
    dataset_collection_matcher.prefetch_summaries(all_hdcas)
```

### Step 4: Also Fix `get_initial_value`

**File:** `lib/galaxy/tools/parameters/basic.py`
**Location:** Lines 1929-1932, inside `get_initial_value()`.

The same N+1 pattern occurs here when iterating `history.active_visible_dataset_collections` to find the initial value. Add prefetching:

```python
else:
    dataset_collection_matcher = dataset_matcher_factory.dataset_collection_matcher(dataset_matcher)
    hdcas = list(reversed(history.active_visible_dataset_collections))
    if hasattr(dataset_collection_matcher, 'prefetch_summaries'):
        dataset_collection_matcher.prefetch_summaries(hdcas)
    for hdca in hdcas:
        if dataset_collection_matcher.hdca_match(hdca):
            return hdca
```

### Step 5: Also Batch-Prefetch `populated_optimized`

**File:** `lib/galaxy/model/__init__.py`
**Location:** Lines 7364-7423.

The `hdca_match` method also calls `dataset_collection.populated_optimized` (line 213), which fires another per-collection query. A similar batch-prefetch approach should be applied:

```python
@classmethod
def batch_fetch_populated_optimized(
    cls,
    session,
    collection_ids: list[int],
) -> dict[int, bool]:
    """
    Batch-check populated state for multiple collections.
    Returns dict mapping collection_id -> bool (True if populated OK).
    """
```

For flat collections, this is a simple check of `populated_state` column on the `dataset_collection` table. For nested collections, check that no sub-collection has `populated_state != 'ok'`.

This can be combined with the summary prefetch call for efficiency.

---

## Edge Cases

1. **Empty histories:** No collections to iterate, no queries fired. The batch fetch should handle an empty `collection_ids` list gracefully (return empty dict, skip query).

2. **Nested vs flat collections:** The batch query must handle different `collection_type` values. Group collections by type and build appropriate queries. Alternatively, use a single recursive CTE approach that works for any depth.

3. **Collections not yet populated:** `populated_optimized` returns `False` for these. The batch query for `populated_optimized` should correctly identify unpopulated sub-collections. The summary fetch can skip these (they'll be filtered out by `hdca_match` before `dataset_states_and_extensions_summary` is accessed).

4. **Mixed collection types in one history:** A history may contain `list`, `paired`, `list:paired`, `list:list:paired` etc. The batch query groups must handle each nesting depth separately, or use a universal recursive approach.

5. **Collections shared across both `match_collections` and `match_multirun_collections`:** Deduplicate by `collection.id` before batch-fetching. The cache injection means the second loop will hit the pre-filled cache.

6. **Detached SQLAlchemy objects:** If a `DatasetCollection` is not in a session (e.g., remote tool evaluation), the existing fallback code paths (iterating `dataset_instances` in-memory) remain untouched.

7. **Very large histories (1000+ collections):** The `IN (:ids)` clause could be large. Consider chunking into batches of 500-1000 IDs if needed, though PostgreSQL and SQLite both handle large IN clauses well.

---

## Testing Strategy

### Unit Tests

**File:** `test/unit/data/test_galaxy_mapping.py`

1. **Test `batch_fetch_dataset_states_and_extensions_summary` for flat collections:**
   - Create 5+ `DatasetCollection` objects (type `list`) with known HDAs.
   - Call batch fetch, verify each summary matches the individual property call.

2. **Test `batch_fetch_dataset_states_and_extensions_summary` for nested collections:**
   - Create `list:paired` collections with known HDAs.
   - Verify batch results match individual calls.

3. **Test `prefill_dataset_states_and_extensions_summary` cache injection:**
   - Prefill summaries, then verify `dataset_states_and_extensions_summary` returns the prefilled value without querying.

4. **Test empty collection list:**
   - Verify batch fetch returns empty dict for empty input.

5. **Test mixed collection types:**
   - Create a mix of flat and nested collections.
   - Verify batch fetch handles all correctly.

### Integration Tests

**File:** `test/integration/test_tool_build.py` or similar.

1. **Test tool form build with many collections:**
   - Create a history with 50+ collections.
   - Call the tool build endpoint.
   - Verify correct results (options populated).
   - Instrument query counting to verify N+1 is eliminated.

2. **Test `__FILTER_EMPTY_DATASETS__` tool specifically:**
   - Build tool form for the specific tool mentioned in the Sentry issue.
   - Verify query count is O(1) not O(N).

### Performance Tests

1. **Benchmark before/after:**
   - Create a history with 200 collections.
   - Time the `to_dict()` call before and after the fix.
   - Verify significant speedup (expected: from ~200 queries to ~2-3 queries).

---

## Risk Assessment

### Low Risk
- **Cache injection via `_dataset_states_and_extensions_summary`:** The property already checks `hasattr` for this attribute (line 7313). Pre-setting it is the exact same caching mechanism the property itself uses. No behavior change.
- **Backwards compatibility:** The individual `dataset_states_and_extensions_summary` property still works as before for any code path that doesn't use the batch prefetch. The optimization is purely additive.

### Medium Risk
- **Correctness of batched query vs individual queries:** The batched query must produce identical results to the per-collection query. Thorough testing with nested collections is essential. The existing test at `test/unit/data/test_galaxy_mapping.py:191` provides a template.
- **Session state:** All collections must be in the same SQLAlchemy session. This is guaranteed in the tool form build code path since they all come from the same history query.

### Low-Medium Risk
- **Database dialect differences:** The existing code already handles PostgreSQL vs SQLite differently for nested collections (lines 7117-7243). The batch query must maintain this dialect-awareness. Using `session.bind.dialect.name` to branch is the established pattern.
- **Interaction with `populated_optimized`:** If `populated_optimized` is not also batch-prefetched, there's still an N+1 for that property. However, its query is simpler (just checking `populated_state` column), so the impact is smaller. It should still be addressed for completeness.

### Mitigation
- Verify correctness by running both batch and individual queries in tests and asserting identical results.
- Add a fallback: if batch fetch fails for any reason, let the individual property queries proceed as before (graceful degradation).
- Monitor Sentry after deployment for any new errors from the batch code path.

---

## Implementation Order

1. Implement `batch_fetch_dataset_states_and_extensions_summary` on `DatasetCollection` (with tests).
2. Implement `prefill_dataset_states_and_extensions_summary` (trivial).
3. Add `prefetch_summaries` to `SummaryDatasetCollectionMatcher`.
4. Integrate prefetch call in `DataCollectionToolParameter.to_dict()`.
5. Integrate prefetch call in `get_initial_value()`.
6. (Optional) Batch-prefetch `populated_optimized`.
7. Run full test suite, add integration tests.
8. Benchmark with large histories.

## Files Modified

| File | Changes |
|------|---------|
| `lib/galaxy/model/__init__.py` | Add `batch_fetch_dataset_states_and_extensions_summary()` classmethod, `prefill_dataset_states_and_extensions_summary()` classmethod, optionally `batch_fetch_populated_optimized()` |
| `lib/galaxy/tools/parameters/dataset_matcher.py` | Add `prefetch_summaries()` method to `SummaryDatasetCollectionMatcher` |
| `lib/galaxy/tools/parameters/basic.py` | Add prefetch calls in `to_dict()` (~line 2665) and `get_initial_value()` (~line 1929) |
| `test/unit/data/test_galaxy_mapping.py` | Add batch-fetch unit tests |
