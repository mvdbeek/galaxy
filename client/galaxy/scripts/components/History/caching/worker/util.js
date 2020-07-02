/**
 * Interior configuration for the worker. We can't access the document
 * from the outside so this needs to be set when the worker is launched
 */

import moment from "moment";
import { of, from, pipe } from "rxjs";
import { tap, map, mergeMap, filter } from "rxjs/operators";
import { ajax } from "rxjs/ajax";
import { createDateStore } from "../../model/DateStore";
import { SearchParams } from "../../model/SearchParams";


/**
 * Configuration var for inside the worker, must be set when worker
 * is fired up because we can't reach the document and that's how stupid,
 * stupid, stupid, stupid, galaxy backbone code gets some of its config.
 */
export const workerConfig = { root: "/" };

export const configure = (options = {}) => {
    console.log("configuring cache worker", options);
    Object.assign(workerConfig, options);
};

/**
 * Prepend against this config. Can't access document so we can't use
 * the standard one from utils
 */
const slashCleanup = /(\/)+/g;
export function prependPath(path) {
    const root = workerConfig.root;
    return `${root}/${path}`.replace(slashCleanup, "/");
}

// Global url date-store, keeps track of the last time a specific url was requested
// Can reset the update_time tracking by passing in a new datestore to the operator configs

export const requestDateStore = createDateStore("requestWithUpdateTime default");

/***
 * Check datestore to get the last time we did this request. Append
 * an update_time clause at the end of the GET url so we only take
 * the fresh updates. Mark the time after the request for future polls
 */
export const requestWithUpdateTime = (config = {}) => (url$) => {
    const {
        context = null,
        dateStore = requestDateStore,
        bufferSeconds = 0,
        dateFieldName = "update_time",
        requestTime = moment.utc(),
    } = config;

    // add context marker in url for debugging purposes
    const baseUrl$ = url$.pipe(
        map((baseUrl) => (context ? `${baseUrl}&context=${context}` : baseUrl))
    );

    // mark and flag this update-time, append to next request with same base
    return baseUrl$.pipe(
        mergeMap((baseUrl) => {
            return of(baseUrl).pipe(
                fullUrl({
                    dateStore,
                    bufferSeconds,
                    dateFieldName,
                }),
                mergeMap(ajax.getJSON),
                tap((results) => {
                    if (results.length) {
                        dateStore.set(baseUrl, requestTime);
                    }
                })
            );
        })
    );
};




/**
 * Takes a base URL appends an update_time-gt restriction based on the lst
 * time this URL was requestd as indicated by the dateStore.
 * (Async in case we choose to store the date in indexDb instead of localStorage)
 */
const fullUrl = (cfg = {}) => {
    const { dateStore, bufferSeconds = 0, dateFieldName = "update_time" } = cfg;

    return pipe(
        mergeMap(async (baseUrl) => {
            if (!dateStore.has(baseUrl)) {
                return baseUrl;
            }

            let lastRequest = dateStore.getLastDate(baseUrl);
            lastRequest = lastRequest.subtract(bufferSeconds, "seconds");

            const parts = [
                baseUrl,
                `q=${dateFieldName}-gt&qv=${lastRequest.toISOString()}`,
                // `q=${dateFieldName}-lt&qv=${rightNow.toISOString()}`,
            ];

            return parts.join("&");
        })
    );
};



export const throttleDistinctDateStore = createDateStore("throttleDistinct default");

export const throttleDistinct = (config = {}) => {

    const {
        timeout = 1000,
        dateStore = throttleDistinctDateStore
    } = config;

    return pipe(
        filter(val => {
            const now = moment();
            let ok = true;
            if (dateStore.has(val)) {
                const lastRequest = dateStore.getLastDate(val);
                ok = (now - lastRequest) > timeout;
            }
            if (ok) {
                dateStore.set(val, now);
            }
            return ok;
        }),
    )
}




// passing SearchParams into the worker removes its class information

export const hydrateInputs = () => pipe(
    map(inputs => {
        const [ id, rawParams ] = inputs;
        return [ id, new SearchParams(rawParams) ];
    })
)


// Breaks inputs into a set of discrete chunks so that the resulting URLs are
// easier to cache
// Source: [history_id, SearchParam] or [url, SeaarchParam]

export const chunkInputs = () => pipe(
    mergeMap(([idParameter, params]) => {
        const chunks = params.chunkParams(SearchParams.chunkSize, true);
        return from(chunks).pipe(
            map(p => [idParameter, p])
        )
    })
)
