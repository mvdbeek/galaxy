/**
 * Generates content results for a set of params an an indicated history
 * Abstracts away the rxjs so developers don't need to mess with it if
 * they don't want to.
 */

import { combineLatest } from "rxjs";
import { tap, mergeMap, map, distinctUntilChanged, switchMap, debounceTime, pluck, share } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";
import { loadDscContent, monitorDscQuery } from "../caching";
import { buildCollectionContentRequest } from "../caching/pouchQueries";
import { v4 as uuidv4 } from 'uuid';

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
        debounceDelay: { type: Number, required: false, default: 100 },
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

        const inputs$ = combineLatest(url$, param$).pipe(
            debounceTime(0),
            distinctUntilChanged(inputsSame),
            debounceTime(this.debounceDelay),
            share()
        );

        if (this.isWatchingCache) {
            this.watchCache(inputs$);
        }

        if (this.isManualLoading) {
            this.watchManualRequest(url$, param$);
        }

    },
    methods: {

        watchCache(src$) {

            const cacheMessages$ = src$.pipe(
                map(buildCollectionContentRequest),
                switchMap((pouchRequest) => {
                    return monitorDscQuery(pouchRequest);
                }),
            );

            this.$subscribeTo(
                cacheMessages$,
                (results) => {
                    console.log("[dscpanel cachewatch] result", results);
                    this.results = results
                },
                (err) => console.warn("[dscpanel cachewatch] error", err),
                () => console.log("[dscpanel cachewatch] stream completed")
            );
        },

        watchManualRequest(url$, param$) {

            const loadMessages$ = url$.pipe(
                switchMap(url => {
                    const channelKey = uuidv4();
                    return param$.pipe(
                        tap(params => console.warn("[dscpanel loader] params changed", url, params)),
                        mergeMap(params => loadDscContent(channelKey, [url, params]))
                    )
                })
            );

            this.$subscribeTo(
                loadMessages$,
                (result) => console.log("[dscpanel loader] next", result),
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
