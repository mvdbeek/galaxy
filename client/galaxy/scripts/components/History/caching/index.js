import { of } from "rxjs";
import { map, mergeMap, shareReplay, take } from "rxjs/operators";
import { spawn, Worker } from "threads";
import { getRootFromIndexLink } from "onload/getRootFromIndexLink";
import config from "config";


/**
 * @constant Observable yields the worker thread instance
 */
const thread$ = of(config).pipe(
    mergeMap(async (mainConfigs) => {
        const worker = new Worker("./worker/cacher");
        const newThread = await spawn(worker);
        const root = getRootFromIndexLink();
        const workerConfigs = { ...mainConfigs, root };
        await newThread.configure(workerConfigs);
        return newThread;
    }),
    shareReplay(1)
);

/**
 * A wrapper to build pass-through observables. Hand it the name of
 * a method from inside the worker, yields a function that returns
 * an observable given its inputs.
 *
 * Define the function:
 *    const pollHistory = observableWrapp('pollHistory')
 * Use:
 *    const poll$ = pollHistory(inputs).subscribe(results => blah)
 *
 * @param {String} method Name of the method inside the worker
 * @param {Boolean} sendResponse Whether to return and serialize a response
 * @returns {Function} Function that returns an observable
 */
export const toObservable = (method, sendResponse = true) => (...request) => {
    return thread$.pipe(
        map((thread) => {
            if (!thread) throw new MissingWorkerError();
            if (!(method in thread)) throw new MissingWorkerMethodError(method);
            return thread[method];
        }),
        mergeMap((method) => method(...request)),
        map((result) => (sendResponse ? result : true))
    );
};

/**
 * A wrapper to build pass-through promise functions. Most of these
 * things look the same. An observable is returned from the worker,
 * and most of the time a promise function is what we want to expose.
 *
 * @param {string} workerMethod Name of method inside the worker
 * @return {Function} Function that returns a promise with one result from workerMethod
 */
export const toPromise = (method, sendResponse) => async (...request) => {
    const wrappedObs = toObservable(method, sendResponse);
    const justOne = wrappedObs(...request).pipe(take(1));
    return await justOne.toPromise();
};



/**
 * Custom Errors
 */

class MissingWorkerError extends Error {}

class MissingWorkerMethodError extends Error {
    constructor(missingMethod, ...args) {
        const msg = `
            Missing method on client cache worker: ${missingMethod}.
            Please write a function named ${missingMethod} in caching/cacheWorker.js
        `;
        super(msg, ...args);
    }
}


/**
 * monitorContentCache
 * returns an event emitter that monitors the contents of the history content cache
 * @param {object} pdbFindConfig pouchdb-find configuration object
 * @param {object} cfg debounceInput, debounceOutput
 * @return {Observable} Observable emitter
 */
export const monitorContentQuery = toObservable("monitorContentQuery");

/**
 * Content cache functions
 */
export const cacheContent = toPromise("cacheContentItem");
export const bulkCacheContent = toPromise("bulkCacheContent");
export const getCachedContentByTypeId = toPromise("getCachedContentByTypeId");
export const uncacheContent = toPromise("uncacheContent", false);

/**
 * Pass historyId + params and let worker load it, might be several requests
 * depending on param range and previous requests
 */
export const loadHistoryContents = toObservable("loadHistoryContents");

/**
 * Returns an observable that starts history content polling.
 * Polls until unsubscribed. Results are cached
 * @param {object} configs historyId and search params
 * @returns {Observable} poll subscription
 */
export const pollHistory = toObservable("pollHistory");

/**
 * Collection content
 */
export const monitorDscQuery = toObservable("monitorDscQuery");
export const loadDscContent = toObservable("loadDscContent");


// Debugging
// export const wipeDatabase = toPromise("wipeDatabase", false);
// export const loadNonsense = toPromise("loadNonsense", false);
