"""Integration tests for SSE-based history update notifications."""

import json
import threading
import time
from urllib.parse import urljoin
from uuid import uuid4

import requests

from galaxy.util.wait import wait_on
from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver.integration_util import IntegrationTestCase


def parse_sse_events(raw: str) -> list[dict]:
    """Parse raw SSE text into a list of event dicts with 'event', 'data', and 'id' keys."""
    events = []
    current: dict[str, str] = {}
    for line in raw.split("\n"):
        if line.startswith(":"):
            continue  # comment / keepalive
        if line == "":
            if current:
                events.append(current)
                current = {}
            continue
        if ": " in line:
            field, _, value = line.partition(": ")
        else:
            field, value = line.rstrip(":"), ""
        if field in ("event", "data", "id"):
            current[field] = value
    if current:
        events.append(current)
    return events


class SSEListener:
    """Manages an SSE connection in a background thread with event collection."""

    def __init__(self, url: str, api_key: str, timeout: int = 30, headers: dict | None = None):
        self.url = url
        self.api_key = api_key
        self.timeout = timeout
        self.headers = headers or {}
        self._collected: list[str] = []
        self._stop = threading.Event()
        self._connected = threading.Event()
        self._thread = threading.Thread(target=self._listen, daemon=True)

    def start(self):
        self._thread.start()
        wait_on(lambda: True if self._connected.is_set() else None, "SSE connection to establish", timeout=10)

    def stop(self):
        self._stop.set()
        self._thread.join(timeout=5)

    def wait_for_event(self, event_type: str, timeout: int = 15) -> list[dict]:
        """Poll collected SSE data until at least one event of the given type appears."""

        def _check():
            events = self._find_events(event_type)
            return events if events else None

        return wait_on(_check, f"SSE {event_type} event", timeout=timeout)

    def get_events(self, event_type: str | None = None) -> list[dict]:
        """Return all collected events, optionally filtered by type."""
        all_events = parse_sse_events("".join(self._collected))
        if event_type is None:
            return all_events
        return [e for e in all_events if e.get("event") == event_type]

    def _find_events(self, event_type: str) -> list[dict] | None:
        events = self.get_events(event_type)
        return events if events else None

    def _listen(self):
        try:
            resp = requests.get(
                self.url,
                params={"key": self.api_key},
                headers=self.headers,
                stream=True,
                timeout=self.timeout,
            )
            self._connected.set()
            for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
                if chunk:
                    self._collected.append(chunk)
                if self._stop.is_set():
                    break
            resp.close()
        except Exception:
            self._connected.set()  # unblock waiters even on failure


class TestHistorySSEIntegration(IntegrationTestCase):
    dataset_populator: DatasetPopulator
    framework_tool_and_types = True

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["enable_celery_tasks"] = False
        config["enable_sse_history_updates"] = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def _events_stream_url(self):
        return urljoin(self.url, "api/events/stream")

    def _create_history(self, name=None):
        """Create a new history and return its encoded ID."""
        name = name or f"test_history_{uuid4()}"
        response = self._post("histories", data={"name": name}, json=True)
        self._assert_status_code_is_ok(response)
        return response.json()["id"]

    def test_sse_events_endpoint_returns_event_stream(self):
        """The /api/events/stream endpoint should return content-type text/event-stream."""
        response = requests.get(
            self._events_stream_url(),
            params={"key": self.galaxy_interactor.api_key},
            stream=True,
            timeout=5,
        )
        assert response.status_code == 200
        assert "text/event-stream" in response.headers.get("content-type", "")
        response.close()

    def test_sse_receives_history_update_on_dataset_upload(self):
        """When a dataset is uploaded, a history_update SSE event should be received."""
        history_id = self._create_history()

        listener = SSEListener(self._events_stream_url(), self.galaxy_interactor.api_key)
        listener.start()
        try:
            self.dataset_populator.new_dataset(history_id, wait=False)
            history_events = listener.wait_for_event("history_update")
            assert len(history_events) > 0
        finally:
            listener.stop()

    def test_history_update_contains_current_history_id(self):
        """The history_update event should contain the history's encoded ID."""
        history_id = self._create_history()

        listener = SSEListener(self._events_stream_url(), self.galaxy_interactor.api_key)
        listener.start()
        try:
            self.dataset_populator.new_dataset(history_id, wait=False)
            history_events = listener.wait_for_event("history_update")
            found = any(
                history_id in json.loads(e["data"]).get("history_ids", []) for e in history_events
            )
            assert found, f"Expected history_id '{history_id}' in history_update events, got: {history_events}"
        finally:
            listener.stop()

    def test_no_history_update_for_other_users(self):
        """User A should not receive history_update events for user B's history."""
        user_b = self._setup_user(f"{uuid4()}@galaxy.test")
        _, user_b_api_key = self._setup_user_get_key(user_b["email"])

        listener = SSEListener(self._events_stream_url(), self.galaxy_interactor.api_key)
        listener.start()
        try:
            # Create a history for user B and upload to it
            create_resp = requests.post(
                urljoin(self.url, "api/histories"),
                params={"key": user_b_api_key},
                json={"name": "User B History"},
            )
            assert create_resp.status_code == 200
            user_b_history_id = create_resp.json()["id"]

            requests.post(
                urljoin(self.url, f"api/histories/{user_b_history_id}/contents"),
                params={"key": user_b_api_key},
                json={"from_hda_id": None, "source": "pasted", "content": "test content"},
            )

            # Give time for any erroneous event to propagate
            time.sleep(5)
        finally:
            listener.stop()

        for event in listener.get_events("history_update"):
            data = json.loads(event["data"])
            assert user_b_history_id not in data.get("history_ids", []), (
                f"User A received history_update for user B's history: {event}"
            )

    def test_existing_polling_api_still_works(self):
        """The existing current_history_json endpoint should continue to work."""
        url = urljoin(self.url, "history/current_history_json")
        response = requests.get(
            url,
            params={"key": self.galaxy_interactor.api_key},
        )
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert "update_time" in data
