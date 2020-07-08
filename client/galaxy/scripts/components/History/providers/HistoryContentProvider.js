/**
 * History contents provider. Keeps subscriptions to three streams:
 *    cacheObservable: watches cache for changes that match current params
 *    loadingObservable: loads new content into the cache from the server
 *    pollingObservable: loads new content into the cache when the polling gets new data
 */
import { of, combineLatest, NEVER } from "rxjs";
import { tap, map, distinctUntilChanged, switchMap, debounceTime, scan, startWith, withLatestFrom } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { pollHistory, monitorContentQuery, loadHistoryContents } from "../caching";
import { buildContentPouchRequest } from "../caching/pouchUtils";
import ContentProviderMixin from "./ContentProviderMixin";

export default {
    mixins: [ContentProviderMixin],
    props: {
        historySize: { type: Number, required: true },
        scrolling: { type: Boolean, required: true },
    },
    computed: {
        // observable scroll value, true when scrolling
        scrolling$() {
            return this.watch$("scrolling");
        },

        // Cache Observer: Subscribe to an observable that looks at the cache
        // filtered by the params. Updates when cache updated, pass values to
        // results property.

        cacheObservable() {
            // make a big empty array
            const makeSpot = (_, i) => ({ _scroll_index: i });
            const makePlaceholders = () => {
                console.log(">> creating placeholders");
                const result = Array.from({ length: this.historySize }, makeSpot);
                console.log(">> done creating placeholders");
                return result;
            };

            // reset if ID or filters change
            const inputs$ = combineLatest(this.id$, this.param$).pipe(
                debounceTime(0),
                distinctUntilChanged((a, b) => {
                    if (a[0] !== b[0]) return false;
                    return SearchParams.filtersEqual(a[1], b[1]);
                })
            );

            // reset if ID or filters change, but not pagination, preserve a
            // big-ass list and splice in updates from the cache watcher
            const cacheUpdates$ = inputs$.pipe(
                switchMap(([id]) => {
                    // reset the placeholders when we switch histories
                    const placeholders = makePlaceholders();

                    return this.param$.pipe(
                        map((params) => buildContentPouchRequest([id, params])),
                        monitorContentQuery(),
                        startWith({}),

                        // create a splice to the running list
                        // add matching _scroll_index to the patch
                        scan((results, update) => {
                            const { matches = [], request = {} } = update;
                            const { skip = 0 } = request;
                            if (matches.length) {
                                const patch = matches.map((row, i) => ({ ...row, _scroll_index: i + skip }));
                                results.splice(skip, patch.length, ...patch);
                            }
                            return results;
                        }, placeholders),
                        tap(() => console.log("giving placeholders to component")),
                    );
                })
            );

            return cacheUpdates$;
        },

        // Manual Loading: When user scrolls through the list, or changes the
        // filters, we may have to make one or more ajax calls, this dispatches
        // the inputs to loadContents() which handles getting and caching the
        // new request

        loadingObservable() {

            // switch when history changes, but keep subscription if just the
            // params change so we can track and filter-out repeated requests
            // within the same history
            const loader$ = this.id$.pipe(
                switchMap(id => this.param$.pipe(
                    map(p => [id, p]),
                    loadHistoryContents()
                ))
            );

            return loader$;
        },

        // Polls the server for updates in the region we're viewing.

        // pollingObservable() {

        //     const input$ = combineLatest(this.id$, this.param$).pipe(
        //         debounceTime(0), // simultaneous vals will trigger 2x
        //         distinctUntilChanged(this.inputsSame)
        //     );

        //     // when inputs change, unsub and resub to pollHistory with new params
        //     const poll$ = input$.pipe(
        //         switchMap(inputs => of(inputs).pipe(
        //             // tap((...args) => console.log("poll args", ...args)),
        //             pollHistory()
        //         ))
        //     )

        //     const polling$ = this.scrolling$.pipe(
        //         startWith(true),
        //         distinctUntilChanged(),
        //         switchMap(isScrolling => isScrolling ? NEVER : poll$)
        //     )

        //     return polling$;

        // },
    },
};
