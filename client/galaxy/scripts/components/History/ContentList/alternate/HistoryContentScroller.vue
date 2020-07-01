<template>
    <Scroller :items="contents" :loading="loading" @update="onScroll"
        v-slot="{ item, index, active }">
        <HistoryContentItem :source="item" :index="index" />
    </Scroller>
</template>

<script>

import Scroller from "./Scroller";
import HistoryContentItem from "../HistoryContentItem";
import ContentListMixin from "../ContentListMixin";

export default {
    mixins: [ ContentListMixin ],
    components: {
        Scroller,
        HistoryContentItem
    },
}

</script>