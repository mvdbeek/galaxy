/**
 * Have to use a factory instead of something sane like a slot because
 * of the way VirtualList accepts its data-component parameter. It is annoying,
 * but the component works well, so I'm putting up with it for now.
 */

import VirtualList from "vue-virtual-scroll-list";
import ContentListMixin from "./ContentListMixin";

export const ContentListFactory = (ItemComponent) => ({
    mixins: [ ContentListMixin ],
    template: `
        <VirtualList class="vvsl"
            v-on="$listeners"
            v-bind="$attrs"
            :data-component="itemComponent"
            :data-sources="contents"
            :data-key="dataKey"
            :keeps="30"
            :estimate-size="36.2"
            wrap-tag="ul"
            item-tag="li"
            @scroll="(evt, { start, end }) => onScroll(start, end)"
        />
    `,
    components: {
        VirtualList,
    },
    computed: {
        itemComponent() {
            return ItemComponent;
        }
    },
});
