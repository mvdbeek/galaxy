/**
 * Lossless backpressure queue for processing observables one at
 * a time without spamming the server or the cache.
 */

import { Subject, timer } from "rxjs";
import { publish, ignoreElements, concatMap, startWith } from "rxjs/operators";

// import { MaxPriorityQueue } from "@datastructures-js/priority-queue";
// export const PRIORITY = { LOW: 10, BACKGROUND: 20, HIGH: 30 };

const hopper = new Subject();
const processQueue = hopper.pipe(
    concatMap((task) => {
        return timer(500).pipe(ignoreElements(), startWith(task));
    })
);

// Subscribe and never stop? maybe make a deferred that rebuilds itself
// when it runs out of things to do?
processQueue.subscribe((publishedTask$) => {
    publishedTask$.connect();
});


// TODO: queue not executing in right order yet
export function enqueue(obs$) {
    // const taskObservable = obs$.pipe(publish());
    // hopper.next(taskObservable);
    // return taskObservable;
    return obs$;
}
