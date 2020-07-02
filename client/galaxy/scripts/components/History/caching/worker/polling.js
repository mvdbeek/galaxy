import { zip, concat, pipe } from "rxjs";
import { tap, map, mergeMap, repeat, delay, share, take } from "rxjs/operators";
import { ajax } from "rxjs/ajax";
import { prependPath, requestWithUpdateTime, hydrateInputs } from "./util";
import { content$, bulkCacheContent } from "../galaxyDb";
import { lastCachedContentRequest } from "../pouchQueries";
import { lastCachedDate } from "../pouchOperators";
import { buildHistoryUpdateUrl, buildHistoryContentsUrl } from "./urls";
import { cacheSummary } from "./loader";

// import { enqueue } from "./queue";


/**
 * Generates an operator that takes inputs: [historyid, params] and generates
 * a repeated poll for history and history content updates. Stops when unsubscribed
 *
 * @param {object} cfg Config options for poll
 * @returns Observable operator
 */
export const pollForHistoryUpdates = (cfg = {}) => src$ => {
    const { pollInterval = 5000 } = cfg;

    const inputs$ = src$.pipe(take(1), hydrateInputs(), share());
    const historyPoll$ = inputs$.pipe(historyPoll());
    const contentPoll$ = inputs$.pipe(contentPoll());

    // both must finish or concat to work
    const poll$ = concat(historyPoll$, contentPoll$).pipe(
        delay(pollInterval),
        repeat()
    );

    return poll$; // enqueue(poll$, "history poll");
}


// Checks server for history updates
const historyPoll = () => pipe(
    map(([id]) => buildHistoryUpdateUrl(id)),
    map(prependPath),
    requestWithUpdateTime({ context: "poll:history" }),
    tap(results => {
        if (results.length) {
            console.log("TODO: send these history updates to the store where we keep the history data", results);
            console.log("updated histories", results);
        }
    }),
)

// Checks server for content updates
const contentPoll = () => input$ => {

    // latest update_time from the cache
    const since$ = input$.pipe(
        map(lastCachedContentRequest),
        lastCachedDate(content$)
    );

    // base query url
    const baseUrl$ = input$.pipe(
        map(buildHistoryContentsUrl)
    );

    // url w/ update_time
    const url$ = zip(baseUrl$, since$).pipe(
        map(([ baseUrl, since ]) => {
            return since !== null ? `${baseUrl}&update_time-gt=${since}` : baseUrl;
        }),
        map(prependPath)
    );

    return url$.pipe(
        mergeMap(ajax.getJSON),
        bulkCacheContent(),
        cacheSummary(),
    );
}

