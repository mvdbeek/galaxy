/**
 * Keeps a pool of observables for those observables that need to have a running
 * state. (watchers, loaders, distinct)
 */

import { BehaviorSubject } from "rxjs";
import { share, filter, finalize } from "rxjs/operators";

const channels = new Map();

export const statefulObservableRoute = (preconfiguredOperator, label = "stateful") => {

    const getObservableInstance = (channelKey) => {
        const input = new BehaviorSubject(null);
        return input.pipe(
            filter(input => input !== null),
            preconfiguredOperator,
            share(),
            finalize(() => {
                console.log("removing observable", label, channelKey, channels.size);
                channels.delete(channelKey);
            })
        );
    }

    return function (channelKey, request) {

        let obs$ = channels.get(channelKey);
        if (!obs$) {
            obs$ = getObservableInstance(channelKey);
            console.log("adding observable", label, channelKey, channels.size);
            channels.set(channelKey, obs$);
        }

        obs$.next(request);

        return obs$;
    }
}
