import { Observable, isObservable, combineLatest } from "rxjs";
import { switchMap, debounceTime, distinctUntilChanged } from "rxjs/operators";
// import { massageSelector } from "pouchdb-selector-core/lib/index.es";
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
        switchMap(buildPouchQueryEmitter),
    );
};


export function buildPouchQueryEmitter(inputs) {
    const [ request, db ] = inputs;

    const {
        selector = {},
        use_index = null,
        sort = []
    } = request;

    const changesCfg = {
        live: true,
        include_docs: true,
        since: 'now',
        timeout: false,
        use_index,
        selector
    };

    const findCfg = {
        selector,
        sort,
        use_index,
    };

    return Observable.create((obs) => {

        // monitor subsequent updates
        const emitter = db.changes(changesCfg);

        emitter.on('change', (change) => {
            // console.log("change");
            const { deleted = false, doc } = change;
            const action = deleted ? "DELETED" : "UPDATE";
            obs.next({ action, doc });
        });

        // Do initial query
        db.find(findCfg)
            .then((result) => {
                // console.log("initial find result", result):
                const { docs: initialMatches } = result;
                obs.next({ initialMatches })
            })
            .catch(err => {
                console.warn("Error on initial search", err);
                console.log("changesCfg", changesCfg);
                console.log("findCfg", findCfg);
                obs.error(err);
            });

        return () => {
            emitter.cancel();
        }
    })

}
