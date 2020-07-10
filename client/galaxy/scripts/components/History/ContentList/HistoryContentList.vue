<template>

    <VirtualScroller
        v-on="$listeners"
        v-bind="$attrs"
        :key-field="dataKey"
        :item-height="36"
        :items="contents"
        :bench="10"
        :top-buffer="topRows"
        :bottom-buffer="bottomRows"
        v-slot="{ item, index }">

        <HistoryContentItem :item="item" :index="index" />

    </VirtualScroller>

</VirtualScroller>

</template>

<script>

import HistoryContentItem from "./HistoryContentItem";
import VirtualScroller from "./VirtualScroller";
import ContentList from "./ContentList";

export default {
    mixins: [ ContentList ],
    components: {
        VirtualScroller,
        HistoryContentItem
    }
}

</script>