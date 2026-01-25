"""Tests for the populate_store.py script.

These tests cover the core functionality of the tool source population script,
including hash computation, file watching, and Kombu notification sending.
"""

import hashlib
import os
import tempfile
import threading
import time
from pathlib import Path
from unittest.mock import (
    MagicMock,
    patch,
)

import pytest


# Add Galaxy lib to path for imports
galaxy_root = Path(__file__).parent.parent.parent.parent.parent
import sys

sys.path.insert(0, str(galaxy_root / "lib"))
sys.path.insert(0, str(galaxy_root / "scripts" / "tool_source"))

from populate_store import (
    compute_hash,
    iter_tool_sources,
    send_reload_notification,
    ToolFileWatcher,
)


class TestComputeHash:
    """Tests for the compute_hash function."""

    def test_compute_hash_simple(self):
        """Test hash computation for simple string."""
        content = "hello world"
        result = compute_hash(content)
        expected = hashlib.sha256(content.encode()).hexdigest()
        assert result == expected

    def test_compute_hash_empty_string(self):
        """Test hash computation for empty string."""
        content = ""
        result = compute_hash(content)
        expected = hashlib.sha256(content.encode()).hexdigest()
        assert result == expected

    def test_compute_hash_unicode(self):
        """Test hash computation with unicode content."""
        content = "unicode: \u00e9\u00e0\u00fc"
        result = compute_hash(content)
        expected = hashlib.sha256(content.encode()).hexdigest()
        assert result == expected

    def test_compute_hash_xml_content(self):
        """Test hash computation with XML tool content."""
        content = '''<tool id="test_tool" name="Test" version="1.0">
            <command>echo hello</command>
        </tool>'''
        result = compute_hash(content)
        # Verify it returns a valid SHA256 hex string
        assert len(result) == 64
        assert all(c in "0123456789abcdef" for c in result)

    def test_compute_hash_deterministic(self):
        """Test that hash computation is deterministic."""
        content = "test content"
        result1 = compute_hash(content)
        result2 = compute_hash(content)
        assert result1 == result2

    def test_compute_hash_different_content(self):
        """Test that different content produces different hashes."""
        content1 = "content one"
        content2 = "content two"
        assert compute_hash(content1) != compute_hash(content2)


class TestIterToolSources:
    """Tests for the iter_tool_sources function."""

    def test_iter_tool_sources_empty_toolbox(self):
        """Test iteration over empty toolbox."""
        mock_toolbox = MagicMock()
        mock_toolbox._tools_by_id = {}

        result = list(iter_tool_sources(mock_toolbox))
        assert result == []

    def test_iter_tool_sources_with_tools(self):
        """Test iteration over toolbox with tools."""
        mock_tool = MagicMock()
        mock_tool.version = "1.0"
        mock_tool.tool_source = MagicMock()
        mock_tool.tool_dir = "/path/to/tool"

        mock_toolbox = MagicMock()
        mock_toolbox._tools_by_id = {"test_tool": mock_tool}

        result = list(iter_tool_sources(mock_toolbox))
        assert len(result) == 1
        assert result[0][0] == "test_tool"
        assert result[0][1] == "1.0"

    def test_iter_tool_sources_with_pattern_match(self):
        """Test filtering tools by pattern."""
        mock_tool1 = MagicMock()
        mock_tool1.version = "1.0"
        mock_tool1.tool_source = MagicMock()

        mock_tool2 = MagicMock()
        mock_tool2.version = "2.0"
        mock_tool2.tool_source = MagicMock()

        mock_toolbox = MagicMock()
        mock_toolbox._tools_by_id = {
            "filter_tool": mock_tool1,
            "other_tool": mock_tool2,
        }

        result = list(iter_tool_sources(mock_toolbox, pattern="filter"))
        assert len(result) == 1
        assert result[0][0] == "filter_tool"

    def test_iter_tool_sources_with_pattern_no_match(self):
        """Test filtering when no tools match pattern."""
        mock_tool = MagicMock()
        mock_tool.version = "1.0"
        mock_tool.tool_source = MagicMock()

        mock_toolbox = MagicMock()
        mock_toolbox._tools_by_id = {"test_tool": mock_tool}

        result = list(iter_tool_sources(mock_toolbox, pattern="nonexistent"))
        assert result == []

    def test_iter_tool_sources_skips_without_tool_source(self):
        """Test that tools without tool_source attribute are skipped."""
        mock_tool_with = MagicMock()
        mock_tool_with.version = "1.0"
        mock_tool_with.tool_source = MagicMock()

        mock_tool_without = MagicMock(spec=[])
        mock_tool_without.version = "2.0"

        mock_toolbox = MagicMock()
        mock_toolbox._tools_by_id = {
            "tool_with": mock_tool_with,
            "tool_without": mock_tool_without,
        }

        result = list(iter_tool_sources(mock_toolbox))
        assert len(result) == 1
        assert result[0][0] == "tool_with"


class TestSendReloadNotification:
    """Tests for the send_reload_notification function."""

    def test_send_reload_notification_no_amqp_url(self):
        """Test that notification fails gracefully without AMQP URL."""
        mock_config = MagicMock()
        mock_config.amqp_internal_connection = None

        result = send_reload_notification(mock_config)
        assert result is False

    def test_send_reload_notification_success(self):
        """Test successful notification sending."""
        mock_config = MagicMock()
        mock_config.amqp_internal_connection = "amqp://localhost"

        mock_producer = MagicMock()
        mock_producers = MagicMock()
        mock_producers.__getitem__.return_value.acquire.return_value.__enter__ = MagicMock(
            return_value=mock_producer
        )
        mock_producers.__getitem__.return_value.acquire.return_value.__exit__ = MagicMock(
            return_value=False
        )

        with patch.dict(
            "sys.modules",
            {
                "kombu": MagicMock(),
                "kombu.pools": MagicMock(producers=mock_producers),
            },
        ):
            with patch("kombu.Connection") as mock_connection:
                with patch("kombu.pools.producers", mock_producers):
                    result = send_reload_notification(mock_config)
                    assert result is True
                    mock_producer.publish.assert_called_once()

    def test_send_reload_notification_exception(self):
        """Test that exceptions are handled gracefully."""
        mock_config = MagicMock()
        mock_config.amqp_internal_connection = "amqp://localhost"

        with patch.dict(
            "sys.modules",
            {
                "kombu": MagicMock(Connection=MagicMock(side_effect=Exception("Connection failed"))),
            },
        ):
            # The function should catch the exception and return False
            result = send_reload_notification(mock_config)
            assert result is False


class TestToolFileWatcher:
    """Tests for the ToolFileWatcher class."""

    def test_watcher_initialization(self):
        """Test watcher initialization."""
        mock_config = MagicMock()
        mock_store = MagicMock()
        tools_dirs = [Path("/tmp/tools")]

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=tools_dirs,
            debounce_seconds=1.0,
            use_polling=False,
            verbose=True,
        )

        assert watcher.config == mock_config
        assert watcher.store == mock_store
        assert watcher.debounce_seconds == 1.0
        assert watcher.use_polling is False
        assert watcher.verbose is True

    def test_watcher_queue_change_debouncing(self):
        """Test that file changes are debounced."""
        mock_config = MagicMock()
        mock_store = MagicMock()

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
            debounce_seconds=0.5,
        )

        # Queue multiple changes rapidly
        watcher._queue_change("/path/to/tool1.xml")
        watcher._queue_change("/path/to/tool2.xml")
        watcher._queue_change("/path/to/tool1.xml")  # Duplicate

        # Check that changes are queued (deduplicated)
        assert len(watcher._pending_changes) == 2
        assert "/path/to/tool1.xml" in watcher._pending_changes
        assert "/path/to/tool2.xml" in watcher._pending_changes

        # Cancel the timer to prevent processing
        if watcher._debounce_timer:
            watcher._debounce_timer.cancel()

    def test_watcher_process_tool_file_not_a_tool(self):
        """Test processing a non-tool XML file."""
        mock_config = MagicMock()
        mock_store = MagicMock()

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            f.write("<data>not a tool</data>")
            temp_path = f.name

        try:
            result = watcher._process_tool_file(temp_path)
            assert result is False
        finally:
            os.unlink(temp_path)

    def test_watcher_process_tool_file_valid_tool(self):
        """Test processing a valid tool XML file."""
        mock_config = MagicMock()
        mock_store = MagicMock()
        mock_store.exists.return_value = False

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        tool_content = '''<tool id="test_tool" name="Test" version="1.0">
            <command>echo hello</command>
        </tool>'''

        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            f.write(tool_content)
            temp_path = f.name

        try:
            # The function imports StoredToolSource from galaxy.tool_source_store
            # We just need to verify the store.store() is called
            result = watcher._process_tool_file(temp_path)
            assert result is True
            mock_store.store.assert_called_once()
            # Verify the stored object has correct attributes
            stored_obj = mock_store.store.call_args[0][0]
            assert stored_obj.tool_id == "test_tool"
            assert stored_obj.tool_version == "1.0"
        finally:
            os.unlink(temp_path)

    def test_watcher_process_tool_file_unchanged(self):
        """Test processing an unchanged tool file (already in store)."""
        mock_config = MagicMock()
        mock_store = MagicMock()
        mock_store.exists.return_value = True  # Already stored

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        tool_content = '''<tool id="test_tool" name="Test" version="1.0">
            <command>echo hello</command>
        </tool>'''

        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            f.write(tool_content)
            temp_path = f.name

        try:
            result = watcher._process_tool_file(temp_path)
            assert result is False
            mock_store.store.assert_not_called()
        finally:
            os.unlink(temp_path)

    def test_watcher_process_tool_file_extracts_id_and_version(self):
        """Test that tool ID and version are correctly extracted."""
        mock_config = MagicMock()
        mock_store = MagicMock()
        mock_store.exists.return_value = False

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        tool_content = '''<tool id="my_tool_id" version="2.5.1" name="My Tool">
            <command>echo test</command>
        </tool>'''

        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            f.write(tool_content)
            temp_path = f.name

        try:
            result = watcher._process_tool_file(temp_path)
            assert result is True
            # Check the stored object has correct ID and version
            stored_obj = mock_store.store.call_args[0][0]
            assert stored_obj.tool_id == "my_tool_id"
            assert stored_obj.tool_version == "2.5.1"
        finally:
            os.unlink(temp_path)

    def test_watcher_shutdown(self):
        """Test watcher shutdown."""
        mock_config = MagicMock()
        mock_store = MagicMock()

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        # Set up a debounce timer
        watcher._debounce_timer = threading.Timer(10.0, lambda: None)
        watcher._debounce_timer.start()

        watcher.shutdown()

        assert watcher._shutdown_event.is_set()

    @pytest.mark.skipif(
        True,  # Skip by default as watchdog may not be installed
        reason="Requires watchdog library",
    )
    def test_watcher_start_without_watchdog(self):
        """Test that start fails gracefully without watchdog."""
        mock_config = MagicMock()
        mock_store = MagicMock()

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        with patch.dict("sys.modules", {"watchdog": None, "watchdog.events": None, "watchdog.observers": None}):
            result = watcher.start()
            # Should fail if watchdog is not available
            assert result is False


class TestProcessPendingChanges:
    """Tests for the _process_pending_changes method."""

    def test_process_pending_changes_empty(self):
        """Test processing when no changes are pending."""
        mock_config = MagicMock()
        mock_store = MagicMock()

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        # Should not raise any errors
        watcher._process_pending_changes()

    def test_process_pending_changes_with_updates(self):
        """Test processing pending changes that result in updates."""
        mock_config = MagicMock()
        mock_store = MagicMock()
        mock_store.exists.return_value = False

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        tool_content = '''<tool id="test_tool" name="Test" version="1.0">
            <command>echo hello</command>
        </tool>'''

        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            f.write(tool_content)
            temp_path = f.name

        try:
            watcher._pending_changes.add(temp_path)

            # Patch at the module level where it's used
            import populate_store

            with patch.object(populate_store, "send_reload_notification") as mock_send_notification:
                watcher._process_pending_changes()

                # Should have sent notification
                mock_send_notification.assert_called_once_with(mock_config)
        finally:
            os.unlink(temp_path)

    def test_process_pending_changes_no_updates(self):
        """Test that notification is not sent when no tools were updated."""
        mock_config = MagicMock()
        mock_store = MagicMock()
        mock_store.exists.return_value = True  # Already stored

        watcher = ToolFileWatcher(
            config=mock_config,
            store=mock_store,
            tools_dirs=[],
        )

        tool_content = '''<tool id="test_tool" name="Test" version="1.0">
            <command>echo hello</command>
        </tool>'''

        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            f.write(tool_content)
            temp_path = f.name

        try:
            watcher._pending_changes.add(temp_path)

            # Patch at the module level where it's used
            import populate_store

            with patch.object(populate_store, "send_reload_notification") as mock_send_notification:
                watcher._process_pending_changes()

                # Should NOT have sent notification since tool was unchanged
                mock_send_notification.assert_not_called()
        finally:
            os.unlink(temp_path)
