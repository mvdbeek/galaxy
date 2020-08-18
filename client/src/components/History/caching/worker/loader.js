/**
 * Manual loading operators for content lists. These get run as the user scrolls
 * or filters data in the listing for immediate lookups. All of them will run
 * one or more ajax calls against the api and cache ther results.
 */
import { pipe, merge } from "rxjs";
import { map, finalize, withLatestFrom, pluck, share, filter } from "rxjs/operators";
import { tag } from "rxjs-spy/operators/tag";

import { throttleDistinct } from "utils/observable/throttleDistinct";
import { buildHistoryContentsUrl, buildDscContentUrl } from "./urls";
import { bulkCacheContent, bulkCacheDscContent } from "../galaxyDb";
import { prependPath, requestWithUpdateTime, hydrateParams, chunkInputs, chunkParam } from "./util";
// import { enqueue } from "./queue";
import { SearchParams } from "../../model/SearchParams";

/**
 * Turn historyId + params into content update urls. Send distinct requests
 * within a 30 sec period. Polling will pick up any other server side variations
 */
export const loadHistoryContents = (cfg = {}) => (src$) => {
    const {
        // This is how often you can request the exact same content url
        // We have a separate polling operation so this isn't urgent
        onceEvery = 60 * 1000,

        // Search a few pages up and down to get a little overlap in the cache for
        // when the user scrolls a little
        pageSize = SearchParams.pageSize,

        // will turn the hid input HID into a multiple of pageSize so we don't
        // get so many unique urls, this must be smaller than the pageSize
        chunkSize = Math.floor(SearchParams.pageSize / 2),
    } = cfg;

    // [historyId, filters, hid]
    const inputs$ = src$.pipe(
        hydrateParams(1),
        // chunk the HID so we don't end up with a zillion uncacheable urls
        chunkParam(2, chunkSize),
        tag("loadHistoryContents inputs")
    );

    const url$ = inputs$.pipe(
        map(buildHistoryContentsUrl({ pageSize })),
        // ignore repeated identical requests
        throttleDistinct({ timeout: onceEvery }),
        map(prependPath),
        tag("loadHistoryContents url")
    );

    const ajaxResponse$ = url$.pipe(
        // repeated requests to the same url get an update_time > whatever
        requestWithUpdateTime(),
        share()
    );

    const cacheSummary$ = ajaxResponse$.pipe(
        pluck("response"),
        bulkCacheContent(),
        summarizeCacheOperation() // don't need all the details
    );

    const load$ = cacheSummary$.pipe(
        withLatestFrom(ajaxResponse$),
        map(([summary, ajaxResponse]) => {

            // actual list
            const { xhr, response = [] } = ajaxResponse;
            const { max: maxHid, min: minHid } = getPropRange(response, "hid");

            // header counts
            const matchesUp = +xhr.getResponseHeader('matches_up');
            const matchesDown = +xhr.getResponseHeader('matches_down');
            const totalMatchesUp = +xhr.getResponseHeader('total_matches_up');
            const totalMatchesDown = +xhr.getResponseHeader('total_matches_down');

            const result = {
                ...summary,
                minHid,
                maxHid,
                matchesUp,
                matchesDown,
                matches: response.length,
                totalMatchesUp,
                totalMatchesDown,
                totalMatches: totalMatchesUp + totalMatchesDown
            }

            return result;
        }),
        finalize(() => {
            // we unsubscribe when the history changes, otherwise we keep this
            // subscription so that throttleDistinct continues to filter out
            // repeated requests.
            console.log("[loadHistoryContents] loadHistoryContents unsubscribed");
        })
    );

    return load$;
};

/**
 * Load collection content (drill down)
 * Params: contents_url + search params
 */
export const loadDscContent = (cfg = {}) => (src$) => {
    const { onceEvery = 10 * 1000 } = cfg;

    // clean and chunk inputs
    const inputs$ = src$.pipe(hydrateParams(), chunkInputs());

    // request, throttle frequently repeated requests
    const ajaxResponse$ = inputs$.pipe(
        map(buildDscContentUrl),
        throttleDistinct({ timeout: onceEvery }),
        map(prependPath),
        requestWithUpdateTime()
    );

    // add contents_url to cache data, will use it as a key
    const url$ = inputs$.pipe(map((inputs) => inputs[0]));

    const response$ = ajaxResponse$.pipe(
        withLatestFrom(url$),
        map(([response, contents_url]) => {
            return response.result.map((row) => ({ ...row, contents_url }));
        })
    );

    const cached$ = response$.pipe(
        bulkCacheDscContent(),
        summarizeCacheOperation(),
        finalize(() => {
            console.log("[loader] loadDscContent subscription end");
        })
    );

    return cached$; // enqueue(load$, "load contents");
};

/**
 * Once data was cached, there's no need to send everything back over into the
 * main thread since the cache watcher will pick up those new values. This just
 * summarizes what pouchdb did during the bulk cache and sends back some stats.
 */
export const summarizeCacheOperation = () => {
    return pipe(
        map((list) => {
            const cached = list.filter((result) => result.updated || result.ok);
            return {
                updatedItems: cached.length,
                totalReceived: list.length,
            };
        })
    );
};

// Picks out min/max value from array of objects

export const getPropRange = (list, propName) => {
    return list.reduce(
        (acc, row) => {
            const val = parseInt(row[propName], 10);
            acc.max = Math.max(acc.max, val);
            acc.min = Math.min(acc.min, val);
            return acc;
        },
        {
            min: Infinity,
            max: -Infinity,
        }
    );
};
