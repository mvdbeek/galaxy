import { SearchParams } from "../../model/SearchParams";

// generate a content update url for the indicated history id, searches up or
// down from passed hid threshold
export const buildHistoryContentsUrl = (cfg = {}) => ([historyId, filters, hid]) => {
    const { dir = "dsc", pageSize = SearchParams.pageSize } = cfg;
    // console.log("buildHistoryContentsUrl", hid, dir);

    // limits, searching against a hid limit like this allows us to query
    // regions where we're not sure whther or not the HID even exists
    // TODO: lte & gte not available filters
    const hidClause = dir == "asc" ? `q=hid-ge&qv=${hid}` : `q=hid-le&qv=${hid}`;
    const orderClause = `order=hid-${dir}`;
    const limitClause = `limit=${pageSize}`;

    // Filtering
    const { showDeleted, showHidden } = filters;
    let deletedClause = "q=deleted&qv=False";
    let visibleClause = "q=visible&qv=True";
    if (showDeleted) {
        deletedClause = "q=deleted&qv=True";
        visibleClause = "";
    }
    if (showHidden) {
        deletedClause = "";
        visibleClause = "q=visible&qv=False";
    }
    if (showDeleted && showHidden) {
        deletedClause = "q=deleted&qv=True";
        visibleClause = "q=visible&qv=False";
    }

    const filterMap = filters.parseTextFilter();
    const textfilters = Array.from(filterMap.entries()).map(([field, val]) => `q=${field}-contains&qv=${val}`);

    const parts = [
        "v=dev",
        "view=betawebclient",
        // `keys=${contentFields.join(",")}`,

        // filters
        deletedClause,
        visibleClause,
        ...textfilters,

        // hid
        hidClause,
        orderClause,

        // same num results every time
        limitClause,
    ];

    const baseUrl = `/api/histories/${historyId}/contents`;
    const qs = parts.filter((o) => o.length).join("&");
    return `${baseUrl}?${qs}`;
};

// Collection + params -> request url w/o update_time
export const buildDscContentUrl = ([contents_url, params]) => {
    const { skip, limit } = params;

    let skipClause = "";
    let limitClause = "";
    if (params) {
        skipClause = `offset=${skip}`;
        limitClause = `limit=${limit}`;
    }

    const qs = [skipClause, limitClause].filter((o) => o.length).join("&");
    return `${contents_url}?${qs}`;
};

/**
 * Generates history update url
 * TODO: Move into history model? Use history model?
 * TODO: fix stupid q/qv api syntax
 * TODO: finalize a new serialization view for the new history client on the server
 *
 * @param {string} id History id
 * @returns {string} History update url without update_time
 */
export function buildHistoryUpdateUrl(id) {
    const parts = [
        `q=encoded_id-in&qv=${id}`,
        // `keys=${historyFields.join(",")}`,
        "view=betawebclient",
    ];
    const qs = parts.join("&");
    return `/api/histories?${qs}`;
}
