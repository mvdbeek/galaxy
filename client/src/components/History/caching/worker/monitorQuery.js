import { Observable, isObservable, combineLatest } from "rxjs";
import { switchMap, debounceTime, distinctUntilChanged } from "rxjs/operators";
import deepEqual from "deep-equal";

/**
 * Turns a selector into a live cache result emitter.
 *
 * @param {Observable} db$ Observable PouchDB instance
 * @param {Observable} request$ Observable Pouchdb-find configuration
 */
export const monitorQuery = (cfg = {}) => (request$) => {
    const {
        // pouch database to monitor
        db$ = null,
        // how often to create a new query monitor
        inputDebounce = 250,
    } = cfg;

    if (!isObservable(db$)) {
        throw new Error("Please pass a database observable to the configuration of monitorQuery");
    }

    const req$ = request$.pipe(debounceTime(inputDebounce), distinctUntilChanged(deepEqual));

    // this is the actual emitter that watches the cache, it is customized
    // to a specific db and query\
    return combineLatest(db$, req$).pipe(
        debounceTime(0),
        switchMap(([db, req]) => {
            return pouchQueryEmitter(db, {
                ...req,
                aggregate: false,
            });
        })
    );
};

/**
 * Build an observable that monitors a pouchdb instance by taking a pouchdb-find
 * select config and returning matching results when the cache changes.
 *
 * @param {PouchDB} db PouchDB instance
 * @param {Object} request pouchdb find config
 */
function pouchQueryEmitter(db, request) {
    return Observable.create((obs) => {
        const feed = db.liveFind(request);
        feed.on("update", (update) => obs.next(update));
        feed.on("error", (err) => obs.error(err));
        return () => feed.cancel();
    });
}
