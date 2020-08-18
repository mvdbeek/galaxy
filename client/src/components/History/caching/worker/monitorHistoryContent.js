/**
 * Search cache upward and downward from the scroll HID, filtering out results
 * which do not match params, we don't want to return the entire result set for
 * 2 reasons: it might be huge, and we might not yet have large sections of the
 * contents if the user is rapidly dragging the scrollbar to different regions
 */

import { merge } from "rxjs";
import { map } from "rxjs/operators";
import { content$ } from "../galaxyDb";
import { monitorQuery } from "./monitorQuery";
import { buildContentPouchRequest, buildContentSelectorFromParams } from "../pouchUtils";
import { hydrateParams } from "./util";
import { SearchParams } from "../../model/SearchParams";

export const monitorHistoryContent = (cfg = {}) => (src$) => {
    // maximum number of rows above and below the hid cursor
    const { benchSize = SearchParams.pageSize, pageSize = SearchParams.pageSize } = cfg;

    const input$ = src$.pipe(
        hydrateParams(1) // fix params
    );

    const seekUp$ = input$.pipe(
        buildContentPouchRequest({ seek: "asc", limit: benchSize }), // look up from hid cursor
        monitorQuery({ db$: content$ })
    );

    const seekDown$ = input$.pipe(
        buildContentPouchRequest({ seek: "desc", limit: pageSize }), // down from hid cursor,
        monitorQuery({ db$: content$ })
    );

    return merge(seekUp$, seekDown$);
};

// Tryiung single load, see if it's faster, using skiplist for aggregation in
// provider component, so might be ok

export const monitorHistoryContentSingle = () => (src$) => {
    const input$ = src$.pipe(
        hydrateParams(1) // fix params
    );

    const singleSeek$ = input$.pipe(
        map((inputs) => {
            const [id, params] = inputs;

            return {
                selector: {
                    history_id: { $eq: id },
                    hid: {},
                    ...buildContentSelectorFromParams(params),
                },
                sort: [{ hid: "desc" }, { history_id: "desc" }],
            };
        })
    );

    return singleSeek$.pipe(monitorQuery({ db$: content$ }));
};
