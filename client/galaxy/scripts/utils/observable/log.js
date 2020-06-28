import { pipe } from "rxjs";
import { tap } from "rxjs/operators";

export const log = (label, ...messages) => pipe(
    tap(streamVal => {
        console.log(`[${label}]`, ...messages, streamVal);
    })
)

export const warn = (label, ...messages) => pipe(
    tap(streamVal => {
        console.warn(`[${label}]`, ...messages, streamVal);
    })
)
