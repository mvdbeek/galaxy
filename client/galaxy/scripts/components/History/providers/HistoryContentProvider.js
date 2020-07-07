/**
 * History contents provider. Keeps subscriptions to three streams:
 *    cacheObservable: watches cache for changes that match current params
 *    loadingObservable: loads new content into the cache from the server
 *    pollingObservable: loads new content into the cache when the polling gets new data
 */
import { defer, combineLatest } from "rxjs";
import { tap, map, distinctUntilChanged, switchMap, debounceTime, scan } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { pollHistory, monitorContentQuery, loadHistoryContents } from "../caching";
import { buildContentPouchRequest } from "../caching/pouchQueries";
import { contentListMixin } from "./mixins";

export default {
    mixins: [contentListMixin],
    computed: {
        // Cache Observer: Subscribe to an observable that looks at the cache
        // filtered by the params. Updates when cache updated, pass values to
        // results property.

        cacheObservable() {
            // cache watcher does not care about skip/limit
            const limitlessParam$ = this.param$.pipe(
                // tap(p => p.report("[dscpanel cachewatch] start")),
                map((p) => p.resetPagination()),
                // tap(p => p.report("[dscpanel cachewatch] reset pagination")),
                // debounceTime(this.debouncePeriod),
                distinctUntilChanged(SearchParams.equals)
            );

            // switchmap on id, mergemap on params
            const cache$ = this.id$.pipe(
                switchMap((id) => {
                    return limitlessParam$.pipe(
                        map((params) => buildContentPouchRequest([id, params])),
                        monitorContentQuery()
                    );
                })
            );

            return cache$;
        },

        // Manual Loading: When user scrolls through the list, or changes the
        // filters, we may have to make an ajax call, this dispatches the inputs
        // to loadContents() which handles getting and caching the new request

        loadingObservable() {
            // need to pad the range before we give it to the loader so we
            // load a little more than we're looking at right now
            const paddedParams$ = this.param$.pipe(
                tap((p) => p.report("[loader] start")),
                map((p) => p.pad()),
                tap((p) => p.report("[loader] padded"))
            );

            const load$ = combineLatest(this.id$, paddedParams$).pipe(
                debounceTime(0),
                distinctUntilChanged(this.inputsSame),
                loadHistoryContents()
            );

            return load$;
        },

        /**
         * Polling Subscription: The app polls for server-generated updates.
         * This subscribes to a process in the worker that periodicially polls
         * an endpoint corresponding to the history + params and dumps the
         * results in the local cache
         */
        pollingObservable() {
            const poll$ = combineLatest(this.id$, this.cumulativeRange$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(this.inputsSame),
                tap((inputs) => console.log("[poll] inputs changed", inputs)),
                pollHistory()
            );

            return poll$;
        },

        // need to reset when history id changes
        cumulativeRange$() {
            const historyId$ = this.id$;

            const newRange$ = defer(() => {
                return this.param$.pipe(
                    scan((range, newParam) => {
                        range.skip = Math.min(range.skip, newParam.skip);
                        range.end = Math.max(range.end, newParam.end);
                        return range;
                    }, new SearchParams())
                );
            });

            const cumulativeRange$ = historyId$.pipe(
                distinctUntilChanged(),
                switchMap(() => newRange$)
            );

            return cumulativeRange$;
        },
    },
};
