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
        console.warn("Building new worker");
        const worker = new Worker("./worker");
        const newThread = await spawn(worker);
        const root = getRootFromIndexLink();
        const workerConfigs = { ...mainConfigs, root };
        await newThread.configure(workerConfigs);
        await newThread.init();
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
export const toObservable = (methodName, sendResponse = true) => (...request) => {
    return thread$.pipe(
        map((thread) => {
            if (!thread) throw new MissingWorkerError();
            if (!(methodName in thread)) throw new MissingWorkerMethodError(methodName);
            return thread[methodName];
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
