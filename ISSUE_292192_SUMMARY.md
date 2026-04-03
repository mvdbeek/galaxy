# Triage Summary: GALAXY-MAIN-4KSCZZZ0014M9 (N+1 Query)

## Top-Line Summary

This is a **low-severity N+1 query performance issue** detected on Galaxy 26.0.rc1 in production (TACC/usegalaxy.org). When building tool forms for any tool with `data_collection` inputs, the `SummaryDatasetCollectionMatcher.hdca_match` method calls `DatasetCollection.dataset_states_and_extensions_summary` once per collection in the user's history, each firing a separate SQL query. In this event, 12 sub-collections produced 12 individual queries totaling ~200ms of DB time out of ~502ms total transaction time. The Sentry event was captured on `POST /api/tools/__FILTER_EMPTY_DATASETS__/build`, but the root cause affects **all tools with collection inputs** during form building. This is a **long-standing pattern**, not a regression in 26.0.rc1. The most probable fix is to batch-fetch collection summaries for all candidate collections in a single query before the matching loop, pre-populating the per-object cache so individual queries never fire. The key code path is: `Tool.to_json` -> `DataCollectionToolParameter.to_dict` -> `match_collections`/`match_multirun_collections` -> `SummaryDatasetCollectionMatcher.hdca_match` -> `DatasetCollection.dataset_states_and_extensions_summary` (at `lib/galaxy/model/__init__.py:7308`).

## Importance Assessment

| Dimension | Assessment |
|-----------|------------|
| **Severity** | Low -- performance issue only, no crash/data loss/correctness impact |
| **Blast radius** | Narrow but broader than it appears -- affects all collection-accepting tools during form building, not just `__FILTER_EMPTY_DATASETS__`. Only users with nested collections in their active history are affected. |
| **Regression status** | Long-standing -- not a regression. The per-collection summary query pattern has existed across multiple releases. |
| **Workaround** | Trivial -- users are not blocked, forms just load slightly slower (~200ms overhead) |
| **User impact signals** | None -- no GitHub issues or user reports found |
| **Overall recommendation** | **Backlog** -- low-severity performance debt. Should be tracked for a future optimization pass, not for immediate action or hotfix. |

## Discussion Questions

1. **Scaling concern**: The N+1 scales linearly with collections in the history. Has anyone observed histories with 50+ nested collections where this could push overhead to 1-2+ seconds? Is there telemetry on typical history sizes on usegalaxy.org?

2. **Broader optimization pass**: Since this affects all collection-accepting tools, should the fix be prioritized as part of a broader "tool form build performance" initiative rather than just this one Sentry issue?

3. **`populated_optimized` N+1**: The `hdca_match` method also calls `populated_optimized` per collection, which is another potential N+1 for nested collections. Should both be addressed together?

4. **SQLite vs PostgreSQL**: The existing `_build_nested_collection_attributes_stmt` has PostgreSQL-specific optimizations using `ARRAY(subquery)`. A batch version needs to handle both dialects. Is SQLite testing coverage adequate for this code path?

## Complexity Assessment

| Dimension | Assessment |
|-----------|------------|
| **Fix complexity** | **Medium** -- Requires a new batch-fetch classmethod on `DatasetCollection`, cache injection helper, and integration in 2-3 call sites. Must handle nested vs flat collections and PostgreSQL/SQLite dialect differences. |
| **Reproducibility** | **Easy** -- Create a history with 10+ nested collections (e.g., `list:paired`), open any collection-accepting tool form, observe repeated DB queries in Sentry or SQL logging. |
| **Testing** | **Medium** -- Unit tests for batch-fetch correctness, integration tests for tool form build with many collections, and query-count verification. |
