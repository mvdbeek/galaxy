// Simple dataset provider, looks at api for result, renders to slot prop
import axios from "axios";
import { prependPath } from "utils/redirect"

export default {
    props: {
        typeId: { type: String, required: true }
    },
    data() {
        return {
            loading: false,
            dataset: null
        }
    },
    watch: {
        watch: {
            typeId: {
                immediate: true,
                handler(newVal, oldVal) {
                    if (newVal !== oldVal) {
                        this.load();
                    }
                }
            }
        }
    },
    methods: {
        async load() {
            this.loading = true;
            const url = prependPath(`/api/dataset/${this.typeId}`);
            const result = await axios.get(url);
            this.dataset = result;
            this.loading = false;
        },
        async save(newProps) {
            this.loading = true;
            const url = prependPath(`/api/dataset/${this.typeId}`);
            const result = await axios.put(url, newProps);
            this.dataset = result;
            this.loading = false;
        },
    },
    render() {
        return this.$scopedSlots.default({
            loading: this.loading,
            dataset: this.dataset,
            save: this.save
        });
    },
}
