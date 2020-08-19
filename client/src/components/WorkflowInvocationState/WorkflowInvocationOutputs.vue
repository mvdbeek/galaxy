<template>
    <HistoryContentProvider
        :history="history"
        v-slot="{
            contents,
            bench,
            topRows,
            bottomRows,
            scrollStartKey,
            totalMatches,
            onListScroll,
            scrolling,
            loading,
            params,
            updateParams,
        }"
    >
        <Layout>
            <template v-slot:listcontrols v-if="contents.length > 0">
                <ContentOperations
                    :history="history"
                    :params="params"
                    @update:params="updateParams"
                    :total-matches="totalMatches || history.hid_counter - 1"
                    :contents="contents"
                    :loading="loading"
                    :content-selection.sync="listState.selected"
                    :show-selection.sync="listState.showSelection"
                />
    Contents: {{contents}}
            </template>

            <template v-slot:listing>
                <div :class="{ loadingBackground: loading }">
                    <VirtualScroller
                        key-field="hid"
                        :item-height="36"
                        :items="contents"
                        :bench="bench"
                        :top-placeholders="topRows"
                        :bottom-placeholders="bottomRows"
                        :scroll-start-key="scrollStartKey"
                        @scroll="onListScroll"
                        v-slot="{ item, index }"
                    >
                        <HistoryContentItem :item="item" :index="index" />
                    </VirtualScroller>
                </div>
            </template>

            <template v-slot:modals>
                <ToolHelpModal />
            </template>
        </Layout>
    </HistoryContentProvider>
</template>

<script>
import { History } from "components/History/model";
// import { SearchParams } from "./model/SearchParams";
import { HistoryContentProvider } from "components/History/providers";
import Layout from "components/History/Layout";
import HistoryMessages from "components/History/HistoryMessages";
import HistoryDetails from "components/History/HistoryDetails";
import HistoryEmpty from "components/History/HistoryEmpty";
import ContentOperations from "components/History/ContentOperations";
import ToolHelpModal from "components/History/ToolHelpModal";
import ListMixin from "components/History/ListMixin";
import VirtualScroller from "components/VirtualScroller";
import { HistoryContentItem } from "components/History/ContentItem";

export default {
    mixins: [ListMixin],
    components: {
        HistoryContentProvider,
        Layout,
        HistoryMessages,
        HistoryDetails,
        HistoryEmpty,
        ContentOperations,
        ToolHelpModal,
        VirtualScroller,
        HistoryContentItem,
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
            }
        },
    },
};
</script>
