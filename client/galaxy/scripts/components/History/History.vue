<template>
    <HistoryContentProvider :history-id="historyId" :params="params" :debounce-period="500"
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
                    data-key="_id"
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
    </HistoryContentProvider>
</template>


<script>

import { History } from "./model";
import { SearchParams } from "./model/SearchParams";
import { HistoryContentProvider } from "./providers";
import Layout from "./Layout";
import HistoryMessages from "./HistoryMessages";
import HistoryDetails from "./HistoryDetails";
import HistoryEmpty from "./HistoryEmpty";
import { HistoryContentList } from "./ContentList";
import ContentOperations from "./ContentOperations";
import ToolHelpModal from "./ToolHelpModal";
import ListMixin from "./ListMixin";

export default {
    mixins: [ ListMixin ],
    components: {
        HistoryContentProvider,
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
    computed: {
        historyId() {
            return this.history.id;
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
    },
}

</script>
