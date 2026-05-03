"""Unit tests for CompositeToolSourceStore + merged ToolIndex."""

import os
import tempfile

import pytest

from galaxy.tool_source_store import (
    ReadOnlyStoreError,
    StoredToolSource,
)
from galaxy.tool_source_store.composite import CompositeToolSourceStore
from galaxy.tool_source_store.index import (
    ToolIndex,
    ToolIndexEntry,
)
from galaxy.tool_source_store.sqlalchemy import SqlAlchemyToolSourceStore as SqliteToolSourceStore


@pytest.fixture
def two_paths():
    with tempfile.TemporaryDirectory() as d:
        yield os.path.join(d, "a.sqlite"), os.path.join(d, "b.sqlite")


def _src(hash, tool_id="t", version="1"):
    return StoredToolSource(
        hash=hash,
        tool_source_class="XmlToolSource",
        raw_source=f'<tool id="{tool_id}" version="{version}"/>',
        tool_id=tool_id,
        tool_version=version,
    )


def test_priority_order_first_hit_wins(two_paths):
    pa, pb = two_paths
    a = SqliteToolSourceStore(path=pa)
    b = SqliteToolSourceStore(path=pb)
    # Same hash, different tool_id payloads, to prove which member answered.
    a.store(_src("dup", tool_id="from_a"))
    b.store(_src("dup", tool_id="from_b"))
    composite = CompositeToolSourceStore(members=[("a", a), ("b", b)], default="b")
    got = composite.get("dup")
    assert got.tool_id == "from_a"


def test_writes_go_to_default(two_paths):
    pa, pb = two_paths
    a = SqliteToolSourceStore(path=pa)
    b = SqliteToolSourceStore(path=pb)
    composite = CompositeToolSourceStore(members=[("a", a), ("b", b)], default="b")
    composite.store(_src("h1"))
    assert b.exists("h1")
    assert not a.exists("h1")


def test_default_must_not_be_read_only(two_paths):
    pa, pb = two_paths
    rw = SqliteToolSourceStore(path=pa)
    rw.store(_src("seed"))  # so the file exists
    ro = SqliteToolSourceStore(path=pa, read_only=True)
    with pytest.raises(ValueError):
        CompositeToolSourceStore(members=[("ro", ro), ("rw", rw)], default="ro")


def test_store_to_named_member(two_paths):
    pa, pb = two_paths
    a = SqliteToolSourceStore(path=pa)
    b = SqliteToolSourceStore(path=pb)
    composite = CompositeToolSourceStore(members=[("a", a), ("b", b)], default="b")
    composite.store_to("a", _src("hA"))
    assert a.exists("hA")
    assert not b.exists("hA")


def test_store_to_read_only_member_raises(two_paths):
    pa, pb = two_paths
    SqliteToolSourceStore(path=pa).store(_src("seed"))
    ro = SqliteToolSourceStore(path=pa, read_only=True)
    rw = SqliteToolSourceStore(path=pb)
    composite = CompositeToolSourceStore(members=[("ro", ro), ("rw", rw)], default="rw")
    with pytest.raises(ReadOnlyStoreError):
        composite.store_to("ro", _src("hX"))


def test_list_all_dedupes_across_members(two_paths):
    pa, pb = two_paths
    a = SqliteToolSourceStore(path=pa)
    b = SqliteToolSourceStore(path=pb)
    a.store(_src("h1"))
    a.store(_src("dup"))
    b.store(_src("dup"))
    b.store(_src("h2"))
    composite = CompositeToolSourceStore(members=[("a", a), ("b", b)], default="b")
    assert sorted(composite.list_all()) == ["dup", "h1", "h2"]
    assert composite.count() == 3


def test_load_index_merges_and_dedupes(two_paths):
    pa, pb = two_paths
    a = SqliteToolSourceStore(path=pa)
    b = SqliteToolSourceStore(path=pb)
    a.store_index(ToolIndex(entries={
        "shared": ToolIndexEntry(id="shared", name="from_a"),
        "only_a": ToolIndexEntry(id="only_a", name="A only"),
    }))
    b.store_index(ToolIndex(entries={
        "shared": ToolIndexEntry(id="shared", name="from_b"),
        "only_b": ToolIndexEntry(id="only_b", name="B only"),
    }))
    composite = CompositeToolSourceStore(members=[("a", a), ("b", b)], default="b")
    merged = composite.load_index()
    assert merged is not None
    assert set(merged.entries.keys()) == {"shared", "only_a", "only_b"}
    # Earlier member wins on collision.
    assert merged.entries["shared"].name == "from_a"


def test_load_index_returns_none_when_no_member_has_one(two_paths):
    pa, pb = two_paths
    a = SqliteToolSourceStore(path=pa)
    b = SqliteToolSourceStore(path=pb)
    composite = CompositeToolSourceStore(members=[("a", a), ("b", b)], default="b")
    assert composite.load_index() is None


def test_invalidate_fans_out(two_paths):
    pa, pb = two_paths
    a = SqliteToolSourceStore(path=pa)
    b = SqliteToolSourceStore(path=pb)
    a.store_index(ToolIndex(entries={"x": ToolIndexEntry(id="x")}))
    b.store_index(ToolIndex(entries={"y": ToolIndexEntry(id="y")}))
    a.load_index()
    b.load_index()
    assert a._cached_index is not None
    assert b._cached_index is not None
    composite = CompositeToolSourceStore(members=[("a", a), ("b", b)], default="b")
    composite.invalidate_index_cache()
    assert a._cached_index is None
    assert b._cached_index is None


def test_writable_members_excludes_read_only(two_paths):
    pa, pb = two_paths
    SqliteToolSourceStore(path=pa).store(_src("seed"))
    ro = SqliteToolSourceStore(path=pa, read_only=True)
    rw = SqliteToolSourceStore(path=pb)
    composite = CompositeToolSourceStore(members=[("ro", ro), ("rw", rw)], default="rw")
    assert [n for n, _ in composite.writable_members()] == ["rw"]
