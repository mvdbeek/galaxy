import { map, mergeMap, withLatestFrom } from "rxjs/operators";

/**
 * Operator that retrieves the most recently cached document.
 * Source is a pouchdb-find query config
 */
export const lastCachedDoc = (db$) => (query$) => {
    return query$.pipe(
        withLatestFrom(db$),
        mergeMap(async ([query, db]) => {
            const response = await db.find(query);
            if (response.docs && response.docs.length == 1) {
                return response.docs[0];
            }
            return null;
        })
    );
};

/**
 * Retrieves date from last cached document.
 * source: pouchdb-find query config
 */
export const lastCachedDate = (db$) => (query$) => {
    return query$.pipe(
        lastCachedDoc(db$),
        map((lastCached) => {
            return lastCached ? lastCached.update_time : null;
        })
    );
};
