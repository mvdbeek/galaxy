import moment from "moment";
import { of, from, pipe } from "rxjs";
import { tap, map, mergeMap } from "rxjs/operators";
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
    console.log("[worker] configuring cache worker", options);
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

/**
 * Global url date-store, keeps track of the last time a specific url was
 * requested Can reset the update_time tracking by passing in a new datestore to
 * the operator configs
 */
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
        map((url) => {
            return context ? `${url}&context=${context}` : url;
        })
    );

    // mark and flag this update-time, append to next request with same base
    return baseUrl$.pipe(
        mergeMap((baseUrl) => {
            return of(baseUrl).pipe(
                appendUpdateTime({
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
const appendUpdateTime = (cfg = {}) => {
    const {
        dateStore = requestDateStore,
        // bufferSeconds = 0,
        dateFieldName = "update_time",
    } = cfg;

    return pipe(
        mergeMap(async (baseUrl) => {
            if (!dateStore.has(baseUrl)) return baseUrl;

            const lastRequest = dateStore.getLastDate(baseUrl);
            // lastRequest = lastRequest.subtract(bufferSeconds, "seconds");

            const parts = [baseUrl, `q=${dateFieldName}-gt&qv=${lastRequest.toISOString()}`];

            return parts.join("&");
        })
    );
};

/**
 * passing SearchParams into the worker removes its class information
 */
export const hydrateInputs = () => {
    return pipe(
        map((inputs) => {
            const [id, rawParams] = inputs;
            return [id, new SearchParams(rawParams)];
        })
    );
};

/**
 * Breaks inputs up into discrete chunks so the resulting URLs are esier to cache
 * Source: [history_id, SearchParam] or [url, SeaarchParam]
 */
export const chunkInputs = () => {
    return pipe(
        mergeMap(([idParameter, params]) => {
            const chunks = params.chunkParams(SearchParams.pageSize);
            return from(chunks).pipe(map((p) => [idParameter, p]));
        })
    );
};
