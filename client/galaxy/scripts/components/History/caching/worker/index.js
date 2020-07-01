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
import { configure } from "./util";
import { monitorQuery } from "./monitorQuery";
import { wipeDatabase } from "./debugging";
import { statefulObservableRoute } from "./stateful";


expose({

    // Debugging & utils

    wipeDatabase,
    configure,


    // content

    monitorContentQuery: monitorQuery(content$),

    cacheContentItem: (props) =>
        of(props).pipe(cacheContent()),

    uncacheContent: (props) =>
        of(props).pipe(unacheItem(content$)),

    getCachedContentByTypeId: (id) =>
        of(id).pipe(getItemByKey(content$, "type_id")),

    loadHistoryContents: statefulObservableRoute(
        loadHistoryContents({
            onceEvery: 30 * 1000
        })
    ),

    pollHistory: (inputs) =>
        of(inputs).pipe(pollForHistoryUpdates()),


    // collection contents

    monitorDscQuery: monitorQuery(dscContent$),

    loadDscContent: statefulObservableRoute(
        loadDscContent({
            onceEvery: 30 * 1000
        })
    ),

});
