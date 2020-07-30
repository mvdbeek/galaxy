/**
 * Search cache upward and downward from the scroll HID, filtering out results
 * which do not match params, we don't want to return the entire result set for
 * 2 reasons: it might be huge, and we might not yet have large sections of the
 * contents if the user is rapidly dragging the scrollbar to different regions
 */

import { merge } from "rxjs";
import { content$ } from "../galaxyDb";
import { monitorQuery } from "./monitorQuery";
import { buildContentPouchRequest } from "../pouchUtils";
import { hydrateInputs } from "./util";


export const monitorHistoryContent = () => src$ => {

    const inputs$ = src$.pipe(
        hydrateInputs(1)
    );

    // look up from hid cursor
    const seekUp$ = inputs$.pipe(
        buildContentPouchRequest({ seek: "asc" }),
        monitorQuery({ db$: content$ }),
    );

    // look down from hid cursor
    const seekDown$ = inputs$.pipe(
        buildContentPouchRequest({ seek: "desc" }),
        monitorQuery({ db$: content$ }),
    );

    return merge(seekUp$, seekDown$);
}
