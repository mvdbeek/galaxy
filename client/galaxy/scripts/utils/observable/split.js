/**
 * Split array result, emit individual items
 */

import { from, pipe } from "rxjs";
import { mergeMap, filter } from "rxjs/operators";

export const split = () => pipe(
    filter(ray => Array.isArray(ray)),
    mergeMap(stuff => from(stuff)),
);
