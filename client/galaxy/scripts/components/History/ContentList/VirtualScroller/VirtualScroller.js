import Scroll from './Scroll';
import "./scroller.scss";

// dumb formatter
export function cssLength(str, unit = 'px') {
    if (str == null || str === '') {
        return undefined
    } else if (isNaN(+str)) {
        return String(str)
    } else {
        return `${Number(str)}${unit}`
    }
}

export default {
    directives: {
        Scroll
    },
    props: {
        items: { type: Array, default: () => [] },
        keyField: { type: String, required: true },
        minItemHeight: { type: Number, required: true },
        // bench: { type: Number, default: 0 },
    },
    data() {
        return {
            scrollTop: 0, // We determine everything based on this
            sliceSize: 10, // guess initial value
        }
    },
    mounted() {
        // adjust slice size to size of container
        this.sliceSize = this.getSliceSize();
    },
    computed: {

        // first visible row, disregarding bench
        first() {
            return Math.floor(this.scrollTop / this.minItemHeight);
        },

        // last row that should be visible, disregarding bench
        last() {
            return this.first + this.sliceSize;
        },

        range() {
            return { start: this.first, end: this.last };
        },

        // height of the scrolling region including padding
        fullHeight() {
            return Math.max(100000, this.minItemHeight * this.items.length);
        },

        topPadding() {
            return this.scrollTop;
        },

        bottomPadding() {
            return this.fullHeight - this.scrollTop;
        },

        // data index for the first bench row
        // benchFirst() {
        //     return Math.max(0, this.first - this.bench)
        // },
        // data index for the last bench row
        // benchLast() {
        //     return Math.min(this.items.length, this.last + this.bench)
        // },

    },

    watch: {
        height: 'onScroll',
        minItemHeight: 'onScroll',
        range(newRange) {
            this.$emit('scroll', newRange);
        }
    },

    methods: {

        // gets last index by assuming minimum heights, worse case scenario
        // is we have a few extra rows at the bottom. Can't be calculated
        // because depends on rendered element height, have to call on mounted
        // or updated
        getSliceSize() {
            return Math.ceil(this.$el.clientHeight / this.minItemHeight);
        },

        onScroll() {
            this.scrollTop = this.$el.scrollTop;
        },

        // Rendering funcs

        renderList(from, to) {
            return this.items.slice(from, to).map(this.renderItem);
        },

        renderItem(item, i) {
            const key = item[this.keyField];
            const h = this.$createElement;
            const index = i + this.benchFirst
            const slotChild = this.renderSlot('default', { key, index, item });
            return h('li', { key }, slotChild);
        },

        renderSlot(name = 'default', data, optional = false) {
            if (this.$scopedSlots[name]) {
                return this.$scopedSlots[name](data instanceof Function ? data() : data)
            } else if (this.$slots[name] && (!data || optional)) {
                return this.$slots[name]
            }
            return undefined;
        }

    },

    render(h) {

        // Top Bench (may not be needed)
        // const benchList = h('ul', {}, this.renderList(this.benchFirst, this.first));
        // const bench = h('div', { staticClass: "bench" }, [ benchList ])

        // Main list
        const content = h('ul', {
            staticClass: "slice",
            style: {
                paddingBottom: cssLength(this.bottomPadding)
            },
        }, this.renderList(this.first, this.last));

        // wrap lists in a div of fixed height
        const wrapper = h('div', {
            style: {
                paddingTop: cssLength(this.topPadding),
                // transform: `translateY(${cssLength(this.topPadding)})`
            },
        }, [content]);

        // list container
        return h('div', {
            staticClass: 'virtual-scroller',
            directives: [{
                name: 'scroll',
                modifiers: { self: true },
                value: this.onScroll,
            }],
        }, [wrapper])
    },
}
