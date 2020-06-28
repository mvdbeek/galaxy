// We don't use a schema anymore and we don't even bother separating
// content and datasets/collections because there is barely any performance
// benefit in doing so, but we need a list of fields to ask the api for
// during content polling and pagination

// TODO: when this list is finished make new views
// in the HDA and HDCA serializers so we don't have
// to list them every time we send a request

export const historyFields = [
    "annotation",
    "contents_active",
    "contents_url",
    "create_time",
    "deleted",
    "empty",
    "genome_build",
    "hid_counter",
    "id",
    "importable",
    "name",
    "nice_size",
    "published",
    "purged",
    "shared",
    "size",
    "slug",
    "state",
    "tags",
    "update_time",
    "url",
    "username_and_slug",
    "user_id",
];

export const contentFields = [
    // common to both hda & hdca
    "create_time",
    "deleted",
    "hid",
    "history_content_type",
    "history_id",
    "id",
    "name",
    "tags",
    "type",
    "type_id",
    "update_time",
    "url",
    "visible",

    // dataset only
    "accessible",
    "api_type",
    "annotation",
    "created_from_basename",
    "creating_job",
    "dataset_id",
    "data_type",
    "display_apps",
    "display_types",
    "download_url",
    "extension",
    "file_ext",
    "file_name",
    "file_size",
    "genome_build",
    "hda_ldda",
    "metadata_data_lines",
    "metadata_dbkey",
    "meta_files",
    "misc_blurb",
    "misc_info",
    "model_class",
    "peek",
    "purged",
    "rerunnable",
    "resubmitted",
    "state",
    "uuid",
    "validated_state",
    "validated_state_message",

    // collection only
    "collection_id",
    "collection_type",
    "contents_url",
    "element_count",
    "job_source_id",
    "job_source_type",
    "job_state_summary",
    "populated",
    "populated_state",
    "populated_state_message",
];
