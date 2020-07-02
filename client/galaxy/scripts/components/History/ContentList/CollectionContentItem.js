import ContentItemMixin from "./mixins/ContentItemMixin";

export default {
    mixins: [ContentItemMixin],

    computed: {
        contentItemComponent() {
            if (this.source === null) {
                return "Loading";
            }
            if (this.scrolling) {
                return "Placeholder";
            }
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
