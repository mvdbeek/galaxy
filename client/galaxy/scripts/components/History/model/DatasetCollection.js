/**
 * Our API is very inconsistent which makes re-using components difficult.
 * This wrapper is supposed to make sub-collections look reasonably close to
 * the dataset collections that are loose in the content results so
 * we can pass them to the same components.
 */

import { Content, STATES } from "./index";
import { JobStateSummary } from "./JobStateSummary";

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

    get hasDetails() {
        return this.populated_state;
    }

    // This only gets used for the color of the collection content box
    // It's an attempt to get an overall state for a collection, this
    // needs more UI to drill down because there's going to be several
    // states from the job summary

    get jobStateSummary() {
        return new JobStateSummary(this.job_state_summary);
    }

    get state() {
        // stolen from existing model, must clean this crap up

        let state;

        const summary = this.jobStatesSummary;
        if (summary) {
            if (summary.new) {
                state = "loading";
            } else if (summary.errored) {
                state = "error";
            } else if (summary.terminal) {
                state = "ok";
            } else if (summary.running) {
                state = "running";
            } else {
                state = "queued";
            }
        } else if (this.job_source_id) {
            // Initial rendering - polling will fill in more details in a bit.
            state = "loading";
        } else {
            state = this.populated_state ? STATES.OK : STATES.RUNNING;
        }

        return state;
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
