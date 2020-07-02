import { SearchParams } from "../model/SearchParams";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";


export const contentListMixin = {
    mixins: [vueRxShortcuts],
    props: {
        id: { type: String, required: true },
        debouncePeriod: { type: Number, required: false, default: 250 },
    },
    data: () => ({
        params: new SearchParams(),
        results: []
    }),
    computed: {
        loading() {
            // should I bother?
            return false;
        },
        totalMatches() {
            return this.results.length;
        },
    },
    created() {

        const id$ = this.watch$("id");
        const param$ = this.watch$("params");

        const cacheWatcher$ = this.cacheObservable(id$, param$);
        if (cacheWatcher$) {
            this.$subscribeTo(
                cacheWatcher$,
                ({ matches }) => {
                    console.log("[cache] results", matches.length);
                    this.results = matches
                },
                (err) => console.warn("[cache] error", err),
                () => console.log("[cache] stream complete")
            );
        }

        const loading$ = this.loadingObservable(id$, param$)
        if (loading$ ) {
            this.$subscribeTo(
                loading$,
                (result) => console.log("[loader] result", result),
                (err) => console.warn("[loader] error", err),
                () => console.warn("[loader] complete: should only complete on unsub")
            );
        }

        const polling$ = this.pollingObservable(id$, param$)
        if (this.isPolling) {
            this.$subscribeTo(
                polling$,
                (result) => console.log("[poll] result", result),
                (err) => console.warn("[poll] error", err),
                () => console.warn("[poll] complete: should only complete on unsub")
            );
        }
    },
    methods: {

        // override me

        cacheObservable() {
            return null;
        },

        loadingObservable() {
            return null;
        },

        pollingObservable() {
            return null;
        },

        updateParams(newParams) {
            if (SearchParams.equals(newParams, this.contentParams)) return;
            // reset paginaton if filters are different
            if (!SearchParams.filtersEqual(newParams, this.contentParams)) {
                this.contentParams = newParams.resetPagination();
                return;
            }
            this.contentParams = newParams.clone();
        },

        // equality comparator for "inputs" which is [ id, SearchParams ]
        // and appears a lot in streams
        inputsSame(a, b) {
            const idSame = a[0] == b[0];
            const paramSame = SearchParams.equals(a[1], b[1]);
            return idSame && paramSame;
        }

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
    }
}