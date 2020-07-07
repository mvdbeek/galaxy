/**
 * Manual loading operators for content lists. These get run as the user scrolls
 * or filters data in the listing for immediate lookups. All of them will run
 * one or more ajax calls against the api and cache ther results.
 */
import { of, pipe, zip } from "rxjs";
import { tap, share, mergeMap, map, finalize, withLatestFrom, distinctUntilChanged } from "rxjs/operators";
import { throttleDistinct } from "utils/observable/throttleDistinct";
import { buildHistoryContentsUrl, buildDscContentUrl } from "./urls";
import { bulkCacheContent, bulkCacheDscContent } from "../galaxyDb";
import { prependPath, requestWithUpdateTime, hydrateInputs, chunkInputs } from "./util";
import { enqueue } from "./queue";

/**
 * Turn historyId + params into content update urls. Send distinct requests
 * within a 30 sec period. Polling will pick upany other server side variations
 */
export const loadHistoryContents = (cfg = {}) => (src$) => {
    const { context = "load-contents", onceEvery = 10 * 1000 } = cfg;

    // construct url, throttle if repeated request
    const url$ = src$.pipe(
        hydrateInputs(),
        chunkInputs(),
        map(buildHistoryContentsUrl),
        throttleDistinct({ timeout: onceEvery })
    );

    const load$ = url$.pipe(
        mergeMap((url) => {
            // loads and caches one url
            const task$ = of(url).pipe(
                map(prependPath),
                requestWithUpdateTime({ context }),
                bulkCacheContent(),
                cacheSummary()
            );

            // send back an observable that waits to emit until
            // the processing queue gets to it
            return enqueue(task$);
        })
    );

    return load$.pipe(
        finalize(() => {
            console.warn("[loadHistoryContents] loadHistoryContents subscription end");
        })
    );
};

/**
 * Load collection content (drill down)
 * Params: contents_url + search params
 */
export const loadDscContent = (cfg = {}) => (src$) => {
    const { context = "load-collection", onceEvery = 10 * 1000 } = cfg;

    // clean and chunk inputs
    const inputs$ = src$.pipe(hydrateInputs(), chunkInputs());

    // request, throttle frequently repeated requests
    const ajaxResponse$ = inputs$.pipe(
        map(buildDscContentUrl),
        throttleDistinct({ timeout: onceEvery }),
        map(prependPath),
        requestWithUpdateTime({ context })
    );

    // add contents_url to cache data, will use it as a key
    const url$ = inputs$.pipe(map((inputs) => inputs[0]));

    const response$ = ajaxResponse$.pipe(
        withLatestFrom(url$),
        map(([responses, contents_url]) => {
            return responses.map((row) => ({ ...row, contents_url }));
        })
    );

    const cached$ = response$.pipe(
        bulkCacheDscContent(),
        cacheSummary(),
        finalize(() => {
            console.warn("[loader] loadDscContent subscription end");
        })
    );

    return cached$; // enqueue(load$, "load contents");
};

/**
 * Utility operator that accepts a source url, throttles out subsequent idential
 * requests within the timeout period. When a request does make it through the
 * filter, appends an update_time so that the second request only gets new
 * updates since first time we asked.
 *
 * Source: Observable url string
 *
 * @param {object} cfg Operator configs
 */
// export const deSpamRequest = (cfg = {}) => (url$) => {
//     const { context, onceEvery = 10000 } = cfg;

//     return url$.pipe(
//         throttleDistinct({
//             timeout: onceEvery,
//         }),
//         tap((url) => {
//             console.log("[loader] sending", url);
//         }),
//         map(prependPath),
//         requestWithUpdateTime({
//             context,
//         })
//     );
// };

/**
 * Once data was cached, there's no need to send everything back over into the
 * main thread since the cache watcher will pick up those new values. This just
 * summarizes what pouchdb did during the bulk cache and sends back some stats.
 */
export const cacheSummary = () =>
    pipe(
        map((list) => {
            const cached = list.filter((result) => result.ok);
            return {
                updatedItems: cached.length,
                totalReceived: list.length,
            };
        })
    );
