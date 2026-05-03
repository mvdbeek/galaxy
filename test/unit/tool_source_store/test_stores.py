"""Unit tests for tool source storage backends.

Tests verify that the tool source store classes work correctly with
different backends (database, disk). These tests directly instantiate
the stores to test the backend implementations.
"""

import tempfile

import pytest

from galaxy.app_unittest_utils.galaxy_mock import MockApp
from galaxy.tool_source_store import (
    build_tool_source_store,
    ConfigurationError,
    StoredToolSource,
)
from galaxy.tool_source_store.database import DatabaseToolSourceStore
from galaxy.tool_source_store.disk import DiskToolSourceStore
from galaxy.tool_source_store.index import (
    ToolIndex,
    ToolIndexEntry,
)


class FakeConfig:
    """Fake config for testing store factory."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class TestDatabaseBackend:
    """Unit tests for database backend using MockApp."""

    def test_database_store_basic_operations(self):
        """Test basic store/get operations with database backend."""
        app = MockApp()
        store = DatabaseToolSourceStore(app)
        test_hash = "test_hash_unit_123"

        try:
            tool_source = StoredToolSource(
                hash=test_hash,
                tool_source_class="XmlToolSource",
                raw_source='<tool id="test" version="1.0"><command>echo</command></tool>',
                tool_id="test_unit_tool",
                tool_version="1.0",
            )

            store.store(tool_source)
            app.model.context.commit()

            assert store.exists(tool_source.hash)

            retrieved = store.get(tool_source.hash)
            assert retrieved is not None
            assert retrieved.tool_id == "test_unit_tool"
            assert retrieved.tool_version == "1.0"
            assert "<tool" in retrieved.raw_source

            assert store.delete(tool_source.hash)
            app.model.context.commit()
            assert not store.exists(tool_source.hash)
        finally:
            if store.exists(test_hash):
                store.delete(test_hash)
                app.model.context.commit()

    def test_database_store_index_operations(self):
        """Test tool index storage with database backend."""
        app = MockApp()
        store = DatabaseToolSourceStore(app)

        index = ToolIndex()
        index.entries["test_tool_db"] = ToolIndexEntry(
            id="test_tool_db",
            name="Test Tool DB",
            version="1.0",
            description="A test tool",
        )

        store.store_index(index)
        app.model.context.commit()

        # Clear the cached index to force reload from database
        store.invalidate_index_cache()

        loaded_index = store.load_index()
        assert loaded_index is not None
        assert "test_tool_db" in loaded_index.entries
        assert loaded_index.entries["test_tool_db"].name == "Test Tool DB"

    def test_database_store_get_by_tool_id(self):
        """Test retrieving tool sources by tool ID."""
        app = MockApp()
        store = DatabaseToolSourceStore(app)

        unique_id = "tool_by_id_test_unit"
        test_hash = f"hash_for_{unique_id}"

        try:
            tool_source = StoredToolSource(
                hash=test_hash,
                tool_source_class="XmlToolSource",
                raw_source=f'<tool id="{unique_id}" version="1.0"><command>echo</command></tool>',
                tool_id=unique_id,
                tool_version="1.0",
            )
            store.store(tool_source)
            app.model.context.commit()

            sources = store.get_by_tool_id(unique_id)
            assert len(sources) >= 1
            assert any(s.tool_id == unique_id for s in sources)
        finally:
            if store.exists(test_hash):
                store.delete(test_hash)
                app.model.context.commit()

    def test_database_store_count(self):
        """Test counting stored tool sources."""
        app = MockApp()
        store = DatabaseToolSourceStore(app)
        test_hash = "count_test_hash_unit"

        try:
            initial_count = store.count()

            tool_source = StoredToolSource(
                hash=test_hash,
                tool_source_class="XmlToolSource",
                raw_source='<tool id="count_test"><command>echo</command></tool>',
                tool_id="count_test",
                tool_version="1.0",
            )
            store.store(tool_source)
            app.model.context.commit()

            assert store.count() == initial_count + 1

            store.delete(test_hash)
            app.model.context.commit()
            assert store.count() == initial_count
        finally:
            if store.exists(test_hash):
                store.delete(test_hash)
                app.model.context.commit()


class TestDiskBackend:
    """Tests for disk backend."""

    def test_disk_store_basic_operations(self):
        """Test basic store/get operations with disk backend."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = DiskToolSourceStore(tmpdir)

            tool_source = StoredToolSource(
                hash="disk_test_hash_123",
                tool_source_class="XmlToolSource",
                raw_source='<tool id="disk_test" version="2.0"><command>cat</command></tool>',
                tool_id="disk_test_tool",
                tool_version="2.0",
            )

            store.store(tool_source)

            assert store.exists("disk_test_hash_123")
            retrieved = store.get("disk_test_hash_123")
            assert retrieved is not None
            assert retrieved.tool_id == "disk_test_tool"

            assert store.count() >= 1

            assert store.delete("disk_test_hash_123")
            assert not store.exists("disk_test_hash_123")

    def test_disk_store_index_operations(self):
        """Test tool index with disk backend."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = DiskToolSourceStore(tmpdir)

            index = ToolIndex()
            index.entries["disk_tool"] = ToolIndexEntry(
                id="disk_tool",
                name="Disk Tool",
                version="1.0",
                description="Tool stored on disk",
            )

            store.store_index(index)

            loaded = store.load_index()
            assert loaded is not None
            assert "disk_tool" in loaded.entries

    def test_disk_store_persistence(self):
        """Test that disk storage persists across store instances."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store1 = DiskToolSourceStore(tmpdir)
            tool_source = StoredToolSource(
                hash="persist_test_hash",
                tool_source_class="XmlToolSource",
                raw_source='<tool id="persist"><command>echo</command></tool>',
                tool_id="persist_tool",
                tool_version="1.0",
            )
            store1.store(tool_source)

            store2 = DiskToolSourceStore(tmpdir)

            assert store2.exists("persist_test_hash")
            retrieved = store2.get("persist_test_hash")
            assert retrieved is not None
            assert retrieved.tool_id == "persist_tool"

    def test_disk_store_list_all(self):
        """Test listing all hashes from disk store."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = DiskToolSourceStore(tmpdir)

            hashes = ["hash_a", "hash_b", "hash_c"]
            for h in hashes:
                store.store(
                    StoredToolSource(
                        hash=h,
                        tool_source_class="XmlToolSource",
                        raw_source=f'<tool id="{h}"><command>echo</command></tool>',
                        tool_id=h,
                        tool_version="1.0",
                    )
                )

            listed = list(store.list_all())
            assert len(listed) == 3
            for h in hashes:
                assert h in listed

    def test_disk_store_get_by_tool_id(self):
        """Test retrieving by tool ID from disk store."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = DiskToolSourceStore(tmpdir)

            store.store(
                StoredToolSource(
                    hash="v1_hash",
                    tool_source_class="XmlToolSource",
                    raw_source='<tool id="multi_version" version="1.0"><command>v1</command></tool>',
                    tool_id="multi_version",
                    tool_version="1.0",
                )
            )
            store.store(
                StoredToolSource(
                    hash="v2_hash",
                    tool_source_class="XmlToolSource",
                    raw_source='<tool id="multi_version" version="2.0"><command>v2</command></tool>',
                    tool_id="multi_version",
                    tool_version="2.0",
                )
            )

            sources = store.get_by_tool_id("multi_version")
            assert len(sources) == 2

            sources_v1 = store.get_by_tool_id("multi_version", version="1.0")
            assert len(sources_v1) == 1
            assert sources_v1[0].tool_version == "1.0"


class TestBuildToolSourceStore:
    """Tests for the store factory function."""

    def test_build_database_store(self):
        """Test building database store from config."""
        app = MockApp()
        # Build from app
        store = build_tool_source_store(app)
        assert isinstance(store, DatabaseToolSourceStore)

    def test_build_disk_store(self):
        """Test building disk store from config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = FakeConfig(
                tool_source_store="disk",
                tool_source_disk_path=tmpdir,
            )
            store = build_tool_source_store(config)
            assert isinstance(store, DiskToolSourceStore)

    def test_build_disk_store_missing_path_raises(self):
        """Test that missing disk path raises ConfigurationError."""
        config = FakeConfig(tool_source_store="disk")
        with pytest.raises(ConfigurationError):
            build_tool_source_store(config)

    def test_build_redis_store_missing_url_raises(self):
        """Test that missing Redis URL raises ConfigurationError."""
        config = FakeConfig(tool_source_store="redis")
        with pytest.raises(ConfigurationError):
            build_tool_source_store(config)


class _FakeApp:
    """Tiny app stand-in for build_tool_source_store tests.

    Avoids the heavier MockApp/database fixtures since these tests only
    need ``app.config`` and (for the disk path) no model.
    """

    def __init__(self, config):
        self.config = config


class TestPerConfStoreRouting:
    """Tests for per-conf store routing in build_tool_source_store."""

    def test_lazy_off_ignores_unknown_per_conf_store(self, tmp_path, caplog):
        # tool_conf opting into a store that is *not* in tool_source_stores —
        # should not raise when use_lazy_toolbox is off, just log and return
        # the default store.
        conf = tmp_path / "extra_tool_conf.xml"
        conf.write_text('<?xml version="1.0"?>\n<toolbox store="missing_alias"/>\n')
        disk_dir = tmp_path / "sources"
        config = FakeConfig(
            tool_source_store="disk",
            tool_source_disk_path=str(disk_dir),
            tool_configs=[str(conf)],
            tool_source_stores={},
            use_lazy_toolbox=False,
        )
        with caplog.at_level("INFO", logger="galaxy.tool_source_store"):
            store = build_tool_source_store(_FakeApp(config))
        from galaxy.tool_source_store.composite import CompositeToolSourceStore

        assert isinstance(store, DiskToolSourceStore)
        assert not isinstance(store, CompositeToolSourceStore)
        assert any("missing_alias" in rec.message for rec in caplog.records)

    def test_lazy_unset_also_ignores_per_conf_store(self, tmp_path):
        # The default deployment (use_lazy_toolbox unset) must not silently
        # flip to lazy via per-conf stores — the attribute is ignored.
        conf = tmp_path / "extra_tool_conf.xml"
        conf.write_text('<?xml version="1.0"?>\n<toolbox store="anything"/>\n')
        disk_dir = tmp_path / "sources"
        config = FakeConfig(
            tool_source_store="disk",
            tool_source_disk_path=str(disk_dir),
            tool_configs=[str(conf)],
            tool_source_stores={},
            use_lazy_toolbox=None,
        )
        store = build_tool_source_store(_FakeApp(config))
        assert isinstance(store, DiskToolSourceStore)

    def test_lazy_on_with_unknown_store_still_raises(self, tmp_path):
        # When the user explicitly opts in, we *do* want a clear error if a
        # tool_conf references a store that isn't declared.
        conf = tmp_path / "extra_tool_conf.xml"
        conf.write_text('<?xml version="1.0"?>\n<toolbox store="missing_alias"/>\n')
        disk_dir = tmp_path / "sources"
        config = FakeConfig(
            tool_source_store="disk",
            tool_source_disk_path=str(disk_dir),
            tool_configs=[str(conf)],
            tool_source_stores={},
            use_lazy_toolbox=True,
        )
        with pytest.raises(ConfigurationError):
            build_tool_source_store(_FakeApp(config))


class TestToolIndex:
    """Tests for ToolIndex functionality."""

    def test_index_search(self):
        """Test searching the tool index."""
        index = ToolIndex()
        index.entries["filter_tool"] = ToolIndexEntry(
            id="filter_tool",
            name="Filter Tool",
            version="1.0",
            description="Filters data by column",
        )
        index.entries["cat_tool"] = ToolIndexEntry(
            id="cat_tool",
            name="Concatenate",
            version="2.0",
            description="Concatenates files",
        )

        results = index.search("Filter", limit=10)
        assert len(results) >= 1
        assert any(r.id == "filter_tool" for r in results)

        results = index.search("column", limit=10)
        assert len(results) >= 1
        assert any(r.id == "filter_tool" for r in results)

    def test_index_serialization(self):
        """Test index to_dict/from_dict round trip."""
        index = ToolIndex()
        index.entries["test_tool"] = ToolIndexEntry(
            id="test_tool",
            name="Test",
            version="1.0",
            description="Test tool",
            labels=["genomics"],
        )
        index.by_section["section1"] = ["test_tool"]

        data = index.to_dict()

        restored = ToolIndex.from_dict(data)

        assert "test_tool" in restored.entries
        assert restored.entries["test_tool"].name == "Test"
        assert "section1" in restored.by_section

    def test_index_get_tests_summary(self):
        """Test generating tests summary from index."""
        index = ToolIndex()
        index.entries["tool1"] = ToolIndexEntry(
            id="tool1",
            name="Tool 1",
            version="1.0",
            test_count=3,
        )
        index.entries["tool2"] = ToolIndexEntry(
            id="tool2",
            name="Tool 2",
            version="2.0",
            test_count=0,
        )

        summary = index.get_tests_summary()
        # Tools with tests must appear; tools without tests must not.
        assert "tool1" in summary
        assert summary["tool1"]["1.0"]["count"] == 3
        assert summary["tool1"]["1.0"]["tool_name"] == "Tool 1"
        assert "tool2" not in summary

    def test_index_get_all_requirements(self):
        """Test aggregating all requirements from index."""
        index = ToolIndex()
        index.entries["tool1"] = ToolIndexEntry(
            id="tool1",
            name="Tool 1",
            version="1.0",
            requirements=[
                {"name": "samtools", "version": "1.0", "type": "package"},
            ],
        )

        requirements = index.get_all_requirements()
        assert isinstance(requirements, list)
        assert {"name": "samtools", "version": "1.0", "type": "package"} in requirements
