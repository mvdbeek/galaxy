import { from, pipe } from "rxjs";
import { tap, mergeMap, map } from "rxjs/operators";
import { throttleDistinct } from "utils/observable";
import { prependPath } from "utils/redirect";

import { loadHistoryContents } from "../../caching";
import { buildHistoryContentsUrl } from "../../caching/worker/urls";


// Turn historyId + params into content update urls to send to the worker

export const manualLoader = ({ onceEvery = 20000 } = {}) => pipe(

    // break params into chunks, convert those into urls
    mergeMap(([ id, params ]) => {

        params.report(`Starting params: ${id}`);
        const chunks = params.chunkParams();
        chunks.forEach(p => p.report(">>> chunk"));

        const urls = chunks.map((p) => buildHistoryContentsUrl(id, p));
        return from(urls);
    }),
    map(prependPath),

    // each distinct url can only go out once every so often
    throttleDistinct({ timeout: onceEvery }),

    // each of these should result in an ajax request
    tap(url => console.warn("requesting", url)),

    // tell worker to request and cache responses
    mergeMap(url => loadHistoryContents(url))
);
