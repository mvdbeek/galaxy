import json
from functools import lru_cache
from pathlib import Path

from celery.contrib.abortable import AbortableTask

from galaxy import model
from galaxy.celery import galaxy_task
from galaxy.config import GalaxyAppConfiguration
from galaxy.datatypes.registry import Registry as DatatypesRegistry
from galaxy.jobs import MinimalJobWrapper
from galaxy.managers.collections import DatasetCollectionManager
from galaxy.managers.hdas import HDAManager
from galaxy.managers.lddas import LDDAManager
from galaxy.managers.markdown_util import generate_branded_pdf
from galaxy.managers.model_stores import ModelStoreManager
from galaxy.metadata.set_metadata import set_metadata_portable
from galaxy.model.scoped_session import galaxy_scoped_session
from galaxy.objectstore import BaseObjectStore
from galaxy.schema.tasks import (
    GeneratePdfDownload,
    PrepareDatasetCollectionDownload,
    SetupHistoryExportJob,
)
from galaxy.structured_app import MinimalManagerApp
from galaxy.tools import create_tool_from_representation
from galaxy.tools.data_fetch import do_fetch
from galaxy.util.custom_logging import get_logger
from galaxy.web.short_term_storage import ShortTermStorageMonitor

log = get_logger(__name__)


@lru_cache()
def cached_create_tool_from_representation(app, raw_tool_source):
    return create_tool_from_representation(
        app=app, raw_tool_source=raw_tool_source, tool_dir="", tool_source_class="XmlToolSource"
    )


@galaxy_task(ignore_result=True, action="recalculate a user's disk usage")
def recalculate_user_disk_usage(session: galaxy_scoped_session, user_id=None):
    if user_id:
        user = session.query(model.User).get(user_id)
        if user:
            user.calculate_and_set_disk_usage()
            log.info(f"New user disk usage is {user.disk_usage}")
        else:
            log.error(f"Recalculate user disk usage task failed, user {user_id} not found")
    else:
        log.error("Recalculate user disk usage task received without user_id.")


@galaxy_task(ignore_result=True, action="purge a history dataset")
def purge_hda(hda_manager: HDAManager, hda_id):
    hda = hda_manager.by_id(hda_id)
    hda_manager._purge(hda)


@galaxy_task(action="set metadata for job")
def set_job_metadata(
    tool_job_working_directory,
    extended_metadata_collection: bool,
    datatypes_registry: DatatypesRegistry,
    object_store: BaseObjectStore,
):
    set_metadata_portable(
        tool_job_working_directory,
        datatypes_registry=datatypes_registry,
        object_store=object_store,
        extended_metadata_collection=extended_metadata_collection,
    )


@galaxy_task(action="set dataset association metadata")
def set_metadata(
    hda_manager: HDAManager, ldda_manager: LDDAManager, dataset_id, model_class="HistoryDatasetAssociation"
):
    if model_class == "HistoryDatasetAssociation":
        dataset = hda_manager.by_id(dataset_id)
    elif model_class == "LibraryDatasetDatasetAssociation":
        dataset = ldda_manager.by_id(dataset_id)
    dataset.datatype.set_meta(dataset)


@galaxy_task
def setup_fetch_data(job_id: int, raw_tool_source: str, app: MinimalManagerApp, sa_session: galaxy_scoped_session):
    tool = cached_create_tool_from_representation(app=app, raw_tool_source=raw_tool_source)
    job = sa_session.query(model.Job).get(job_id)
    # TODO: assert state
    mini_job_wrapper = MinimalJobWrapper(job=job, app=app, tool=tool)
    mini_job_wrapper.change_state(model.Job.states.QUEUED, flush=False, job=job)
    # Set object store after job destination so can leverage parameters...
    mini_job_wrapper._set_object_store_ids(job)
    request_json = Path(mini_job_wrapper.working_directory) / "request.json"
    request_json_value = next(iter(p.value for p in job.parameters if p.name == "request_json"))
    request_json.write_text(json.loads(request_json_value))
    mini_job_wrapper.setup_external_metadata(
        output_fnames=mini_job_wrapper.job_io.get_output_fnames(),
        set_extension=True,
        tmp_dir=mini_job_wrapper.working_directory,
        # We don't want to overwrite metadata that was copied over in init_meta(), as per established behavior
        kwds={"overwrite": False},
    )
    mini_job_wrapper.prepare()
    # Technically this should be changed in fetch_data
    mini_job_wrapper.change_state(model.Job.states.RUNNING, flush=True, job=job)
    return mini_job_wrapper.working_directory, str(request_json), mini_job_wrapper.job_io.file_sources_dict


@galaxy_task
def finish_job(job_id: int, raw_tool_source: str, app: MinimalManagerApp, sa_session: galaxy_scoped_session):
    tool = cached_create_tool_from_representation(app=app, raw_tool_source=raw_tool_source)
    job = sa_session.query(model.Job).get(job_id)
    # TODO: assert state ?
    mini_job_wrapper = MinimalJobWrapper(job=job, app=app, tool=tool)
    mini_job_wrapper.finish("", "")


@galaxy_task(action="Run fetch_data", bind=True, base=AbortableTask)
def fetch_data(
    self,
    setup_return,
    datatypes_registry: DatatypesRegistry,
):
    tool_job_working_directory, request_path, file_sources_dict = setup_return
    working_directory = Path(tool_job_working_directory) / "working"
    do_fetch(
        request_path=request_path,
        working_directory=str(working_directory),
        registry=datatypes_registry,
        file_sources_dict=file_sources_dict,
    )
    return tool_job_working_directory


@galaxy_task(ignore_result=True, action="setting up export history job")
def export_history(
    model_store_manager: ModelStoreManager,
    request: SetupHistoryExportJob,
):
    model_store_manager.setup_history_export_job(request)


@galaxy_task(action="preparing compressed file for collection download")
def prepare_dataset_collection_download(
    request: PrepareDatasetCollectionDownload,
    collection_manager: DatasetCollectionManager,
):
    """Create a short term storage file tracked and available for download of target collection."""
    collection_manager.write_dataset_collection(request)


@galaxy_task(action="preparing Galaxy Markdown PDF for download")
def prepare_pdf_download(
    request: GeneratePdfDownload, config: GalaxyAppConfiguration, short_term_storage_monitor: ShortTermStorageMonitor
):
    """Create a short term storage file tracked and available for download of target PDF for Galaxy Markdown."""
    generate_branded_pdf(request, config, short_term_storage_monitor)


@galaxy_task(action="pruning history audit table")
def prune_history_audit_table(sa_session: galaxy_scoped_session):
    """Prune ever growing history_audit table."""
    model.HistoryAudit.prune(sa_session)


@galaxy_task(action="clean up short term storage")
def cleanup_short_term_storage(storage_monitor: ShortTermStorageMonitor):
    """Cleanup short term storage."""
    storage_monitor.cleanup()
