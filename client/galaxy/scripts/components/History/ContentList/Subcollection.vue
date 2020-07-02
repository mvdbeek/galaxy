<!-- a separate collection content item for collections
    inside of other collections -->

<template>
    <div v-bind="$attrs" v-on="$listeners"
        class="collapsed" :data-state="dsc.state"
        @keydown.arrow-right.self.stop.prevent="eventHub.$emit('selectCollection', dsc)">

        <nav class="content-top-menu d-flex align-items-center justify-content-between p-1"
            @click.stop="eventHub.$emit('selectCollection', dsc)">

            <h5 class="flex-grow-1 overflow-hidden mr-auto text-nowrap text-truncate">
                <span class="name">{{ dsc.name }}</span>
                <span class="description">
                    ({{ dsc.collectionType | localize }} {{ dsc.collectionCount | localize }})
                </span>
            </h5>
        </nav>
    </div>
</template>

<script>

import { DatasetCollection } from "../model/DatasetCollection";

export default {
    props: {
        item: { type: Object, required: true },
        index: { type: Number, required: true },
    },
    computed: {
        dsc() {
            return new DatasetCollection(this.item);
        }
    },
};

</script>
