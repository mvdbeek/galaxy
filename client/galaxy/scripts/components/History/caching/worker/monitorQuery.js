import { of, Observable, combineLatest } from "rxjs";
import { map, share, switchMap, shareReplay, debounceTime } from "rxjs/operators";
import hash from "object-hash";
// import { SearchParams } from "../../model/SearchParams";
// import deepEqual from "deep-equal";


/**
 * Turns a selector into a live cache result emitter.
 *
 * @param {Observable} db$ PouchDB observable
 * @param {object} request Pouchdb find configuration selector
 */
export const monitorQuery = (db$, cfg = {}) => request => {
    const { debouncePeriod = 100 } = cfg;

    // incoming request
    const request$ = of(request).pipe(share());

    // selector with just the filters, will return entire matching set
    const filters$ = request$.pipe(
        map(({ skip, limit, ...requestNoLimits }) => requestNoLimits)
    );

    // this is the actual emitter that watches the cache, it is customized
    // to a specific db and query
    const watcher$ = combineLatest(filters$, db$).pipe(
        debounceTime(0),
        switchMap(inputs => getWatcher(...inputs)),
        debounceTime(debouncePeriod),
        map(({ /* feed, */ matches, request }) => {
            return { matches, request };
        })
    );

    return watcher$;
}

// sort & paginate, guess not necessary?
// const { skip, limit, sort } = request;
// const matches = feed.paginate({ skip, limit, sort });


/**
 * Pool of query emittters, keep these live inside the worker
 * so they should all be hot observables (shareReplay(1))
 */

const watchers = new Map();

function getWatcherKey(selector, db) {
    return hash({ selector, databaseName: db.name });
}

function getWatcher(request, db) {
    const key = getWatcherKey(request, db);
    if (!watchers.has(key)) {
        const newWatcher$ = pouchQueryEmitter(request, db).pipe(shareReplay(1))
        watchers.set(key, newWatcher$);
    }
    return watchers.get(key);
}


/**
 * Build an observable that monitors a pouchdb instance by taking a pouchdb-find
 * select config and returning matching results when the cache changes.
 *
 * @param {Object} request pouchdb find config
 * @param {PouchDB} db pouch database instance
 */
function pouchQueryEmitter(request, db) {

    return Observable.create((obs) => {

        let lastMatches = [];

        const feed = db.liveFind({ ...request, aggregate: true });

        feed.on("update", (update, matches) => {
            obs.next({ feed, matches, request });
            lastMatches = matches;
        });

        feed.on("ready", () => {
            obs.next({ feed, matches: lastMatches, request })
        });

        feed.on("error", (err) => obs.error(err));

        return () => feed.cancel();
    });
}
