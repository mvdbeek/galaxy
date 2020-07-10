/**
 * History contents provider. Keeps subscriptions to three streams:
 *    cacheObservable: watches cache for changes that match current params
 *    loadingObservable: loads new content into the cache from the server
 *    pollingObservable: loads new content into the cache when the polling gets new data
 */

import { of, combineLatest, zip, defer, NEVER } from "rxjs";
import { tap, map, distinctUntilChanged, startWith, debounceTime, switchMap, share, pluck, finalize } from "rxjs/operators";
import { pollHistory, monitorContentQuery, loadHistoryContents } from "../caching";
import { buildContentPouchRequest } from "../caching/pouchUtils";
import { SearchParams } from "../model/SearchParams";
import ContentProvider from "./ContentProvider";


export default {
    mixins: [ContentProvider],

    data() {
        return {
            maxHid: 0,
            topRows: 0,
            bottomRows: 0
        }
    },

    created() {

        // This value is set by the returned load results and is the first hid
        // returned for the filtered result set. used to help calculate the
        // appearance of the scroll bar by giving it the right height

        this.maxHid$ = this.watch$('maxHid');


        // This HID is a best guess based on the scroller position, the known
        // search matche count and the HID at the top of the list. We can't know
        // a precise HID without having all the results from the list already,
        // from filtered out results (hidden, deleted, etc.)

        this.scrollHid$ = combineLatest(this.scrollFraction$, this.maxHid$).pipe(
            debounceTime(0),
            map(([scale, maxHid]) => Math.floor((1 - scale) * maxHid)),
        );


        // History + parameters, but does not vary with pagination

        this.filterParams$ = this.params$.pipe(
            distinctUntilChanged(SearchParams.filtersEqual)
        );


        this.$subscribeTo(
            this.cacheObservable(),
            (response) => {
                console.log("[history.cache] next", response);
                const { contents, topRows, bottomRows } = response;
                this.results = contents;
                this.topRows = topRows;
                this.bottomRows = bottomRows;
            },
            (err) => console.warn(`[history.cache] error`, err),
            () => console.log(`[history.cache] complete`)
        );


        this.$subscribeTo(
            this.loader(),
            (response) => {
                console.log("[history.loader] next", response);
                const { totalMatches, maxHid } = response;
                this.maxHid = Math.max(this.maxHid, +maxHid);
                this.totalMatches = +totalMatches;
            },
            (err) => console.warn(`[history.load] error`, err),
            () => console.log(`[history.load] complete`)
        );

        // polling for server-initiated changes
        // this.listenTo(this.pollingObservable(), 'history.poll');
    },

    methods: {


        // Loads data from server. Most of the results are sent right to the
        // cache but we need to get the totalMatches and the maximum HID value
        // for the history back to make the cacheObservable work properly.

        loader() {

            const loaderInputs$ = combineLatest(this.id$, this.filterParams$).pipe(
                debounceTime(this.debouncePeriod)
            );

            const loader$ = loaderInputs$.pipe(
                switchMap(([id]) => this.params$.pipe(
                    map(p => [id, p]),
                    loadHistoryContents(),
                    finalize(() => {
                        this.maxHid = 0;
                    })
                ))
            );

            return loader$;
        },


        // Cache Observer: Monitors cache results matching the current search
        // parameters and scroller location

        cacheObservable() {

            // width of cache window to observe for the scroller
            const windowSize = 200;

            // Updates for one set of user parameters, returns a sparse array
            // where the indices are the HIDs. Could have gone with a Map, but
            // the sparse array preserves hid sort order

            const update$ = defer(() => {

                const inputs$ = combineLatest(this.id$, this.filterParams$, this.scrollHid$).pipe(
                    debounceTime(this.debouncePeriod),
                    tap(inputs => console.log("update inputs", inputs)),
                    share(),
                );

                // Looks above our guess hid location for a few rows of buffer
                // for quick scrollilng
                const seekUp$ = inputs$.pipe(
                    buildContentPouchRequest({
                        seek: "asc",
                        limit: windowSize
                    }),
                    monitorContentQuery(),
                    map(({ matches, request }) => {
                        console.log("seekUp results", request, matches);
                        matches.reverse();
                        return matches;
                    })
                );

                // Get a bunch of rows so we can scroll a bit before seeing
                // loading boxes
                const seekDown$ = inputs$.pipe(
                    buildContentPouchRequest({
                        seek: "desc",
                        limit: windowSize
                    }),
                    monitorContentQuery(),
                    tap(({ matches, request }) => {
                        console.log("seekDown results", request, matches);
                    }),
                    pluck('matches'),
                );

                return zip(seekUp$, seekDown$).pipe(
                    finalize(() => {
                        console.log("changing cache queries...");
                    })
                )
            });

            // when matches change, resubscribe to updates
            const reset$ = combineLatest(this.totalMatches$, this.maxHid$).pipe(
                debounceTime(0)
            );

            const cacheUpdate$ = reset$.pipe(
                switchMap(([size, maxHid]) => update$.pipe(
                    debounceTime(this.debouncePeriod),
                    map(([bench, contents]) => {
                        console.log("bench hids", bench.map(c => c.hid));
                        console.log("hids", contents.map(c => c.hid));
                        const firstHid = bench.length ? bench[0].hid : contents.length ? contents[0].hid : 0;
                        const topRows = maxHid - firstHid;
                        const bottomRows = size - bench.length - contents.length;
                        return { topRows, bottomRows, bench, contents };
                    })
                ))
            );

            return cacheUpdate$;
        },



        // Polls the server for updates in the region we're viewing.

        pollingObservable() {

            const poll$ = combineLatest(this.id$, this.params$).pipe(
                debounceTime(0),
                switchMap(inputs => of(inputs).pipe(
                    pollHistory()
                ))
            );

            // don't poll while scrolling
            const polling$ = this.scrolling$.pipe(
                startWith(true),
                distinctUntilChanged(),
                switchMap(isScrolling => isScrolling ? NEVER : poll$)
            );

            return polling$;
        },

    },

};



// makePlaceholders(startHid, endHid) {
//     const ph = (_, i) => ({ hid: startHid - i });
//     return Array.from({ length: startHid - endHid }, ph);
// },
