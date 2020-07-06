import { from, of } from "rxjs";
import { filter, finalize, materialize, pluck, map, mergeMap, shareReplay, take } from "rxjs/operators";
import { spawn } from "threads";
import { v4 as uuidv4 } from "uuid";

import config from "config";
import { getRootFromIndexLink } from "onload/getRootFromIndexLink";

// works but no sourcemaps, using threads-plugin for the moment
import CacheWorker from "worker-loader!./worker";

/**
 * @constant Observable yields the worker thread instance
 */
const thread$ = of(config).pipe(
    mergeMap(async (mainConfigs) => {
        console.warn("Building new worker");
        const newThread = await spawn(new CacheWorker());

        // configure the worker, send in some settings
        const root = getRootFromIndexLink();
        const workerConfigs = { ...mainConfigs, root };
        await newThread.configure(workerConfigs);

        // init, internal subscriptions
        await newThread.init();

        return newThread;
    }),
    shareReplay(1)
);

// Give this a string of the function name on the worker thread instance
// that you want to call (I'm assuming you're exporting a module and not
// a function from your worker, otherwise you'll have to modify this)

export const toOperator = (fnName) => {
    // "ObservablePromise" makes it awkward to extract the actual
    // observable back from the method call. Not a fan. Would prefer
    // if the function just returned either an observable or a promise
    // depending on how you explicitly decided to expose it.

    const method$ = thread$.pipe(
        pluck(fnName),
        map((f) => (...args) => from(f(...args)))
    );

    const operator = () => (src$) => {
        // "Hat on a hat"
        // This looks like something that probably already existed in the
        // threads transfer layer, but I don't think I have access to the
        // internals.
        const id = uuidv4();

        return method$.pipe(
            mergeMap((method) =>
                src$.pipe(
                    materialize(),
                    map((notification) => method({ id, ...notification })),
                    // first emission will be the observable
                    // we want, rest will be nulls,
                    filter(Boolean),
                    mergeMap((val) => val),
                    finalize(async () => {
                        method({ id, kind: "C" });
                    })
                )
            )
        );
    };

    return operator;
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
