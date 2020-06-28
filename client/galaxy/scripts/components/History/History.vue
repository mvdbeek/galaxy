<template>
    <ContentProvider :history-id="historyId" :params="params"
        v-slot="{ loading, results: contents, totalMatches }">

        <Layout>

            <!-- we're going to want to make this optional for when we put multiple
                histories on the page, so pass the slot through from the parent -->
            <template #nav>
                <slot name="nav"></slot>
            </template>

            <template #details>
                <HistoryDetails class="history-details" :history="history" />
            </template>

            <template #messages>
                <HistoryMessages class="history-messages m-2" :history="history" />
                <HistoryEmpty v-if="history.empty" class="m-2" />
            </template>

            <template #listcontrols>
                <ContentOperations v-if="!history.empty"
                    :history="history"
                    :params.sync="params"
                    :total-matches="totalMatches"
                    :contents="contents"
                    :loading="loading"
                    :contentSelection.sync="listState.selected"
                    :showSelection.sync="listState.showSelection"
                />
            </template>

            <template #listing :class="{ loadingBackground: loading }">
                <HistoryContentList v-if="!history.empty"
                    :params.sync="params"
                    :contents="contents"
                    :loading="loading"
                    :scrolling.sync="listState.scrolling"
                />
            </template>

            <template #modals>
                <ToolHelpModal />
            </template>

        </Layout>
    </ContentProvider>
</template>

<script>

import { History, SearchParams } from "./model";
import ContentProvider from "./providers/HistoryContentProvider";
import Layout from "./Layout";
import HistoryMessages from "./HistoryMessages";
import HistoryDetails from "./HistoryDetails";
import HistoryEmpty from "./HistoryEmpty";
import { HistoryContentList } from "./ContentList";
import ContentOperations from "./ContentOperations";
import ToolHelpModal from "./ToolHelpModal";


export default {
    components: {
        ContentProvider,
        Layout,
        HistoryMessages,
        HistoryDetails,
        HistoryEmpty,
        ContentOperations,
        HistoryContentList,
        ToolHelpModal,
    },
    props: {
        history: { type: History, required: true },
    },
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
            listState: this.listState
        }
    },
    computed: {
        historyId() {
            return this.history.id;
        },
        params: {
            get() {
                return this.contentParams;
            },
            set(newParams) {
                if (SearchParams.equals(newParams, this.contentParams)) return;
                // reset paginaton if filters are different
                if (!SearchParams.filtersEqual(newParams, this.contentParams)) {
                    this.contentParams = newParams.resetLimits();
                    return;
                }
                this.contentParams = newParams.clone();
            }
        },
    },
    watch: {
        historyId(newId, oldId) {
            if (newId && newId !== oldId) {
                this.listState.selected = new Set();
                this.listState.expanded = new Set();
                this.listState.showSelection = false;
                this.params = new SearchParams();
            }
        },
        "listState.selected": function(newSet) {
            if (newSet.size > 0) {
                this.showSelection = true;
            }
        },
    },
}

</script>
