/**
 * Rxjs operator that turns history + params into a series urls.
 * Throw those at the worker and it'll figure out when to send them
 */

import { of, from, pipe } from "rxjs";
import { tap, mergeMap, map, distinct } from "rxjs/operators";
import { bulkCacheContent, bulkCacheDscContent } from "../galaxyDb";
import { prependPath, requestWithUpdateTime } from "./util";
import { SearchParams } from "../../model/SearchParams";
// import { buildDscContentUrl } from "./urls";
import { enqueue } from "./queue";


/**
 * Load contents from passed url. Cache. Return summary
 * of cache results, but don't push all the results back
 * over the wire since we're monitoring the cache with
 * another observable.
 */
export const loadContents = () => pipe(
    requestWithUpdateTime(),
    bulkCacheContent(),
    map((list) => {
        const cached = list.filter((result) => result.ok);
        return {
            updatedItems: cached.length,
            totalReceived: list.length,
        };
    }),
    enqueue("loadContents")
);



/**
 * Load collection content (drill down)
 * Params: contents_url + SearchParams
 */
export const loadDscContent = () => input$ => {

    const load$ = input$.pipe(
        map(([ contents_url, rawParams ]) => {
            return [ contents_url, new SearchParams(rawParams) ];
        }),
        // mergeMap(([contents_url, params]) => {

        //     // break params into discrete chunks
        //     const urls = params.chunkParams().map((p) => {
        //         return buildDscContentUrl(contents_url, p);
        //     });

        //     // request each chunk with update_time
        //     return from(urls).pipe(
        //         distinct(),
        //         map(prependPath),
        //         requestWithUpdateTime(),
        //         // append the contents_url to the cached data like a primary key
        //         bulkCacheDscContent({ contents_url }),
        //     )
        // }),
        // map((list) => {
        //     const cached = list.filter((result) => result.ok);
        //     return {
        //         cached,
        //         updatedItems: cached.length,
        //         totalReceived: list.length,
        //     };
        // })
    );

    return load$;
    // return enqueue(load$);
}
