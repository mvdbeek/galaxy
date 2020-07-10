import Scroll from "./Scroll";
import Resize from "./Resize";
import "./scroller.scss";


// dumb formatter
export function cssLength(str, unit = 'px') {
    if (str == null || str === '') {
        return undefined
    } else if (isNaN(+str)) {
        return String(str)
    } else {
        const val = Number(str);
        return `${val}${unit}`
    }
}


export default {

    directives: {
        Scroll,
        Resize
    },

    props: {
        // list of data objects
        items: { type: Array, required: true },

        // field from the objects in items to use as a key for the v-for loop
        keyField: { type: String, required: true },

        // used to determine the number of rows to render, doesn't need to be
        // perfect, should be a rough estimate, but this is the size rows will
        // be smashed into when they are in the bench region
        itemHeight: { type: Number, required: true },

        // number of items from the top of the list to keep in reserve in case
        // the user scrolls upward, changes the starting render index
        bench: { type: Number, default: 0 },

        // since we are rendering very large lists and a lot of the data may not
        // yet be available in the cache, the items array represents a local
        // window in the complete set. These two numbers are used to approximate
        // the number of rows above and below that window in order to make the
        // scrollbar proportionately sized.
        topBuffer: { type: Number, default: 0 },
        bottomBuffer: { type: Number, default: 0 },

        // some browsers have an upper limit on element of around a million,
        // which we will go way over
        maxHeight: { type: Number, default: 10000 },
    },

    data() {
        return {
            scrollTop: 0,

            // dom height of the contents of the scroller
            contentHeight: 0,

            // com height of the container
            scrollerHeight: null,
        }
    },

    watch: {
        range(newRange) {
            const { scrollTop, contentHeight, fraction } = this;

            this.$emit("scroll", {
                ...newRange,
                scrollTop,
                contentHeight,
                fraction
            });
        }
    },

    mounted() {
        this.scrollTo(this.bufferPaddingTop);
    },

    computed: {

        range() {
            return {
                start: this.first + this.topBuffer,
                end: this.last + this.topBuffer
            }
        },

        fraction() {
            return (this.contentHeight > 0) ? this.scrollTop / this.contentHeight : 0;
        },


        // first visible index
        first() {
            const scrollTop = this.scrollTop - this.bufferPaddingTop;
            const rowsAboveLine = 1.0 * scrollTop / this.itemHeight;
            const firstIndex = Math.floor(rowsAboveLine);
            // console.log(">> compute: first", firstIndex);
            return firstIndex;
        },

        // first rendered index
        benchFirst() {
            const idx = Math.max(0, this.first - this.bench);
            // console.log(">> compute: benchFirst", idx);
            return idx;
        },

        // last visible index
        last() {
            const idx = this.first + this.visibleRowEstimate;
            // console.log(">> compute: last", idx);
            return idx;
        },

        // number of rows to render starting at benchFirst
        sliceSize() {
            const len = Math.max(0, this.first - this.benchFirst) + this.visibleRowEstimate + this.bench;
            // console.log(">> compute: sliceSize", len);
            return len;
        },

        // guess a reasonable number of rows to render based on container height and
        // minimum row height
        visibleRowEstimate() {
            const rows = Math.ceil(this.scrollerHeight / this.itemHeight);
            // console.log(">> compute: visibleRowEstimate", rows);
            return rows;
        },

        // padding representing non-rendered rows above the bench
        paddingTop() {
            const padding = Math.max(0, this.first - this.bench) * this.itemHeight;
            // console.log(">> compute paddingTop", padding);
            return padding;
        },

        // padding representing non-rendered rows below the slice, probably
        // doesn't have to be perfect
        paddingBottom() {
            const bottomRows = Math.max(0, this.items.length - this.benchFirst - this.sliceSize);
            const padding = bottomRows * this.itemHeight;
            // console.log(">> compute paddingBottom", padding);
            return padding;
        },


        // spacing representing rows that were not provided to content but need
        // to be represented by the scroll bar
        bufferPaddingTop() {
            return this.topBuffer * this.itemHeight;
        },

        // ...same on the bottom
        bufferPaddingBottom() {
            return this.bottomBuffer * this.itemHeight;
        },

    },

    methods: {

        // scrolling recalculates the first index from the scrolltop

        onScroll() {
            if (!this.suppressScrollEvent) {
                this.scrollTop = this.$el.scrollTop;
                // console.warn("<<<<< setting scrollTop", this.scrollTop);
            }
        },


        // Resizing of various elements, need to keep track of the height of the
        // scroller, the height of the rendered content (because items can
        // expand/contract and otherwise change size) and the individual heights
        // of those items.

        onContainerResize(height) {
            if (height !== this.scrollerHeight) {
                // console.warn("<<<<< setting scrollerHeight", height);
                this.scrollerHeight = height;
            }
        },

        onContentResize(height) {
            if (height !== this.contentHeight) {
                this.contentHeight = height;
            }
        },


        // Scrolling: using these methods does not trigger the normal scroll event

        scrollToIndex(n) {
            const ht = this.getHeightFromRow(n);
            this.scrollTo(ht);
        },

        scrollTo(height) {
            this.suppressScrollEvent = true;
            this.$refs.scroller.scrollTop = height;
            setTimeout(() => {
                this.suppressScrollEvent = false;
            }, 0)
        },




        // Rendering

        renderList() {
            const list = this.items.slice(this.benchFirst, this.benchFirst + this.sliceSize);
            return list.map(this.renderItem);
        },

        renderItem(item, sliceIndex) {
            const key = item[this.keyField];
            const index = sliceIndex + this.benchFirst; // data index
            const isBench = index < this.first;

            const h = this.$createElement;
            const slotChild = this.renderSlot('default', { key, index, item });

            return h('li', {
                key,
                class: {
                    first: index == this.first,
                    benchFirst: index == this.benchFirst,
                    bench: isBench
                },
                // force bench items to be itemHeight tall regardless of
                // whatever's going on with their normal rendering, this makes
                // all the rendering math a lot faster
                style: {
                    height: isBench ? `${cssLength(this.itemHeight)} !important` : ''
                },
                attrs: {
                    "data-index": index,
                    "data-key": key
                },
            }, slotChild);
        },

        renderSlot(name = 'default', data, optional = false) {
            if (this.$scopedSlots[name]) {
                return this.$scopedSlots[name](data instanceof Function ? data() : data)
            } else if (this.$slots[name] && (!data || optional)) {
                return this.$slots[name]
            }
            return undefined;
        },

    },

    render(h) {

        // simple ul, each item is a slot inside a LI

        const list = h('ul', {}, this.renderList());


        // wrapper around content, houses topPadding + bottomPadding + ul
        // this wrapper handles the normal paddingTop/paddingBottom which
        // represent non-rendered rows in the dataset

        const wrapper = h('div', {
            style: {
                paddingTop: cssLength(this.paddingTop),
                paddingBottom: cssLength(this.paddingBottom),
            },
        }, [list]);


        // This div handles the topBuffer and bottomBuffer values which is extra
        // spacing meant to represent rows which were not provided to the items
        // array in the event that items is a small slice of a very very large
        // dataset. Essentially this is to keep the scrollbars looking roughly right

        const bufferWrapper = h('div', {
            ref: 'content',
            staticClass: 'scrollContent',
            style: {
                paddingTop: cssLength(this.bufferPaddingTop),
                paddingBottom: cssLength(this.bufferPaddingBottom),
            },
            directives: [
                { name: 'resize', value: this.onContentResize }
            ]
        }, [ wrapper ]);


        // container, fixed height, wrapper is longer and scrolls within this

        return h('div', {
            staticClass: 'virtualScroller',
            ref: 'scroller',
            directives: [
                { name: 'scroll', modifiers: { self: true }, value: this.onScroll },
                { name: 'resize', value: this.onContainerResize }
            ],
        }, [ bufferWrapper ])
    },
}
