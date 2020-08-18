import { SearchParams } from "../../model/SearchParams";

// generate a content update url for the indicated history id, searches up or
// down from passed hid threshold
export const buildHistoryContentsUrl = (cfg = {}) => ([historyId, filters, hid]) => {
    const { pageSize = SearchParams.pageSize } = cfg;
    // console.log("buildHistoryContentsUrl", hid, dir);

    // Filtering
    const { showDeleted, showHidden } = filters;
    let deletedClause = "deleted=False";
    let visibleClause = "visible=True";
    if (showDeleted) {
        deletedClause = "deleted=True";
        visibleClause = "";
    }
    if (showHidden) {
        deletedClause = "";
        visibleClause = "visible=False";
    }
    if (showDeleted && showHidden) {
        deletedClause = "deleted=True";
        visibleClause = "visible=False";
    }

    const filterMap = filters.parseTextFilter();
    const textfilters = Array.from(filterMap.entries()).map(([field, val]) => `${field}-contains=${val}`);

    const parts = [
        deletedClause,
        visibleClause,
        ...textfilters,
    ];

    const baseUrl = `/api/histories/${historyId}/contents/near/${hid}/${pageSize}`;
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
