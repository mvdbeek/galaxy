<!-- When a collection is selected, the panel shows the contents of that selection -->

<template>
    <DscProvider :is-root="isRoot" :collection="selectedCollection"
        v-slot="{ dsc }">

        <CollectionContentProvider v-if="dsc" :collection="dsc" :params="params"
            v-slot="{ loading, results: contents }">

            <Layout>
                <template #nav>
                    <TopNav :history="history"
                        :selected-collections="selectedCollections"
                        :show-tags.sync="showTags"
                        :show-filter.sync="showFilter"
                        v-on="$listeners" />
                </template>

                <template #details>
                    <Details :dsc="dsc" :writable="writable"
                        :show-tags.sync="showTags"
                        :show-filter.sync="showFilter"
                        @update:dsc="updateDsc(dsc, $event)" />
                </template>

                <template #listing>
                    <ContentList
                        :params="params"
                        :contents="contents"
                        :expanded-content="expandedContentIds"
                        :loading="loading" />
                </template>
            </Layout>

        </CollectionContentProvider>
    </DscProvider>
</template>


<script>

import { SearchParams, History, DatasetCollection } from "../model";
import { updateContentFields } from "../model/queries";
import { cacheContent } from "../caching";

import { DscProvider, CollectionContentProvider } from "../providers";
import { CollectionContentList as ContentList } from "../ContentList";
import Layout from "../Layout";
import TopNav from "./TopNav";
import Details from "./Details";


export default {
    components: {
        DscProvider,
        CollectionContentProvider,
        Layout,
        TopNav,
        Details,
        ContentList,
    },
    props: {
        history: { type: History, required: true },
        selectedCollections: { type: Array, required: true },
    },
    data: () => ({
        params: new SearchParams(),
        expandedContentIds: new Set(),
        showTags: false,
        showFilter: false,
        listState: {
            showSelection: false,
            selected: new Set(),
            expanded: new Set()
        }
    }),
    provide() {
        return {
            listState: this.listState
        }
    },
    computed: {
        selectedCollection() {
            const arr = this.selectedCollections;
            return arr[arr.length - 1];
        },
        isRoot() {
            return this.selectedCollection == this.selectedCollections[0];
        },
        writable() {
            return this.isRoot;
        },
    },
    methods: {

        // change the data of the root collection, anything past the root
        // collection is part of the dataset collection, which i believe is supposed to
        // be immutable, so only edit name, tags, blah of top-level selected collection,

        async updateDsc(collection, fields) {
            // console.log("updateDsc", this.writable, collection, fields);
            if (this.writable) {
                const ajaxResult = await updateContentFields(collection, fields);
                await cacheContent({ ...collection, ...ajaxResult });
            }
        },

        // expand/contract datasets
        // the virtual scrollers work better if the value for a dataset's
        // expanded status is known in the props going ito the array

        expandContent({ type_id }) {
            this.expandedContentIds = new Set(this.expandedContentIds.add(type_id));
        },
        collapseContent({ type_id }) {
            this.expandedContentIds = new Set(this.expandedContentIds.delete(type_id));
        },
        toggleExpand({ type_id }) {
            const newSet = new Set(this.expandedContentIds);
            newSet.has(type_id) ? newSet.delete(type_id) : newSet.add(type_id);
            this.expandedContentIds = newSet;
        },
        collapseAllContent() {
            this.expandedContentIds = new Set();
        },
    },
    created() {
        this.eventHub.$on("expandContent", this.expandContent);
        this.eventHub.$on("collapseContent", this.collapseContent);
        this.eventHub.$on("toggleExpand", this.toggleExpand);
        this.eventHub.$on("collapseAllContent", this.collapseAllContent);
    }
};
</script>
