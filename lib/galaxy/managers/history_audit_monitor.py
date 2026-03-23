"""Monitor for history audit table changes.

Detects history changes via PostgreSQL LISTEN/NOTIFY (instant) or by polling
the history_audit table (SQLite fallback). Dispatches SSE events to connected
users via Kombu control tasks.

Only active when ``enable_sse_history_updates`` is True in the Galaxy config.
"""

import logging
import select
import threading
import time
from collections import defaultdict
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    Optional,
    TYPE_CHECKING,
)

from sqlalchemy import select as sa_select

from galaxy.model import (
    History,
    HistoryAudit,
)

if TYPE_CHECKING:
    from galaxy.app import UniverseApplication

log = logging.getLogger(__name__)

CHANNEL_NAME = "galaxy_history_update"


class HistoryAuditMonitor:
    """Background thread that monitors history_audit for changes and dispatches SSE events.

    On PostgreSQL: uses LISTEN/NOTIFY for instant notification.
    On SQLite: polls history_audit table at a configurable interval.
    """

    def __init__(self, app: "UniverseApplication") -> None:
        self.app = app
        self.poll_interval: int = app.config.history_audit_monitor_poll_interval
        self._is_postgres: bool = "postgres" in app.model.engine.name
        self._exit = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._active = False
        # Cache: history_id -> user_id, refreshed on miss
        self._history_owner_cache: dict[int, int] = {}

    def start(self) -> None:
        if self._active:
            return
        self._active = True
        target = self._listen_postgres if self._is_postgres else self._poll_audit_table
        self._thread = threading.Thread(
            target=target,
            name="history_audit_monitor",
            daemon=True,
        )
        self._thread.start()
        log.info(
            "HistoryAuditMonitor started (mode=%s, interval=%ds)",
            "pg_listen" if self._is_postgres else "poll",
            self.poll_interval,
        )

    def shutdown(self) -> None:
        self._active = False
        self._exit.set()
        if self._thread:
            self._thread.join(timeout=5)

    # --- PostgreSQL LISTEN/NOTIFY mode ---

    def _listen_postgres(self) -> None:
        """Use a raw psycopg2 connection to LISTEN for history update notifications."""
        engine = self.app.model.engine
        # Get a raw DBAPI connection outside the SA pool
        raw_url = engine.url
        try:
            import psycopg2

            conn = psycopg2.connect(str(raw_url))
        except Exception:
            log.warning(
                "Failed to create psycopg2 LISTEN connection, falling back to polling",
                exc_info=True,
            )
            self._poll_audit_table()
            return

        conn.set_isolation_level(0)  # autocommit
        cursor = conn.cursor()
        cursor.execute(f"LISTEN {CHANNEL_NAME};")
        log.debug("LISTEN %s established on dedicated connection", CHANNEL_NAME)

        pending: dict[int, float] = {}  # history_id -> first_seen_time
        debounce_seconds = 0.2

        try:
            while not self._exit.is_set():
                # Wait for notifications with timeout
                if select.select([conn], [], [], self.poll_interval) == ([], [], []):
                    # Timeout — flush any pending debounced events
                    if pending:
                        self._dispatch_history_updates(set(pending.keys()))
                        pending.clear()
                    continue

                conn.poll()
                while conn.notifies:
                    notify = conn.notifies.pop(0)
                    try:
                        history_id = int(notify.payload)
                        if history_id not in pending:
                            pending[history_id] = time.monotonic()
                    except (ValueError, TypeError):
                        pass

                # Debounce: dispatch events that have been pending long enough
                now = time.monotonic()
                ready = {hid for hid, ts in pending.items() if now - ts >= debounce_seconds}
                if ready:
                    self._dispatch_history_updates(ready)
                    for hid in ready:
                        del pending[hid]
        except Exception:
            log.exception("HistoryAuditMonitor LISTEN loop error")
        finally:
            try:
                cursor.close()
                conn.close()
            except Exception:
                pass

    # --- SQLite polling fallback ---

    def _poll_audit_table(self) -> None:
        """Poll history_audit for recent changes."""
        last_check = datetime.utcnow() - timedelta(seconds=self.poll_interval)

        while not self._exit.is_set():
            try:
                check_time = datetime.utcnow()
                stmt = (
                    sa_select(HistoryAudit.history_id)
                    .where(HistoryAudit.update_time > last_check)
                    .group_by(HistoryAudit.history_id)
                )
                with self.app.model.new_session() as session:
                    changed_ids = set(session.scalars(stmt).all())

                if changed_ids:
                    self._dispatch_history_updates(changed_ids)

                last_check = check_time
            except Exception:
                log.exception("HistoryAuditMonitor poll error")

            self._exit.wait(self.poll_interval)

    # --- Common dispatch logic ---

    def _dispatch_history_updates(self, history_ids: set[int]) -> None:
        """Map history_ids to user_ids and send Kombu control task."""
        # Resolve owners for unknown history_ids
        unknown = history_ids - self._history_owner_cache.keys()
        if unknown:
            self._refresh_owner_cache(unknown)

        # Group by user_id, encoding history IDs for the frontend
        encode = self.app.security.encode_id
        user_updates: dict[int, list[str]] = defaultdict(list)
        for history_id in history_ids:
            user_id = self._history_owner_cache.get(history_id)
            if user_id is not None:
                user_updates[user_id].append(encode(history_id))

        if not user_updates:
            return

        from galaxy.queue_worker import send_control_task

        send_control_task(
            self.app,
            "history_update",
            kwargs={
                "user_updates": {str(uid): hids for uid, hids in user_updates.items()},
                "event_id": datetime.utcnow().isoformat(),
            },
            expiration=10,
        )

    def _refresh_owner_cache(self, history_ids: set[int]) -> None:
        """Look up user_id for given history_ids and update cache."""
        try:
            stmt = sa_select(History.id, History.user_id).where(History.id.in_(history_ids))
            with self.app.model.new_session() as session:
                for row in session.execute(stmt):
                    self._history_owner_cache[row[0]] = row[1]
        except Exception:
            log.debug("Failed to refresh history owner cache", exc_info=True)
