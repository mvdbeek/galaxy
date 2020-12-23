// Simple dataset provider, looks at api for result, renders to slot prop
import Vue from "vue";
import axios from "axios";
import { prependPath } from "utils/redirect";
import { cacheContent } from "../caching";

import { of } from "rxjs";
import { map } from "rxjs/operators";
import { monitorQuery } from "../caching/db/monitorQuery";
import { content$ } from "../caching/db/observables";

var SimpleProviderMixin = {
    props: {
        id: { type: String, required: true },
    },
    data() {
        return {
            loading: false,
            item: null,
        };
    },
    watch: {
        id: {
            immediate: true,
            handler(newVal, oldVal) {
                if (newVal !== oldVal) {
                    this.load();
                }
            },
        },
    },
    methods: {
        async load() {
            this.loading = true;
            const result = await axios.get(this.url);
            this.item = result.data;
            this.loading = false;
            const cachedContent = await cacheContent(result.data);
            console.log(this.item.id);
            console.log(cachedContent);
            const item_id = this.item.id;
            const selector = { id: item_id };
            const monitor$ = of({selector}).pipe(
                monitorQuery({db$: content$}),
                map((update) => {
                    console.log(update);
                    const { initialMatches = [], doc = null, deleted } = update;
                    if (deleted) {
                        return null;
                    }
                    let updatedDoc = doc;
                    if (initialMatches.length == 1) {
                        updatedDoc = initialMatches[0];
                    }
                    return updatedDoc;
                }),
            );
            this.$subscribeTo(monitor$, (doc) => {
                console.log(doc);
                if (doc) {
                    this.item = doc;
                }
            });
            await new Promise(r => setTimeout(r, 2000));
            const new_item = {...this.item};
            new_item.name = '123 hey';
            console.log('Updating now');
            await cacheContent(new_item);
            // monitor$.subscribe({
            //     next: result => {
            //         console.log(result);
            //         if (result) {
            //             this.item = result;
            //         }
            //     }
            // });

        },
        async save(newProps) {
            this.loading = true;
            const result = await axios.put(this.url, newProps);
            this.item = result.data;
            this.loading = false;
        },
    },
    render() {
        return this.$scopedSlots.default({
            loading: this.loading,
            item: this.item,
            save: this.save,
        });
    },
};

var DatasetProvider = Vue.extend({
    mixins: [SimpleProviderMixin],
    computed: {
        url() {
            return prependPath(`api/datasets/${this.id}`);
        },
    },
});

var DatasetCollectionProvider = Vue.extend({
    mixins: [SimpleProviderMixin],
    computed: {
        url() {
            return prependPath(`api/dataset_collections/${this.id}?instance_type=history`);
        },
    },
});

var DatasetCollectionContentProvider = Vue.extend({
    mixins: [SimpleProviderMixin],
    computed: {
        url() {
            // ugh ...
            return prependPath(this.id);
        },
    },
});

var JobProvider = Vue.extend({
    mixins: [SimpleProviderMixin],
    computed: {
        url() {
            return prependPath(`api/jobs/${this.id}?full=true`);
        },
    },
});

export { DatasetProvider, DatasetCollectionProvider, DatasetCollectionContentProvider, JobProvider };
