/** common functionality between History contents List and Collection contents
 * List  */

import { SearchParams } from "./model/SearchParams";

export default {
    data: () => ({
        contentParams: new SearchParams(),
        listState: {

            // some of the UI is not super-responsive
            // while the virtual scroller is active so
            // we flip those parts on and off
            scrolling: false,

            // shows the checkboxes on the content items
            showSelection: false,

            // current list of selected type_ids for bulk operations
            selected: new Set(),

            // list of expanded datasets
            expanded: new Set()
        }
    }),
    provide() {
        return {
            listState: this.listState,
            isExpanded: this.isExpanded,
            isSelected: this.isSelected,
            setExpanded: this.setExpanded,
            setSelected: this.setSelected,
        }
    },
    computed: {
        params: {
            get() {
                return this.contentParams;
            },
            set(newParams) {
                if (SearchParams.equals(newParams, this.contentParams)) return;
                // reset paginaton if filters are different
                if (!SearchParams.filtersEqual(newParams, this.contentParams)) {
                    this.contentParams = newParams.resetPagination();
                    return;
                }
                this.contentParams = newParams.clone();
            }
        },
    },
    methods: {
        isSelected({ type_id }) {
            return this.listState.selected.has(type_id);
        },
        isExpanded({ type_id }) {
            return this.listState.expanded.has(type_id);
        },
        setSelected({ type_id }, val) {
            const newSet = new Set(this.listState.selected);
            val ? newSet.add(type_id) : newSet.delete(type_id);
            this.listState.selected = newSet;
        },
        setExpanded({ type_id }, val) {
            const newSet = new Set(this.listState.expanded);
            val ? newSet.add(type_id) : newSet.delete(type_id);
            this.listState.expanded = newSet;
        }
    },
    watch: {
        "listState.selected": function(newSet) {
            if (newSet.size > 0) {
                this.showSelection = true;
            }
        },
    },
}
