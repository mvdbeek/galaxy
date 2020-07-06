/**
 * Lossless backpressure queue for processing observables one at
 * a time without spamming the server or the cache.
 */

import { Subject } from "rxjs";
import { concatMap, publish, finalize, delay } from "rxjs/operators";

const hopper = new Subject();

export const processQueue = hopper.pipe(
    concatMap(({ task$, label }) => {
        console.log("[queue] next task", label);
        task$.connect();
        return task$.pipe(
            delay(5000),
            finalize(() => {
                console.log("[queue] task done", label);
            })
        );
    })
);

export function enqueue(obs$, label) {
    console.log("[queue] enqueue", label);
    const task$ = obs$.pipe(publish());
    hopper.next({ task$, label });
    return task$;
}
