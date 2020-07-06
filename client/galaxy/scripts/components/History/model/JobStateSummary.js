import { STATES } from "./states";
import somefuckingnonsnse from "mvc/history/job-states-model";

// console.log("get state");
// {"running":0,"upload":0,"all_jobs":0,"deleted":0,"new":0,
// "queued":0,"waiting":0,"failed":0,"deleted_new":0,
// "paused":0,"error":0,"ok":0,"resubmitted":0}

export class JobStateSummary {
    constructor(props = {}) {
        this._states = new Map(Object.entries(props));
        Object.assign(this, props);
    }

    // get uniqueJobStates() {
    //     const summary = this;
    //     const stateVals = new Set(Object.values(STATES));
    //     const validStates = Object.keys(this).filter((s) => stateVals.has(s) && summary[s] > 0);
    //     return new Set(validStates);
    // }

    // job states contain any of the args
    has(...queryStates) {
        return queryStates.any((s) => {
            this._states.has(s);
        });
    }

    // num of jobs in indicated state
    stateCount(queryState) {
        return 0;
    }

    // count the jobs that are in error;
    get errorCount() {
        // return this.numWithStates(ERROR_STATES);
        return 0;
    }

    get runningCount() {
        return 0;
    }

    // collection is new?
    get new() {
        return false;
    }

    // collection has errors
    get errored() {
        // return this.get("populated_state") === "error" || this.anyWithStates(ERROR_STATES);
        return false;
    }

    // colleciton is running
    get running() {
        // return this.anyWithState("running");
        return false;
    }

    // huh?
    get terminal() {
        // if (this.new()) { //isNew
        //     return false;
        // } else {
        //     var anyNonTerminal = this.anyWithStates(NON_TERMINAL_STATES);
        //     return !anyNonTerminal;
        // }
        return false;
    }

    get isNew() {
        // return !this.hasDetails() || this.get("populated_state") == "new";
        return false;
    }
}
