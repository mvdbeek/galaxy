import equals from "fast-deep-equal";

const pairSplitRE = /(\w+=\w+)|(\w+="(\w|\s)+")/g;
const scrubFieldRE = /[^\w]/g;
const scrubQuotesRE = /'|"/g;
const scrubSpaceRE = /\s+/g;

const validTextFields = new Set([
    "name",
    "history_content_type",
    "file_ext",
    "extension",
    "misc_info",
    "state",
    "hid",
    "tag",
]);

export class SearchParams {
    constructor(props = {}) {
        // filters
        this.filterText = "";
        this.showDeleted = false;
        this.showHidden = false;

        // skip/limit
        this.skip = 0;
        this.limit = SearchParams.pageSize;

        Object.assign(this, props);
    }

    clone() {
        return new SearchParams(this);
    }

    // reset to beginning of search results when filter parameters change
    resetLimits() {
        const newParams = this.clone();
        newParams.skip = 0;
        newParams.limit = SearchParams.pageSize;
        return newParams;
    }

    setLimits(startIndex, endIndex = 0) {
        const newParams = this.clone();
        newParams.skip = startIndex;
        newParams.limit = Math.max(SearchParams.pageSize, endIndex - startIndex);
        return newParams;
    }

    chunkParams(size = SearchParams.pageSize) {
        const result = [];
        const initialParams = this;
        let currentParams = initialParams.chunk(size);
        result.push(currentParams);
        while (currentParams.skip + currentParams.limit < initialParams.skip + initialParams.limit) {
            currentParams = currentParams.nextPage(size);
            result.push(currentParams);
        }
        return result;
    }

    chunk(size = SearchParams.pageSize) {
        const newParams = this.clone();
        newParams.skip = size * Math.floor(newParams.skip / size);
        newParams.limit = size;
        return newParams;
    }

    nextPage(size = SearchParams.pageSize) {
        const newParams = this.clone();
        newParams.skip = newParams.skip + size;
        return newParams;
    }

    // extends limit on content query down for scrolling on UI
    extendLimit(pages = 0.5) {
        const newParams = this.clone();
        newParams.limit = newParams.limit + Math.floor(pages * SearchParams.pageSize);
        return newParams;
    }

    parseTextFilter() {
        const raw = this.filterText;

        const result = new Map();
        if (!raw.length) return result;

        let matches = raw.match(pairSplitRE);
        if (matches === null && raw.length) matches = [`name=${raw}`];

        return matches.reduce((result, pair) => {
            const [field, val] = pair.split("=");
            const cleanField = field.replace(scrubFieldRE, "");

            if (validTextFields.has(cleanField)) {
                const cleanVal = val.replace(scrubQuotesRE, "").replace(scrubSpaceRE, " ");
                result.set(cleanField, cleanVal);
            }

            return result;
        }, result);
    }

    // output current state to log
    report(label = "params") {
        const { skip, limit, showDeleted, showHidden, filterText } = this;
        const dString = showDeleted ? "showDeleted" : "";
        const hString = showHidden ? "showHidden" : "";
        console.groupCollapsed(label, `(skip: ${skip}, take: ${limit}), ${dString} ${hString}`);
        console.log("showDeleted", showDeleted);
        console.log("showHidden", showHidden);
        console.log("filterText", filterText);
        console.log("skip", skip);
        console.log("limit", limit);
        console.groupEnd();
    }

    // compare 2 param objects, trying fast-deep-equals but
    // I'm a little worried that Vue might add nonsense to the class
    // that affects the result when it adds its reactivity features.
    static equals(a, b) {
        return equals(a, b);
    }

    // equivalence test ignoring skip/limit
    static filtersEqual(a, b) {
        const aa = a.resetLimits();
        const bb = b.resetLimits();
        return SearchParams.equals(aa, bb);
    }
}

// size of requests from server
SearchParams.pageSize = 100;
