/**
 * Generates content results for a set of params an an indicated history
 * Abstracts away the rxjs so developers don't need to mess with it if
 * they don't want to.
 */

import { combineLatest, NEVER } from "rxjs";
import { tap, map, distinctUntilChanged, switchMap, debounceTime } from "rxjs/operators";
import { SearchParams } from "../../model";
import { contentCacheWatcher } from "./contentCacheWatcher";
import { manualLoader } from "./manualLoader";
import { pollHistory } from "../../caching";
import { log } from "utils/observable";
import { vueRxShortcuts } from "../../../plugins/vueRxShortcuts";

// equivalence comparator for historyId + params
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
        inputDebouncePeriod: { type: Number, required: false, default: 250 },
    },
    data: () => ({
        results: [],
        isWatchingCache: true,
        isManualLoading: true,
        isPolling: true,
    }),
    computed: {
        loading() {
            // should I bother?
            // return this.cacheLoading || this.pollLoading || this.manualLoading;
            return false;
        },
        totalMatches() {
            return this.results ? this.results.length : [];
        },
    },
    created() {
        const noop = () => null;

        // #region debugging toggles, lets you flip the subscriptions on and off

        const isWatchingCache$ = this.watch$("isWatchingCache");
        const cacheFlagMessages$ = isWatchingCache$.pipe(log("cachewatch"));
        this.$subscribeTo(cacheFlagMessages$, noop);

        const isManualLoading$ = this.watch$("isManualLoading");
        const loadingFlagMessage$ = isManualLoading$.pipe(log("loading"));
        this.$subscribeTo(loadingFlagMessage$, noop);

        const isPolling$ = this.watch$("isPolling");
        const pollingFlagMessage$ = isPolling$.pipe(log("polling"));
        this.$subscribeTo(pollingFlagMessage$, noop);

        // #endregion

        // #region input observables

        const historyId$ = this.watch$("historyId").pipe(distinctUntilChanged());

        const param$ = this.watch$("params").pipe(distinctUntilChanged(SearchParams.equals));

        const inputs$ = combineLatest(historyId$, param$).pipe(
            debounceTime(this.inputDebouncePeriod),
            distinctUntilChanged(inputsSame),
            tap(inputs => {
                console.log("inputs changed", inputs);
            })
        );

        // polling and cache observation do not care about skip/limit,
        // remove those properties to avoid unnecessary events
        const paramWithoutLimits$ = param$.pipe(
            map((p) => p.resetLimits()),
            distinctUntilChanged(SearchParams.equals)
        );

        const inputsWithoutLimits$ = combineLatest(historyId$, paramWithoutLimits$).pipe(
            debounceTime(this.inputDebouncePeriod),
            distinctUntilChanged(inputsSame)
        );

        // #endregion

        // watches cache for changes, emits results. Returns all matches to the
        // passed parameters, emits on the results slotProp for the UI to render
        this.watchCache(inputsWithoutLimits$, isWatchingCache$);

        // watches changes to history id and params, requests new data from api
        // when necessary. That data gets dumped directly into the cache and will
        // show up in .watchCache() above eventually
        this.watchUserRequest(inputs$, isManualLoading$);

        // subscribes to polling observable. We don't actually do anything with
        // the results other than hold the subscription to the observable until
        // the cmoponent closes. The worker does all the requests and caching
        this.startPolling(inputsWithoutLimits$, isPolling$);
    },
    methods: {

        // Subscribe to an observable that looks at the cache filtered by the params.
        // Updates when cache updated, pass values to results property. Ignore the limits
        // on the search params. Just return everything in the db and the virtual scroller
        // will deal with only showing part of it.

        watchCache(src$, toggle$) {
            const cacheMessages$ = src$.pipe(
                contentCacheWatcher()
            );
            const cacheWatch$ = toggle$.pipe(
                switchMap((isOn) => (isOn ? cacheMessages$ : NEVER))
            );

            this.$subscribeTo(
                cacheWatch$,
                (update) => {
                    const { matches, loading, request } = update;
                    console.log("[cachewatch] result", matches.length, request, loading);
                    this.results = matches;
                },
                (err) => console.warn("[cachewatch] error", err),
                () => console.log("[cachewatch] stream completed")
            );
        },

        // Manual Loading: When user scrolls through the list, or changes
        // the filters, we may have to make an ajax call, this dispatches
        // the inputs to loadContents() which handles getting and caching
        // the new requested stuff

        watchUserRequest(src$, toggle$) {
            const loads$ = src$.pipe(manualLoader());
            const toggledLoads$ = toggle$.pipe(switchMap((isOn) => (isOn ? loads$ : NEVER)));

            this.$subscribeTo(
                toggledLoads$,
                (result) => console.log("[loader] next", result),
                (err) => console.warn("[loader] error", err),
                () => console.warn("[loader] complete: should only complete on unsub")
            );
        },

        // Polling Subscription
        // The app also polls for server-pushed updates to the cache data. This
        // subscribes to a process in the worker that periodicially polls an
        // endpoint corresponding to the history + params and dumps the results
        // in the local cache, eventually it will show up in the cacheMessages$

        startPolling(src$, toggle$) {
            const pollMessages$ = src$.pipe(switchMap(pollHistory));
            const pollWatch$ = toggle$.pipe(switchMap((isOn) => (isOn ? pollMessages$ : NEVER)));

            this.$subscribeTo(
                pollWatch$,
                (results) => console.log("[poll] result", results),
                (err) => console.warn("[poll] error", err),
                () => console.warn("[poll] complete: should only complete on unsub")
            );
        },

        updateManualLoading(val) {
            this.isManualLoading = val;
        },

        updatePolling(val) {
            this.isPolling = val;
        },
    },
    render() {
        return this.$scopedSlots.default({
            params: this.params,
            results: this.results,
            totalMatches: this.totalMatches,
            loading: this.loading,
            // debugging props
            isPolling: this.isPolling,
            isManualLoading: this.isManualLoading,
            updatePolling: this.updatePolling,
            updateManualLoading: this.updateManualLoading,
        });
    },
};
