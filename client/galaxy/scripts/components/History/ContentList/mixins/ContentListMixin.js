import { Subject } from "rxjs";
import { activity } from "utils/observable/activity";
import { SearchParams } from "../../model/SearchParams";
import { vueRxShortcuts } from "../../../plugins/vueRxShortcuts";

export default {
    mixins: [ vueRxShortcuts ],
    props: {
        dataKey: { type: String, required: true },
        params: { type: SearchParams, required: true },
        contents: { type: Array, required: true },
        loading: { type: Boolean, required: false, default: false },
        scrolling: { type: Boolean, required: false, default: false },
    },
    created() {
        this.scrollPing$ = new Subject();
        const scrolling$ = this.scrollPing$.pipe(activity());
        this.$subscribeTo(scrolling$, val => {
            this.$emit('update:scrolling', val);
        })
    },
    methods: {
        onScroll(start, end) {
            // console.log("onScroll", start, end);
            this.scrollPing$.next(true);
            const newParams = this.params.clone();
            newParams.skip = start;
            newParams.limit = end - start;
            if (!SearchParams.equals(this.params, newParams)) {
                // newParams.report("update:params");
                this.$emit("update:params", newParams);
            }
        },
        atTop() {
            console.log("atTop", ...arguments);
            // const moreTop = this.params.clone();
            // moreTop.limit += SearchParams.chunkSize;
        },
        atBottom() {
            this.params.report("atBottom");
            const moreBottom = this.params.clone();
            moreBottom.limit += SearchParams.chunkSize;
            moreBottom.report("Morebottom");
            this.$emit("update:params", moreBottom);
        }
    },
}
