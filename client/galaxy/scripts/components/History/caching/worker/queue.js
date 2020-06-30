/**
 * Lossless backpressure queue for processing observables one at
 * a time without spamming the server or the cache.
 */

import { timer, Subject } from "rxjs";
import { tap, publish, ignoreElements, concatMap, startWith,
    mergeMap, delay } from "rxjs/operators";


const hopper = new Subject();

const processQueue = hopper.pipe(
    concatMap((task) => {
        return timer(50).pipe(
            ignoreElements(),
            startWith(task),
            mergeMap(task => {
                task.connect();
                return task;
            })
        );
    })
);

processQueue.subscribe(
    (result) => {
        console.log("[queue] result", result);
    },
    err => console.warn("[queue] error", err),
    () => console.log("why is queue complete")
);


// export function enqueue(obs$, label) {
//     const task = obs$.pipe(
//         delay(500),
//         tap(() => console.log("[queue] starting", label)),
//         publish()
//     );
//     hopper.next(task);
//     return task;
// }

export const enqueue = (label, gap = 250) => obs$ => {
    const task = obs$.pipe(
        delay(gap),
        tap(() => console.log("[queue] starting", label)),
        publish()
    );
    hopper.next(task);
    return task;
}

// export const enqueue = (label = "task") => obs$ => {
//     const task$ = obs$.pipe(publish());
//     hopper.next(task$);
//     return task$;
// }
