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
import dist from "vue-virtual-scroll-list";


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

        const inputs$ = combineLatest(id$, param$).pipe(
            debounceTime(0),
            distinctUntilChanged(inputsSame),
            debounceTime(this.debouncePeriod),
            share()
        );

        if (this.isWatchingCache) {
            this.watchCache(id$, param$);
        }

        if (this.isManualLoading) {
            this.watchManualRequest(id$, param$);
        }

        if (this.isPolling) {
            this.startPolling(inputs$);
        }
    },
    methods: {

        // Cache Observer: Subscribe to an observable that looks at the cache
        // filtered by the params. Updates when cache updated, pass values to
        // results property.

        watchCache(id$, param$) {

            const cache$ = id$.pipe(
                switchMap(id => {
                    return param$.pipe(

                        // cache watcher does not care about pagination, since
                        // the results are for the entire cached set, but that
                        // may change if the performance lags for big lists
                        map(p => p.resetPagination()),

                        distinctUntilChanged(SearchParams.equals),
                        debounceTime(this.debouncePeriod),
                        tap(params => params.report(`[cachewatch] inputs... history: ${id}`)),
                        map(params => buildContentPouchRequest([id, params])),
                        switchMap(monitorContentQuery)
                    )
                })
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

        watchManualRequest(id$, param$) {

            // switchmap on id, mergemap on params
            const load$ = id$.pipe(
                switchMap(historyId => {
                    return param$.pipe(
                        debounceTime(this.debouncePeriod),
                        tap(params => params.report("[loader] SENDING...")),
                        mergeMap(params => {
                            return loadHistoryContents([historyId, params])
                        })
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
