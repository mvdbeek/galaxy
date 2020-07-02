/**
 * Return all content matches for the search params
 */
export function buildContentPouchRequest([history_id, params]) {
    const { skip, limit } = params;
    return {
        selector: {
            hid: { $gt: null }, // stupid but required syntax
            history_id: { $eq: history_id },
            ...buildContentSelectorFromParams(params),
        },
        sort: [{ hid: "desc" }, { history_id: "desc" }],
        skip,
        limit,
    };
}

/**
 * Finds the most recently cached row matching the search.
 */
export function lastCachedContentRequest([history_id, params]) {
    return {
        selector: {
            cached_at: { $gt: null }, // stupid but required syntax
            history_id: { $eq: history_id },
            ...buildContentSelectorFromParams(params),
        },
        sort: [{ cached_at: "desc" }],
        limit: 1,
    };
}

/**
 * Build search selector for params filters:
 * deleted, visible, text search
 *
 * @param {SearchParams} params
 */
export function buildContentSelectorFromParams(params) {
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

/**
 * Collection contents, takes a contents_url representing the parent and
 * search params for filters/pagination
 */
export const buildCollectionContentRequest = ([contents_url, params]) => {
    // const { skip, limit, filterText } = params;
    return {
        selector: {
            // we put the contents_url in the id, should
            // come back with auto ordered and sorted results
            _id: { $regex: new RegExp(contents_url, "i") },
            // ...buildSelectorFromParams(params),
        },
        // skip,
        // limit
    };
};
