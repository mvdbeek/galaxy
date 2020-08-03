/**
 * Functions used by the history content observable to handle content update
 * aggregation as items appear and disappear from the cache.
 */

import SkipList from "proper-skip-list";
import { toArray, compose, slice, map } from "iter-tools/es2018";
import { SearchParams } from "../model/SearchParams";


// sorted map, keys are hids

export const newHidMap = () => new SkipList();


// scan function for consuming updates from the pouchdb-live-find. Update
// variable will either be a big initial chunk of results matching the query or
// a follow-up incremental change (if some other process modifies the cache).
// End result is a SkipList keyed by HID

export function processContentUpdate(hidMap, update) {
    const { initialMatches = [], action, doc } = update;

    // initial load
    if (initialMatches.length) {
        initialMatches.forEach(match => {
            hidMap.upsert(+match.hid, match);
        });
    }

    // incremental updates
    if (action && doc) {
        switch (action) {
            case "ADD":
            case "UPDATE":
                hidMap.upsert(+doc.hid, doc);
                break;
            case "DELETE":
                hidMap.delete(+doc.hid, doc);
                break;
        }
    }

    return hidMap;
}


// create iterator transformer to nab values from skip list, this is better
// than just converting it to an array because the map might be huge and getting
// just the window we want is going to be faster for large-N.
// skiplist iterators return [key, val, index], map to val

const grab = n => compose(toArray, map(entry => entry[1]), slice(n));


// A Skiplist provides iterators for finding keys searching forward or backward
// which is good because the map might get very large for some histories. We use
// iterator operations to find the window of stuff we care about without looping
// over the whole thing.

export function buildContentResult(inputs) {
    const [ hidMap, hidCursor, totalMatches, maxHid ] = inputs;

    // grab a few items above the line for the bench, and a full page below
    const bench = Math.floor(SearchParams.pageSize / 2);
    const grabBench = grab(bench);
    const grabPage = grab(SearchParams.pageSize);

    // bench (list of content above hid cursor)
    // ascending iterator
    const { asc } = hidMap.findEntries(hidCursor + 1);
    const benchContent = grabBench(asc).reverse();

    // page (list of content below hid cursor)
    // descending iterator
    const { desc } = hidMap.findEntries(hidCursor);
    const pageContent = grabPage(desc);

    // jam them together
    const contents = benchContent.concat(pageContent);

    // stats for padding on the scrollbar
    const firstRow = contents.length ? contents[0] : { hid: hidCursor };
    const firstHid = firstRow.hid;
    const topRows = Math.max(0, maxHid - firstHid);
    const bottomRows = totalMatches !== null ? Math.max(0, totalMatches - contents.length - topRows) : 0;


    console.groupCollapsed("buildContentResult");
    console.log("input: hidMap (skiplist)", hidMap.length);
    console.log("input: hidCursor", hidCursor);
    console.log("input: totalMatches", totalMatches);
    console.log("input: maxHid", maxHid);
    console.log("input: firstHid", firstHid);

    console.log("output: bench", bench);
    // console.log("output: firstRow", firstRow);
    console.log("output: firstHid", firstHid);
    console.log("output: topRows", topRows);
    console.log("output: bottomRows", bottomRows);

    console.groupCollapsed("output: contents");
        console.log("> contents", contents.map(x => x.hid));
        console.log("> benchContent", benchContent.map(x => x.hid));
        console.log("> pageContent", pageContent.map(x => x.hid));
    console.groupEnd();

    console.groupEnd();


    return { contents, bench, topRows, bottomRows };
}
