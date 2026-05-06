"""Helpers shared by data/data_collection tool parameters when paginating
their option lists in ``to_dict``.

These live in the manager layer rather than alongside the parameter classes
because they are application-level pagination orchestration — building pages
out of DB chunks and a Python predicate — rather than parameter definition
logic. Keeping them here also lets future schemes (cursor-based, prefetched)
slot in without further bloating ``basic.py``.
"""

from collections.abc import (
    Callable,
    Mapping,
)
from typing import (
    Any,
    Optional,
    TypeVar,
)

DEFAULT_OPTIONS_PAGE_SIZE = 50
MAX_OPTIONS_PAGE_SIZE = 500

#: Pagination spec for a single parameter, keyed by source (``hda``/``hdca``/
#: ``dce``/...) → ``{"offset": int, "limit": int}``.
ParameterPaginationT = Mapping[str, Mapping[str, Any]]

#: Full pagination map keyed by full ``|``-separated parameter name to a
#: per-parameter spec.
OptionsPaginationT = Mapping[str, ParameterPaginationT]

T = TypeVar("T")


def normalize_pagination(pagination: Optional[ParameterPaginationT], src: str) -> tuple[int, int, Optional[str]]:
    """Return a clamped ``(offset, limit, search)`` for ``src``.

    Falls back to ``(0, DEFAULT_OPTIONS_PAGE_SIZE, None)`` when no spec is
    provided. Always clamps ``limit`` to the inclusive range
    ``[1, MAX_OPTIONS_PAGE_SIZE]`` and ``offset`` to ``>= 0`` — this is the
    server-side guarantee that no single request can pull an unbounded slice.
    ``search`` is coerced to ``None`` when empty/whitespace so a cleared search
    box behaves like no search at all.
    """
    if not pagination:
        return 0, DEFAULT_OPTIONS_PAGE_SIZE, None
    spec = pagination.get(src) or {}
    offset = max(int(spec.get("offset", 0)), 0)
    limit = int(spec.get("limit", DEFAULT_OPTIONS_PAGE_SIZE))
    limit = min(max(limit, 1), MAX_OPTIONS_PAGE_SIZE)
    raw_search = spec.get("search")
    search: Optional[str] = None
    if isinstance(raw_search, str) and raw_search.strip():
        search = raw_search.strip()
    return offset, limit, search


def accumulate_with_filter(
    query_fn: Callable[..., tuple[list, int]],
    filter_fn: Callable[[Any], Optional[T]],
    post_filter_offset: int,
    limit: int,
    chunk_size: Optional[int] = None,
) -> tuple[list[T], int, bool]:
    """Walk DB chunks via ``query_fn(offset=, limit=)`` and apply ``filter_fn``.

    ``filter_fn`` returns falsy to drop a row, or any truthy value (the "match")
    to keep it. Returns ``(matches, pre_filter_total, has_more)`` where:

    - ``matches`` is up to ``limit`` filter results starting from the
      ``post_filter_offset``-th match;
    - ``pre_filter_total`` is the count reported by the underlying query (the
      best estimate available without scanning the full filtered space);
    - ``has_more`` is true if more DB rows exist past the consumed window — it
      may over-estimate when the trailing rows would all be filtered out, but
      a follow-up page request returning empty matches resolves that.

    Used by data-tool-parameter ``to_dict`` for the chunked path that
    accommodates Python-only predicates (``options_filter_attribute``,
    ``data_destination`` public-role checks, collection subcollection mapping).
    """
    chunk_size = chunk_size or max(limit, 50)
    matches: list[T] = []
    skipped = 0
    db_offset = 0
    pre_filter_total = 0
    initialized = False
    while len(matches) < limit:
        rows, total = query_fn(offset=db_offset, limit=chunk_size)
        if not initialized:
            pre_filter_total = total
            initialized = True
        if not rows:
            return matches, pre_filter_total, False
        for row in rows:
            result = filter_fn(row)
            if not result:
                continue
            if skipped < post_filter_offset:
                skipped += 1
                continue
            matches.append(result)
            if len(matches) >= limit:
                break
        db_offset += len(rows)
        if len(matches) >= limit:
            break
        if db_offset >= pre_filter_total:
            return matches, pre_filter_total, False
    has_more = db_offset < pre_filter_total
    return matches, pre_filter_total, has_more
