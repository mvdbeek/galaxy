import { toPromise, toObservable, toOperator } from "./client";

/**
 * monitor cache for changes
 */
export const monitorContentQuery = toOperator("monitorContentQuery");
export const monitorDscQuery = toOperator("monitorDscQuery");

/**
 * Cache promise functions
 */
export const cacheContent = toPromise("cacheContentItem");
export const bulkCacheContent = toPromise("bulkCacheContent");
export const getCachedContentByTypeId = toPromise("getCachedContentByTypeId");
export const uncacheContent = toPromise("uncacheContent", false);

/**
 * Loaders
 */
export const loadHistoryContents = toOperator("loadHistoryContents");
export const loadDscContent = toOperator("loadDscContent");

/**
 * Returns an observable that starts history content polling.
 * Polls until unsubscribed. Results are cached
 */
export const pollHistory = toObservable("pollHistory");

// Debugging
export const wipeDatabase = toPromise("wipeDatabase", false);
