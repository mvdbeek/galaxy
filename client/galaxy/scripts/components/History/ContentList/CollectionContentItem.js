import ContentItemMixin from "./mixins/ContentItemMixin";

export default {
    mixins: [ContentItemMixin],

    computed: {
        contentItemComponent() {
            if (this.item === null) {
                return "Loading";
            }
            if (this.scrolling) {
                return "Placeholder";
            }
            const { history_content_type } = this.item;
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
