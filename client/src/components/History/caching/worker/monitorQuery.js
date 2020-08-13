import { Observable, isObservable, combineLatest } from "rxjs";
import { switchMap, debounceTime, distinctUntilChanged } from "rxjs/operators";
import { massageSelector } from "pouchdb-selector-core/lib/index.es";
import deepEqual from "deep-equal";


/**
 * Turns a selector into a live cache result emitter.
 *
 * @param {Observable} db$ Observable PouchDB instance
 * @param {Observable} request$ Observable Pouchdb-find configuration
 */
export const monitorQuery = (cfg = {}) => (request$) => {
    // console.log("monitorQuery", cfg);

    const {
        db$ = null, // pouch database to monitor
        inputDebounce = 250, // how often to create a new query monitor
    } = cfg;

    if (!isObservable(db$)) {
        throw new Error("Please pass a database observable to the configuration of monitorQuery");
    }

    const debouncedRequest$ = request$.pipe(
        debounceTime(inputDebounce), // some inputs change a lot
        distinctUntilChanged(deepEqual),
    );

    return combineLatest(debouncedRequest$, db$).pipe(
        switchMap(pouchQueryEmitter),
    );
};


function pouchQueryEmitter(inputs) {
    const [ request, db ] = inputs;
    const { selector = {}, use_index = null, sort = [] } = request;

    return Observable.create((obs) => {

        // monitor subsequent updates
        const emitter = db.changes({
            live: true,
            include_docs: true,
            since: 'now',
            timeout: false,
            use_index,
            selector
        });

        emitter.on('change', (change) => {
            // console.log("change");
            const { deleted = false, doc } = change;
            const action = deleted ? "DELETED" : "UPDATE";
            obs.next({ action, doc });
        });

        // Do initial query
        db.find({
            selector: massageSelector(selector),
            sort,
            use_index,
        }).then(({ docs: initialMatches }) => {
            // console.log("initialMatches");
            obs.next({ initialMatches });
        }).catch(err => {
            console.warn("Error on initial search", err);
        });

        return () => {
            emitter.cancel();
        }
    })

}


/**
 * Build an observable that monitors a pouchdb instance by taking a pouchdb-find
 * select config and returning matching results when the cache changes.
 *
 * @param {PouchDB} db PouchDB instance
 * @param {Object} request pouchdb find config
 */
function OLD_pouchQueryEmitter(db, request) {
    return Observable.create((obs) => {
        const { aggregate } = request;
        const feed = db.liveFind(request);

        if (aggregate) {
            // emit individual updates now that initial query done
            feed.then(() => {
                const result = feed.paginate(request);
                obs.next({ initialMatches: result, request });
                feed.on("update", (update) => obs.next(update));
            })
        } else {
            // ... or just emit everything individually
            feed.on("update", (update) => obs.next(update));
        }

        feed.on("error", (err) => obs.error(err));

        return () => feed.cancel();
    });
}
