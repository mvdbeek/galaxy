import deepEqual from "deep-equal";

const pairSplitRE = /(\w+=\w+)|(\w+="(\w|\s)+")/g;
const scrubFieldRE = /[^\w]/g;
const scrubQuotesRE = /'|"/g;
const scrubSpaceRE = /\s+/g;

// Fields thata can be used for text searches
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
        this._skip = 0;
        this._limit = SearchParams.pageSize;

        Object.assign(this, props);
    }

    // Prop Access

    get skip() {
        return this._skip;
    }

    set skip(val) {
        val = Math.floor(val);
        if (val < 0) {
            throw new Error("skip must be positive");
        }
        this._skip = Math.max(val, 0);
    }

    get limit() {
        return this._limit;
    }

    set limit(val) {
        val = Math.floor(val);
        if (val <= 0) {
            throw new Error("limit must be greater than 0");
        }
        this._limit = Math.min(SearchParams.chunkSize, val);
    }

    get end() {
        return this.skip + this.limit;
    }

    set end(val) {
        val = Math.floor(val);
        if (val <= this.skip) {
            throw new Error("endpoint must be after start point");
        }
        this.limit = val - this.skip;
    }


    // Utils

    clone() {
        return new SearchParams(this);
    }


    // need this because of what Vue does to objects to make them reactive
    export() {
        const { filterText, showDeleted, showHidden, skip, limit } = this;
        return { filterText, showDeleted, showHidden, skip, limit };
    }


    // Pagination

    setPagination(skip, limit) {
        const newParams = this.clone();
        newParams.skip = skip;
        newParams.limit = limit;
        return newParams;
    }

    setRange(start, end) {
        const newParams = this.clone();
        newParams.skip = start;
        newParams.end = end;
        return newParams;
    }

    resetPagination() {
        return this.setPagination(0, SearchParams.pageSize);
    }

    nextPage() {
        const newParams = this.clone();
        newParams.skip += newParams.limit;
        return newParams;
    }

    pad(amt) {
        return this.setPagination(this.slip - amt, this.limit + amt);
    }


    // transforms param range (skip/limit) into discrete chunks that result in
    // request urls that are more likely to be cached

    chunkParams(chunkSize = SearchParams.chunkSize, debug = false) {
        const initialParams = this;
        const result = [];
        let currentParams = initialParams.chunk(chunkSize);
        result.push(currentParams);
        while (currentParams.end < initialParams.end) {
            currentParams = currentParams.nextPage();
            result.push(currentParams);
        }
        if (debug) {
            result.forEach(p => p.report(">>> chunk"));
        }
        return result;
    }

    chunk(size) {
        const chunked = this.clone();
        chunked.limit = size;
        chunked.skip = chunked.limit * Math.floor(chunked.skip / chunked.limit);
        return chunked;
    }


    // Filtering, turns field=val into an object we can use to build selectors

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

}



// Statics

SearchParams.pageSize = 60;
SearchParams.chunkSize = 200;

SearchParams.equals = function(a, b) {
    return deepEqual(a.export(), b.export());
}

// equivalence test ignoring skip/limit
SearchParams.filtersEqual = function(a,b) {
    const aa = a.resetPagination();
    const bb = b.resetPagination();
    return SearchParams.equals(aa, bb);
}
