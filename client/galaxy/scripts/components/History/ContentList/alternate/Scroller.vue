<!-- this is a better virtual scroller api but it's buggy and slow. :( -->

<template>
    <div class="vvs" :class="{ loadingBackground: loading }"
        v-bind="$attrs">

        <DynamicScroller
            :items="items"
            :min-item-size="36"
            :emit-update="true"
            v-on="$listeners">

            <template v-slot:default="{ item, index, active }">
                <DynamicScrollerItem
                    :item="item"
                    :active="active"
                    :data-index="index"
                    :size-dependencies="[ item.expanded ]">
                    <slot :item="item" :active="active" :index="index">
                        <pre>{{ item }}</pre>
                    </slot>
                </DynamicScrollerItem>
            </template>

        </DynamicScroller>

    </div>
</template>


<script>

import { DynamicScroller, DynamicScrollerItem } from "vue-virtual-scroller";

export default {
    components: {
        DynamicScroller,
        DynamicScrollerItem,
    },
    props: {
        items: { type: Array, required: true },
        loading: { type: Boolean, required: false, default: false },
    },
};

</script>

<style lang="css" src="vue-virtual-scroller/dist/vue-virtual-scroller.css"></style>
