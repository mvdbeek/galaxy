import { zip, of, concat, pipe } from "rxjs";
import { tap, map, mergeMap, switchMap, repeat, delay, withLatestFrom, debounceTime, share } from "rxjs/operators";
import { ajax } from "rxjs/ajax";
import { prependPath, requestWithUpdateTime, hydrateInputs } from "./util";
import { content$, bulkCacheContent } from "../galaxyDb";
import { buildHistoryUpdateUrl, buildHistoryContentsUrl } from "./urls";
import { lastCachedContentRequest } from "../pouchQueries";
// import { enqueue } from "./queue";


/**
 * Generates an operator that takes inputs: [historyid, params] and generates
 * a repeated poll for history and history content updates. Stops when unsubscribed
 *
 * @param {object} cfg Config options for poll
 * @returns Observable operator
 */
export const pollForHistoryUpdates = (cfg = {}) => {
    const { pollInterval = 5000 } = cfg;

    return pipe(
        hydrateInputs(),
        switchMap((inputs) => {

            // do history poll
            const historyPoll$ = of(inputs).pipe(
                historyPoll(),
                delay(pollInterval),
            );

            // do content poll
            const contentPoll$ = of(inputs).pipe(
                contentPoll(),
                delay(pollInterval),
            );

            // both must finishf or concat to work
            return concat(historyPoll$, contentPoll$).pipe(
                repeat()
            );
        })
    )
}


// Checks server for history updates
const historyPoll = () => pipe(
    map(([id]) => buildHistoryUpdateUrl(id)),
    map(prependPath),
    requestWithUpdateTime({ context: "poll:history" }),
    tap(results => {
        if (results.length) {
            console.log("TODO: send these history updates to the store where we keep the history data", results);
        }
    }),
)

// Checks server for content updates
const contentPoll = () => src$ => {

    const input$ = src$.pipe(share());
    const since$ = input$.pipe(lastCachedContentDate());

    const baseUrl$ = input$.pipe(
        map(buildHistoryContentsUrl)
    );

    const url$ = zip(baseUrl$, since$).pipe(
        map(([ baseUrl, since ]) => {
            return since !== null ? `${baseUrl}&update_time-gt=${since}` : baseUrl;
        }),
        map(prependPath)
    );

    const cached$ = url$.pipe(
        mergeMap(ajax.getJSON),
        bulkCacheContent()
    );

    // Summarize what we did, no point in sending everything back over
    // the wire when the cache watcher will pick it up
    const summary$ = cached$.pipe(
        map(list => {
            const updated = list.filter((result) => result.updated);
            return {
                updatedItems: updated.length,
                totalReceived: list.length,
            };
        }),
    );

    return summary$;
}


// look up the most recently cached item that matches search params
// source: pouchdb-find query config

const lastCachedContent = () => pipe(
    withLatestFrom(content$),
    mergeMap(async ([queryConfig, db]) => {
        const response = await db.find(queryConfig);
        if (response.docs && response.docs.length == 1) {
            return response.docs[0];
        }
        return null;
    }),
)

const lastCachedContentDate = () => pipe(
    map(lastCachedContentRequest),
    lastCachedContent(),
    map(lastCached => {
        return lastCached ? lastCached.update_time : null;
    })
)
