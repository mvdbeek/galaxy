/**
 * Have to use a factory instead of something sane like a slot because
 * of the way VirtualList accepts its data-component parameter. It is annoying,
 * but the component works well, so I'm putting up with it for now.
 */

import { Subject } from "rxjs";
import { activity } from "utils/observable";
import { SearchParams } from "../model";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";
import VirtualList from "vue-virtual-scroll-list";

export const ContentListFactory = (ItemComponent) => ({
    mixins: [ vueRxShortcuts ],
    template: `
        <VirtualList
            v-on="$listeners"
            v-bind="$attrs"
            :data-component="itemComponent"
            :data-sources="contents"
            data-key="_id"
            :keeps="40"
            :estimate-size="36"
            wrap-tag="ul"
            item-tag="li"
            @scroll="onScroll"
        />
    `,
    components: {
        VirtualList,
    },
    props: {
        params: { type: SearchParams, required: true },
        contents: { type: Array, required: true },
        loading: { type: Boolean, required: false, default: false },
        scrolling: { type: Boolean, required: false, default: false },
    },
    computed: {
        itemComponent() {
            return ItemComponent;
        }
    },
    created() {
        this.scrollPing$ = new Subject();
        const scrolling$ = this.scrollPing$.pipe(activity());
        this.$subscribeTo(scrolling$, val => {
            this.$emit('update:scrolling', val);
        })
    },
    methods: {
        onScroll(evt, { start, end }) {
            this.scrollPing$.next(true);
            const newParams = this.params.setLimits(start, end);
            if (!SearchParams.equals(this.params, newParams)) {
                this.$emit("update:params", newParams);
            }
        },
    },
});
