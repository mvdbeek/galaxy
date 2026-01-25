"""Integration tests for tool source storage backends.

Tests verify that the tool source storage system works correctly with
different backends (database, disk). These tests directly instantiate
the stores to test the backend implementations.
"""

import os
import tempfile

import pytest

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
from galaxy_test.driver import integration_util


class FakeConfig:
    """Fake config for testing store backends."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class TestDatabaseBackend(integration_util.IntegrationTestCase):
    """Integration tests for database backend using real Galaxy database."""

    framework_tool_and_types = True

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)

    def test_database_store_basic_operations(self):
        """Test basic store/get operations with database backend."""
        config = FakeConfig(
            tool_source_store="database",
            database_connection=self._app.config.database_connection,
        )
        store = DatabaseToolSourceStore(config)

        tool_source = StoredToolSource(
            hash="test_hash_integration_" + str(id(self)),
            tool_source_class="XmlToolSource",
            raw_source='<tool id="test" version="1.0"><command>echo</command></tool>',
            tool_id="test_integration_tool",
            tool_version="1.0",
        )

        store.store(tool_source)

        assert store.exists(tool_source.hash)

        retrieved = store.get(tool_source.hash)
        assert retrieved is not None
        assert retrieved.tool_id == "test_integration_tool"
        assert retrieved.tool_version == "1.0"
        assert "<tool" in retrieved.raw_source

        assert store.delete(tool_source.hash)
        assert not store.exists(tool_source.hash)

    def test_database_store_index_operations(self):
        """Test tool index storage with database backend."""
        config = FakeConfig(
            tool_source_store="database",
            database_connection=self._app.config.database_connection,
        )
        store = DatabaseToolSourceStore(config)

        index = ToolIndex()
        index.entries["test_tool_db"] = ToolIndexEntry(
            id="test_tool_db",
            name="Test Tool DB",
            version="1.0",
            description="A test tool",
        )

        store.store_index(index)

        loaded_index = store.load_index()
        assert loaded_index is not None
        assert "test_tool_db" in loaded_index.entries
        assert loaded_index.entries["test_tool_db"].name == "Test Tool DB"

    def test_database_store_get_by_tool_id(self):
        """Test retrieving tool sources by tool ID."""
        config = FakeConfig(
            tool_source_store="database",
            database_connection=self._app.config.database_connection,
        )
        store = DatabaseToolSourceStore(config)

        unique_id = f"tool_by_id_test_{id(self)}"
        tool_source = StoredToolSource(
            hash=f"hash_for_{unique_id}",
            tool_source_class="XmlToolSource",
            raw_source=f'<tool id="{unique_id}" version="1.0"><command>echo</command></tool>',
            tool_id=unique_id,
            tool_version="1.0",
        )
        store.store(tool_source)

        sources = store.get_by_tool_id(unique_id)
        assert len(sources) >= 1
        assert any(s.tool_id == unique_id for s in sources)

        store.delete(tool_source.hash)

    def test_database_store_count(self):
        """Test counting stored tool sources."""
        config = FakeConfig(
            tool_source_store="database",
            database_connection=self._app.config.database_connection,
        )
        store = DatabaseToolSourceStore(config)

        initial_count = store.count()

        tool_source = StoredToolSource(
            hash=f"count_test_hash_{id(self)}",
            tool_source_class="XmlToolSource",
            raw_source='<tool id="count_test"><command>echo</command></tool>',
            tool_id="count_test",
            tool_version="1.0",
        )
        store.store(tool_source)

        assert store.count() == initial_count + 1

        store.delete(tool_source.hash)
        assert store.count() == initial_count


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
        config = FakeConfig(
            tool_source_store="database",
            database_connection="sqlite:///:memory:",
        )
        store = build_tool_source_store(config)
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


@integration_util.skip_unless_environ("GALAXY_TEST_TOOL_SOURCE_REDIS_URL")
class TestRedisBackend:
    """Tests for Redis backend (requires Redis)."""

    def test_redis_store_basic_operations(self):
        """Test basic operations with Redis backend."""
        from galaxy.tool_source_store.redis import RedisToolSourceStore

        redis_url = os.environ.get("GALAXY_TEST_TOOL_SOURCE_REDIS_URL")
        store = RedisToolSourceStore(redis_url)

        tool_source = StoredToolSource(
            hash="redis_test_hash_456",
            tool_source_class="XmlToolSource",
            raw_source='<tool id="redis_test"><command>redis</command></tool>',
            tool_id="redis_test_tool",
            tool_version="3.0",
        )

        store.store(tool_source)

        assert store.exists("redis_test_hash_456")
        retrieved = store.get("redis_test_hash_456")
        assert retrieved is not None
        assert retrieved.tool_id == "redis_test_tool"

        store.delete("redis_test_hash_456")

    def test_redis_store_index(self):
        """Test index operations with Redis backend."""
        from galaxy.tool_source_store.redis import RedisToolSourceStore

        redis_url = os.environ.get("GALAXY_TEST_TOOL_SOURCE_REDIS_URL")
        store = RedisToolSourceStore(redis_url)

        index = ToolIndex()
        index.entries["redis_tool"] = ToolIndexEntry(
            id="redis_tool",
            name="Redis Tool",
            version="1.0",
            description="Tool in Redis",
        )

        store.store_index(index)

        loaded = store.load_index()
        assert loaded is not None
        assert "redis_tool" in loaded.entries


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
        assert isinstance(summary, dict)

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
        assert isinstance(requirements, (list, dict))
