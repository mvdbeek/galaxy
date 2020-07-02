/*
History contents provider
props.id = history_id
*/

import { combineLatest } from "rxjs";
import { tap, map, distinctUntilChanged, switchMap, mergeMap, debounceTime, scan } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { pollHistory, monitorContentQuery, loadHistoryContents } from "../caching/index";
import { buildContentPouchRequest } from "../caching/pouchQueries";
import { contentListMixin } from "./mixins";

export default {
    mixins: [contentListMixin],
    methods: {

        // Cache Observer: Subscribe to an observable that looks at the cache
        // filtered by the params. Updates when cache updated, pass values to
        // results property.

        cacheObservable(historyId$, param$) {

            // cache watcher does not care about skip/limit
            const limitlessParam$ = param$.pipe(
                // tap(p => p.report("[cachewatch] start")),
                map(p => p.resetPagination()),
                // tap(p => p.report("[cachewatch] reset pagination")),
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(SearchParams.equals)
            );

            // switchmap on id, mergemap on params
            const cache$ = historyId$.pipe(
                switchMap(id => {
                    return limitlessParam$.pipe(
                        map(params => buildContentPouchRequest([id, params])),
                        mergeMap(monitorContentQuery)
                    )
                })
            );

            return cache$;
        },

        // Manual Loading: When user scrolls through the list, or changes the
        // filters, we may have to make an ajax call, this dispatches the inputs
        // to loadContents() which handles getting and caching the new request

        loadingObservable(historyId$, param$) {

            // need to pad the range before we give it to the loader so we
            // load a little more than we're looking at right now
            const paddedParams$ = param$.pipe(
                // tap(p => p.report("[loader] start")),
                map(p => p.pad()),
                // tap(p => p.report("[loader] padded pagination")),
            );

            const load$ = combineLatest(historyId$, paddedParams$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(this.inputsSame),
                switchMap(loadHistoryContents),
            );

            return load$;
        },

        // Polling Subscription: The app polls for server-generated updates.
        // This subscribes to a process in the worker that periodicially polls
        // an endpoint corresponding to the history + params and dumps the
        // results in the local cache

        pollingObservable(id$, param$) {

            const cumulativeRange = param$.pipe(
                scan((range, newParam) => {
                    range.skip = Math.min(range.skip, newParam.skip);
                    range.limit = Math.max(range.limit, newParam.limit);
                }, new SearchParams())
            )

            const poll$ = combineLatest(id$, cumulativeRange).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(this.inputsSame),
                tap(inputs => console.warn("[poll] inputs changed", inputs)),
                switchMap(pollHistory)
            );

            return poll$;
        },
    }
};
