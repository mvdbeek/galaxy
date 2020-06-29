/**
 * Return a pouchdb find config given a history id and search params
 * @param {string} history_id
 * @param {SearchParams} params
 */
export function buildContentPouchRequest(history_id, params) {
    // Omit skip/limit and return the all the cached matches.
    // The new virtual scroller can handle the load since
    // not all of that data is going to be rendered.
    // const { skip, limit } = params;

    return {
        selector: {
            hid: { $gt: null }, // stupid but required syntax
            history_id: { $eq: history_id },
            ...buildContentSelectorFromParams(params),
        },
        sort: [{ hid: "desc" }, { history_id: "desc" }],
        // skip,
        // limit
    };
}


export function lastCachedContentRequest(history_id, params) {
    return {
        selector: {
            cached_at: { $gt: null }, // stupid but required syntax
            history_id: { $eq: history_id },
            ...buildContentSelectorFromParams(params),
        },
        sort: [{ cached_at: "desc" }],
        limit: 1
    };
}


/**
 * Set fields related to the search params
 * @param {SearchParams} params
 */
function buildContentSelectorFromParams(params) {
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
