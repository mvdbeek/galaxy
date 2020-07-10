/**
 * Manual loading operators for content lists. These get run as the user scrolls
 * or filters data in the listing for immediate lookups. All of them will run
 * one or more ajax calls against the api and cache ther results.
 */
import { of, pipe } from "rxjs";
import { mergeMap, map, finalize, withLatestFrom, pluck } from "rxjs/operators";
import { throttleDistinct } from "utils/observable/throttleDistinct";
import { buildHistoryContentsUrl, buildDscContentUrl } from "./urls";
import { bulkCacheContent, bulkCacheDscContent } from "../galaxyDb";
import { prependPath, requestWithUpdateTime, hydrateInputs, chunkInputs } from "./util";

// import { enqueue } from "./queue";

/**
 * Turn historyId + params into content update urls. Send distinct requests
 * within a 30 sec period. Polling will pick upany other server side variations
 */
export const loadHistoryContents = (cfg = {}) => (src$) => {
    const { context = "load-contents", onceEvery = 30 * 1000 } = cfg;

    // construct url, throttle if repeated request
    const url$ = src$.pipe(
        hydrateInputs(),
        chunkInputs(),
        map(buildHistoryContentsUrl),
        // throttles by url. Only one request for same url within the period
        throttleDistinct({ timeout: onceEvery })
    );

    const load$ = url$.pipe(
        mergeMap((url) => {

            // loads and caches one url
            const task$ = of(url).pipe(
                map(prependPath),
                requestWithUpdateTime({ context }),
                mergeMap(response => of(response).pipe(
                    pluck('result'),
                    bulkCacheContent(),
                    summarizeCacheOperation(),
                    map(summary => {
                        const { totalMatches, result } = response;
                        const { max: maxHid, min: minHid } = getPropRange(result, "hid");
                        return { ...summary, totalMatches, minHid, maxHid };
                    })
                ))
            );

            // TODO: implement backpressure queue
            // send back an observable that waits to emit until
            // the processing queue gets to it
            // return enqueue(task$);
            return task$;
        }),
        finalize(() => {
            // we unsubscribe when the history changes, otherwise we keep this
            // subscription so that throttleDistinct continues to filter out
            // repeated requests.
            console.warn("[loadHistoryContents] loadHistoryContents unsubscribed");
        })
    );

    return load$;
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
        map(([response, contents_url]) => {
            return response.result.map((row) => ({ ...row, contents_url }));
        })
    );

    const cached$ = response$.pipe(
        bulkCacheDscContent(),
        summarizeCacheOperation(),
        finalize(() => {
            console.warn("[loader] loadDscContent subscription end");
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
            const cached = list.filter((result) => result.ok);
            return {
                updatedItems: cached.length,
                totalReceived: list.length,
            };
        })
    );
};



// Picks out min/max value from array of objects

export const getPropRange = (list, propName) => {
    return list.reduce((acc, row) => {
        const val = parseInt(row[propName], 10);
        acc.max = Math.max(acc.max, val);
        acc.min = Math.min(acc.min, val);
        return acc;
    }, {
        min: Infinity,
        max: -Infinity
    })
}
