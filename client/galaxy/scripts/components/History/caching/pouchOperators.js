import { pipe } from "rxjs";
import { map, mergeMap, withLatestFrom } from "rxjs/operators";

/**
 * Operator that retrieves the most recently cached document.
 * Source is a pouchdb-find configuration
 * (see pouchQueries)
 */
export const lastCachedDoc = (db$) =>
    pipe(
        withLatestFrom(db$),
        mergeMap(async ([queryConfig, db]) => {
            const response = await db.find(queryConfig);
            if (response.docs && response.docs.length == 1) {
                return response.docs[0];
            }
            return null;
        })
    );

/**
 * Retrieves date from last cached document.
 * source: pouchdb-find query config
 */
export const lastCachedDate = (db$) =>
    pipe(
        lastCachedDoc(db$),
        map((lastCached) => {
            return lastCached ? lastCached.update_time : null;
        })
    );
