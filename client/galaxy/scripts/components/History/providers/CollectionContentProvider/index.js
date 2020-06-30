/**
 * Generates content results for a set of params an an indicated history
 * Abstracts away the rxjs so developers don't need to mess with it if
 * they don't want to.
 */

import { combineLatest, NEVER } from "rxjs";
import { distinctUntilChanged, switchMap, debounceTime, pluck } from "rxjs/operators";
import { SearchParams } from "../../model";
import { log } from "utils/observable";
import { vueRxShortcuts } from "../../../plugins/vueRxShortcuts";
import { loadDscContent, monitorDscQuery } from "../../caching";
import { buildCollectionContentRequest } from "../../caching/pouchQueries";


// equivalence comparator for historyId + params
const inputsSame = (a, b) => {
    const idSame = a[0] == b[0];
    const paramSame = SearchParams.equals(a[1], b[1]);
    return idSame && paramSame;
};


export default {
    mixins: [vueRxShortcuts],
    props: {
        collection: { type: Object, required: true },
        params: { type: SearchParams, required: true },
        inputDebouncePeriod: { type: Number, required: false, default: 250 },
    },
    data: () => ({
        results: [],
        isWatchingCache: true,
        isManualLoading: true,
    }),
    computed: {
        loading() {
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

        // #endregion

        // #region input observables

        const url$ = this.watch$("collection", true).pipe(
            distinctUntilChanged(),
            pluck('contents_url'),
        );

        const param$ = this.watch$("params", true).pipe(
            distinctUntilChanged(SearchParams.equals)
        );
        const inputs$ = combineLatest(url$, param$).pipe(
            debounceTime(this.inputDebouncePeriod),
            distinctUntilChanged(inputsSame),
        );

        // #endregion

        // watches cache for changes, emits results. Returns all matches to the
        // passed parameters, emits on the results slotProp for the UI to render
        this.watchCache(inputs$, isWatchingCache$);

        // watches changes to history id and params, requests new data from api
        // when necessary. That data gets dumped directly into the cache and will
        // show up in .watchCache() above eventually
        this.watchUserRequest(inputs$, isManualLoading$);
    },
    methods: {
        // Subscribe to an observable that looks at the cache filtered by the params.
        // Updates when cache updated, pass values to results property. Ignore the limits
        // on the search params. Just return everything in the db and the virtual scroller
        // will deal with only showing part of it.

        watchCache(src$, toggle$) {

            const cacheMessages$ = src$.pipe(
                switchMap(([ contents_url, params ]) => {
                    const pouchRequest = buildCollectionContentRequest(contents_url, params);
                    return monitorDscQuery(pouchRequest);
                }),
            );

            const cacheWatch$ = toggle$.pipe(
                switchMap((isOn) => (isOn ? cacheMessages$ : NEVER))
            );

            this.$subscribeTo(
                cacheWatch$,
                (update) => {
                    const { matches, loading, request } = update;
                    console.log("[dscpanel cachewatch] result", matches.length, request, loading);
                    this.results = Object.freeze(matches);
                },
                (err) => console.warn("[dscpanel cachewatch] error", err),
                () => console.log("[dscpanel cachewatch] stream completed")
            );
        },

        // Manual Loading: When user scrolls through the list, or changes
        // the filters, we may have to make an ajax call, this dispatches
        // the inputs to loadContents() which handles getting and caching
        // the new requested stuff

        watchUserRequest(src$, toggle$) {
            const loadMessages$ = src$.pipe(switchMap(loadDscContent));
            const loadWatch$ = toggle$.pipe(switchMap((isOn) => (isOn ? loadMessages$ : NEVER)));

            this.$subscribeTo(
                loadWatch$,
                (result) => console.log("[dscpanel loader] next", result),
                (err) => console.warn("[dscpanel loader] error", err),
                () => console.warn("[dscpanel loader] complete: should only complete on unsub")
            );
        },

        updateManualLoading(val) {
            this.isManualLoading = val;
        },
    },
    render() {
        return this.$scopedSlots.default({
            params: this.params,
            results: this.results,
            totalMatches: this.totalMatches,
            loading: this.loading,
            // debugging props
            isManualLoading: this.isManualLoading,
            updateManualLoading: this.updateManualLoading,
        });
    },
};
