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
    } = cfg;

    if (!isObservable(db$)) {
        const msg = `
            Please pass a database observable to the
            configuration of monitorQuery
        `;
        console.error(msg);
        throw new Error(msg);
    }

    // this is the actual emitter that watches the cache, it is customized
    // to a specific db and query
    return request$.pipe(
        distinctUntilChanged(deepEqual),
        withLatestFrom(db$),
        debounceTime(inputDebounce),
        switchMap((inputs) => pouchQueryEmitter(...inputs))
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
    // console.warn("creating new pouchQueryEmitter", request);

    return Observable.create((obs) => {

        let isReady = false;
        const feed = db.liveFind({ ...request, aggregate: true });

        feed.on("update", (update) => {
            if (isReady) {
                obs.next(update);
            }
        });

        feed.on("ready", () => {
            const result = feed.paginate(request);
            obs.next({ initialMatches: result, request });
            isReady = true;
        });

        feed.on("error", (err) => {
            console.warn("liveFind error", err, request, db);
            obs.error(err)
        });

        return () => {
            // console.warn("destroying old pouchQueryEmitter");
            feed.cancel();
        };
    });
}
