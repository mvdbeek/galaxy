"""Integration tests for SSE-based history update notifications."""

import json
import threading
import time
from urllib.parse import urljoin
from uuid import uuid4

import requests

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


def _listen_sse(url, api_key, collected_data, stop_event, timeout=30):
    """Background thread helper to listen on an SSE stream."""
    try:
        resp = requests.get(
            url,
            params={"key": api_key},
            stream=True,
            timeout=timeout,
        )
        for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
            if chunk:
                collected_data.append(chunk)
            if stop_event.is_set():
                break
        resp.close()
    except Exception:
        pass


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

    def _create_history(self, name=None):
        """Create a new history and return its encoded ID."""
        name = name or f"test_history_{uuid4()}"
        response = self._post("histories", data={"name": name}, json=True)
        self._assert_status_code_is_ok(response)
        return response.json()["id"]

    def test_sse_events_endpoint_returns_event_stream(self):
        """The /api/events/stream endpoint should return content-type text/event-stream."""
        url = urljoin(self.url, "api/events/stream")
        response = requests.get(
            url,
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

        # Start SSE connection in a background thread
        url = urljoin(self.url, "api/events/stream")
        collected_data: list[str] = []
        stop_event = threading.Event()

        listener = threading.Thread(
            target=_listen_sse,
            args=(url, self.galaxy_interactor.api_key, collected_data, stop_event),
            daemon=True,
        )
        listener.start()

        # Give the SSE connection time to establish
        time.sleep(2)

        # Upload a dataset — this triggers HDA INSERT and thus history_audit update.
        # Don't wait for completion; the HDA creation itself is enough to trigger the event.
        self.dataset_populator.new_dataset(history_id, wait=False)

        # Wait for the SSE event to arrive (audit monitor polls every 2s)
        time.sleep(5)
        stop_event.set()
        listener.join(timeout=5)

        # Parse collected SSE data
        raw_sse = "".join(collected_data)
        events = parse_sse_events(raw_sse)

        # Find a history_update event
        history_events = [e for e in events if e.get("event") == "history_update"]
        assert len(history_events) > 0, f"Expected history_update events, got: {events}"

    def test_history_update_contains_current_history_id(self):
        """The history_update event should contain the history's encoded ID."""
        history_id = self._create_history()

        url = urljoin(self.url, "api/events/stream")
        collected_data: list[str] = []
        stop_event = threading.Event()

        listener = threading.Thread(
            target=_listen_sse,
            args=(url, self.galaxy_interactor.api_key, collected_data, stop_event),
            daemon=True,
        )
        listener.start()
        time.sleep(2)

        self.dataset_populator.new_dataset(history_id, wait=False)

        time.sleep(5)
        stop_event.set()
        listener.join(timeout=5)

        raw_sse = "".join(collected_data)
        events = parse_sse_events(raw_sse)

        history_events = [e for e in events if e.get("event") == "history_update"]
        assert len(history_events) > 0

        # Verify the event data contains the history ID
        found = False
        for event in history_events:
            data = json.loads(event["data"])
            if history_id in data.get("history_ids", []):
                found = True
                break
        assert found, f"Expected history_id '{history_id}' in history_update events, " f"got: {history_events}"

    def test_no_history_update_for_other_users(self):
        """User A should not receive history_update events for user B's history."""
        user_b = self._setup_user(f"{uuid4()}@galaxy.test")
        _, user_b_api_key = self._setup_user_get_key(user_b["email"])

        # User A listens on SSE
        url = urljoin(self.url, "api/events/stream")
        collected_data: list[str] = []
        stop_event = threading.Event()

        listener = threading.Thread(
            target=_listen_sse,
            args=(url, self.galaxy_interactor.api_key, collected_data, stop_event),
            daemon=True,
        )
        listener.start()
        time.sleep(2)

        # Create a history for user B and upload to it
        create_resp = requests.post(
            urljoin(self.url, "api/histories"),
            params={"key": user_b_api_key},
            json={"name": "User B History"},
        )
        assert create_resp.status_code == 200
        user_b_history_id = create_resp.json()["id"]

        # Upload to user B's history
        requests.post(
            urljoin(self.url, f"api/histories/{user_b_history_id}/contents"),
            params={"key": user_b_api_key},
            json={"from_hda_id": None, "source": "pasted", "content": "test content"},
        )

        time.sleep(5)
        stop_event.set()
        listener.join(timeout=5)

        raw_sse = "".join(collected_data)
        events = parse_sse_events(raw_sse)

        # User A should NOT see user B's history in their events
        for event in events:
            if event.get("event") == "history_update":
                data = json.loads(event["data"])
                assert user_b_history_id not in data.get(
                    "history_ids", []
                ), f"User A received history_update for user B's history: {event}"

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
