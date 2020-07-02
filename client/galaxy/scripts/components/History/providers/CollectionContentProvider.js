/**
 * Generates content results for a set of params an an indicated history
 * Abstracts away the rxjs so developers don't need to mess with it if
 * they don't want to.
 */

import { combineLatest } from "rxjs";
import { tap, mergeMap, map, distinctUntilChanged, switchMap, debounceTime, pluck } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";
import { loadDscContent, monitorDscQuery } from "../caching";
import { buildCollectionContentRequest } from "../caching/pouchQueries";
import { inputsSame } from "./inputsSame";


export default {
    mixins: [vueRxShortcuts],
    props: {
        collection: { type: Object, required: true },
        params: { type: SearchParams, required: true },
        debouncePeriod: { type: Number, required: false, default: 100 },
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
        const url$ = this.watch$("collection").pipe(pluck('contents_url'));
        const param$ = this.watch$("params");

        if (this.isWatchingCache) {
            this.watchCache(url$, param$);
        }
        if (this.isManualLoading) {
            this.watchManualRequest(url$, param$);
        }
    },
    methods: {

        watchCache(url$, param$) {

            // cache watcher does not care about skip/limit
            const limitlessParam$ = param$.pipe(
                tap(p => p.report("[dscpanel cachewatch] start")),
                map(p => p.resetPagination()),
                tap(p => p.report("[dscpanel cachewatch] reset pagination")),
            );

            const cache$ = combineLatest(url$, limitlessParam$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(inputsSame),
                map(buildCollectionContentRequest),
                switchMap(monitorDscQuery)
            );

            this.$subscribeTo(
                cache$,
                ({ matches }) => {
                    console.log("[dscpanel cachewatch] results", matches.length);
                    this.results = matches
                },
                (err) => console.warn("[dscpanel cachewatch] error", err),
                () => console.log("[dscpanel cachewatch] stream completed")
            );
        },


        watchManualRequest(url$, param$) {

            // need to pad the range before we give it to the loader so we
            // load a little more than we're looking at right now
            const paddedParams$ = param$.pipe(
                tap(p => p.report("[dscpanel loader] start")),
                map(p => p.pad()),
                tap(p => p.report("[dscpanel loader] padded pagination")),
            );

            const load$ = combineLatest(url$, paddedParams$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(inputsSame),
                switchMap(loadDscContent),
            );

            this.$subscribeTo(
                load$,
                (result) => console.log("[dscpanel loader] result", result),
                (err) => console.warn("[dscpanel loader] error", err),
                () => console.warn("[dscpanel loader] complete: should only complete on unsub")
            );
        },
    },
    render() {
        return this.$scopedSlots.default({
            params: this.params,
            results: this.results,
            totalMatches: this.totalMatches,
            loading: this.loading
        });
    },
};
