import hash from "object-hash";

/**
 * Builds a provider that gets its result from a single promise-based query function and
 * caches the result of lookup for subsequent instantiations.
 *
 * @param   {Function}  lookup  async function that loads the result, parameters will be an object
 *                              whose properties are the attributes assigned to the provider component
 * @return  {VueComponentOptions} Vue component options definition
 */
export const SingleQueryProvider = (lookup) => {
    const promiseCache = new Map();

    return {
        props: {
            useCache: {
                type: Boolean,
                default: true,
            },
        },
        data() {
            return {
                result: undefined,
                error: undefined,
            };
        },
        computed: {
            loading() {
                return this.result === undefined;
            },
            cacheKey() {
                return hash(this.$attrs || {});
            },
        },
        mounted() {
            let lookupPromise;
            if (this.useCache) {
                lookupPromise = promiseCache.get(this.cacheKey);
                if (!lookupPromise) {
                    lookupPromise = lookup(this.$attrs);
                    promiseCache.set(this.cacheKey, lookupPromise);
                }
            } else {
                lookupPromise = lookup(this.$attrs);
            }
            lookupPromise.then(
                (result) => {
                    this.result = result;
                },
                (err) => {
                    this.result = {};
                    this.error = err;
                    this.$emit("error", err);
                }
            );
        },
        render() {
            return this.$scopedSlots.default({
                loading: this.loading,
                result: this.result,
                error: this.error,
            });
        },
    };
};
