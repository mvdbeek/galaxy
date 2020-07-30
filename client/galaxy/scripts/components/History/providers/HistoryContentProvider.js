/**
 * History contents provider. Keeps subscriptions to three streams:
 *    cacheObservable: watches cache for changes that match current params
 *    loadingObservable: loads new content into the cache from the server
 *    pollingObservable: loads new content into the cache when the polling gets new data
 */

import { of, combineLatest, NEVER } from "rxjs";
import { map, withLatestFrom, distinctUntilChanged, startWith, debounceTime, switchMap, finalize, scan } from "rxjs/operators";
import { activity } from "utils/observable/activity";
import { newHidMap, processContentUpdate, buildContentResult } from "./processing";
import { pollHistory, monitorHistoryContent, loadHistoryContents } from "../caching";
import { SearchParams } from "../model/SearchParams";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";


export default {
    mixins: [vueRxShortcuts],

    props: {
        historyId: { type: String, required: true },
        // maximum hid value for unfiltered history
        maxHistoryHid: { type: Number, required: true },
        debouncePeriod: { type: Number, default: 200 },
    },

    data() {
        return {
            // search params
            params: new SearchParams(),

            // results
            contents: [],
            bench: 0,
            topRows: 0,
            bottomRows: 0,
            totalMatches: null,

            scrollCursor: 0,
            hidCursor: this.maxHistoryHid,
            maxFilteredHid: this.maxHistoryHid,
            loading: false,
            scrolling: false,
        }
    },

    computed: {
        maxHid() {
            return this.maxFilteredHid || this.maxHistoryHid;
        }
    },

    watch: {
        maxHistoryHid(val) {
            console.warn("maxHistoryHid", val);
        },
        maxFilteredHid(val) {
            console.warn("maxFilteredHid", val);
        },
        maxHid(val) {
            console.warn("maxHid", val);
        },
    },

    created() {

        // #region Input Observables

        const id$ = this.watch$('historyId');

        const params$ = this.watch$("params").pipe(
            distinctUntilChanged(SearchParams.equals)
        );

        const filter$ = params$.pipe(
            distinctUntilChanged(SearchParams.filtersEqual)
        );

        const inputs$ = combineLatest(id$, params$).pipe(
            debounceTime(0),
            distinctUntilChanged(this.filteredInputsSame),
        );

        const maxHid$ = this.watch$('maxHid');
        const hidCursor$ = this.watch$('hidCursor');
        const totalMatches$ = this.watch$("totalMatches");

        // #endregion

        // #region Activity Flags
        // 0-1 value from the scroller, represents how far down from the top
        // the scrollTop is. Used to calculate search criteria for the cache
        // and for server requests when it cannot be calculated from data
        // that already exists in the cache
        const scrollCursor$ = this.watch$("scrollCursor");

        // flag that's true when scroll cursor is changing
        const scrolling$ = scrollCursor$.pipe(activity());

        this.$subscribeTo(scrolling$, val => this.scrolling = val);

        // #endregion

        // #region Cache Observer
        // Monitors cache results matching the current search parameters and
        // scroller location, resets when id or filters changes

        const cacheUpdate$ = combineLatest(id$, filter$).pipe(
            debounceTime(0),
            switchMap(([id, params]) => {

                const hidMap$ = hidCursor$.pipe(
                    debounceTime(this.debouncePeriod),
                    map(hid => [id, params, hid]),
                    monitorHistoryContent(),
                    scan(processContentUpdate, newHidMap()),
                );

                return hidMap$.pipe(
                    withLatestFrom(hidCursor$, totalMatches$, maxHid$),
                    debounceTime(this.debouncePeriod),
                    map(buildContentResult)
                );
            })
        );

        this.$subscribeTo(
            cacheUpdate$,
            ({ contents, bench, topRows, bottomRows }) => {
                // console.log("[history.cache] next", contents.length, bench, topRows, bottomRows);
                this.contents = contents;
                this.bench = bench;
                this.topRows = topRows;
                this.bottomRows = bottomRows;
            },
            (err) => console.warn(`[history.cache] error`, err),
            () => console.log(`[history.cache] complete`)
        );

        // #endregion

        // #region Loader
        // Loads data from server. Most of the results are sent right to the
        // cache but we need to get the totalMatches and the maximum HID value
        // for the history back to make the scroller work properly.

        const loader$ = inputs$.pipe(
            switchMap(([id, param]) => {
                return combineLatest(of(id), of(param), hidCursor$).pipe(
                    loadHistoryContents(),
                    finalize(() => {
                        this.maxFilteredHid = null;
                    })
                )
            })
        );

        this.$subscribeTo(
            loader$,
            ({ totalMatches, maxHid }) => {
                if (maxHid) {
                    this.maxFilteredHid = Math.max(+maxHid, this.maxFilteredHid);
                }
                this.totalMatches = +totalMatches;
            },
            (err) => console.warn(`[history.load] error`, err),
            () => console.log(`[history.load] complete`)
        );

        // #endregion

        // #region Polling

        const poll$ = combineLatest(id$, params$).pipe(
            debounceTime(0),
            switchMap(inputs => of(inputs).pipe(
                pollHistory()
            ))
        );

        const polling$ = scrolling$.pipe(
            startWith(true),
            distinctUntilChanged(),
            switchMap(isScrolling => isScrolling ? NEVER : poll$)
        );

        // this.listenTo(polling$, 'history.poll');

        // #endregion

    },

    methods: {

        // reset pagination when filtering changes

        updateParams(newParams) {
            if (!SearchParams.filtersEqual(newParams, this.params)) {
                this.params = newParams.resetPagination();
            }
            else if (!SearchParams.equals(newParams, this.params)) {
                this.params = newParams.clone();
            }
        },


        // If we have a startItem, use its hid as the cursor. This will
        // happen when we scroll into a region that is already cached
        // Otherwise estimate based on scroll position, this will happen
        // when the scrollbar is dragged into an uncached region

        onListScroll(payload) {
            console.log("onListScroll", payload);
            const { cursor, startKey } = payload;

            let startHid;
            if (startKey) {
                startHid = startKey;
            } else {
                const scale = 1.0 - cursor;
                startHid = Math.floor(scale * this.maxHid);
                startHid = Math.max(this.maxHistoryHid, startHid);
            }

            this.hidCursor = startHid;
            this.scrollCursor = cursor;
        },


        // Equality comparator for "inputs" which is [ id, SearchParams ]
        // a combination that appears a lot

        inputsSame(a, b) {
            const idSame = a[0] == b[0];
            const paramSame = SearchParams.equals(a[1], b[1]);
            return idSame && paramSame;
        },

        filteredInputsSame(a, b) {
            const idSame = a[0] == b[0];
            const paramSame = SearchParams.filtersEqual(a[1], b[1]);
            return idSame && paramSame;
        },


        // Generic subscriber with debugging output. Assumes you don't need
        // to do anything special with the result.

        listenTo(obs$, label) {
            if (!obs$) return;
            this.$subscribeTo(
                obs$,
                (result) => console.log(`[${label}] next`, typeof (result)),
                (err) => console.warn(`[${label}] error`, err),
                () => console.log(`[${label}] complete`)
            );
        },

    },

    render() {
        return this.$scopedSlots.default({
            ...this.$data,
            updateParams: this.updateParams,
            onListScroll: this.onListScroll,
        });
    },

};
