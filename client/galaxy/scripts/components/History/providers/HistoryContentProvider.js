/**
 * History contents provider. Keeps subscriptions to three streams:
 *    cacheObservable: watches cache for changes that match current params
 *    loadingObservable: loads new content into the cache from the server
 *    pollingObservable: loads new content into the cache when the polling gets new data
 */
1;
import { of, combineLatest, NEVER } from "rxjs";
import { map, distinctUntilChanged, startWith, debounceTime, switchMap, scan } from "rxjs/operators";
import { tag } from "rxjs-spy/operators/tag";
import { activity } from "utils/observable/activity";
import { pollHistory, loadHistoryContents, monitorHistoryContentSingle } from "../caching";
import { newHidMap, processContentUpdate, buildContentResult } from "./processing";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";
import { History } from "../model";
import { SearchParams } from "../model/SearchParams";

export default {
    mixins: [vueRxShortcuts],

    props: {
        history: { type: History, required: true },
        debouncePeriod: { type: Number, default: 250 },
    },

    data() {
        const startData = this.freshData();
        return {
            params: new SearchParams(),
            ...startData,
        };
    },

    watch: {
        historyId(newId, oldId) {
            if (newId !== oldId) {
                this.reset();
                this.params = new SearchParams();
            }
        },
        params(newParams, oldParams) {
            if (!SearchParams.equals(newParams, oldParams)) {
                this.reset();
            }
        },
    },

    computed: {
        historyId() {
            return this.history.id;
        },

        maxHistoryHid() {
            return this.history.hidItems;
        },

        // either a known maximum resulting from a filtering server request, or
        // just he maximum hid reported by the history object

        maxHid() {
            if (this.maxFilteredHid !== null) {
                return this.maxFilteredHid;
            }
            return this.maxHistoryHid;
        },

        minHid() {
            if (this.minFilteredHid !== null) {
                return this.minFilteredHid;
            }
            return 0;
        },

        // a HID representing where we think the scroller is. This can be
        // exactly known in the case when we're scrolling within an already
        // loaded content range. In that event, we just read the value off the
        // scroll handler. Or it can be estimated when the user drags the
        // scrollbar into an unloaded region of the history, in which case we do
        // some math to try and guess what hid it might be near

        hidCursor() {
            // reported by scroller
            if (this.knownStartingHid !== null) {
                return this.knownStartingHid;
            }

            // estimate from scrollCursor and hid extrema reported by loader
            if (this.scrollCursor !== null) {
                const scale = 1.0 - this.scrollCursor;
                const height = scale * Math.abs(this.maxHid - this.minHid);
                return Math.floor(scale * height + this.minHid);
            }

            // starting position
            return this.maxHistoryHid;
        },

        // When we load data, we'll get an accurate totalMatches result

        totalMatches() {
            if (this.totalFilteredMatches !== null) {
                return this.totalFilteredMatches;
            }
            return this.maxHid - this.minHid;
        },
    },

    methods: {
        freshData() {
            return {
                // output
                contents: [],
                bench: 0,
                topRows: 0,
                bottomRows: 0,
                loading: true,
                scrolling: false,
                scrollStartKey: null,

                // returned from scroller
                scrollCursor: null,
                knownStartingHid: null,

                // returned from loader
                totalFilteredMatches: null,
                maxFilteredHid: null,
                minFilteredHid: null,
            };
        },

        reset() {
            // resets everything except params
            const fresh = this.freshData();
            for (const [key, value] of Object.entries(fresh)) {
                this[key] = value;
            }
        },

        updateParams(newParams) {
            if (!SearchParams.equals(newParams, this.params)) {
                this.params = newParams.clone();
            }
        },

        onListScroll(payload) {
            const { cursor, startKey } = payload;
            this.knownStartingHid = startKey ? startKey : null;
            this.scrollCursor = cursor;
        },
    },

    created() {
        // #region Base Observables

        // base props
        const id$ = this.watch$("historyId", true);
        const filter$ = this.watch$("params", true);

        // supplied by loader
        // const totalMatches$ = this.watch$("totalMatches", true);
        const maxHid$ = this.watch$("maxHid", true);
        const minHid$ = this.watch$("minHid", true);

        // 0-1 value from scroller
        const scrollCursor$ = this.watch$("scrollCursor", true);

        // known HID target or estimate based on scrollCursor
        const hidCursor$ = this.watch$("hidCursor", true);

        const throttledHidCursor$ = hidCursor$.pipe(debounceTime(this.debouncePeriod), distinctUntilChanged());

        // needs a better name, combo of history id + Searchparams
        const inputs$ = combineLatest(id$, filter$).pipe(
            debounceTime(0),
            distinctUntilChanged((a, b) => {
                const idSame = a[0] == b[0];
                const paramSame = SearchParams.equals(a[1], b[1]);
                return idSame && paramSame;
            }),
            tag("inputs changed")
        );

        // #endregion

        // #region Activity Flags

        const scrolling$ = scrollCursor$.pipe(activity());

        this.$subscribeTo(scrolling$, (val) => (this.scrolling = val));

        // #endregion

        // #region Cache Observer

        // Monitors cache results matching the current search parameters and
        // scroller location, resets when id or filters changes

        const cacheUpdate$ = inputs$.pipe(
            tag("cache monitor reset"),
            switchMap((inputs) => {
                // aggregate cache monitor emissions into a searchable in-memory
                // hidMap that represents all results of the query
                const hidMap$ = of(inputs).pipe(
                    monitorHistoryContentSingle(),
                    scan(processContentUpdate, newHidMap()),
                    debounceTime(50)
                    // throttleTime(this.debouncePeriod, undefined, { leading: true, trailing: true }),
                );

                // slice out a section of the hidMap to display
                const cacheResult$ = combineLatest(hidMap$, throttledHidCursor$, maxHid$, minHid$).pipe(
                    debounceTime(0), // 0 consolidates simultaneous events
                    map(buildContentResult)
                );

                return cacheResult$;
            }),
            tag("cache response")
        );

        this.$subscribeTo(
            cacheUpdate$,
            (result) => {
                const { contents, bench, topRows, bottomRows, scrollStartKey } = result;
                this.contents = contents;
                this.bench = bench;
                this.topRows = topRows;
                this.bottomRows = bottomRows;
                this.scrollStartKey = scrollStartKey;
            },
            (err) => console.warn(`[history.cache] error`, err),
            () => console.log(`[history.cache] complete`)
        );

        // #endregion

        // #region Loader

        // when inputs change, resubscribe to a loader in the worker. Want to
        // keep this subscription open as cursor changes so we can track which
        // urls have already been requested internally

        const load$ = inputs$.pipe(
            switchMap((inputs) =>
                throttledHidCursor$.pipe(
                    map((hid) => [...inputs, hid]),
                    loadHistoryContents()
                )
            )
        );

        this.$subscribeTo(
            load$,
            (result) => {
                const { totalMatches, maxHid, minHid } = result;
                if (isFinite(maxHid)) {
                    this.maxFilteredHid = Math.max(+maxHid, this.maxFilteredHid);
                }
                if (isFinite(minHid)) {
                    this.minFilteredHid = Math.min(+minHid, this.minFilteredHid);
                }
                if (isFinite(totalMatches)) {
                    this.totalFilteredMatches = totalMatches;
                }
            },
            (err) => console.warn(`[history.load] error`, err),
            () => console.log(`[history.load] complete`)
        );

        // #endregion

        // #region Polling

        const poll$ = inputs$.pipe(switchMap((inputs) => of(inputs).pipe(pollHistory())));

        const polling$ = scrolling$.pipe(
            startWith(true),
            distinctUntilChanged(),
            switchMap((isScrolling) => (isScrolling ? NEVER : poll$))
        );

        // this.listenTo(polling$, 'history.poll');

        // #endregion
    },

    render() {
        return this.$scopedSlots.default({
            ...this.$data,

            // relevant computed values
            totalMatches: this.totalMatches,
            maxHid: this.maxHid,
            minHid: this.minHid,

            // update methods
            updateParams: this.updateParams,
            onListScroll: this.onListScroll,
        });
    },
};
