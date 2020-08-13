import { merge } from "rxjs";
import { map } from "rxjs/operators";
import { content$ } from "../galaxyDb";
import { monitorQuery } from "./monitorQuery";
import { buildContentPouchRequest, buildContentSelectorFromParams } from "../pouchUtils";
import { hydrateParams } from "./util";
import { SearchParams } from "../../model/SearchParams";

/**
 * Search cache upward and downward from the scroll HID, filtering out results
 * which do not match params, we don't want to return the entire result set for
 * 2 reasons: it might be huge, and we might not yet have large sections of the
 * contents if the user is rapidly dragging the scrollbar to different regions
 */
export const monitorHistoryContent = (cfg = {}) => (src$) => {
    console.log("monitorHistoryContent", cfg);

    const {
        benchSize = SearchParams.pageSize, // rows above cursor
        pageSize = SearchParams.pageSize  // rows below cursor
    } = cfg;

    const input$ = src$.pipe(
        hydrateParams(1) // fix params
    );

    const seekUp$ = input$.pipe(
        buildContentPouchRequest({ seek: "asc", limit: benchSize }), // look up from hid cursor
        map(request => {
            return {
                ...request,
                use_index: 'idx-content-history-id-hid-asc'
            }
        }),
        monitorQuery({ db$: content$ })
    );

    const seekDown$ = input$.pipe(
        buildContentPouchRequest({ seek: "desc", limit: pageSize }), // down from hid cursor,
        map(request => {
            return {
                ...request,
                use_index: 'idx-content-history-id-hid-desc'
            }
        }),
        monitorQuery({ db$: content$ })
    );

    return merge(seekUp$, seekDown$);
};
