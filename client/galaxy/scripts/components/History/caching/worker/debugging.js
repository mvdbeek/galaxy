// import { of } from "rxjs";
import { mergeMap } from "rxjs/operators";
import { content$ } from "../galaxyDb";

// import { ajax } from "rxjs/ajax";
// import { bulkCacheContent, content$ } from "./galaxyDb";
// import { prependPath } from "./workerConfig";

/**
 * Clear entire database
 */

//  export const wipeDatabase = () => {
//     console.log("starting wipe in worker");
//     return content$.pipe(
//         mergeMap(async db => {
//             const result = await db.destroy();
//             console.log("destroy result", result);
//             return result;
//         })
//     )
//  }

/**
 * Load up a bunch of random content from the current history and cache it
 * @param {*} historyId
 */

// export const loadRandomHistoryContent = historyId =>
//     of(historyId).pipe(
//         map(buildContentsUrl),
//         map(prependPath),
//         mergeMap(ajax.getJSON),
//         bulkCacheContent(),
//         tap(loadedStuff => console.log("loadRandomHistoryContent loaded stuff", loadedStuff)),
//     );

// function buildContentsUrl(id) {
//     console.log("buildContentsUrl", id);

//     const limit = Math.floor( Math.random() * 100 );
//     const parts = [
//         `/api/histories/${id}/contents?v=dev`,
//         "view=summary",
//         "keys=history_id",
//         `limit=${limit}`
//     ];

//     return parts.join("&");
// }

// export function loadNonsense() {
//     console.log(loadNonsense, arguments);
// }
