/**
 * Indices are required by pouchdb to use the pouuchdb.find functionality. These
 * are the indices we keep on the main history content database (content$)
 */

export const contentIndices = [
    {
        index: {
            fields: ["hid", "history_id"],
        },
        name: "by history and hid descending",
        ddoc: "idx-content-history-id-hid",
    },
    {
        index: {
            fields: [{ hid: "desc" }, { history_id: "desc" }],
        },
        name: "by history and hid descending",
        ddoc: "idx-content-history-id-hid-desc",
    },
    // {
    //     index: {
    //         fields: [
    //             { hid: "asc" },
    //             { history_id: "asc" }
    //         ],
    //     },
    //     name: "by history and hid ascending",
    //     ddoc: "idx-content-history-id-hid-asc",
    // },
    // {
    //     index: {
    //         fields: [
    //             'hid',
    //             'history_id',
    //             'isDeleted',
    //             'visible'
    //         ],
    //     },
    //     name: "by everything",
    //     ddoc: "idx-content-by-everything",
    // },
    {
        index: {
            fields: [{ cached_at: "desc" }],
        },
        name: "by cache time",
        ddoc: "idx-content-history-cached_at",
    },
];

/**
 * ...and the collection contents
 */

export const dscContentIndices = [
    {
        index: {
            fields: ["name", { element_index: "asc" }],
        },
        name: "by contents url",
        ddoc: "idx-collection-contents-name",
    },
    {
        index: {
            fields: [{ cached_at: "desc" }],
        },
        name: "by cache time",
        ddoc: "idx-collection-contents-cached_at",
    },
];
