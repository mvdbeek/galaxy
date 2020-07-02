/**
 * Lossless backpressure queue for processing observables one at
 * a time without spamming the server or the cache.
 */

import { timer, Subject } from "rxjs";
import { ignoreElements, concatMap, startWith, mergeMap } from "rxjs/operators";

const hopper = new Subject();

export const processQueue = hopper.pipe(
    concatMap((task) => {
        return timer(100).pipe(
            ignoreElements(),
            startWith(task),
            mergeMap((task) => {
                console.log("[queue] connecting task");
                task.connect();
                return task;
            })
        );
    })
);

export function enqueue(obs$, label) {
    console.log(`[queue] enqueue: ${label}`);

    // const task = obs$.pipe(
    //     delay(500),
    //     tap(() => console.log("[queue] task starting", label)),
    //     publish()
    // );
    // hopper.next(task);
    // return task;

    return obs$;
}
