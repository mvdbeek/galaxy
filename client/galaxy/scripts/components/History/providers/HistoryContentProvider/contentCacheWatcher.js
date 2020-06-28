import { pipe } from "rxjs";
import { map, switchMap } from "rxjs/operators";
import { monitorContentQuery } from "../../caching";


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
        map(buildPouchRequest),
        switchMap((request) => monitorContentQuery(request, cfg))
    );
}

export function buildPouchRequest([history_id, params]) {
    // Omit skip/limit and return the all the cached matches.
    // The new virtual scroller can handle the load since
    // not all of that data is going to be rendered.
    // const { skip, limit } = params;

    return {
        selector: {
            hid: { $gt: null },
            history_id: { $eq: history_id },
            ...buildSelectorFromParams(params),
        },
        sort: [{ hid: "desc" }, { history_id: "desc" }],
        // skip,
        // limit
    };
}

export function buildSelectorFromParams(params) {
    const selector = {
        visible: { $eq: true },
        isDeleted: { $eq: false },
    };

    if (params.showDeleted) {
        delete selector.visible;
        selector.isDeleted = { $eq: true };
    }

    if (params.showHidden) {
        delete selector.isDeleted;
        selector.visible = { $eq: false };
    }

    if (params.showDeleted && params.showHidden) {
        selector.visible = { $eq: false };
        selector.isDeleted = { $eq: true };
    }

    const textFields = params.parseTextFilter();
    for (const [field, val] of textFields.entries()) {
        selector[field] = { $regex: new RegExp(val, "gi") };
    }

    return selector;
}
