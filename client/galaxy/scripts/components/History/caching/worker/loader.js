/**
 * Rxjs operator that turns history + params into a series of requests, and
 * cache operations. Will avoid re-sending frequently requested urls (when a
 * user is scrolling, for instance) and will track urls requested and send
 * subsequent requests with an appended update_time
 */

import { of, pipe } from "rxjs";
import { mergeMap, map } from "rxjs/operators";
import { throttleDistinct } from "utils/observable/throttleDistinct";
import { buildHistoryContentsUrl, buildDscContentUrl } from "./urls";
import { bulkCacheContent, bulkCacheDscContent } from "../galaxyDb";
import { prependPath, requestWithUpdateTime, hydrateInputs, chunkInputs } from "./util";


// TODO: Implement priority queue so we don't spam too much ajax at once
// import { enqueue } from "./queue";


/**
 * Turn historyId + params into content update urls. Send distinct requests
 * within a 30 sec period. Polling will pick upany other server side variations
 */

export const loadHistoryContents = (cfg = {}) => {

    const {
        context = "load-contents",
        onceEvery = 10 * 1000
    } = cfg;

    return pipe(
        hydrateInputs(),
        chunkInputs(),
        map(([id, params]) => buildHistoryContentsUrl(id, params)),
        deSpamRequest({ context, onceEvery }),
        bulkCacheContent(),
        cacheSummary(),
    )
}


/**
 * Load collection content (drill down)
 * Params: contents_url + search params
 */
export const loadDscContent = (cfg = {}) => {

    const {
        context = "load-collection",
        onceEvery = 10 * 1000
    } = cfg;

    return pipe(
        hydrateInputs(),
        chunkInputs(),

        mergeMap(([contents_url, params]) => {
            const url = buildDscContentUrl(contents_url, params);
            return of(url).pipe(
                deSpamRequest({ context, onceEvery }),
                // need to include the url in the cached results, it's used as
                // part of the cache key
                bulkCacheDscContent({ contents_url }),
            )
        }),

        cacheSummary()
    )
}



// sends a url out if it hasn't been spammed.
// keeps track of the last time we used that URL and sends
// with an update_time > whatever when it does emit
// Source: url$

const deSpamRequest = ({ context, onceEvery = 30000 } = {}) => pipe(
    throttleDistinct({ timeout: onceEvery }),
    map(prependPath),
    requestWithUpdateTime({ context }),
)


// Don't want to return the entire cache response to the client since
// we've got another observable that is monitoring changes, but send back
// a quick report of what we did.

const cacheSummary = () => pipe(
    map((list) => {
        const cached = list.filter((result) => result.ok);
        return {
            updatedItems: cached.length,
            totalReceived: list.length,
        }
    })
)
