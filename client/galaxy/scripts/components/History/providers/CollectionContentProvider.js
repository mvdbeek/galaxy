/*
Collection contents provider
props.id = contents_url
*/

import { map, distinctUntilChanged, switchMap, debounceTime, startWith, scan } from "rxjs/operators";
import { SearchParams } from "../model/SearchParams";
import { loadDscContent, monitorDscQuery } from "../caching";
import { buildCollectionContentRequest } from "../caching/pouchUtils";
import ContentProviderMixin from "./ContentProviderMixin";

export default {
    mixins: [ContentProviderMixin],
    computed: {
        cacheObservable() {
            const url$ = this.id$;

            const limitlessParam$ = this.param$.pipe(
                // tap(p => p.report("[dscpanel cachewatch] start")),
                map((p) => p.resetPagination()),
                // tap(p => p.report("[dscpanel cachewatch] reset pagination")),
                debounceTime(this.debouncePeriod),
                distinctUntilChanged(SearchParams.equals)
            );

            // We want to switchMap on url, mergeMap on params. This gives us
            // the option of incrementally updating a result-set inside the
            // provider as params change which may be necessary for big lists
            const cacheUpdates$ = url$.pipe(
                switchMap((url) => {
                    return limitlessParam$.pipe(
                        map((params) => buildCollectionContentRequest([url, params])),
                        monitorDscQuery(),
                        startWith({ matches: [] })
                    );
                })
            );

            const result$ = cacheUpdates$.pipe(
                scan((results, response) => {
                    if (response.matches) return response.matches;
                    return results;
                }, [])
            );

            return result$;
        },

        loadingObservable() {
            // contents_url is the "parent" id for collections
            const url$ = this.id$;

            const loader$ = url$.pipe(
                switchMap(url => this.param$.pipe(
                    map(p => [url, p]),
                    loadDscContent()
                ))
            );

            return loader$;
        },
    },
};
