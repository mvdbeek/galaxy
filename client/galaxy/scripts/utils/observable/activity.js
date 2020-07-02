/**
 * Observable operator that emits one value when the source
 * is emitting and another after it has stopped
 */

import { of, merge } from "rxjs";
import { throttleTime, mapTo, delay, switchMap, share, distinctUntilChanged } from "rxjs/operators";

export const activity = (config = {}) => (source) => {
    const { period = 500, trailPeriod = 100, activeVal = true, inactiveVal = false } = config;

    // need a little gap after last active timeout or we'll get two events
    const inactivePeriod = period + trailPeriod;

    const active = source.pipe(mapTo(activeVal), throttleTime(period), share());

    const inactive = active.pipe(switchMap(() => of(inactiveVal).pipe(delay(inactivePeriod))));

    return merge(active, inactive).pipe(distinctUntilChanged());
};
