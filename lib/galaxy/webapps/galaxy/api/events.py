"""
API endpoint for Server-Sent Events (SSE) stream.

Provides a unified event stream for all real-time push events (notifications,
history updates, etc.) independent of the notification system configuration.
"""

import asyncio
import logging
from datetime import datetime
from typing import Optional

from fastapi import (
    Header,
    Request,
)
from starlette.responses import StreamingResponse

from galaxy.managers.context import ProvidesUserContext
from galaxy.managers.sse import SSEEvent
from galaxy.structured_app import StructuredApp
from . import (
    DependsOnApp,
    DependsOnTrans,
    Router,
)

log = logging.getLogger(__name__)

router = Router(tags=["events"])


@router.cbv
class FastAPIEvents:
    app: StructuredApp = DependsOnApp

    @router.get(
        "/api/events/stream",
        summary="Server-Sent Events stream for real-time updates.",
        response_class=StreamingResponse,
    )
    async def stream_events(
        self,
        request: Request,
        trans: ProvidesUserContext = DependsOnTrans,
        last_event_id: Optional[str] = Header(None, alias="Last-Event-ID"),
    ):
        """Opens a Server-Sent Events (SSE) connection that pushes real-time
        updates for notifications, history changes, and other events.

        On reconnect, the browser sends the ``Last-Event-ID`` header automatically.
        If the notification system is enabled, any notifications created since that
        timestamp are delivered as a catch-up ``notification_status`` event.

        Anonymous users receive only broadcast events.
        """
        user_id = trans.user.id if not trans.anonymous else None
        sse_manager = self.app.sse_connection_manager
        queue = sse_manager.connect(user_id)

        # On reconnect, send catch-up notification status if notification system is enabled
        if last_event_id and getattr(self.app.config, "enable_notification_system", False):
            try:
                from galaxy.webapps.galaxy.services.notifications import (
                    NotificationService,
                )

                notification_service = self.app[NotificationService]
                since = datetime.fromisoformat(last_event_id)
                catchup = notification_service.get_notifications_status(trans, since)
                await queue.put(
                    SSEEvent(
                        event="notification_status",
                        data=catchup.model_dump_json(),
                        id=datetime.utcnow().isoformat(),
                    )
                )
            except (ValueError, TypeError):
                pass  # Invalid Last-Event-ID, skip catch-up
            except Exception:
                log.debug("Failed to send notification catch-up", exc_info=True)

        async def event_generator():
            try:
                while True:
                    if await request.is_disconnected():
                        break
                    try:
                        event: SSEEvent = await asyncio.wait_for(queue.get(), timeout=30.0)
                        yield f"event: {event.event}\ndata: {event.data}\n"
                        if event.id:
                            yield f"id: {event.id}\n"
                        yield "\n"
                    except asyncio.TimeoutError:
                        # Send keepalive comment to prevent proxy/client timeout
                        yield ": keepalive\n\n"
            finally:
                sse_manager.disconnect(user_id, queue)

        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )
