/**
 * Manual loading operators for content lists. These get run as the user scrolls
 * or filters data in the listing for immediate lookups. All of them will run
 * one or more ajax calls against the api and cache ther results.
 */
import { of, pipe, zip } from "rxjs";
import { tap, share, mergeMap, map, finalize } from "rxjs/operators";
import { throttleDistinct } from "utils/observable/throttleDistinct";
import { buildHistoryContentsUrl, buildDscContentUrl } from "./urls";
import { bulkCacheContent, bulkCacheDscContent } from "../galaxyDb";
import { prependPath, requestWithUpdateTime, hydrateInputs, chunkInputs } from "./util";
import { enqueue } from "./queue";
import { v4 as uuidv4 } from "uuid";

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
            const id = uuidv4();

            // loads and caches one url
            const task$ = of(url).pipe(
                map(prependPath),
                requestWithUpdateTime({ context }),
                bulkCacheContent(),
                cacheSummary(),
                tap(() => console.log("[loadHistoryContents] load done", id))
            );

            // send back an observable that waits to emit until
            // the processing queue gets to it
            return enqueue(task$, id);
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

    debugger;

    // clean and chunk inputs
    const inputs$ = src$.pipe(
        hydrateInputs(),
        chunkInputs(),
        tap((things) => {
            debugger;
        }),
        share()
    );

    // will need contents_url later
    const contentsUrl$ = inputs$.pipe(
        map((inputs) => inputs[0]),
        tap((things) => {
            debugger;
        })
    );

    // send request
    const response$ = inputs$.pipe(
        map(buildDscContentUrl),
        tap((things) => {
            debugger;
        }),
        deSpamRequest({ context, onceEvery }),
        tap((things) => {
            debugger;
        })
    );

    const load$ = zip(response$, contentsUrl$).pipe(
        map(([responses, contents_url]) => {
            debugger;
            return responses.map((row) => ({ ...row, contents_url }));
        }),
        tap((stuff) => {
            debugger;
        }),
        bulkCacheDscContent(),
        tap((things) => {
            debugger;
        }),
        cacheSummary(),
        tap((things) => {
            debugger;
        }),
        finalize(() => {
            console.warn("[loader] loadDscContent subscription end");
        })
    );

    return load$; // enqueue(load$, "load contents");
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
export const deSpamRequest = (cfg = {}) => (url$) => {
    const { context, onceEvery = 10000 } = cfg;

    return url$.pipe(
        throttleDistinct({
            timeout: onceEvery,
        }),
        tap((url) => {
            console.log("[loader] sending", url);
        }),
        map(prependPath),
        requestWithUpdateTime({
            context,
        })
    );
};

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
