/**
 * These scrolling lists are really similar. Have tried to implement them using
 * mixins. Each needs a listing component which handles the scrolling and a
 * separate Item component to determine whether a Dataset, Collection or other
 * node type gets displayed on the listing.
 */


import { ContentListFactory } from "./ContentListFactory";
import ContentItem from "./ContentItem";


const HistoryContentItem = {
    mixins: [ ContentItem ],

    computed: {
        contentItemComponent() {
            const { history_content_type } = this.source;
            switch (history_content_type) {
                case "dataset":
                    return "Dataset";
                case "dataset_collection":
                    return "DatasetCollection";
                default:
                    return "Placeholder";
            }
        },
    },
};


const CollectionContentItem = {
    mixins: [ ContentItem ],

    computed: {
        contentItemComponent() {
            const { history_content_type } = this.source;
            switch (history_content_type) {
                case "dataset":
                    return "Dataset";
                case "dataset_collection":
                    return "Subcollection";
                default:
                    return "Placeholder";
            }
        },
    },
};


export const HistoryContentList = ContentListFactory(HistoryContentItem);
export const CollectionContentList = ContentListFactory(CollectionContentItem);

import "./ContentList.scss";
