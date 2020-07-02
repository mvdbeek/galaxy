/**
 * Generic pouch db operators
 */

import config from "config";

import { of, pipe, from } from "rxjs";
import { map, mergeMap, withLatestFrom, catchError, reduce, share } from "rxjs/operators";
import deepEqual from "deep-equal";

import PouchDB from "pouchdb-browser";
import PouchDebug from "pouchdb-debug";
import PouchAdapterMemory from "pouchdb-adapter-memory";
import PouchUpsert from "pouchdb-upsert";
import PouchFind from "pouchdb-find";
import PouchLiveFind from "pouchdb-live-find";
import PouchErase from "pouchdb-erase";

PouchDB.plugin(PouchDebug);
PouchDB.plugin(PouchAdapterMemory);
PouchDB.plugin(PouchUpsert);
PouchDB.plugin(PouchFind);
PouchDB.plugin(PouchLiveFind);
PouchDB.plugin(PouchErase);

// PouchDB.debug.enable('pouchdb:find');

/**
 * Generate an observable that initializes and shares a pouchdb instance.
 *
 * @param {object} options pouchdb initialization configs
 * @return {Observable} observable that emits the pouch instance
 */
export const collection = (options) =>
    of(options).pipe(
        map((opts) => {
            console.warn("building new PouchDB instance", opts);
            return new PouchDB({ ...config.caching, ...opts });
        }),
        // scan((inst, name) => inst ? inst : createDb({ ...config.caching, name }), null),
        catchError((err) => console.warn("OOPS!", err)),
        share()
    );

/**
 * Retrieves an object from the cache
 *
 * @param {Observable} coll$ Observable of a pouchdb instance
 * @param {string} keyName Field to lookup object by
 * @returns {Function} Observable operator
 */
export const getItemByKey = (coll$, keyName = "_id") =>
    pipe(
        withLatestFrom(coll$),
        mergeMap(async ([keyValue, coll]) => {
            const searchConfig = {
                selector: { [keyName]: keyValue },
                limit: 1,
            };
            const response = await coll.find(searchConfig);
            if (response.warning) {
                console.warn(response.warning, searchConfig);
            }
            if (response.docs.length > 1) {
                console.warn("Too many documents found", response);
            }
            return response.docs[0];
        })
    );

/**
 * Operator that caches all source documents in the indicated collection
 *
 * @source Observable stream of docs to cache
 * @param {Observable} coll$ Observable pouchdb instance
 * @returns {Function} Observable operator
 */
export const cacheItem = (coll$) =>
    pipe(
        withLatestFrom(coll$),
        mergeMap(([content, coll]) => {
            return coll.upsert(content._id, (existing) => {
                // if what we're caching is the same as what's in there, don't bother
                // eslint-disable-next-line no-unused-vars
                const { _rev, ...existingFields } = existing;
                if (deepEqual(content, existingFields)) {
                    return false;
                }
                return { ...existing, ...content };
            });
        })
    );

/**
 * Rxjs operator that bulk caches a list of documents. Attempts a bulk transfer
 * first. If any of those fail due to conflicts, the conflicts run individually
 * through cacheItm()
 *
 * @source Observable of docs to cache
 * @param {Observable} coll$ Observable of a PouchDB instance
 * @returns {Function} Observable operator
 */
export const bulkCache = (coll$) =>
    pipe(
        withLatestFrom(coll$),

        // first try a bulk insert
        mergeMap(async ([content, coll]) => {
            const bulkResult = await coll.bulkDocs(content);
            return { content, bulkResult };
        }),

        // assemble the stuff we need to retry
        map(({ content, bulkResult }) => {
            const contentMap = content.reduce((result, c) => result.set(c._id, c), new Map());
            const okResults = bulkResult.filter((row) => !row.error);
            const conflictResults = bulkResult.filter((row) => row.error && row.status == 409);
            const conflicts = conflictResults.map((err) => contentMap.get(err.id));
            return { okResults, conflicts };
        }),

        // retry the conflicts one at a time using the single operator
        mergeMap(({ okResults, conflicts }) => {
            return from(conflicts).pipe(
                cacheItem(coll$),
                reduce((finalResults, retryResult) => {
                    return [...finalResults, retryResult];
                }, okResults)
            );
        })
    );

/**
 * Deletes item from cache. In pouchdb, deleting just means setting _deleted to true.
 *
 * @source Observable stream of documents to uncache
 * @param {Observable} coll$ Observable of the pouchdb instance
 * @returns {Function} Observable operator
 */
export const unacheItem = (coll$) =>
    pipe(
        withLatestFrom(coll$),
        mergeMap(([doomedDoc, coll]) => {
            return coll.remove(doomedDoc);
        })
    );

/**
 * Install indexes in pouchdb instance. These need to exist
 * for the .find(selector) functionality to work.
 *
 * @param {PouchDB} db pouch db instance
 * @param {Array} indexes array of index configs
 * @returns {Promise}
 */
export async function installIndexes(db, indexes) {
    for (const idx of indexes) {
        await db.createIndex(idx);
    }
}

/**
 * Delete existing indices in a pouchdb database.
 *
 * @param {PouchDB} db pouch db instance
 * @returns {Promise}
 */
export async function deleteIndexes(db) {
    const response = await db.getIndexes();
    const doomedIndex = response.indexes.filter((idx) => idx.ddoc !== null);
    for (const idx of doomedIndex) {
        await db.deleteIndex(idx);
    }
}
