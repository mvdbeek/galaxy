/**
 * Makes interior worker methods available to the outside
 */

// TODO: isn't @babel/polyfill like bad now?
import "@babel/polyfill";

import { of } from "rxjs";
import { log } from "utils/observable/log";
import { expose } from "threads/worker";
import { getItemByKey, unacheItem } from "../db";
import { content$, cacheContent, dscContent$ } from "../galaxyDb";
import { pollForHistoryUpdates } from "./polling";
import { loadContents, loadDscContent } from "./loader";
import { configure } from "./util";
// import { wipeDatabase, loadNonsense } from "./debugging";

import { updateQuery, monitorQuery } from "./monitorQuery";

expose({

    configure,

    // content
    monitorContentQuery: monitorQuery(content$),

    cacheContentItem: (props) => of(props).pipe(cacheContent()),
    uncacheContent: (props) => of(props).pipe(unacheItem(content$)),
    getCachedContentByTypeId: (id) => of(id).pipe(getItemByKey(content$, "type_id")),
    loadHistoryContents: (url) => of(url).pipe(loadContents()),

    pollHistory: (inputs) => of(inputs).pipe(pollForHistoryUpdates()),


    // collection contents

    monitorDscQuery: monitorQuery(dscContent$),

    loadDscContent: (inputs) => of(inputs).pipe(loadDscContent()),


    // Debugging & utils
    // wipeDatabase,
    // loadNonsense,
});
