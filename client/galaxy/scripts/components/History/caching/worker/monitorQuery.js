import { of, Observable, combineLatest } from "rxjs";
import { map, share, switchMap, shareReplay, scan, debounceTime } from "rxjs/operators";
// import { SearchParams } from "../../model";
import hash from "object-hash";
import { result } from "underscore";
// import deepEqual from "fast-deep-equal";


/**
 * Turns a selector into a live cache result emitter.
 *
 * @param {Observable} db$ PouchDB observable
 * @param {object} request Pouchdb find configuration selector
 */
export const monitorQuery = (db$, cfg = {}) => request => {

    const { debouncePeriod = 250 } = cfg;

    // incoming request
    const request$ = of(request).pipe(share());

    // selector with just the filters, will return entire matching set
    const filters$ = request$.pipe(
        map(({ skip, limit, ...requestNoLimits }) => requestNoLimits)
    );

    // this is the actual emitter that watches the cache, it is customized
    // to a specific db (content/collection content) and query
    const watcher$ = combineLatest(filters$, db$).pipe(
        switchMap(inputs => getWatcher(...inputs)),
    );

    // assemble a subset of the total matches around the region the user
    // is currently staring at, by using pagination + the full result set
    const summary$ = combineLatest(watcher$, request$).pipe(
        debounceTime(100),
        map(inputs => {
            const [ { feed, matches }, request ] = inputs;
            // const { skip, limit, sort } = request;

            // // add an index for the virtual scroller
            // for (let i = 0, len = allMatches.length; i < len; i++) {
            //     allMatches[i]._scroll_index = i;
            // }

            // // sort & paginate
            // const matches = feed.paginate({ skip, limit, sort });

            return { request, matches, totalMatches: matches.length };
        })
    );

    return summary$;
}



/**
 * Pool of query emittters, keep these live inside the worker
 * so they should all be hot observables (shareReplay(1))
 */

const watchers = new Map();

function getWatcherKey(selector, db) {
    return hash({ selector, databaseName: db.name });
}

function getWatcher(selector, db) {
    const key = getWatcherKey(selector, db);
    if (!watchers.has(key)) {
        watchers.set(key, createQueryWatcher(selector, db));
    }
    return watchers.get(key);
}


/**
 * Live observer of cache, emits changes to the cache.
 *
 * @param {object} selector Pouch Db find selector
 * @param {PouchDB} db Pouch database instance
 */
function createQueryWatcher(selector, db) {
    return pouchQueryEmitter(selector, db, false).pipe(
        scan((results, { feed, matches }) => {
            return { feed, matches };
        }, {}),
        shareReplay(1),
    );
}


/**
 * Build an observable that monitors a pouchdb instance by taking a pouchdb-find
 * select config and returning matching results when the cache changes.
 *
 * @param {Object} request pouchdb find config
 * @param {PouchDB} db pouch database instance
 */
export function pouchQueryEmitter(request, db) {

    return Observable.create((obs) => {

        let lastMatches = [];

        const feed = db.liveFind({
            ...request,
            aggregate: true
        });

        feed.on("update", (update, matches) => {
            obs.next({ feed, matches });
            lastMatches = matches;
        });

        feed.on("ready", () => {
            obs.next({ feed, matches: lastMatches })
        });

        feed.on("error", (err) => obs.error(err));

        return () => feed.cancel();
    });
}
