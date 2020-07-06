/**
 * asObservable takes an observable transformation and persists its state while
 * it is running inside the worker. Normally when threads.js invokes an
 * observable, it runs once, its subscription ends and subsequent calls to that
 * same exposed function will start a new subscription.
 *
 * With asObservable, a subject is created inside the worker and subsequent
 * method calls put their new value on that Subject, which is connected to the
 * wrapped observable. Therefore the observable state is preserved until it is
 * explicitly unsubscribed from the outside, and distinct(), scan(), or other
 * stateful observable operators will continue to work.
 */
import { Subject, of } from "rxjs";
import { startWith } from "rxjs/operators";

// list of current subscriptions

export const asObservable = (operation) => {
    const currentSubs = new Map();

    return (payload) => {
        // console.log("asObservable", payload, currentSubs.size);
        const { id, value, kind } = payload;

        // initialization
        if (!currentSubs.has(id)) {
            const input$ = new Subject();
            const output$ = input$.pipe(startWith(value), operation);
            currentSubs.set(id, { input$, output$ });
            return output$;
        }

        // process notifications
        const sub = currentSubs.get(id);

        // materialize exposed a "kind" variable for all observable messages,
        // it's either N,C,E for next, complete, error

        if (kind == "C" || kind == "E") {
            sub.input$.complete();
            currentSubs.delete(id);
        }

        if (kind == "N") {
            sub.input$.next(value);
        }

        // If we're just running against the existing stored observable do not
        // return a new one.
        return of(null);
    };
};
