/*
Collection contents provider
props.id = contents_url
*/

import { combineLatest } from "rxjs";
import { mergeMap, map, distinctUntilChanged, switchMap, debounceTime, pluck } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { loadDscContent, monitorDscQuery } from "../caching";
import { buildCollectionContentRequest } from "../caching/pouchQueries";
import { contentListMixin } from "./mixins";

export default {
    mixins: [contentListMixin],
    methods: {

        cacheObservable(url$, param$) {

            // cache watcher does not care about skip/limit
            const limitlessParam$ = param$.pipe(
                // tap(p => p.report("[dscpanel cachewatch] start")),
                map(p => p.resetPagination()),
                // tap(p => p.report("[dscpanel cachewatch] reset pagination")),
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(SearchParams.equals)
            );

            const cache$ = url$.pipe(
                switchMap(url => {
                    return limitlessParam$.pipe(
                        map(params => buildCollectionContentRequest([url, params])),
                        mergeMap(monitorDscQuery)
                    )
                })
            );

            return cache$;
        },


        loadingObservable(url$, param$) {

            // need to pad the range before we give it to the loader so we
            // load a little more than we're looking at right now
            const paddedParams$ = param$.pipe(
                // tap(p => p.report("[dscpanel loader] start")),
                map(p => p.pad()),
                // tap(p => p.report("[dscpanel loader] padded pagination")),
            );

            const load$ = combineLatest(url$, paddedParams$).pipe(
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(this.inputsSame),
                switchMap(loadDscContent),
            );

            return load$;
        },

    }
};
