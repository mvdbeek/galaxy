/**
 * Generates content results for a set of params an an indicated history
 * Abstracts away the rxjs so developers don't need to mess with it if
 * they don't want to.
 */

import { combineLatest } from "rxjs";
import { tap, map, distinctUntilChanged, switchMap, debounceTime } from "rxjs/operators";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";
import { SearchParams } from "../model/SearchParams";
import { pollHistory, monitorContentQuery, loadHistoryContents } from "../caching/index";
import { buildContentPouchRequest } from "../caching/pouchQueries";
import { inputsSame } from "./inputsSame";


export default {
    mixins: [vueRxShortcuts],
    props: {
        historyId: { type: String, required: true },
        params: { type: SearchParams, required: true },
        debouncePeriod: { type: Number, required: false, default: 250 },
    },
    data: () => ({
        results: [],
        isWatchingCache: true,
        isManualLoading: true,
        isPolling: false,
    }),
    computed: {
        loading() {
            // should I bother?
            // return this.cacheLoading || this.pollLoading || this.manualLoading;
            return false;
        },
        totalMatches() {
            return this.results.length;
        },
    },
    created() {
        const id$ = this.watch$("historyId");
        const param$ = this.watch$("params");

        if (this.isWatchingCache) {
            this.watchCache(id$, param$);
        }
        if (this.isManualLoading) {
            this.watchManualRequest(id$, param$);
        }
        if (this.isPolling) {
            this.startPolling(id$, param$);
        }
    },
    methods: {

        // Cache Observer: Subscribe to an observable that looks at the cache
        // filtered by the params. Updates when cache updated, pass values to
        // results property.

        watchCache(id$, param$) {

            // cache watcher does not care about skip/limit
            const limitlessParam$ = param$.pipe(
                tap(p => p.report("[cachewatch] start")),
                map(p => p.resetPagination()),
                tap(p => p.report("[cachewatch] reset pagination")),
            );

            const cache$ = combineLatest(id$, limitlessParam$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(inputsSame),
                map(buildContentPouchRequest),
                switchMap(monitorContentQuery)
            );

            this.$subscribeTo(
                cache$,
                ({ matches }) => {
                    console.log("[cachewatch] results", matches.length);
                    this.results = matches
                },
                (err) => console.warn("[cachewatch] error", err),
                () => console.log("[cachewatch] stream complete")
            );
        },

        // Manual Loading: When user scrolls through the list, or changes the
        // filters, we may have to make an ajax call, this dispatches the inputs
        // to loadContents() which handles getting and caching the new request

        watchManualRequest(id$, param$) {

            // need to pad the range before we give it to the loader so we
            // load a little more than we're looking at right now
            const paddedParams$ = param$.pipe(
                tap(p => p.report("[loader] start")),
                map(p => p.pad()),
                tap(p => p.report("[loader] padded pagination")),
            );

            const load$ = combineLatest(id$, paddedParams$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(inputsSame),
                switchMap(loadHistoryContents),
            );

            this.$subscribeTo(
                load$,
                (result) => console.log("[loader] result", result),
                (err) => console.warn("[loader] error", err),
                () => console.warn("[loader] complete: should only complete on unsub")
            );
        },

        // Polling Subscription: The app polls for server-generated updates.
        // This subscribes to a process in the worker that periodicially polls
        // an endpoint corresponding to the history + params and dumps the
        // results in the local cache

        startPolling(id$, param$) {

            const poll$ = combineLatest(id$, param$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(inputsSame),
                tap(inputs => console.warn("[poll] inputs changed", inputs)),
                switchMap(pollHistory)
            );

            this.$subscribeTo(
                poll$,
                (results) => console.log("[poll] result", results),
                (err) => console.warn("[poll] error", err),
                () => console.warn("[poll] complete: should only complete on unsub")
            );
        },

    },
    render() {
        return this.$scopedSlots.default({
            params: this.params,
            results: this.results,
            totalMatches: this.totalMatches,
            loading: this.loading,
        });
    },
};
