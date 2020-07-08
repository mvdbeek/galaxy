/**
 * Makes interior worker methods available to the main thread
 */

// TODO: isn't @babel/polyfill bad now? I don't like having to put this
// inside the worker.
import "@babel/polyfill";

import { expose } from "threads/worker";
import { of } from "rxjs";
import { getItemByKey, unacheItem } from "../db";
import { content$, dscContent$, cacheContent } from "../galaxyDb";

import { pollForHistoryUpdates } from "./polling";
import { loadHistoryContents, loadDscContent } from "./loader";
import { configure } from "./util";
import { monitorQuery } from "./monitorQuery";
import { wipeDatabase } from "./debugging";
import { asObservable } from "./asObservable";

expose({
    configure,

    monitorContentQuery: asObservable(
        monitorQuery({
            db$: content$,
        })
    ),

    monitorDscQuery: asObservable(
        monitorQuery({
            db$: dscContent$,
        })
    ),

    cacheContentItem(props) {
        return of(props).pipe(cacheContent());
    },

    uncacheContent(props) {
        return of(props).pipe(unacheItem(content$));
    },

    getCachedContentByTypeId(id) {
        return of(id).pipe(getItemByKey(content$, "type_id"));
    },

    loadHistoryContents: asObservable(
        loadHistoryContents({
            onceEvery: 30 * 1000,
        })
    ),

    loadDscContent: asObservable(
        loadDscContent({
            onceEvery: 30 * 1000,
        })
    ),

    pollHistory: asObservable(pollForHistoryUpdates()),

    wipeDatabase,
});
