<template>

    <VirtualScroller
        v-on="$listeners"
        v-bind="$attrs"
        :items="contents"
        :key-field="dataKey"
        :min-item-height="36"
        @scroll="onScroll"
        v-slot="{ item, index }">

        <HistoryContentItem :item="item" :index="index" />

    </VirtualScroller>

</template>

<script>

import HistoryContentItem from "./HistoryContentItem";
import VirtualScroller from "./VirtualScroller";
import ContentListMixin from "./mixins/ContentListMixin";

export default {
    mixins: [ ContentListMixin ],
    components: {
        VirtualScroller,
        HistoryContentItem
    }
}

</script>