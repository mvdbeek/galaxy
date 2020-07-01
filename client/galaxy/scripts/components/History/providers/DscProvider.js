import { combineLatest } from "rxjs";
import { debounceTime, filter, map, pluck, switchMap, distinctUntilChanged } from "rxjs/operators";
import { vueRxShortcuts } from "../../plugins/vueRxShortcuts";
import { monitorContentQuery, monitorDscQuery } from "../caching";
import { DatasetCollection } from "../model";

export default {
    mixins:[ vueRxShortcuts ],
    props: {
        collection: { type: Object, required: true },
        isRoot: { type: Boolean, required: true },
    },
    data: () => ({
        dsc: null
    }),
    created() {

        // Watching either content or dscContent depending on whether this is the root
        // Really the only thing this is changing is the collection the worker will monitor
        // It will be either "galaxy-content" or "galaxy-collection-content" depending
        // on how far in we've drilled down.
        const cacheWatcher$ = this.watch$('isRoot', true).pipe(
            map(val => val ? monitorContentQuery : monitorDscQuery)
        );

        // assemble pouchdb.find config for just the one row
        const request$ = this.watch$('collection', true).pipe(
            pluck('_id'),
            distinctUntilChanged(),
            map(_id => ({ selector: { _id } }))
        );

        const liveResults = combineLatest(request$, cacheWatcher$).pipe(
            debounceTime(0),
            switchMap(([request, cacheWatcher]) => cacheWatcher(request)),
            pluck('matches'),
            filter(matches => matches.length > 0),
            map(matches => new DatasetCollection(matches[0]))
        );

        this.$subscribeTo(liveResults, dsc => this.dsc = dsc);

    },
    render() {
        return this.$scopedSlots.default({
            dsc: this.dsc
        });
    },
}