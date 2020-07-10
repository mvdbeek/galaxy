// import { Subject } from "rxjs";
import { SearchParams } from "../model/SearchParams";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";

export default {
    mixins: [vueRxShortcuts],
    props: {
        dataKey: { type: String, required: true },
        params: { type: SearchParams, required: true },
        contents: { type: Array, required: true },
        loading: { type: Boolean, required: false, default: false },
        topRows: { type: Number, required: false, default: 0 },
        bottomRows: { type: Number, required: false, default: 0 },
        scrolling: { type: Boolean, required: false, default: false },
    },
    // created() {
    //     this.scrollPing$ = new Subject();
    //     const scrolling$ = this.scrollPing$.pipe(activity());
    //     this.$subscribeTo(scrolling$, (val) => {
    //         this.$emit("update:scrolling", val);
    //     });
    // },
    // methods: {
    //     onScroll({ start, end }) {
    //         this.scrollPing$.next(true);
    //         const newParams = this.params.setRange(start, end);
    //         if (!SearchParams.equals(this.params, newParams)) {
    //             this.$emit("update:params", newParams);
    //         }
    //     },
    // },
};
