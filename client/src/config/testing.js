export default {
    name: "unit testing configs",
    testBuild: true,
    debug: false,
    caching: {
        adapter: "idb",
        revs_limit: 5,
        deterministic_revs: false,
        auto_compaction: false
    }
}
