import moment from "moment";
import { of, pipe } from "rxjs";
import { tap, map, mapTo, filter, switchMap, repeat, finalize, delay } from "rxjs/operators";
import { SearchParams } from "../../model/SearchParams";
import { prependPath, requestWithUpdateTime } from "./util";
import { bulkCacheContent } from "../galaxyDb";
import { buildHistoryUpdateUrl, buildHistoryContentsUrl } from "./urls";
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
            const requestTime = moment.utc();

            // do history poll
            const historyPoll$ = of(inputs).pipe(
                map(([id]) => buildHistoryUpdateUrl(id)),
                map(prependPath),
                requestWithUpdateTime({
                    context: "poll:history",
                    requestTime,
                }),
                tap(results => {
                    if (results.length) {
                        console.log("TODO: put these results into the store", results);
                    }
                }),
            );

            // do content poll
            const contentPoll$ = historyPoll$.pipe(
                filter((list) => list.length),
                delay(pollInterval),
                mapTo(inputs),
                map(([id, rawParams]) => {
                    const params = new SearchParams(rawParams);
                    return buildHistoryContentsUrl(id, params);
                }),
                map(prependPath),
                requestWithUpdateTime({
                    context: "poll:contents",
                    requestTime,
                }),
                bulkCacheContent(),
                map(list => {
                    const updated = list.filter((result) => result.updated);
                    return {
                        updatedItems: updated.length,
                        totalReceived: list.length,
                    };
                })
            );

            const poll$ = contentPoll$.pipe(
                delay(pollInterval),
                repeat(),
                finalize(() => console.log("poll subscription closed"))
            );

            // return enqueue(poll$);

            return poll$;
        })
    );
