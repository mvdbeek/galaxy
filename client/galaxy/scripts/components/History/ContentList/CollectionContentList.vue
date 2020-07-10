<template>

    <VirtualScroller
        v-on="$listeners"
        v-bind="$attrs"
        :items="contents"
        :key-field="dataKey"
        :min-item-height="36"
        @scroll="onScroll"
        v-slot="{ item, index }">

        <CollectionContentItem :item="item" :index="index" />

    </VirtualScroller>

</template>

<script>

import CollectionContentItem from "./CollectionContentItem";
import VirtualScroller from "./VirtualScroller";
import ContentList from "./ContentList";

export default {
    mixins: [ ContentList ],
    components: {
        VirtualScroller,
        CollectionContentItem
    }
}

</script>