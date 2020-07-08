/**
 * Framework for a content list provider. A scroller like this has 3 observables
 *
 * Cache watcher. (this.cacheObservable)
 * Watches cache for changes. Emits updates from the worker
 *
 * Loader
 * This monitors user input and loads new content on demand. It monitors the
 * pagination (skip/limit) and filter properties contained in SearchParams,
 * then issues a request to the worker to load and cache matching data.
 *
 * Polling
 * This subscribes to a long-running observable inside the worker that polls
 * the history to get updates which may not have come from the user. Monitors
 * parameter history to reduce the range of responses.
 */

import { distinctUntilChanged } from "rxjs/operators";
import { activity } from "utils/observable/activity";
import { SearchParams } from "../model/SearchParams";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";

export default {
    mixins: [vueRxShortcuts],
    props: {
        id: { type: String, required: true },
        debouncePeriod: { type: Number, required: false, default: 250 },
    },
    data: () => ({
        params: new SearchParams(),
        results: [],
    }),
    computed: {
        loading() {
            // should I bother?
            return false;
        },
        totalMatches() {
            return this.results.length;
        },
        id$() {
            return this.watch$("id").pipe(distinctUntilChanged());
        },
        param$() {
            return this.watch$("params").pipe(distinctUntilChanged(SearchParams.equals));
        },
        scrolling$() {
            // we are "scrolling" if the params keep changing
            return this.param$.pipe(
                activity({
                    throttlePeriod: this.debouncePeriod,
                    trailPeriod: 100,
                })
            );
        },

        // Override
        cacheObservable() {
            return null;
        },
        loadingObservable() {
            return null;
        },
        pollingObservable() {
            return null;
        },
    },
    created() {
        if (this.cacheObservable) {
            this.$subscribeTo(
                this.cacheObservable,
                (results) => {
                    console.log("[provider.cache] next", results.length);
                    this.results = results;
                },
                (err) => console.warn("[provider.cache] error", err),
                () => console.log("[provider.cache] stream complete")
            );
        }
        if (this.loadingObservable) {
            this.$subscribeTo(
                this.loadingObservable,
                (result) => console.log("[provider.loader] result", result),
                (err) => console.warn("[provider.loader] error", err),
                () => console.warn("[provider.loader] complete: should only complete on unsub")
            );
        }
        if (this.pollingObservable) {
            this.$subscribeTo(
                this.pollingObservable,
                (result) => console.log("[provider.poll] result", result),
                (err) => console.warn("[provider.poll] error", err),
                () => console.warn("[provider.poll] complete: should only complete on unsub")
            );
        }
    },
    methods: {
        updateParams(newParams) {
            if (SearchParams.equals(newParams, this.params)) return;
            // reset paginaton if filters are different
            if (!SearchParams.filtersEqual(newParams, this.params)) {
                this.params = newParams.resetPagination();
                return;
            }
            this.params = newParams.clone();
        },

        // equality comparator for "inputs" which is [ id, SearchParams ]
        // and appears a lot in streams
        inputsSame(a, b) {
            const idSame = a[0] == b[0];
            const paramSame = SearchParams.equals(a[1], b[1]);
            return idSame && paramSame;
        },
    },
    render() {
        return this.$scopedSlots.default({
            params: this.params,
            updateParams: this.updateParams,
            results: this.results,
            totalMatches: this.totalMatches,
            loading: this.loading,
        });
    },
    watch: {
        id(newId, oldId) {
            if (newId && newId !== oldId) {
                this.params = new SearchParams();
            }
        },
    },
};
