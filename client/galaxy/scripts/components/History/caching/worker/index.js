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
import { monitorHistoryContent } from "./monitorHistoryContent";

expose({
    configure,

    // generic content query monitor
    monitorContentQuery: asObservable(
        monitorQuery({ db$: content$ })
    ),

    // generic collection content monitor
    monitorDscQuery: asObservable(
        monitorQuery({ db$: dscContent$ })
    ),

    // 2-way seeking monitor for history cursor search
    monitorHistoryContent: asObservable(
        monitorHistoryContent()
    ),

    cacheContentItem(props) {
        return of(props).pipe(
            cacheContent()
        );
    },

    uncacheContent(props) {
        return of(props).pipe(
            unacheItem(content$)
        );
    },

    getCachedContentByTypeId(id) {
        return of(id).pipe(
            getItemByKey(content$, "type_id")
        );
    },

    loadHistoryContents: asObservable(
        loadHistoryContents({ onceEvery: 30 * 1000 })
    ),

    loadDscContent: asObservable(
        loadDscContent({ onceEvery: 30 * 1000 })
    ),

    pollHistory: asObservable(
        pollForHistoryUpdates()
    ),

    wipeDatabase,
});
