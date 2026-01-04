# Galaxy API Client



API Version: 0.1.0

## Installation

```bash
pip install httpx pydantic
```

## Usage

```python
from galaxy_api_client import APIClient

# Initialize the client
client = APIClient(
    base_url="https://api.example.com",
    api_key="your-api-key"  # or bearer_token="your-token"
)

# Use the client
with client:
    # Make API calls
    response = client.some_method()
    print(response.data)
```

## Async Usage

```python
import asyncio
from galaxy_api_client import APIClient

async def main():
    client = APIClient(
        base_url="https://api.example.com",
        api_key="your-api-key"
    )
    
    async with client:
        # Make async API calls
        response = await client.some_method_async()
        print(response.data)

asyncio.run(main())
```

## Available Methods

- `ai__agents__list_agents()`
- `ai__agents_custom_tool__create_custom_tool()`
- `ai__agents_error_analysis__analyze_error()`
- `ai__agents_query__query_agent()`
- `authenticate__baseauth__get_api_key()`
- `chat__exchange_feedback__set_exchange_feedback()`
- `chat__exchange_messages__get_exchange_messages()`
- `chat__feedback__feedback()`
- `chat__history__clear_chat_history()`
- `chat__history__get_chat_history()`
- `chat__query()`
- `configuration__decode__decode_id()`
- `configuration__dynamic_tool_confs__dynamic_tool_confs()`
- `configuration__encode__encode_id()`
- `configuration__index()`
- `configuration__tool_lineages__tool_lineages()`
- `configuration__toolbox__reload_toolbox()`
- `configuration__version()`
- `configuration__whoami()`
- `context__index()`
- `data_libraries_folders__contents__create()`
- `data_libraries_folders__contents__index()`
- `data_libraries_folders__create()`
- `data_libraries_folders__delete()`
- `data_libraries_folders__permissions__get_permissions()`
- `data_libraries_folders__permissions__set_permissions()`
- `data_libraries_folders__show()`
- `data_libraries_folders__update()`
- `dataset_collections__attributes__attributes()`
- `dataset_collections__content()`
- `dataset_collections__contents__contents()`
- `dataset_collections__copy__copy()`
- `dataset_collections__create()`
- `dataset_collections__download()`
- `dataset_collections__show()`
- `dataset_collections__suitable_converters__suitable_converters()`
- `dataset_collections__update_collection()`
- `dataset_collections__workbook_download()`
- `dataset_collections__workbook_download_for_collection()`
- `dataset_collections__workbook_parse()`
- `dataset_collections__workbook_parse_for_collection()`
- `datasets__content__get_structured_content()`
- `datasets__contents_display__display_history_content()`
- `datasets__contents_extra_files__extra_files_history()`
- `datasets__converted__converted()`
- `datasets__converted__converted_ext()`
- `datasets__delete()`
- `datasets__delete_batch()`
- `datasets__display__display()`
- `datasets__extra_files__extra_files()`
- `datasets__extra_files_raw__extra_file_raw()`
- `datasets__get_content_as_text__get_content_as_text()`
- `datasets__get_metadata_file()`
- `datasets__hash__compute_hash()`
- `datasets__index()`
- `datasets__inheritance_chain__show_inheritance_chain()`
- `datasets__metadata_file__get_metadata_file_datasets()`
- `datasets__permissions__update_permissions()`
- `datasets__report__report()`
- `datasets__show()`
- `datasets__storage__show_storage()`
- `datasets__update_dataset()`
- `datasets__update_object_store_id()`
- `datatypes__converters__converters()`
- `datatypes__edam_data__edam_data()`
- `datatypes__edam_data_detailed__edam_data_detailed()`
- `datatypes__edam_formats__edam_formats()`
- `datatypes__edam_formats_detailed__edam_formats_detailed()`
- `datatypes__index()`
- `datatypes__mapping__mapping()`
- `datatypes__show()`
- `datatypes__sniffers__sniffers()`
- `datatypes__types_and_mapping__types_and_mapping()`
- `datatypes__visualizations__visualization_for_datatype()`
- `delete_api_unprivileged_tools_uuid()`
- `display_applications__create_link__create_link()`
- `display_applications__index()`
- `display_applications__reload__reload()`
- `drs__download()`
- `drs__v1_objects__get_object()`
- `drs__v1_objects_access__get_access_url()`
- `drs__v1_service_info__service_info()`
- `dynamic_tools__build__build()`
- `dynamic_tools__create()`
- `dynamic_tools__delete()`
- `dynamic_tools__index()`
- `dynamic_tools__runtime_model__runtime_model()`
- `dynamic_tools__show()`
- `file_sources__create_instance()`
- `file_sources__instances_get()`
- `file_sources__instances_index()`
- `file_sources__instances_purge()`
- `file_sources__instances_test_instance()`
- `file_sources__instances_update()`
- `file_sources__template_oauth2()`
- `file_sources__templates_index()`
- `file_sources__test_instances_update()`
- `file_sources__test_new_instance_configuration()`
- `forms__delete()`
- `forms__undelete__undelete()`
- `genomes__index()`
- `genomes__indexes__indexes()`
- `genomes__sequences__sequences()`
- `genomes__show()`
- `get_api_remote_files()`
- `get_api_unprivileged_tools()`
- `get_api_unprivileged_tools_uuid()`
- `group_roles__roles__delete()`
- `group_roles__roles__index()`
- `group_roles__roles__show()`
- `group_roles__roles__update()`
- `group_users__user__delete()`
- `group_users__user__show()`
- `group_users__user__update()`
- `group_users__users__delete()`
- `group_users__users__index()`
- `group_users__users__show()`
- `group_users__users__update()`
- `groups__create()`
- `groups__delete()`
- `groups__index()`
- `groups__purge__purge()`
- `groups__show()`
- `groups__undelete__undelete()`
- `groups__update()`
- `head_api_datasets_history_content_id_display()`
- `head_api_histories_history_id_contents_history_content_id_display()`
- `head_api_proxy()`
- `help__forum_search__search_forum()`
- `histories__archive__archive_history()`
- `histories__archive_restore__restore_archived_history()`
- `histories__archived__get_archived_histories()`
- `histories__batch_delete__batch_delete()`
- `histories__batch_undelete__batch_undelete()`
- `histories__citations__citations()`
- `histories__contents__update_batch()`
- `histories__contents_bulk__bulk_operation()`
- `histories__contents_datasets_materialize__materialize_dataset()`
- `histories__contents_from_store__create_from_store()`
- `histories__contents_jobs_summary__show_jobs_summary()`
- `histories__contents_permissions__update_permissions()`
- `histories__contents_prepare_store_download__prepare_store_download()`
- `histories__contents_tags__create()`
- `histories__contents_tags__delete()`
- `histories__contents_tags__index()`
- `histories__contents_tags__show()`
- `histories__contents_tags__update()`
- `histories__contents_validate__validate()`
- `histories__contents_write_store__write_store()`
- `histories__count__count()`
- `histories__create()`
- `histories__custom_builds_metadata__get_custom_builds_metadata()`
- `histories__delete()`
- `histories__deleted__index_deleted()`
- `histories__deleted_undelete__undelete()`
- `histories__disable_link_access__disable_link_access()`
- `histories__enable_link_access__enable_link_access()`
- `histories__exports__archive_download()`
- `histories__exports__archive_export()`
- `histories__exports__index_exports()`
- `histories__from_store__create_from_store()`
- `histories__from_store_async__create_from_store_async()`
- `histories__index()`
- `histories__jobs_summary__index_jobs_summary()`
- `histories__materialize__materialize_to_history()`
- `histories__most_recently_used__show_recent()`
- `histories__prepare_download__prepare_collection_download()`
- `histories__prepare_store_download__prepare_store_download()`
- `histories__publish__publish()`
- `histories__published__published()`
- `histories__share_with_users__share_with_users()`
- `histories__shared_with_me__shared_with_me()`
- `histories__sharing__sharing()`
- `histories__show()`
- `histories__slug__set_slug()`
- `histories__tags__create()`
- `histories__tags__delete()`
- `histories__tags__index()`
- `histories__tags__show()`
- `histories__tags__update()`
- `histories__tool_requests__tool_requests()`
- `histories__unpublish__unpublish()`
- `histories__update()`
- `histories__write_store__write_store()`
- `history_contents__archive()`
- `history_contents__archive_named()`
- `history_contents__copy_contents()`
- `history_contents__create()`
- `history_contents__create_typed()`
- `history_contents__delete_legacy()`
- `history_contents__delete_typed()`
- `history_contents__download_collection()`
- `history_contents__get_metadata_file()`
- `history_contents__index()`
- `history_contents__index_typed()`
- `history_contents__show()`
- `history_contents__show_legacy()`
- `history_contents__update_legacy()`
- `history_contents__update_typed()`
- `job_lock__job_lock_status()`
- `job_lock__update_job_lock()`
- `jobs__common_problems__common_problems()`
- `jobs__console_output__console_output()`
- `jobs__create()`
- `jobs__delete()`
- `jobs__destination_params__destination_params()`
- `jobs__error__error()`
- `jobs__index()`
- `jobs__inputs__inputs()`
- `jobs__metrics__metrics_by_dataset()`
- `jobs__metrics__metrics_by_job()`
- `jobs__outputs__outputs()`
- `jobs__parameters_display__parameters_display_by_dataset()`
- `jobs__parameters_display__parameters_display_by_job()`
- `jobs__resume__resume()`
- `jobs__search__search()`
- `jobs__show()`
- `libraries__contents__create_form()`
- `libraries__contents__delete()`
- `libraries__contents__index()`
- `libraries__contents__show()`
- `libraries__contents__update()`
- `libraries__create()`
- `libraries__delete()`
- `libraries__deleted__index_deleted()`
- `libraries__from_store__create_from_store()`
- `libraries__index()`
- `libraries__permissions__get_permissions()`
- `libraries__permissions__set_permissions()`
- `libraries__show()`
- `libraries__update()`
- `licenses__get()`
- `licenses__index()`
- `metrics__create()`
- `notifications__broadcast__broadcast_notification()`
- `notifications__broadcast__get_all_broadcasted()`
- `notifications__broadcast__get_broadcasted()`
- `notifications__broadcast__update_broadcasted_notification()`
- `notifications__delete_user_notification()`
- `notifications__delete_user_notifications()`
- `notifications__get_user_notifications()`
- `notifications__preferences__get_notification_preferences()`
- `notifications__preferences__update_notification_preferences()`
- `notifications__send_notification()`
- `notifications__show_notification()`
- `notifications__status__get_notifications_status()`
- `notifications__update_user_notification()`
- `notifications__update_user_notifications()`
- `oauth2__oauth2_callback()`
- `object_stores__create_instance()`
- `object_stores__index()`
- `object_stores__instances_get()`
- `object_stores__instances_index()`
- `object_stores__instances_purge()`
- `object_stores__instances_test_instance()`
- `object_stores__instances_update()`
- `object_stores__show_info()`
- `object_stores__templates_index()`
- `object_stores__test_instances_update()`
- `object_stores__test_new_instance_configuration()`
- `pages__create()`
- `pages__delete()`
- `pages__disable_link_access__disable_link_access()`
- `pages__enable_link_access__enable_link_access()`
- `pages__index()`
- `pages__prepare_download__prepare_pdf()`
- `pages__publish__publish()`
- `pages__share_with_users__share_with_users()`
- `pages__sharing__sharing()`
- `pages__show()`
- `pages__show_pdf()`
- `pages__slug__set_slug()`
- `pages__undelete__undelete()`
- `pages__unpublish__unpublish()`
- `pages__update()`
- `post_api_unprivileged_tools()`
- `post_ga4gh_drs_v1_objects_object_id()`
- `post_ga4gh_drs_v1_objects_object_id_access_access_id()`
- `put_api_folders_id()`
- `quotas__create()`
- `quotas__delete()`
- `quotas__deleted__index_deleted()`
- `quotas__deleted__show_deleted()`
- `quotas__deleted_undelete__undelete()`
- `quotas__index()`
- `quotas__purge__purge()`
- `quotas__show()`
- `quotas__update()`
- `remote_files__create_entry()`
- `remote_files__index()`
- `remote_files__oidc_tokens__get_token()`
- `remote_files__plugins__plugins()`
- `roles__create()`
- `roles__delete()`
- `roles__index()`
- `roles__purge__purge()`
- `roles__show()`
- `roles__undelete__undelete()`
- `short_term_storage__ready__is_ready()`
- `short_term_storage__serve()`
- `storage_management__datasets__cleanup_datasets()`
- `storage_management__datasets_discarded__discarded_datasets()`
- `storage_management__datasets_discarded_summary__discarded_datasets_summary()`
- `storage_management__histories__cleanup_histories()`
- `storage_management__histories_archived__archived_histories()`
- `storage_management__histories_archived_summary__archived_histories_summary()`
- `storage_management__histories_discarded__discarded_histories()`
- `storage_management__histories_discarded_summary__discarded_histories_summary()`
- `tags__update()`
- `tasks__result__get_result()`
- `tasks__state__state()`
- `tool_data_tables__create()`
- `tool_data_tables__delete()`
- `tool_data_tables__fields__show_field()`
- `tool_data_tables__fields_files__download_field_file()`
- `tool_data_tables__index()`
- `tool_data_tables__reload__reload()`
- `tool_data_tables__show()`
- `tool_shed_repositories__check_for_updates__check_for_updates()`
- `tool_shed_repositories__index()`
- `tool_shed_repositories__show()`
- `tools__claim__claim_landing()`
- `tools__create_data_landing()`
- `tools__create_file_landing()`
- `tools__create_landing()`
- `tools__fetch__fetch_form()`
- `tools__fetch_workbook_download()`
- `tools__fetch_workbook_parse()`
- `tools__get_landing()`
- `tools__get_tool_request()`
- `tools__icon__get_icon()`
- `tools__inputs__tool_inputs()`
- `tools__parameter_landing_request_schema()`
- `tools__parameter_request_schema()`
- `tools__parameter_test_case_xml_schema()`
- `tools__state__tool_request_state()`
- `tours__generate__generate_tour()`
- `tours__index()`
- `tours__show()`
- `tours__update_tour()`
- `users__api_key__create_api_key()`
- `users__api_key__delete_api_key()`
- `users__api_key__get_or_create_api_key()`
- `users__api_key_detailed__get_api_key()`
- `users__beacon__get_beacon()`
- `users__beacon__set_beacon()`
- `users__create()`
- `users__credentials__delete_service_credentials()`
- `users__credentials__list_user_credentials()`
- `users__credentials__provide_credential()`
- `users__credentials__update_user_credentials_group()`
- `users__credentials_groups__delete_credentials()`
- `users__credentials_groups__update_user_credentials()`
- `users__current_recalculate_disk_usage__recalculate_disk_usage()`
- `users__custom_builds__add_custom_builds()`
- `users__custom_builds__delete_custom_builds()`
- `users__custom_builds__get_custom_builds()`
- `users__delete()`
- `users__deleted__index_deleted()`
- `users__deleted__show_deleted()`
- `users__deleted_undelete__undelete()`
- `users__favorites__remove_favorite()`
- `users__favorites__set_favorite()`
- `users__index()`
- `users__objectstore_usage__objectstore_usage()`
- `users__recalculate_disk_usage__recalculate_disk_usage()`
- `users__recalculate_disk_usage__recalculate_disk_usage_by_user_id()`
- `users__roles__get_user_roles()`
- `users__send_activation_email__send_activation_email()`
- `users__show()`
- `users__theme__set_theme()`
- `users__update()`
- `users__usage__usage()`
- `users__usage__usage_for()`
- `utilities__proxy()`
- `visualizations__create()`
- `visualizations__disable_link_access__disable_link_access()`
- `visualizations__enable_link_access__enable_link_access()`
- `visualizations__index()`
- `visualizations__publish__publish()`
- `visualizations__share_with_users__share_with_users()`
- `visualizations__sharing__sharing()`
- `visualizations__show()`
- `visualizations__slug__set_slug()`
- `visualizations__unpublish__unpublish()`
- `visualizations__update()`
- `workflows__cancel_invocation()`
- `workflows__claim__claim_landing()`
- `workflows__create_landing()`
- `workflows__delete_workflow()`
- `workflows__disable_link_access__disable_link_access()`
- `workflows__enable_link_access__enable_link_access()`
- `workflows__error__report_error()`
- `workflows__from_store__create_invocations_from_store()`
- `workflows__get_landing()`
- `workflows__index()`
- `workflows__index_invocations()`
- `workflows__invocation_counts()`
- `workflows__invocations__cancel_workflow_invocation()`
- `workflows__invocations__index_workflow_invocations()`
- `workflows__invocations__invoke()`
- `workflows__invocations__show_workflow_invocation()`
- `workflows__invocations_jobs_summary__workflow_invocation_jobs_summary()`
- `workflows__invocations_report__show_workflow_invocation_report()`
- `workflows__invocations_report_pdf__show_workflow_invocation_report_pdf()`
- `workflows__invocations_step_jobs_summary__workflow_invocation_step_jobs_summary()`
- `workflows__invocations_steps__update_workflow_invocation_step()`
- `workflows__invocations_steps__workflow_invocation_step()`
- `workflows__jobs_summary__invocation_jobs_summary()`
- `workflows__menu__get_workflow_menu()`
- `workflows__metrics__get_invocation_metrics()`
- `workflows__prepare_store_download__prepare_store_download()`
- `workflows__publish__publish()`
- `workflows__refactor__refactor()`
- `workflows__report__show_invocation_report()`
- `workflows__report_pdf__show_invocation_report_pdf()`
- `workflows__request__invocation_as_request()`
- `workflows__share_with_users__share_with_users()`
- `workflows__sharing__sharing()`
- `workflows__show_invocation()`
- `workflows__show_workflow()`
- `workflows__slug__set_slug()`
- `workflows__step_jobs_summary__invocation_step_jobs_summary()`
- `workflows__steps__invocation_step()`
- `workflows__steps__step()`
- `workflows__steps__update_invocation_step()`
- `workflows__tags__create()`
- `workflows__tags__delete()`
- `workflows__tags__index()`
- `workflows__tags__show()`
- `workflows__tags__update()`
- `workflows__undelete__undelete_workflow()`
- `workflows__unpublish__unpublish()`
- `workflows__usage__cancel_workflow_invocation()`
- `workflows__usage__index_workflow_invocations()`
- `workflows__usage__invoke()`
- `workflows__usage__show_workflow_invocation()`
- `workflows__usage_jobs_summary__workflow_invocation_jobs_summary()`
- `workflows__usage_report__show_workflow_invocation_report()`
- `workflows__usage_report_pdf__show_workflow_invocation_report_pdf()`
- `workflows__usage_step_jobs_summary__workflow_invocation_step_jobs_summary()`
- `workflows__usage_steps__update_workflow_invocation_step()`
- `workflows__usage_steps__workflow_invocation_step()`
- `workflows__versions__show_versions()`
- `workflows__write_store__write_store()`

## Error Handling

The client provides custom exceptions for common error cases:

- `ApiError`: General API errors
- `ValidationError`: Request validation errors
- `AuthenticationError`: Authentication failures (401)
- `NotFoundError`: Resource not found (404)

## Generated with openapi-to-httpx

This client was automatically generated from an OpenAPI specification.