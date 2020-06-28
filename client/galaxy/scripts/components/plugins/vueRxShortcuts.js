import Vue from "vue";
import VueRx from "vue-rx";
import { pluck } from "rxjs/operators";

Vue.use(VueRx);

export const vueRxShortcuts = {
    methods: {
        /**
         * This is almost always how we're going to want to "watchAsObservable" and it's shorter
         * @param {string} propName Member to watch
         * @param {boolean} immediate Check right now?
         * @returns Observable of new value
         */
        watch$(propName, immediate = true) {
            const opts = { immediate };
            const watchedProp = this.$watchAsObservable(propName, opts);
            return watchedProp.pipe(pluck("newValue"));
        },
    },
};
