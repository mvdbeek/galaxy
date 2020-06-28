/**
 * Makes interior worker methods available to the outside
 */

// TODO: isn't @babel/polyfill like bad now?
import "@babel/polyfill";

import { of } from "rxjs";
import { log } from "utils/observable/log";
import { expose } from "threads/worker";
import { buildLiveQuery, getItemByKey, unacheItem } from "../db";
import { content$, cacheContent, dscContent$ } from "../galaxyDb";
import { pollForHistoryUpdates } from "./polling";
import { loadContents, loadDscContent } from "./loader";
import { configure } from "./util";
// import { wipeDatabase, loadNonsense } from "./debugging";

expose({
    configure,


    // content

    monitorContentQuery: (request, options) =>
        of(request).pipe(buildLiveQuery(content$, options)),

    cacheContentItem: (props) =>
        of(props).pipe(
            cacheContent(),
            log("cacheContentItem", "just cached an item"),
        ),

    uncacheContent: (props) =>
        of(props).pipe(unacheItem(content$)),

    getCachedContentByTypeId: (id) =>
        of(id).pipe(getItemByKey(content$, "type_id")),

    loadHistoryContents: (url) =>
        of(url).pipe(loadContents()),

    pollHistory: (inputs) =>
        of(inputs).pipe(pollForHistoryUpdates()),


    // collection contents

    monitorDscQuery: (request, options) =>
        of(request).pipe(buildLiveQuery(dscContent$, options)),

    loadDscContent: (inputs) =>
        of(inputs).pipe(loadDscContent()),


    // Debugging & utils
    // wipeDatabase,
    // loadNonsense,
});
