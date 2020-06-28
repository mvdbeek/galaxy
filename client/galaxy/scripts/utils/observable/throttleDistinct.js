import { pipe } from "rxjs";
import { groupBy, mergeMap, throttleTime } from "rxjs/operators";

/**
 * Emits distinct values as they show up, but repeated values are throttled
 * until the timout expires.
 *
 * @param {integer} timeout throttle duration
 */
export const throttleDistinct = (timeout = 1000) => pipe(
    groupBy(value => value),
    mergeMap(grouped => grouped.pipe(
        throttleTime(timeout)
    ))
);
