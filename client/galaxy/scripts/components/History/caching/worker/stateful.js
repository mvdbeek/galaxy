/**
 * Keeps a pool of observables for those observables that
 * need to have a running state. (watchers, loaders)
 * TODO: talk to author of threads to see if this was something
 * that he intended to do, or if the staelessness is a bug.
 */

import { BehaviorSubject } from "rxjs";
import { share, filter, finalize } from "rxjs/operators";

const channels = new Map();

export const statefulObservableRoute = (preconfiguredOperator) => {

    const getObservableInstance = (channelKey) => {
        const input = new BehaviorSubject(null);
        return input.pipe(
            filter(input => input !== null),
            preconfiguredOperator,
            share(),
            finalize(() => {
                channels.delete(channelKey);
            })
        );
    }

    return function (channelKey, request) {

        let obs$ = channels.get(channelKey);
        if (!obs$) {
            obs$ = getObservableInstance(channelKey);
            channels.set(channelKey, obs$);
        }

        obs$.next(request);

        return obs$;
    }
}
