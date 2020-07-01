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
                        data-key="_id"
                        :params="params"
                        :contents="contents"
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
import ListMixin from "../ListMixin";

export default {
    mixins: [ ListMixin ],
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
        showTags: false,
        showFilter: false,
    }),
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

    }
};
</script>
