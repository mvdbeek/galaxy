"""Server-Sent Events (SSE) connection manager for real-time notifications.

Manages per-worker in-memory mapping of user IDs to asyncio.Queue instances,
enabling push of events from any thread (e.g. Kombu control queue worker)
to async SSE endpoint handlers running in the uvicorn event loop.
"""

import asyncio
import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

log = logging.getLogger(__name__)


@dataclass
class SSEEvent:
    """An event to be sent to an SSE client."""

    event: str  # e.g. "notification_update", "broadcast_update", "notification_status"
    data: str  # JSON payload
    id: Optional[str] = (
        None  # ISO timestamp, used by EventSource as Last-Event-ID on reconnect
    )


class SSEConnectionManager:
    """Per-worker manager for SSE connections.

    Maps user_ids to sets of asyncio.Queue instances. Each SSE connection
    gets its own queue. The manager is thread-safe for push operations
    via ``loop.call_soon_threadsafe``.

    Lifecycle:
    - Instantiated once per Galaxy worker process (on app object).
    - ``connect()`` is called from the SSE async endpoint (event loop thread).
    - ``disconnect()`` is called from the SSE endpoint's ``finally`` block.
    - ``push_to_user()`` / ``push_broadcast()`` are called from ANY thread
      (typically the Kombu daemon thread via control task handlers).
    """

    def __init__(self) -> None:
        self._connections: dict[int, set[asyncio.Queue]] = defaultdict(set)
        self._broadcast_connections: set[asyncio.Queue] = set()
        self._loop: Optional[asyncio.AbstractEventLoop] = None

    def _ensure_loop(self) -> None:
        """Capture the running asyncio event loop. Must be called from async context."""
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()

    # -- Called from ASYNC context (uvicorn event loop thread) --

    def connect(self, user_id: Optional[int]) -> asyncio.Queue:
        """Register a new SSE connection. Returns a queue to await events from.

        Called from the SSE endpoint handler (async context).
        """
        self._ensure_loop()
        queue: asyncio.Queue = asyncio.Queue(maxsize=64)
        if user_id is not None:
            self._connections[user_id].add(queue)
        self._broadcast_connections.add(queue)
        log.debug(
            "SSE connection opened for user_id=%s (total=%d)",
            user_id,
            len(self._broadcast_connections),
        )
        return queue

    def disconnect(self, user_id: Optional[int], queue: asyncio.Queue) -> None:
        """Unregister an SSE connection.

        Called from the SSE endpoint's ``finally`` block (async context).
        """
        if user_id is not None:
            self._connections[user_id].discard(queue)
            if not self._connections[user_id]:
                del self._connections[user_id]
        self._broadcast_connections.discard(queue)
        log.debug(
            "SSE connection closed for user_id=%s (total=%d)",
            user_id,
            len(self._broadcast_connections),
        )

    # -- Called from ANY thread (Kombu thread or async) --

    def push_to_user(self, user_id: int, event: SSEEvent) -> None:
        """Thread-safe. Push an event to all SSE connections for a specific user."""
        for queue in list(self._connections.get(user_id, [])):
            self._safe_put(queue, event)

    def push_broadcast(self, event: SSEEvent) -> None:
        """Thread-safe. Push an event to ALL connected SSE clients."""
        for queue in list(self._broadcast_connections):
            self._safe_put(queue, event)

    def _safe_put(self, queue: asyncio.Queue, event: SSEEvent) -> None:
        """Cross the thread boundary safely using ``call_soon_threadsafe``."""
        if self._loop is None or self._loop.is_closed():
            return
        try:
            self._loop.call_soon_threadsafe(self._do_put, queue, event)
        except RuntimeError:
            # Event loop is closed or shutting down
            pass

    @staticmethod
    def _do_put(queue: asyncio.Queue, event: SSEEvent) -> None:
        """Runs ON the event loop thread. Safe to touch asyncio.Queue here."""
        try:
            queue.put_nowait(event)
        except asyncio.QueueFull:
            log.warning("SSE queue full, dropping event: %s", event.event)

    @property
    def connected_user_ids(self) -> set[int]:
        return set(self._connections.keys())

    @property
    def total_connections(self) -> int:
        return len(self._broadcast_connections)
