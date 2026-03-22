"""Integration tests for the notification SSE (Server-Sent Events) endpoint."""

import threading
import time
from datetime import datetime
from typing import Optional
from urllib.parse import urljoin
from uuid import uuid4

import requests

from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver.integration_util import IntegrationTestCase


def notification_test_data(
    subject: Optional[str] = None, message: Optional[str] = None
):
    return {
        "source": "integration_tests",
        "variant": "info",
        "category": "message",
        "content": {
            "category": "message",
            "subject": subject or "Testing Subject",
            "message": message or "Testing Message",
        },
    }


def notification_broadcast_test_data(
    subject: Optional[str] = None, message: Optional[str] = None
):
    return {
        "source": "integration_tests",
        "variant": "info",
        "category": "broadcast",
        "content": {
            "category": "broadcast",
            "subject": subject or "Testing Broadcast Subject",
            "message": message or "Testing Broadcast Message",
        },
    }


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


class TestNotificationSSEIntegration(IntegrationTestCase):
    dataset_populator: DatasetPopulator
    framework_tool_and_types = False

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["enable_celery_tasks"] = False
        config["enable_notification_system"] = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def test_sse_endpoint_returns_event_stream(self):
        """The SSE endpoint should return content-type text/event-stream."""
        url = urljoin(self.url, "api/notifications/stream")
        response = requests.get(
            url,
            params={"key": self.galaxy_interactor.api_key},
            stream=True,
            timeout=5,
        )
        assert response.status_code == 200
        assert "text/event-stream" in response.headers.get("content-type", "")
        response.close()

    def test_sse_receives_notification_events(self):
        """When a notification is created, the SSE stream should receive it."""
        user = self._setup_user(f"{uuid4()}@galaxy.test")
        _, user_api_key = self._setup_user_get_key(user["email"])

        # Start SSE connection in a background thread
        url = urljoin(self.url, "api/notifications/stream")
        collected_data: list[str] = []
        stop_event = threading.Event()

        def listen_sse():
            try:
                resp = requests.get(
                    url,
                    params={"key": user_api_key},
                    stream=True,
                    timeout=30,
                )
                for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
                    if chunk:
                        collected_data.append(chunk)
                    if stop_event.is_set():
                        break
                resp.close()
            except Exception:
                pass

        listener = threading.Thread(target=listen_sse, daemon=True)
        listener.start()

        # Give the SSE connection time to establish
        time.sleep(1)

        # Send a notification to the user
        subject = f"sse_test_{uuid4()}"
        request = {
            "recipients": {"user_ids": [user["id"]]},
            "notification": notification_test_data(
                subject=subject, message="SSE test notification"
            ),
        }
        response = self._post("notifications", data=request, admin=True, json=True)
        self._assert_status_code_is_ok(response)

        # Wait for the SSE event to arrive
        time.sleep(2)
        stop_event.set()
        listener.join(timeout=5)

        # Parse collected SSE data
        raw_sse = "".join(collected_data)
        events = parse_sse_events(raw_sse)

        # Find a notification_update event containing our subject
        notification_events = [
            e for e in events if e.get("event") == "notification_update"
        ]
        assert len(notification_events) > 0, (
            f"Expected notification_update events, got: {events}"
        )
        assert any(subject in e.get("data", "") for e in notification_events), (
            f"Expected subject '{subject}' in SSE events, got: {notification_events}"
        )

    def test_sse_receives_broadcast_events(self):
        """When a broadcast is created, the SSE stream should receive it."""
        # Start SSE connection (as regular user)
        url = urljoin(self.url, "api/notifications/stream")
        collected_data: list[str] = []
        stop_event = threading.Event()

        def listen_sse():
            try:
                resp = requests.get(
                    url,
                    params={"key": self.galaxy_interactor.api_key},
                    stream=True,
                    timeout=30,
                )
                for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
                    if chunk:
                        collected_data.append(chunk)
                    if stop_event.is_set():
                        break
                resp.close()
            except Exception:
                pass

        listener = threading.Thread(target=listen_sse, daemon=True)
        listener.start()
        time.sleep(1)

        # Send a broadcast notification
        subject = f"broadcast_sse_test_{uuid4()}"
        payload = notification_broadcast_test_data(subject=subject)
        response = self._post(
            "notifications/broadcast", data=payload, admin=True, json=True
        )
        self._assert_status_code_is_ok(response)

        time.sleep(2)
        stop_event.set()
        listener.join(timeout=5)

        raw_sse = "".join(collected_data)
        events = parse_sse_events(raw_sse)

        broadcast_events = [e for e in events if e.get("event") == "broadcast_update"]
        assert len(broadcast_events) > 0, (
            f"Expected broadcast_update events, got: {events}"
        )
        assert any(subject in e.get("data", "") for e in broadcast_events), (
            f"Expected subject '{subject}' in broadcast SSE events, got: {broadcast_events}"
        )

    def test_sse_catchup_on_reconnect(self):
        """When reconnecting with Last-Event-ID, the stream should send catch-up data."""
        user = self._setup_user(f"{uuid4()}@galaxy.test")
        _, user_api_key = self._setup_user_get_key(user["email"])

        before = datetime.utcnow()

        # Create a notification while NOT connected to SSE
        subject = f"catchup_test_{uuid4()}"
        request = {
            "recipients": {"user_ids": [user["id"]]},
            "notification": notification_test_data(
                subject=subject, message="Catch-up test"
            ),
        }
        response = self._post("notifications", data=request, admin=True, json=True)
        self._assert_status_code_is_ok(response)

        # Now connect with Last-Event-ID set to before the notification was created
        url = urljoin(self.url, "api/notifications/stream")
        collected_data: list[str] = []
        stop_event = threading.Event()

        def listen_sse():
            try:
                resp = requests.get(
                    url,
                    params={"key": user_api_key},
                    headers={"Last-Event-ID": before.isoformat()},
                    stream=True,
                    timeout=10,
                )
                for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
                    if chunk:
                        collected_data.append(chunk)
                    if stop_event.is_set():
                        break
                resp.close()
            except Exception:
                pass

        listener = threading.Thread(target=listen_sse, daemon=True)
        listener.start()
        time.sleep(2)
        stop_event.set()
        listener.join(timeout=5)

        raw_sse = "".join(collected_data)
        events = parse_sse_events(raw_sse)

        # Should have received a notification_status catch-up event
        status_events = [e for e in events if e.get("event") == "notification_status"]
        assert len(status_events) > 0, (
            f"Expected notification_status catch-up event, got: {events}"
        )
        assert any(subject in e.get("data", "") for e in status_events), (
            f"Expected subject '{subject}' in catch-up event, got: {status_events}"
        )

    def test_existing_polling_api_still_works(self):
        """The existing polling endpoint should continue to work alongside SSE."""
        user = self._setup_user(f"{uuid4()}@galaxy.test")

        before = datetime.utcnow()

        subject = f"polling_test_{uuid4()}"
        request = {
            "recipients": {"user_ids": [user["id"]]},
            "notification": notification_test_data(subject=subject),
        }
        response = self._post("notifications", data=request, admin=True, json=True)
        self._assert_status_code_is_ok(response)

        with self._different_user(user["email"]):
            status_response = self._get(
                f"notifications/status?since={before.isoformat()}"
            )
            self._assert_status_code_is_ok(status_response)
            status = status_response.json()
            assert status["total_unread_count"] == 1
            assert len(status["notifications"]) == 1
            assert status["notifications"][0]["content"]["subject"] == subject
