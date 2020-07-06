// Stolen from existing model.
// It is stupid.

export const STATES = {
    // NOT ready states
    /** is uploading and not ready */
    UPLOAD: "upload",
    /** the job that will produce the dataset queued in the runner */
    QUEUED: "queued",
    /** the job that will produce the dataset is running */
    RUNNING: "running",
    /** metadata for the dataset is being discovered/set */
    SETTING_METADATA: "setting_metadata",

    // ready states
    /** was created without a tool */
    NEW: "new",
    /** has no data */
    EMPTY: "empty",
    /** has successfully completed running */
    OK: "ok",

    /** the job that will produce the dataset paused */
    PAUSED: "paused",
    /** metadata discovery/setting failed or errored (but otherwise ok) */
    FAILED_METADATA: "failed_metadata",
    //TODO: not in trans.app.model.Dataset.states - is in database
    /** not accessible to the current user (i.e. due to permissions) */
    NOT_VIEWABLE: "noPermission",
    /** deleted while uploading */
    DISCARDED: "discarded",
    /** the tool producing this dataset failed */
    ERROR: "error",

    // Adding a mixed state for use on the collection UI
    MIXED: "mixed",

    // found in job-state summary model
    DELETED: "deleted",
    WAITING: "waiting",
    FAILED: "failed",
    DELETEDNEW: "deleted_new",
    RESUBMITTED: "resubmitted",
};

STATES.READY_STATES = [
    STATES.OK,
    STATES.EMPTY,
    STATES.PAUSED,
    STATES.FAILED_METADATA,
    STATES.NOT_VIEWABLE,
    STATES.DISCARDED,
    STATES.ERROR,
];

STATES.NOT_READY_STATES = [STATES.UPLOAD, STATES.QUEUED, STATES.RUNNING, STATES.SETTING_METADATA, STATES.NEW];

// Job-state-summary lists

STATES.NON_TERMINAL_STATES = [STATES.NEW, STATES.QUEUED, STATES.RUNNING];

STATES.ERROR_STATES = [
    STATES.ERROR,
    STATES.DELETED, // does this exist?
];
