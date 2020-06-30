import { from, pipe } from "rxjs";
import { mergeMap, map } from "rxjs/operators";
import { prependPath } from "utils/redirect";
import { throttleDistinct } from "utils/observable";
import { loadHistoryContents } from "../../caching";
import { buildHistoryContentsUrl } from "../../caching/worker/urls";


// Turn historyId + params into content update urls to send to the worker

export const manualLoader = ({ onceEvery = 30000 } = {}) => pipe(

    // break params into chunks, convert those into urls
    mergeMap(([ id, params ]) => {
        const chunks = params.chunkParams();
        const urls = chunks.map((p) => buildHistoryContentsUrl(id, p));
        return from(urls);
    }),
    map(prependPath),

    // each distinct url can only go out once every so often
    throttleDistinct({ timeout: onceEvery }),

    // tell worker to request and cache responses
    mergeMap(loadHistoryContents)
);
