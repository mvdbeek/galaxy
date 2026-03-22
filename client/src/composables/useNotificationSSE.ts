import { onScopeDispose, ref } from "vue";

import { withPrefix } from "@/utils/redirect";

/**
 * Composable for connecting to the SSE notification stream.
 *
 * The browser's EventSource handles reconnection automatically and
 * sends the Last-Event-ID header so the server can catch up on missed events.
 */
export function useNotificationSSE(onEvent: (event: MessageEvent) => void) {
    const connected = ref(false);
    let eventSource: EventSource | null = null;
    let consecutiveErrors = 0;

    const SSE_EVENT_TYPES = ["notification_update", "broadcast_update", "notification_status"] as const;

    function connect() {
        disconnect();
        consecutiveErrors = 0;
        const url = withPrefix("/api/notifications/stream");
        eventSource = new EventSource(url);

        for (const eventType of SSE_EVENT_TYPES) {
            eventSource.addEventListener(eventType, onEvent);
        }

        eventSource.onopen = () => {
            connected.value = true;
            consecutiveErrors = 0;
        };

        eventSource.onerror = () => {
            connected.value = false;
            consecutiveErrors++;
            // EventSource auto-reconnects, but if we get too many errors
            // in a row, the server likely doesn't support SSE — give up
            // and let the caller fall back to polling.
            if (consecutiveErrors > 5) {
                disconnect();
            }
        };
    }

    function disconnect() {
        if (eventSource) {
            for (const eventType of SSE_EVENT_TYPES) {
                eventSource.removeEventListener(eventType, onEvent);
            }
            eventSource.close();
            eventSource = null;
        }
        connected.value = false;
    }

    onScopeDispose(() => {
        disconnect();
    });

    return { connect, disconnect, connected };
}
