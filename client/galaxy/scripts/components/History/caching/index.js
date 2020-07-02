import { toPromise, toObservable } from "./client";


/**
 * monitorContentCache
 * returns an event emitter that monitors the contents of the history content cache
 */
export const monitorContentQuery = toObservable("monitorContentQuery");

/**
 * Content cache functions
 */
export const cacheContent = toPromise("cacheContentItem");
export const bulkCacheContent = toPromise("bulkCacheContent");
export const getCachedContentByTypeId = toPromise("getCachedContentByTypeId");
export const uncacheContent = toPromise("uncacheContent", false);

/**
 * Pass historyId + params and let worker load it, might be several requests
 * depending on param range and previous requests
 */
export const loadHistoryContents = toObservable("loadHistoryContents");

/**
 * Returns an observable that starts history content polling.
 * Polls until unsubscribed. Results are cached
 */
export const pollHistory = toObservable("pollHistory");

/**
 * Collection content
 */
export const monitorDscQuery = toObservable("monitorDscQuery");
export const loadDscContent = toObservable("loadDscContent");

// Debugging
export const wipeDatabase = toPromise("wipeDatabase", false);
