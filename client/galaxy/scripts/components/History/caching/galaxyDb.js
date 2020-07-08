/**
 * Content pouchdb database (galaxy-content)
 */

import moment from "moment";
import { pipe } from "rxjs";
import { tap, map, shareReplay } from "rxjs/operators";
import { collection, cacheItem, bulkCache, installIndexes } from "./db";

// bulk insert helper, runs function on list
const prepList = (fn) => pipe(map((list) => list.map(fn)));

/**
 * History Content
 */

export const content$ = collection({ name: "galaxy-content" }).pipe(
    tap((db) => installIndexes(db, contentIndexes)),
    shareReplay(1)
);

export const cacheContent = () => {
    return pipe(map(prepContent), cacheItem(content$));
};

export const bulkCacheContent = () => {
    return pipe(
        prepList(prepContent), // clean inputs
        bulkCache(content$)
    );
};

const prepContent = (props) => {
    const { history_id, history_content_type, id, type_id: origTypeId, deleted: isDeleted, ...theRest } = props;
    const type_id = origTypeId ? origTypeId : `${history_content_type}-${id}`;
    const _id = `${history_id}-${type_id}`;

    const newProps = {
        _id,
        history_id,
        history_content_type,
        id,
        type_id,
        isDeleted,
        ...theRest,
        cached_at: moment().valueOf(),
    };
    return newProps;
};

export const contentIndexes = [
    // {
    //     index: {
    //         fields: ["hid", "history_id"],
    //     },
    //     name: "by history and hid",
    //     ddoc: "idx-content-history-id-hid",
    // },
    {
        index: {
            fields: [{ hid: "desc" }, { history_id: "desc" }],
        },
        name: "by history and hid descending",
        ddoc: "idx-content-history-id-hid-desc",
    },
    {
        index: {
            fields: [{ cached_at: "desc" }],
        },
        name: "by cache time",
        ddoc: "idx-content-history-cached_at",
    },
];

/**
 * Collection content (drill down into a collection)
 */

export const dscContent$ = collection({ name: "galaxy-collection-content" }).pipe(
    tap((db) => installIndexes(db, dscContentIndexes)),
    shareReplay(1)
);

export const bulkCacheDscContent = () => {
    return pipe(prepList(prepDscContent), bulkCache(dscContent$));
};

// unscrew the api result format
const prepDscContent = (props) => {
    const { contents_url, element_identifier: name, object } = props;
    const { id, model_class, ...otherObjectFields } = object;
    const history_content_type = model_class == "HistoryDatasetAssociation" ? "dataset" : "dataset_collection";
    const type_id = `${history_content_type}-${id}`;
    const _id = `${contents_url}-${type_id}`;
    // const cache_time = moment.utc();

    return {
        // id = content url + counter as that is the most likely query
        _id,
        contents_url,

        // make a type_id so we can re-use all our functions which depend on it
        type_id,
        history_content_type,
        id,

        // switch element_identifier back to name
        name,

        // move stuff out of "object" and into root of cached packet
        ...otherObjectFields,

        // cache_time,
        cached_at: moment().valueOf(),
    };
};

export const dscContentIndexes = [
    {
        index: {
            fields: ["name", { element_index: "asc" }],
        },
        name: "by contents url",
        ddoc: "idx-collection-contents-name",
    },
];
