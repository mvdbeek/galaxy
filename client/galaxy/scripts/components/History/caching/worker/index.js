/**
 * Makes interior worker methods available to the main thread
 */

// TODO: isn't @babel/polyfill like bad now?
import "@babel/polyfill";

import { expose } from "threads/worker";
import { of } from "rxjs";
import { getItemByKey, unacheItem } from "../db";
import { content$, dscContent$, cacheContent } from "../galaxyDb";

import { pollForHistoryUpdates } from "./polling";
import { loadHistoryContents, loadDscContent } from "./loader";
import { init, configure } from "./util";
import { monitorQuery } from "./monitorQuery";
import { wipeDatabase } from "./debugging";
// import { statefulObservableRoute } from "./stateful";

expose({
    configure,
    init,

    monitorContentQuery: monitorQuery(content$),
    monitorDscQuery: monitorQuery(dscContent$),

    cacheContentItem(props) {
        return of(props).pipe(cacheContent());
    },

    uncacheContent(props) {
        return of(props).pipe(unacheItem(content$));
    },

    getCachedContentByTypeId(id) {
        return of(id).pipe(getItemByKey(content$, "type_id"));
    },

    loadHistoryContents(request) {
        return of(request).pipe(loadHistoryContents({ onceEvery: 30 * 1000 }));
    },

    loadDscContent(request) {
        return of(request).pipe(loadDscContent({ onceEvery: 30 * 1000 }));
    },

    pollHistory(inputs) {
        return of(inputs).pipe(pollForHistoryUpdates({ pollInterval: 10 * 1000 }));
    },

    wipeDatabase,

    // Experimental

    // statefulObservableRoute(
    //     loadHistoryContents({ onceEvery: 30 * 1000 }),
    //     "loadHistoryContents"
    // ),

    // loadDscContent: statefulObservableRoute(
    //     loadDscContent({ onceEvery: 30 * 1000 }),
    //     "loadDscContent"
    // ),
});
