import { from, pipe } from "rxjs";
import { mergeMap, map } from "rxjs/operators";
import { throttleDistinct } from "utils/observable";
import { prependPath } from "utils/redirect";

import { SearchParams } from "../../model";
import { loadHistoryContents } from "../../caching";
import { buildHistoryContentsUrl } from "../../caching/worker/urls";


// Turn historyId + params into content update urls to send to the worker

export const manualLoader = ({ timeout = 30000 } = {}) => pipe(

    // break params into chunks, convert those into urls
    mergeMap(([id, rawParams]) => {
        const params = new SearchParams(rawParams);
        const chunks = params.chunkParams();
        const urls = chunks.map((p) => buildHistoryContentsUrl(id, p));
        return from(urls);
    }),
    map(prependPath),

    // each distinct url can only go out once every 30 secs
    throttleDistinct(timeout),

    // tell worker to request and cache responses
    mergeMap(url => loadHistoryContents(url))
);
