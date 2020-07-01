/**
 * Keeps a pool of observables for those observables that
 * need to have a running state. (watchers, loaders)
 * TODO: talk to author of threads to see if this was something
 * that he intended to do, or if the staelessness is a bug.
 */

import { Subject } from "rxjs";
import { share, finalize } from "rxjs/operators";


const channels = new Map();

export const statefulObservableRoute = (preconfiguredOperator) => {

    const getObservableInstance = (channelKey) => {
        const input = new Subject();
        const newObs = input.pipe(
            preconfiguredOperator,
            share(),
            finalize(() => {
                channels.delete(channelKey);
            })
        );
        return newObs;
    }

    return function (channelKey, request) {
        if (!channels.has(channelKey)) {
            const newInstance = getObservableInstance(channelKey);
            channels.set(channelKey, newInstance);
        }
        const obs$ = channels.get(channelKey);
        obs$.next(request);
        return obs$.asObservable();
    }
}
