import { Observable, isObservable } from "rxjs";
import { switchMap, debounceTime, withLatestFrom, distinctUntilChanged } from "rxjs/operators";
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
        inputDebounce = 0,
        // how often to emit query monitor results
        outputDebounce = 0,
    } = cfg;

    if (!isObservable(db$)) {
        const msg = `
            Please pass a database observable to the
            configuration of monitorQuery
        `;
        console.error(msg);
        throw new Error(msg);
    }

    // selector with just the filters, will return entire matching set
    // trim off skip/limit, only emit when actual filters change
    const filters$ = request$.pipe(
        // map(({ skip, limit, ...requestNoLimits }) => requestNoLimits),
        distinctUntilChanged(deepEqual)
    );

    // this is the actual emitter that watches the cache, it is customized
    // to a specific db and query
    return filters$.pipe(
        withLatestFrom(db$),
        debounceTime(inputDebounce),
        switchMap((inputs) => pouchQueryEmitter(...inputs)),
        debounceTime(outputDebounce)
    );
};

/**
 * Build an observable that monitors a pouchdb instance by taking a pouchdb-find
 * select config and returning matching results when the cache changes.
 *
 * @param {Object} request pouchdb find config
 * @param {PouchDB} db pouch database instance
 */
function pouchQueryEmitter(request, db) {
    return Observable.create((obs) => {
        // console.warn("creating new pouchQueryEmitter");

        let lastMatches = [];

        const feed = db.liveFind({ ...request, aggregate: true });

        feed.on("update", (update, matches) => {
            obs.next({ matches, request });
            lastMatches = matches;
        });

        feed.on("ready", () => {
            obs.next({ matches: lastMatches, request });
        });

        feed.on("error", (err) => obs.error(err));

        return () => {
            // console.warn("destroying old pouchQueryEmitter");
            feed.cancel();
        };
    });
}
