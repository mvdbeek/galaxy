<!-- a separate collection content item for collections
    inside of other collections -->

<template>
    <div
        class="collapsed"
        :data-state="dsc.state"
        @keydown.arrow-right.self.stop.prevent="eventHub.$emit('selectCollection', dsc)"
    >
        <nav
            class="content-top-menu d-flex align-items-center justify-content-between"
            @click.stop="eventHub.$emit('selectCollection', dsc)"
        >
            <!--
            <div class="d-flex mr-1 align-items-center" @click.stop>

                <StatusIcon v-if="dsc.state != 'ok'"
                    class="status-icon px-1"
                    :state="dsc.state"
                    @click.stop="onStatusClick" />

                <StateBtn v-if="!dsc.visible"
                    class="px-1"
                    state="hidden"
                    title="Unhide"
                    icon="fa fa-eye-slash"
                    @click.stop="$emit('unhideCollection')" />

                <StateBtn class="px-1"
                    state="ok"
                    title="Collection"
                    icon="fas fa-folder"
                    @click.stop="$emit('selectCollection', dsc)" />
            </div>
            -->

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
import { DatasetCollection, collectionTypeDescription } from "../model/DatasetCollection";

export default {
    props: {
        item: { type: Object, required: true },
        index: { type: Number, required: true },
    },
    computed: {
        dsc() {
            return new DatasetCollection(this.item);
        },
        collectionType() {
            return collectionTypeDescription(this.item.object.collection_type);
        },
    },
};
</script>
