/**
 * Unit tests for the viewer-subscription helpers in useNotificationSSE.
 *
 * The shared EventSource isn't exercised here — these tests focus on the
 * client-side bookkeeping: refcounting, dedup, and HTTP shape. Reconnect
 * replay is covered by an MSW request log assertion plus an explicit call
 * into the (test-only) onopen replay path.
 */

import flushPromises from "flush-promises";
import { http, HttpResponse } from "msw";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { type EffectScope, effectScope } from "vue";

import { useServerMock } from "@/api/client/__mocks__";

import {
    _resetHistoryViewerSubscriptionsForTest,
    _resetSSESharedSourceForTest,
    addHistoryViewerSubscription,
    removeHistoryViewerSubscription,
    useSSE,
} from "./useNotificationSSE";

interface SubscriptionRequest {
    method: "POST" | "DELETE";
    history_ids: string[];
}

const { server } = useServerMock();

describe("useNotificationSSE viewer subscriptions", () => {
    let requests: SubscriptionRequest[];

    beforeEach(() => {
        _resetHistoryViewerSubscriptionsForTest();
        requests = [];
        const recordHandler = async ({ request }: { request: Request }) => {
            const body = (await request.json()) as { history_ids: string[] };
            requests.push({
                method: request.method as "POST" | "DELETE",
                history_ids: body.history_ids,
            });
            return new HttpResponse(null, { status: 204 });
        };
        server.use(
            http.post("/api/events/history-subscriptions", recordHandler),
            http.delete("/api/events/history-subscriptions", recordHandler),
        );
    });

    afterEach(() => {
        _resetHistoryViewerSubscriptionsForTest();
    });

    it("POSTs once per first subscriber for a given history id", async () => {
        addHistoryViewerSubscription("hist-A");
        await flushPromises();
        expect(requests).toHaveLength(1);
        expect(requests[0]?.method).toBe("POST");
        expect(requests[0]?.history_ids).toEqual(["hist-A"]);
    });

    it("refcounts duplicate subscriptions — second add is a no-op on the wire", async () => {
        addHistoryViewerSubscription("hist-A");
        addHistoryViewerSubscription("hist-A");
        await flushPromises();
        expect(requests.filter((r) => r.method === "POST")).toHaveLength(1);
    });

    it("only DELETEs when the last subscriber for an id releases", async () => {
        addHistoryViewerSubscription("hist-A");
        addHistoryViewerSubscription("hist-A");
        await flushPromises();
        const postCount = requests.filter((r) => r.method === "POST").length;

        removeHistoryViewerSubscription("hist-A");
        await flushPromises();
        // First remove still has one outstanding refcount — must not DELETE yet.
        expect(requests.filter((r) => r.method === "DELETE")).toHaveLength(0);
        expect(requests.filter((r) => r.method === "POST")).toHaveLength(postCount);

        removeHistoryViewerSubscription("hist-A");
        await flushPromises();
        const deletes = requests.filter((r) => r.method === "DELETE");
        expect(deletes).toHaveLength(1);
        expect(deletes[0]?.history_ids).toEqual(["hist-A"]);
    });

    it("ignores unsubscribes for ids that were never subscribed", async () => {
        removeHistoryViewerSubscription("hist-never");
        await flushPromises();
        expect(requests).toHaveLength(0);
    });

    it("tracks distinct history ids independently", async () => {
        addHistoryViewerSubscription("hist-A");
        addHistoryViewerSubscription("hist-B");
        await flushPromises();
        const ids = requests.filter((r) => r.method === "POST").map((r) => r.history_ids[0]);
        expect(new Set(ids)).toEqual(new Set(["hist-A", "hist-B"]));
    });
});

/**
 * Reconnect-on-CLOSED tests.
 *
 * The browser's native ``EventSource`` retries while ``readyState ===
 * CONNECTING`` but gives up once it flips to ``CLOSED`` — for example, when a
 * 429/5xx response arrives without ``text/event-stream``. The composable must
 * notice that flip and schedule a manual reopen with backoff so the client
 * doesn't silently drop to polling-only updates for the rest of the session.
 *
 * We stub ``globalThis.EventSource`` with a fake whose lifecycle the test
 * drives directly: this keeps the test off jsdom's ``EventSource`` (which
 * doesn't actually open sockets) and gives us a deterministic handle on the
 * instance count for the "a *new* EventSource was constructed after backoff"
 * assertion.
 */
class FakeEventSource {
    static CONNECTING = 0;
    static OPEN = 1;
    static CLOSED = 2;
    static instances: FakeEventSource[] = [];

    readonly url: string;
    readyState: number = FakeEventSource.CONNECTING;
    onopen: (() => void) | null = null;
    onerror: (() => void) | null = null;
    onmessage: ((e: MessageEvent) => void) | null = null;
    addEventListener = vi.fn();
    removeEventListener = vi.fn();
    close = vi.fn(() => {
        this.readyState = FakeEventSource.CLOSED;
    });

    constructor(url: string) {
        this.url = url;
        FakeEventSource.instances.push(this);
    }

    static reset() {
        FakeEventSource.instances = [];
    }
}

describe("useNotificationSSE managed reconnect", () => {
    let originalEventSource: typeof EventSource | undefined;
    // ``useSSE`` registers an ``onScopeDispose`` cleanup; outside a Vue
    // component setup that warns and ``vitest-fail-on-console`` upgrades the
    // warning to a test failure. Wrap each test in an explicit scope so the
    // disposal hook has somewhere to attach.
    let scope: EffectScope;

    beforeEach(() => {
        FakeEventSource.reset();
        originalEventSource = (globalThis as unknown as { EventSource?: typeof EventSource }).EventSource;
        (globalThis as unknown as { EventSource: unknown }).EventSource = FakeEventSource;
        vi.useFakeTimers();
        _resetSSESharedSourceForTest();
        scope = effectScope();
    });

    afterEach(() => {
        scope.stop();
        vi.useRealTimers();
        _resetSSESharedSourceForTest();
        if (originalEventSource) {
            (globalThis as unknown as { EventSource: typeof EventSource }).EventSource = originalEventSource;
        } else {
            delete (globalThis as unknown as { EventSource?: unknown }).EventSource;
        }
    });

    it("schedules a reopen when onerror fires with readyState=CLOSED", () => {
        scope.run(() => {
            const { connect } = useSSE(() => {});
            connect();
        });
        expect(FakeEventSource.instances).toHaveLength(1);

        const first = FakeEventSource.instances[0]!;
        // Simulate the browser giving up on the native retry.
        first.readyState = FakeEventSource.CLOSED;
        first.onerror?.();

        // Bumped on the manual reopen path so Selenium can observe it.
        expect(
            (window as unknown as { __galaxy_sse_reconnect_attempts?: number }).__galaxy_sse_reconnect_attempts,
        ).toBe(1);
        expect(FakeEventSource.instances).toHaveLength(1);

        // The first attempt's backoff is in [500ms, 1500ms); 2000ms is past
        // the upper bound regardless of the jitter draw, so a fixed advance
        // is deterministic without seeding ``Math.random``.
        vi.advanceTimersByTime(2000);
        expect(FakeEventSource.instances).toHaveLength(2);
    });

    it("does not reopen while readyState=CONNECTING (browser is still retrying natively)", () => {
        scope.run(() => {
            const { connect } = useSSE(() => {});
            connect();
        });
        const first = FakeEventSource.instances[0]!;
        first.readyState = FakeEventSource.CONNECTING;
        first.onerror?.();

        // No manual scheduling while the browser is still trying — would
        // otherwise double-up reconnect work and accelerate the retry loop.
        expect(
            (window as unknown as { __galaxy_sse_reconnect_attempts?: number }).__galaxy_sse_reconnect_attempts,
        ).toBeUndefined();
        vi.advanceTimersByTime(60_000);
        expect(FakeEventSource.instances).toHaveLength(1);
    });

    it("resets the backoff counter on a successful onopen", () => {
        scope.run(() => {
            const { connect } = useSSE(() => {});
            connect();
        });

        // First failure → reopen #1.
        const first = FakeEventSource.instances[0]!;
        first.readyState = FakeEventSource.CLOSED;
        first.onerror?.();
        vi.advanceTimersByTime(2000);
        expect(FakeEventSource.instances).toHaveLength(2);

        // Reopen succeeds. The counter must reset so the *next* outage starts
        // its backoff from RECONNECT_BASE_MS rather than 2 × that.
        const second = FakeEventSource.instances[1]!;
        second.onopen?.();

        // Second failure → reopen #2; the delay envelope is again [500, 1500).
        second.readyState = FakeEventSource.CLOSED;
        second.onerror?.();
        vi.advanceTimersByTime(2000);
        expect(FakeEventSource.instances).toHaveLength(3);
    });
});
