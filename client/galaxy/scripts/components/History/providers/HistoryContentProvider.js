/**
 * History contents provider. Keeps subscriptions to three streams:
 *    cacheObservable: watches cache for changes that match current params
 *    loadingObservable: loads new content into the cache from the server
 *    pollingObservable: loads new content into the cache when the polling gets new data
 */
import { of, defer, combineLatest } from "rxjs";
// eslint-disable-next-line no-unused-vars
import { tap, map, distinctUntilChanged, switchMap, debounceTime, scan, startWith } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { pollHistory, monitorContentQuery, loadHistoryContents } from "../caching";
import { buildContentPouchRequest } from "../caching/pouchQueries";
import { contentListMixin } from "./mixins";

export default {
    mixins: [contentListMixin],
    props: {
        historySize: { type: Number, required: true },
    },
    computed: {
        // Cache Observer: Subscribe to an observable that looks at the cache
        // filtered by the params. Updates when cache updated, pass values to
        // results property.

        cacheObservable() {

            // need to reset when the filters change, but not just on pagination changes
            // const filterParams$ = this.param$.pipe(
            //     map((p) => p.resetPagination()),
            //     // debounceTime(this.debouncePeriod),
            //     distinctUntilChanged(SearchParams.filtersEqual)
            // );

            // make a big empty array
            const makeSpot = (_,i) => ({ _scroll_index: i });
            const makePlaceholders = () => {
                // Note that historySize is always one too big, not sure why
                return Array.from({ length: this.historySize - 1 }, makeSpot);
            }

            // reset if ID or filters change
            const inputs$ = combineLatest(this.id$, this.param$).pipe(
                debounceTime(0),
                distinctUntilChanged((a,b) => {
                    if (a[0] !== b[0]) return false;
                    return SearchParams.filtersEqual(a[1], b[1]);
                })
            )

            // reset if ID changes or filter, but not pagination
            const cacheUpdates$ = inputs$.pipe(
                switchMap(([id]) => {
                    console.log("resetting list");

                    // reset the tombstones when we switch
                    const placeholders = makePlaceholders();

                    return this.param$.pipe(
                        map((params) => buildContentPouchRequest([id, params])),
                        monitorContentQuery(),
                        startWith({}),
                        scan((results, update) => {
                            const { matches = [], request = {} } = update;
                            const { skip = 0 } = request;

                            // create a splice to the running list
                            if (matches.length) {

                                // add matching _scroll_index to the patch
                                const patch = matches.map((row, i) => ({ ...row, _scroll_index: i + skip }));

                                // replace elements with updates
                                results.splice(skip, patch.length, ...patch);
                            }

                            return results;
                        }, placeholders)
                    )

                })
            );

            return cacheUpdates$;
        },

        // Manual Loading: When user scrolls through the list, or changes the
        // filters, we may have to make an ajax call, this dispatches the inputs
        // to loadContents() which handles getting and caching the new request

        loadingObservable() {

            // pad the range before we give it to the loader so we
            // load a little more than we're looking at right now
            const paddedParams$ = this.param$.pipe(
                tap((p) => p.report("[loader] start")),
                // map((p) => p.pad()),
                // tap((p) => p.report("[loader] padded"))
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
                // tap((inputs) => console.log("[poll] inputs", inputs)),
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
