/**
 * This is a single item in the list. The main job of the contentItem is to
 * pick a specific selector for the :is attribute of the generic component
 * placeholder. This should be a dataset, collection, or other component
 * depending on the specific list implementation.
 *
 * The mixin also pulls out "selected", and "expanded" properties which are
 * derived from the current component state rather than the data itself.
 */

import Placeholder from "./Placeholder";
import Dataset from "./Dataset";
import DatasetCollection from "./DatasetCollection";
import Subcollection from "./Subcollection";

export default {

    template: `
        <component :is="contentItemComponent"
            class="content-item p-1"
            :class="{ loading }"
            :index="index"
            :tabindex="index"
            :item="source"
            :selected.sync="selected"
            :expanded.sync="expanded"
            @mouseover.native.self.stop="setFocus(index)"
            @keydown.native.arrow-up.self.stop="setFocus(index - 1)"
            @keydown.native.arrow-down.self.stop="setFocus(index + 1)"
        />
    `,

    components: {
        Placeholder,
        Dataset,
        DatasetCollection,
        Subcollection,
    },

    inject: [ "listState" ],

    props: {
        source: { type: Object, required: true },
        index: { type: Number, required: true },
    },

    data: () => ({
        suppressFocus: false,
    }),

    methods: {
        setFocus(index) {
            if (this.suppressFocus) return;
            const ul = this.$el.closest("[role=group]");
            const el = ul.querySelector(`[tabindex="${index}"]`);
            if (el) el.focus();
        },
    },

    computed: {
        loading() {
            return !this.source;
        },

        contentItemComponent() {
            return "Placeholder";
        },

        typeId() {
            return this.source.type_id;
        },

        expanded: {
            get() {
                return this.listState.expanded.has(this.typeId);
            },
            set(val) {
                const newList = new Set(this.listState.expanded);
                val ? newList.add(this.typeId) : newList.delete(this.typeId);
                this.listState.expanded = newList;
            },
        },

        selected: {
            get() {
                return this.listState.selected.has(this.typeId);
            },
            set(val) {
                const newSet = new Set(this.listState.selected);
                val ? newSet.add(this.typeId) : newSet.delete(this.typeId);
                this.listState.selected = newSet;
            },
        },
    },

    created() {
        this.$root.$on("bv::dropdown::show", () => (this.suppressFocus = true));
        this.$root.$on("bv::dropdown::hide", () => (this.suppressFocus = false));
    },
};
