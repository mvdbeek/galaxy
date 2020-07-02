/**
 * Our API is very inconsistent which makes re-using components difficult.
 * This wrapper is supposed to make sub-collections look reasonably close to
 * the dataset collections that are loose in the content results so
 * we can pass them to the same components.
 */

import { Content, STATES } from "./index";

export class DatasetCollection extends Content {
    loadProps(raw = {}) {
        if (!raw.contents_url) {
            throw new Error("missing contents_url", raw);
        }
        super.loadProps(raw);
    }

    get collectionCount() {
        const count = this.element_count;
        if (count === undefined) return null;
        return count == 1 ? "with 1 item" : `with ${count} items`;
    }

    get collectionType() {
        return collectionTypeDescription(this.collection_type);
    }

    // This only gets used for the color of the collection content box
    // It's an attempt to get an overall state for a collection, this
    // needs more UI to drill down because there's going to be several
    // states from the job summary

    get state() {
        // console.log("get state");
        // {"running":0,"upload":0,"all_jobs":0,"deleted":0,"new":0,
        // "queued":0,"waiting":0,"failed":0,"deleted_new":0,
        // "paused":0,"error":0,"ok":0,"resubmitted":0}

        const states = this.uniqueJobStates();

        // no states? assume good.
        if (states.size == 0) {
            return STATES.OK;
        }

        // just one state, take that.
        if (states.size == 1) {
            return Array.from(states.values())[0];
        }

        // running?
        if (states.has(STATES.RUNNING) || states.has(STATES.QUEUED) || states.has(STATES.NEW)) {
            return STATES.RUNNING;
        }

        // error?
        if (states.has(STATES.ERROR) || states.has(STATES.FAILED_METADATA)) {
            return STATES.ERROR;
        }

        // Hard to say
        return STATES.MIXED;
    }

    uniqueJobStates() {
        const summary = this;
        const stateVals = new Set(Object.values(STATES));
        const validStates = Object.keys(this).filter((s) => stateVals.has(s) && summary[s] > 0);
        return new Set(validStates);
    }
}

// This is handy outside of the model, export separately
export function collectionTypeDescription(collectionType) {
    if (!collectionType) {
        return null;
    }
    switch (collectionType) {
        case "list":
            return "list";
        case "paired":
            return "dataset pair";
        case "list:paired":
            return "list of pairs";
        default:
            return "nested list";
    }
}
