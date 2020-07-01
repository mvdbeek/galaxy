/**
 * Generates content results for a set of params an an indicated history
 * Abstracts away the rxjs so developers don't need to mess with it if
 * they don't want to.
 */

import { combineLatest } from "rxjs";
import { tap, map, distinctUntilChanged, switchMap, mergeMap, debounceTime, share } from "rxjs/operators";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";
import { SearchParams } from "../model/SearchParams";
import { pollHistory, monitorContentQuery, loadHistoryContents } from "../caching/index";
import { buildContentPouchRequest } from "../caching/pouchQueries";
import { v4 as uuidv4 } from 'uuid';

// equivalence comparator for id + params
const inputsSame = (a, b) => {
    const idSame = a[0] == b[0];
    const paramSame = SearchParams.equals(a[1], b[1]);
    return idSame && paramSame;
};


export default {
    mixins: [vueRxShortcuts],
    props: {
        historyId: { type: String, required: true },
        params: { type: SearchParams, required: true },
        debounceDelay: { type: Number, required: false, default: 100 },
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

        const params$ = this.watch$("params");

        const inputs$ = combineLatest(id$, params$).pipe(
            debounceTime(0),
            distinctUntilChanged(inputsSame),
            debounceTime(this.debounceDelay),
            share()
        );

        if (this.isWatchingCache) {
            this.watchCache(inputs$);
        }

        if (this.isManualLoading) {
            this.watchManualRequest(id$, params$);
        }

        if (this.isPolling) {
            this.startPolling(inputs$);
        }
    },
    methods: {

        // Cache Observer: Subscribe to an observable that looks at the cache
        // filtered by the params. Updates when cache updated, pass values to
        // results property.

        watchCache(inputs$) {
            const cache$ = inputs$.pipe(
                tap(inputs => console.warn("[cachewatch] inputs changed", inputs)),
                map(buildContentPouchRequest),
                switchMap(selector => {
                    console.log("SWITCHMAP", selector);
                    return monitorContentQuery(selector)
                }),
            );
            this.$subscribeTo(
                cache$,
                (results) => {
                    console.log("[cachewatch] results", results.length);
                    this.results = results
                },
                (err) => console.warn("[cachewatch] error", err),
                () => console.log("[cachewatch] stream complete")
            );
        },

        // Manual Loading: When user scrolls through the list, or changes the
        // filters, we may have to make an ajax call, this dispatches the inputs
        // to loadContents() which handles getting and caching the new request

        watchManualRequest(id$, params$) {

            // switchmap on id, mergemap on params
            const load$ = id$.pipe(
                switchMap(id => {
                    const channelKey = uuidv4();
                    return params$.pipe(
                        tap(params => console.warn("[loader] inputs changed", id, params)),
                        mergeMap(params => loadHistoryContents(channelKey, [id, params]))
                    )
                })
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

        startPolling(inputs$) {
            const poll$ = inputs$.pipe(
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
