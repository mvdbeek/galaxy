/**
 * Ajax observables customized to galaxy. Prepend configuration api paths,
 * apply general error handling and retries, etc.
 */

import { Subject, merge, pipe } from "rxjs";
import { tap, map, mergeMap, scan, mapTo, startWith } from "rxjs/operators";
import { ajax } from "rxjs/ajax";
import { prependPath } from "utils/redirect";
// import moment from "moment";

// loading indicator
const isLoading = new Subject();
const loading$ = isLoading.pipe(mapTo(1));
const notLoading = new Subject();
const unloading$ = notLoading.pipe(mapTo(-1));
export const ajaxLoading = merge(loading$, unloading$).pipe(
    scan((acc, val) => Math.max(acc + val, 0), 0),
    startWith(0),
    map(val => val > 0)
);

export const ajaxGet = () => pipe(
    tap(() => isLoading.next(1)),
    map(prependPath),
    // tap(url => {
    //     const d = moment.utc();
    //     const [ base, qs ] = url.split("?");
    //     const params = qs.split("&");
    //     console.group(url);
    //     console.log("isoString()", d.toISOString());
    //     console.log("format()", d.format());
    //     console.log("valueOf()", d.valueOf());
    //     console.log(base);
    //     console.log(qs);
    //     console.dir(params);
    //     console.groupEnd();
    // }),
    mergeMap(ajax.getJSON),
    tap(() => notLoading.next(1))
);
