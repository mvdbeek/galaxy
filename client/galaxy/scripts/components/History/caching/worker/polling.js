import moment from "moment";
import { of, concat, pipe } from "rxjs";
import { tap, map, mergeMap, switchMap, repeat, finalize, delay } from "rxjs/operators";
import { ajax } from "rxjs/ajax";
import { SearchParams } from "../../model/SearchParams";
import { prependPath, requestWithUpdateTime } from "./util";
import { content$, bulkCacheContent } from "../galaxyDb";
import { buildHistoryUpdateUrl, buildHistoryContentsUrl } from "./urls";
import { lastCachedContentRequest } from "../queries";
// import { enqueue } from "./queue";


/**
 * Generates an operator that takes inputs: [historyid, params] and generates
 * a repeated poll for history and history content updates. Stops when unsubscribed
 *
 * @param {object} cfg Config options for poll
 * @returns Observable operator
 */
export const pollForHistoryUpdates = ({ pollInterval = 5000 } = {}) =>
    pipe(
        switchMap((inputs) => {

            // params got serialized during transfer to worker
            const [ id, rawParams ] = inputs;
            const params = new SearchParams(rawParams);

            // do history poll
            const historyPoll$ = of(inputs).pipe(
                map(() => buildHistoryUpdateUrl(id)),
                map(prependPath),
                requestWithUpdateTime({
                    context: "poll:history",
                }),
                tap(results => {
                    if (results.length) {
                        console.log("TODO: send these history updates to the store", results);
                    }
                }),
                delay(pollInterval),
            );

            // do content poll
            const contentPoll$ = content$.pipe(

                mergeMap(async (db) => {

                    // look up the most recently cached item that matches search params
                    const queryConfig = lastCachedContentRequest(id, params);
                    const response = await db.find(queryConfig);

                    let since = moment.utc();
                    if (response.docs && response.docs.length == 1) {
                        since = response.docs[0].update_time;
                    }

                    // buld content update url
                    const baseUrl = buildHistoryContentsUrl(id, params);
                    return prependPath(`${baseUrl}&update_time-gt=${since}`);
                }),

                // request & cache
                mergeMap(ajax.getJSON),
                bulkCacheContent(),

                // summarize what we cached
                map(list => {
                    const updated = list.filter((result) => result.updated);
                    return {
                        updatedItems: updated.length,
                        totalReceived: list.length,
                    };
                }),

                delay(pollInterval),
            );

            // both must finishf or concat to work
            return concat(historyPoll$, contentPoll$).pipe(repeat());
        })
    )


// async function getLastCacheDate(findConfig) {
//     const requestTime = moment.utc();
//     return requestTime;
// }