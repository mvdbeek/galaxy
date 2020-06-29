import { pipe } from "rxjs";
import { map, switchMap } from "rxjs/operators";
import { monitorContentQuery } from "../../caching";
import { buildContentPouchRequest } from "../../caching/queries";

/**
 * RxJS operator that takes a historyId + search parameters, queries against the
 * local database showing everything that matches those parameters. Emits
 * an array of matching cached documents.
 *
 * Config options: debounceInput, debounceOutput, see db.js, buildLiveQuery
 *
 * @source [historyId, searchParams]
 * @emits {Array} Array of matching cached content documents
 * @param {object} cfg Configuration, debounceInput, debounceOutput
 */

export const contentCacheWatcher = (cfg = {}) => {
    return pipe(
        map(inputs => buildContentPouchRequest(...inputs)),
        switchMap((request) => monitorContentQuery(request, cfg))
    );
}
