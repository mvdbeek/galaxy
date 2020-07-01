<template>
    <Scroller :items="contents" :loading="loading" @update="onScroll"
        v-slot="{ item, index, active }">
        <CollectionContentItem :source="item" :index="index" />
    </Scroller>
</template>

<script>

import Scroller from "./Scroller";
import CollectionContentItem from "../CollectionContentItem";
import ContentListMixin from "../ContentListMixin";

export default {
    mixins: [ ContentListMixin ],
    components: {
        Scroller,
        CollectionContentItem
    }
}

</script>
