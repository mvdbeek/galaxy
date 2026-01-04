from __future__ import annotations

import enum
from typing import Any, Literal

from pydantic import BaseModel, Field


class AccessMethodType(enum.Enum):
    S3 = "s3"
    GS = "gs"
    FTP = "ftp"
    GSIFTP = "gsiftp"
    GLOBUS = "globus"
    HTSGET = "htsget"
    HTTPS = "https"
    FILE = "file"


class ActionType(enum.Enum):
    """Types of actions agents can suggest."""

    TOOL_RUN = "tool_run"
    DOCUMENTATION = "documentation"
    CONTACT_SUPPORT = "contact_support"
    VIEW_EXTERNAL = "view_external"
    SAVE_TOOL = "save_tool"
    REFINE_QUERY = "refine_query"


class CollectionSourceType(enum.Enum):
    HDA = "hda"
    LDDA = "ldda"
    HDCA = "hdca"
    NEW_COLLECTION = "new_collection"


class ConfidenceLevel(enum.Enum):
    """Confidence levels for agent responses."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class CreateType(enum.Enum):
    FILE = "file"
    FOLDER = "folder"
    COLLECTION = "collection"


class CustomBuildLenType(enum.Enum):
    FILE = "file"
    FASTA = "fasta"
    TEXT = "text"


class DCEType(enum.Enum):
    """Available types of dataset collection elements."""

    HDA = "hda"
    DATASET_COLLECTION = "dataset_collection"


class DataItemSourceType(enum.Enum):
    HDA = "hda"
    LDDA = "ldda"
    HDCA = "hdca"
    DCE = "dce"
    DC = "dc"


class DatasetCollectionPopulatedState(enum.Enum):
    NEW = "new"
    OK = "ok"
    FAILED = "failed"


class DatasetContentType(enum.Enum):
    """For retrieving content from a structured dataset (e.g. HDF5)"""

    META = "meta"
    ATTR = "attr"
    STATS = "stats"
    DATA = "data"


class DatasetPermissionAction(enum.Enum):
    SET_PERMISSIONS = "set_permissions"
    MAKE_PRIVATE = "make_private"
    REMOVE_RESTRICTIONS = "remove_restrictions"


class DatasetSourceTransformActionType(enum.Enum):
    TO_POSIX_LINES = "to_posix_lines"
    SPACES_TO_TABS = "spaces_to_tabs"
    DATATYPE_GROOM = "datatype_groom"


class DatasetSourceType(enum.Enum):
    HDA = "hda"
    LDDA = "ldda"


class DatasetState(enum.Enum):
    NEW = "new"
    UPLOAD = "upload"
    QUEUED = "queued"
    RUNNING = "running"
    OK = "ok"
    EMPTY = "empty"
    ERROR = "error"
    PAUSED = "paused"
    SETTING_METADATA = "setting_metadata"
    FAILED_METADATA = "failed_metadata"
    DEFERRED = "deferred"
    DISCARDED = "discarded"


class DatasetValidatedState(enum.Enum):
    UNKNOWN = "unknown"
    INVALID = "invalid"
    OK = "ok"


class DefaultQuotaTypes(enum.Enum):
    UNREGISTERED = "unregistered"
    REGISTERED = "registered"


class DefaultQuotaValues(enum.Enum):
    UNREGISTERED = "unregistered"
    REGISTERED = "registered"
    NO = "no"


class ElementsFromType(enum.Enum):
    ARCHIVE = "archive"
    BAGIT = "bagit"
    BAGIT_ARCHIVE = "bagit_archive"
    DIRECTORY = "directory"


class ExportObjectType(enum.Enum):
    """Types of objects that can be exported."""

    HISTORY = "history"
    INVOCATION = "invocation"


class ExtraFilesEntryClass(enum.Enum):
    DIRECTORY = "Directory"
    FILE = "File"


class FavoriteObjectType(enum.Enum):
    TOOLS = "tools"


class HashFunctionNameEnum(enum.Enum):
    """Hash function names that can be used to generate checksums for files."""

    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"


class HistoryContentItemOperation(enum.Enum):
    HIDE = "hide"
    UNHIDE = "unhide"
    DELETE = "delete"
    UNDELETE = "undelete"
    PURGE = "purge"
    CHANGE_DATATYPE = "change_datatype"
    CHANGE_DBKEY = "change_dbkey"
    ADD_TAGS = "add_tags"
    REMOVE_TAGS = "remove_tags"


class HistoryContentSource(enum.Enum):
    HDA = "hda"
    HDCA = "hdca"
    LIBRARY = "library"
    LIBRARY_FOLDER = "library_folder"
    NEW_COLLECTION = "new_collection"


class HistoryContentType(enum.Enum):
    """Available types of History contents."""

    DATASET = "dataset"
    DATASET_COLLECTION = "dataset_collection"


class InvocationSerializationView(enum.Enum):
    ELEMENT = "element"
    COLLECTION = "collection"


class InvocationSortByEnum(enum.Enum):
    CREATE_TIME = "create_time"
    UPDATE_TIME = "update_time"
    NONE = "None"


class InvocationState(enum.Enum):
    NEW = "new"
    REQUIRES_MATERIALIZATION = "requires_materialization"
    READY = "ready"
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    FAILED = "failed"


class InvocationStepState(enum.Enum):
    NEW = "new"
    READY = "ready"
    SCHEDULED = "scheduled"


class ItemsFromSrc(enum.Enum):
    URL = "url"
    FILES = "files"
    PATH = "path"
    FTP_IMPORT = "ftp_import"
    SERVER_DIR = "server_dir"


class JobIndexSortByEnum(enum.Enum):
    CREATE_TIME = "create_time"
    UPDATE_TIME = "update_time"


class JobIndexViewEnum(enum.Enum):
    COLLECTION = "collection"
    ADMIN_JOB_LIST = "admin_job_list"


class JobSourceType(enum.Enum):
    """Available types of job sources (model classes) that produce dataset collections."""

    JOB = "Job"
    IMPLICITCOLLECTIONJOBS = "ImplicitCollectionJobs"
    WORKFLOWINVOCATION = "WorkflowInvocation"


class JobState(enum.Enum):
    NEW = "new"
    RESUBMITTED = "resubmitted"
    UPLOAD = "upload"
    WAITING = "waiting"
    QUEUED = "queued"
    RUNNING = "running"
    OK = "ok"
    ERROR = "error"
    FAILED = "failed"
    PAUSED = "paused"
    DELETING = "deleting"
    DELETED = "deleted"
    STOP = "stop"
    STOPPED = "stopped"
    SKIPPED = "skipped"


class LandingRequestState(enum.Enum):
    UNCLAIMED = "unclaimed"
    CLAIMED = "claimed"


class LibraryFolderPermissionAction(enum.Enum):
    SET_PERMISSIONS = "set_permissions"


class LibraryPermissionAction(enum.Enum):
    SET_PERMISSIONS = "set_permissions"
    REMOVE_RESTRICTIONS = "remove_restrictions"


class LibraryPermissionScope(enum.Enum):
    CURRENT = "current"
    AVAILABLE = "available"


class LinkDataOnly(enum.Enum):
    COPY_FILES = "copy_files"
    LINK_TO_FILES = "link_to_files"


class MandatoryNotificationCategory(enum.Enum):
    """These notification categories cannot be opt-out by the user.

    The user will always receive notifications from these categories."""

    BROADCAST = "broadcast"


class ModelStoreFormat(enum.Enum):
    """Available types of model stores for export."""

    TGZ = "tgz"
    TAR = "tar"
    TAR_GZ = "tar.gz"
    BAG_ZIP = "bag.zip"
    BAG_TAR = "bag.tar"
    BAG_TGZ = "bag.tgz"
    ROCRATE_ZIP = "rocrate.zip"
    BCO_JSON = "bco.json"


class NotificationVariant(enum.Enum):
    """The notification variant communicates the intent or relevance of the notification."""

    INFO = "info"
    WARNING = "warning"
    URGENT = "urgent"


class PageContentFormat(enum.Enum):
    MARKDOWN = "markdown"
    HTML = "html"


class PersonalNotificationCategory(enum.Enum):
    """These notification categories can be opt-out by the user and will be
    displayed in the notification preferences."""

    MESSAGE = "message"
    NEW_SHARED_ITEM = "new_shared_item"


class PluginKind(enum.Enum):
    """Enum to distinguish between different kinds or categories of plugins."""

    RFS = "rfs"
    DRS = "drs"
    RDM = "rdm"
    STOCK = "stock"


class QuotaOperation(enum.Enum):
    EQUAL = "="
    PLUS = "+"
    MINUS = "-"


class RefactorActionExecutionMessageTypeEnum(enum.Enum):
    TOOL_VERSION_CHANGE = "tool_version_change"
    TOOL_STATE_ADJUSTMENT = "tool_state_adjustment"
    CONNECTION_DROP_FORCED = "connection_drop_forced"
    WORKFLOW_OUTPUT_DROP_FORCED = "workflow_output_drop_forced"


class RemoteFilesDisableMode(enum.Enum):
    FOLDERS = "folders"
    FILES = "files"


class RemoteFilesFormat(enum.Enum):
    FLAT = "flat"
    JSTREE = "jstree"
    URI = "uri"


class RequestDataType(enum.Enum):
    """Particular pieces of information that can be requested for a dataset."""

    STATE = "state"
    CONVERTED_DATASETS_STATE = "converted_datasets_state"
    DATA = "data"
    FEATURES = "features"
    RAW_DATA = "raw_data"
    TRACK_CONFIG = "track_config"
    GENOME_DATA = "genome_data"
    IN_USE_STATE = "in_use_state"


class Requirement(enum.Enum):
    """Available types of job sources (model classes) that produce dataset collections."""

    LOGGED_IN = "logged_in"
    NEW_HISTORY = "new_history"
    ADMIN = "admin"


class SharingOptions(enum.Enum):
    """Options for sharing resources that may have restricted access to all or part of their contents."""

    MAKE_PUBLIC = "make_public"
    MAKE_ACCESSIBLE_TO_SHARED = "make_accessible_to_shared"
    NO_CHANGES = "no_changes"


class Src(enum.Enum):
    URL = "url"
    PASTED = "pasted"
    FILES = "files"
    PATH = "path"
    COMPOSITE = "composite"
    FTP_IMPORT = "ftp_import"
    SERVER_DIR = "server_dir"


class StoredItemOrderBy(enum.Enum):
    """Available options for sorting Stored Items results."""

    NAME_ASC = "name-asc"
    NAME_DSC = "name-dsc"
    SIZE_ASC = "size-asc"
    SIZE_DSC = "size-dsc"
    UPDATE_TIME_ASC = "update_time-asc"
    UPDATE_TIME_DSC = "update_time-dsc"


class SupportedType(enum.Enum):
    NONE = "None"
    BASICAUTH = "BasicAuth"
    BEARERAUTH = "BearerAuth"
    PASSPORTAUTH = "PassportAuth"


class TaggableItemClass(enum.Enum):
    HISTORY = "History"
    HISTORYDATASETASSOCIATION = "HistoryDatasetAssociation"
    HISTORYDATASETCOLLECTIONASSOCIATION = "HistoryDatasetCollectionAssociation"
    LIBRARYDATASETDATASETASSOCIATION = "LibraryDatasetDatasetAssociation"
    PAGE = "Page"
    STOREDWORKFLOW = "StoredWorkflow"
    VISUALIZATION = "Visualization"


class TaskState(enum.Enum):
    """Enum representing the possible states of a task."""

    PENDING = "PENDING"
    STARTED = "STARTED"
    RETRY = "RETRY"
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"


class ToolRequestState(enum.Enum):
    NEW = "new"
    SUBMITTED = "submitted"
    FAILED = "failed"


class UploadOption(enum.Enum):
    UPLOAD_FILE = "upload_file"
    UPLOAD_PATHS = "upload_paths"
    UPLOAD_DIRECTORY = "upload_directory"


class FetchDatasetHash(BaseModel):
    hash_function: Literal["MD5", "SHA-1", "SHA-256", "SHA-512"]
    hash_value: str


class UserNotificationUpdateRequest(BaseModel):
    """A notification update request specific to the user."""

    deleted: bool | None = Field(
        None,
        description="Whether the notification should be marked as deleted by the user. If not set, the notification will not be changed.",
    )
    seen: bool | None = Field(
        None,
        description="Whether the notification should be marked as seen by the user. If not set, the notification will not be changed.",
    )


class LibraryContentsDeleteResponse(BaseModel):
    deleted: bool
    id: str


class UpdateLicenseAction(BaseModel):
    action_type: str
    license: str


class YamlTemplateConfigFile(BaseModel):
    content: str
    eval_engine: str | None = None
    filename: str | None = None
    name: str | None = None


class ChatResponse(BaseModel):
    error_code: int | None = Field(description="The error code, if any, for the chat query.")
    error_message: str | None = Field(description="The error message, if any, for the chat query.")
    response: str = Field(description="The response to the chat query.")


class CwlIntegerParameterModel(BaseModel):
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    parameter_type: str | None = None


class FavoriteObject(BaseModel):
    object_id: str = Field(description="The id of an object the user wants to favorite.")


class HDABasicInfo(BaseModel):
    id: str
    name: str


class CreatedUserModel(BaseModel):
    active: bool = Field(description="User is active")
    deleted: bool = Field(description=" User is deleted")
    email: str = Field(description="Email of the user")
    id: str = Field(description="Encoded ID of the user")
    last_password_change: str | None = Field(description="")
    model_class: str = Field(description="The name of the database model class.")
    nice_total_disk_usage: str = Field(
        description="Size of all non-purged, unique datasets of the user in a nice format."
    )
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    total_disk_usage: float = Field(description="Size of all non-purged, unique datasets of the user in bytes.")
    username: str = Field(description="The name of the user.")


class CollectionElementIdentifier(BaseModel):
    collection_type: str | None = Field(
        None,
        description="The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.",
    )
    element_identifiers: list[CollectionElementIdentifier] | None = Field(
        None, description="List of elements that should be in the new sub-collection."
    )
    id: str | None = Field(None, description="The encoded ID of the element.")
    name: str | None = Field(None, description="The name of the element.")
    src: CollectionSourceType = Field(description="The source of the element.")
    tags: list[str] | None = Field(None, description="The list of tags associated with the element.")


class ExportHistoryArchivePayload(BaseModel):
    directory_uri: str | None = Field(
        None,
        description="A writable directory destination where the history will be exported using the `galaxy.files` URI infrastructure.",
    )
    file_name: str | None = Field(None, description="The name of the file containing the exported history.")
    force: bool | None = Field(None, description="Whether to force a rebuild of the history archive.")
    gzip: bool | None = Field(None, description="Whether to export as gzip archive.")
    include_deleted: bool | None = Field(
        None, description="Whether to include deleted datasets in the exported archive."
    )
    include_hidden: bool | None = Field(None, description="Whether to include hidden datasets in the exported archive.")


class JobErrorSummary(BaseModel):
    messages: list[list[str]] = Field(description="The error messages for the specified job.")


class UserQuotaUsage(BaseModel):
    quota: str | None = None
    quota_bytes: int | None = None
    quota_percent: float | None = None
    quota_source_label: str | None = None
    total_disk_usage: float


class ShareWithExtra(BaseModel):
    can_share: bool | None = Field(
        None, description="Indicates whether the resource can be directly shared or requires further actions."
    )


class DatasetPermissions(BaseModel):
    """Role-based permissions for accessing and managing a dataset."""

    access: list[str] | None = Field(None, description="The set of roles (encoded IDs) that can access this dataset.")
    manage: list[str] | None = Field(None, description="The set of roles (encoded IDs) that can manage this dataset.")


class ExtraFiles(BaseModel):
    fuzzy_root: bool | None = Field(
        None,
        description="Prevent Galaxy from checking for a single file in a directory and re-interpreting the archive",
    )
    items_from: str | None = None
    src: Src


class FavoriteObjectsSummary(BaseModel):
    tools: list[str] = Field(description="The name of the tools the user favored.")


class RootModelDictStr_int_(BaseModel):
    pass


class ElementsStatesDict(BaseModel):
    deferred: int | None = None
    discarded: int | None = None
    empty: int | None = None
    error: int | None = None
    failed_metadata: int | None = None
    new: int | None = None
    ok: int | None = None
    paused: int | None = None
    queued: int | None = None
    running: int | None = None
    setting_metadata: int | None = None
    upload: int | None = None


class CwlNullParameterModel(BaseModel):
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    parameter_type: str | None = None


class ResourceRequirement(BaseModel):
    cores_max: int | float | None = Field(
        None,
        description="Maximum reserved number of CPU cores.\nMay be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs. For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3).\nThe reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the cores request to the next whole number.\n",
    )
    cores_min: int | float | None = Field(
        None,
        description="Minimum reserved number of CPU cores.\nMay be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs. For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3).\nThe reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the cores request to the next whole number.\n",
    )
    cuda_compute_capability: float | int | None = None
    cuda_device_count_max: float | int | None = None
    cuda_device_count_min: float | int | None = None
    cuda_version_min: float | int | None = None
    gpu_memory_min: float | int | None = None
    ram_max: int | float | None = Field(
        None,
        description="Maximum reserved RAM in mebibytes (2**20).\nMay be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported amount of RAM reserved for the process is a non-zero integer.",
    )
    ram_min: int | float | None = Field(
        None,
        description="Minimum reserved RAM in mebibytes (2**20).\nMay be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported amount of RAM reserved for the process is a non-zero integer.",
    )
    shm_size: float | int | None = None
    tmpdir_max: float | int | None = None
    tmpdir_min: float | int | None = None
    type: str


class ToolOutputInteger(BaseModel):
    hidden: Any = Field(description="If true, the output will not be shown in the history.")
    label: str | None = Field(None, description="Output label. Will be used as dataset name in history.")
    name: Any = Field(description="Parameter name. Used when referencing parameter in workflows.")
    type: str


class EncodedHdcaSourceId(BaseModel):
    id: str
    src: str = Field(description="The source of this dataset, which in the case of the model can only be `hdca`.")


class RegexJobMessage(BaseModel):
    code_desc: str | None = None
    desc: str | None
    error_level: float
    match: str | None
    stream: str | None
    type: str


class HelpForumPost(BaseModel):
    """Model for a post in the help forum."""

    avatar_template: str | None = Field(description="The avatar template of the user.")
    blurb: str | None = Field(description="The blurb of the post.")
    created_at: str | None = Field(description="The creation date of the post.")
    id: int = Field(description="The ID of the post.")
    like_count: int | None = Field(description="The number of likes of the post.")
    name: str | None = Field(description="The name of the post.")
    post_number: int | None = Field(description="The post number of the post.")
    topic_id: int | None = Field(description="The ID of the topic of the post.")
    username: str | None = Field(description="The username of the post author.")


class EncodedDataItemSourceId(BaseModel):
    id: str
    src: DataItemSourceType = Field(
        description="The source of this dataset, either `hda`, `ldda`, `hdca`, `dce` or `dc` depending of its origin."
    )


class CsvDialect(BaseModel):
    delimiter: str
    double_quote: bool
    escape_character: str | None
    line_terminator: str
    quote_character: str | None
    skip_initial_space: bool


class LicenseMetadataModel(BaseModel):
    detailsUrl: str = Field(description="URL to the SPDX json details for this license")
    isDeprecatedLicenseId: bool = Field(description="True if the entire license is deprecated")
    isOsiApproved: bool = Field(description="Indicates if the [OSI](https://opensource.org/) has approved the license")
    licenseId: str = Field(description="SPDX Identifier")
    name: str = Field(description="Full name of the license")
    recommended: bool = Field(description="True if this license is recommended to be used")
    reference: str = Field(description="Reference to the HTML format for the license file")
    referenceNumber: int = Field(description="*Deprecated* - this field is generated and is no longer in use")
    seeAlso: list[str] = Field(description="Cross reference URL pointing to additional copies of the license")
    spdxUrl: str
    url: str = Field(description="License URL")


class InvocationCancellationHistoryDeletedResponse(BaseModel):
    history_id: str = Field(description="History ID of history that was deleted.")
    reason: str


class ReportInvocationErrorPayload(BaseModel):
    email: str | None = Field(
        None, description="Email address for communication with the user. Only required for anonymous users."
    )
    invocation_id: str = Field(description="The ID of the invocation related to the error.")
    message: str | None = Field(None, description="The optional message sent with the error report.")


class LibraryContentsFolderCreatePayload(BaseModel):
    create_type: CreateType = Field(description="the type of item to create")
    description: str | None = None
    extended_metadata: dict[str, Any] | None = Field(
        None, description="sub-dictionary containing any extended metadata to associate with the item"
    )
    folder_id: str = Field(description="the encoded id of the parent folder of the new item")
    from_hda_id: str | None = Field(
        None, description="(only if create_type is 'file') the encoded id of an accessible HDA to copy into the library"
    )
    from_hdca_id: str | None = Field(
        None,
        description="(only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library",
    )
    ldda_message: str | None = Field(None, description="the new message attribute of the LDDA created")
    name: str | None = None
    tag_using_filenames: bool | None = Field(None, description="create tags on datasets using the file's original name")
    tags: list[str] | None = Field(None, description="create the given list of tags on datasets")
    upload_option: UploadOption | None = Field(None, description="the method to use for uploading files")


class StoredItem(BaseModel):
    id: str
    name: str
    size: int
    type: str
    update_time: str = Field(description="The last time and date this item was updated.")


class RoleModelResponse(BaseModel):
    description: str | None
    id: str = Field(description="Encoded ID of the role")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="Name of the role")
    type: str = Field(description="Type or category of the role")
    url: str = Field(description="The relative URL to access this item.")


class InvocationFailureCollectionFailedResponse(BaseModel):
    dependent_workflow_step_id: int = Field(description="Workflow step id of step that caused failure.")
    hdca_id: str = Field(description="HistoryDatasetCollectionAssociation ID that relates to failure.")
    reason: str
    workflow_step_id: int = Field(description="Workflow step id of step that failed.")


class Authorizations(BaseModel):
    bearer_auth_issuers: list[str] | None = Field(
        None,
        description="If authorizations contain `BearerAuth` this is an optional list of issuers that may authorize access to this object. The caller must provide a token from one of these issuers. If this is empty or missing it assumed the caller knows which token to send via other means. It is strongly recommended that the caller validate that it is appropriate to send the requested token to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.",
    )
    passport_auth_issuers: list[str] | None = Field(
        None,
        description="If authorizations contain `PassportAuth` this is a required list of visa issuers (as found in a visa's `iss` claim) that may authorize access to this object. The caller must only provide passports that contain visas from this list. It is strongly recommended that the caller validate that it is appropriate to send the requested passport/visa to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.",
    )
    supported_types: list[SupportedType] | None = Field(
        None,
        description="An Optional list of support authorization types. More than one can be supported and tried in sequence. Defaults to `None` if empty or missing.",
    )


class InvocationInput(BaseModel):
    id: str | None = Field(None, description="The encoded ID of the dataset/dataset collection.")
    label: str | None = Field(
        None, description="Label of the workflow step associated with the input dataset/dataset collection."
    )
    src: str = Field(description="Source type of the input dataset/dataset collection.")
    workflow_step_id: str = Field(
        description="The encoded ID of the workflow step associated with the dataset/dataset collection."
    )


class ContentsObject(BaseModel):
    contents: list[ContentsObject] | None = Field(
        None,
        description='If this ContentsObject describes a nested bundle and the caller specified "?expand=true" on the request, then this contents array must be present and describe the objects within the nested bundle.',
    )
    drs_uri: list[str] | None = Field(
        None,
        description="A list of full DRS identifier URI paths that may be used to obtain the object. These URIs may be external to this DRS instance.",
    )
    id: str | None = Field(
        None,
        description="A DRS identifier of a `DrsObject` (either a single blob or a nested bundle). If this ContentsObject is an object within a nested bundle, then the id is optional. Otherwise, the id is required.",
    )
    name: str = Field(
        description="A name declared by the bundle author that must be used when materialising this object, overriding any name directly associated with the object itself. The name must be unique within the containing bundle. This string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames]."
    )


class LibraryFolderDetails(BaseModel):
    deleted: bool = Field(description="Whether this folder is marked as deleted.")
    description: str | None = Field(None, description="A detailed description of the library folder.")
    genome_build: str | None = Field(None, description="TODO")
    id: str = Field(description="Encoded ID of the library folder.")
    item_count: int = Field(description="A detailed description of the library folder.")
    library_path: list[str] | None = Field(
        None, description="The list of folder names composing the path to this folder."
    )
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the library folder.")
    parent_id: str | None = Field(None, description="Encoded ID of the parent folder. Empty if it's the root folder.")
    parent_library_id: str = Field(description="Encoded ID of the Library this folder belongs to.")
    update_time: str = Field(description="The last time and date this item was updated.")


class PageDetails(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    author_deleted: bool = Field(description="Whether the author of this Page has been deleted.")
    content: str | None = Field(
        None,
        description="Text contents of the last page revision with embedded directives expanded (type dependent on content_format).",
    )
    content_editor: str | None = Field(
        None, description="Raw text contents of the last page revision (type dependent on content_format)."
    )
    content_format: PageContentFormat | None = Field(None, description="Either `markdown` or `html`.")
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this Page has been deleted.")
    email_hash: str = Field(description="The encoded email of the user.")
    generate_time: str | None = Field(None, description="The version of Galaxy this object was generated with.")
    generate_version: str | None = Field(None, description="The version of Galaxy this object was generated with.")
    id: str = Field(description="Encoded ID of the Page.")
    importable: bool = Field(description="Whether this Page can be imported.")
    latest_revision_id: str = Field(description="The encoded ID of the last revision of this Page.")
    model_class: str = Field(description="The name of the database model class.")
    published: bool = Field(description="Whether this Page has been published.")
    revision_ids: list[str] = Field(description="The history with the encoded ID of each revision of the Page.")
    slug: str = Field(description="The identifying slug for the page URL, must be unique.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    title: str = Field(description="The name of the page.")
    update_time: str = Field(description="The last time and date this item was updated.")
    username: str = Field(description="The name of the user owning this Page.")


class InvocationStepJobsResponseStepModel(BaseModel):
    id: str = Field(description="The encoded ID of the workflow invocation.")
    model: str
    populated_state: JobState = Field(description="The absolute state of all the jobs related to the Invocation.")
    states: dict[str, Any] = Field(description="The states of all the jobs related to the Invocation.")


class UserFileSourceModel(BaseModel):
    active: bool
    description: str | None
    hidden: bool
    name: str
    purged: bool
    secrets: list[str]
    template_id: str
    template_version: int
    type: Literal[
        "ftp",
        "posix",
        "s3fs",
        "azure",
        "azureflat",
        "onedata",
        "webdav",
        "dropbox",
        "googledrive",
        "elabftw",
        "inveniordm",
        "zenodo",
        "rspace",
        "dataverse",
        "huggingface",
        "omero",
    ]
    uri_root: str
    uuid: str
    variables: dict[str, Any] | None


class ConcreteObjectStoreQuotaSourceDetails(BaseModel):
    enabled: bool = Field(
        description="Whether the object store tracks quota on the data (independent of Galaxy's configuration)"
    )
    source: str | None = Field(
        description="The quota source label corresponding to the object store the dataset is stored in (or would be stored in)"
    )


class RemoteFileHash(BaseModel):
    hash_function: Literal["MD5", "SHA-1", "SHA-256", "SHA-512"]
    hash_value: str


class UpdateInstancePayload(BaseModel):
    active: bool | None = None
    description: str | None = None
    hidden: bool | None = None
    name: str | None = None
    variables: dict[str, Any] | None = None


class InvocationStepCollectionOutput(BaseModel):
    id: str = Field(description="Dataset Collection ID of the workflow step output.")
    src: str | None = Field(None, description="The source model of the output.")


class LibraryCurrentPermissions(BaseModel):
    access_library_role_list: list[list[str]] = Field(
        description="A list containing pairs of role names and corresponding encoded IDs which have access to the Library."
    )
    add_library_item_role_list: list[list[str]] = Field(
        description="A list containing pairs of role names and corresponding encoded IDs which can add items to the Library."
    )
    manage_library_role_list: list[list[str]] = Field(
        description="A list containing pairs of role names and corresponding encoded IDs which can manage the Library."
    )
    modify_library_role_list: list[list[str]] = Field(
        description="A list containing pairs of role names and corresponding encoded IDs which can modify the Library."
    )


class VisualizationUpdateResponse(BaseModel):
    id: str = Field(description="Encoded ID of the Visualization.")
    revision: str = Field(description="Encoded ID of the Visualization Revision.")


class LibraryFolderDestination(BaseModel):
    library_folder_id: str
    type: str


class FilesSourceSupports(BaseModel):
    pagination: bool | None = Field(None, description="Whether this file source supports server-side pagination.")
    search: bool | None = Field(None, description="Whether this file source supports server-side search.")
    sorting: bool | None = Field(None, description="Whether this file source supports server-side sorting.")


class JobBaseModel(BaseModel):
    create_time: str = Field(description="The time and date this item was created.")
    exit_code: int | None = Field(
        None, description="The exit code returned by the tool. Can be unset if the job is not completed yet."
    )
    galaxy_version: str | None = Field(None, description="The (major) version of Galaxy used to create this job.")
    history_id: str | None = Field(None, description="The encoded ID of the history associated with this item.")
    id: str
    model_class: str = Field(description="The name of the database model class.")
    state: JobState = Field(description="Current state of the job.")
    tool_id: str = Field(description="Identifier of the tool that generated this job.")
    update_time: str = Field(description="The last time and date this item was updated.")


class InvocationEvaluationWarningWorkflowOutputNotFoundResponse(BaseModel):
    output_name: str = Field(description="Output that was designated as workflow output but that has not been found")
    reason: str
    workflow_step_id: int


class JobIdResponse(BaseModel):
    """Contains the ID of the job associated with a particular request."""

    job_id: str


class TaskResult(BaseModel):
    """Contains information about the result of an asynchronous task."""

    result: str = Field(
        description="The result message of the task. Empty if the task is still running. If the task failed, this will contain the exception message."
    )
    state: TaskState = Field(description="The current state of the task.")


class UpdateDatasetPermissionsPayloadAliasC(BaseModel):
    access_ids: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have access permission on the dataset."
    )
    action: DatasetPermissionAction | None = Field(
        None, description="Indicates what action should be performed on the dataset."
    )
    manage_ids: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have manage permission on the dataset."
    )
    modify_ids: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have modify permission on the dataset."
    )


class UserCreationPayload(BaseModel):
    email: str = Field(description="Email of the user")
    password: str = Field(description="The password of the user.")
    username: str = Field(description="The name of the user.")


class CreateInvocationsFromStorePayload(BaseModel):
    history_id: str = Field(description="The ID of the history associated with the invocations.")
    legacy_job_state: bool | None = Field(
        None,
        description="Populate the invocation step state with the job state instead of the invocation step state.\n        This will also produce one step per job in mapping jobs to mimic the older behavior with respect to collections.\n        Partially scheduled steps may provide incomplete information and the listed steps outputs\n        are not the mapped over step outputs but the individual job outputs.",
    )
    model_store_format: ModelStoreFormat | None = None
    step_details: bool | None = Field(
        None,
        description="Include details for individual invocation steps and populate a steps attribute in the resulting dictionary",
    )
    store_content_uri: str | None = None
    store_dict: dict[str, Any] | None = None
    view: InvocationSerializationView | None = Field(
        None,
        description="The name of the view used to serialize this item. This will return a predefined set of attributes of the item.",
    )


class InvocationOutputCollection(BaseModel):
    id: str | None = Field(None, description="The encoded ID of the dataset/dataset collection.")
    src: str = Field(description="Source model of the output dataset collection.")
    workflow_step_id: str = Field(
        description="The encoded ID of the workflow step associated with the dataset/dataset collection."
    )


class InvocationUpdatePayload(BaseModel):
    action: bool = Field(description="Whether to take action on the invocation step.")


class AvailableAgent(BaseModel):
    """Information about an available agent."""

    agent_type: str = Field(description="Unique identifier for the agent")
    description: str = Field(description="Description of the agent's capabilities")
    enabled: bool = Field(description="Whether the agent is currently enabled")
    model: str | None = Field(None, description="LLM model used by the agent")
    name: str = Field(description="Human-readable name")
    specialties: list[str] | None = Field(None, description="Areas of specialization")


class DataColumnParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    multiple: bool
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str
    value: int | list[int] | None = None


class JobExportHistoryArchiveModel(BaseModel):
    download_url: str = Field(description="Relative API URL to download the exported history archive.")
    external_download_latest_url: str = Field(
        description="Fully qualified URL to download the latests version of the exported history archive."
    )
    external_download_permanent_url: str = Field(
        description="Fully qualified URL to download this particular version of the exported history archive."
    )
    id: str = Field(description="The encoded database ID of the export request.")
    job_id: str = Field(description="The encoded database ID of the job that generated this history export archive.")
    preparing: bool = Field(description="Whether the archive is currently being built or in preparation.")
    ready: bool = Field(description="Whether the export has completed successfully and the archive is ready")
    up_to_date: bool = Field(description="False, if a new export archive should be generated.")


class HDAObject(BaseModel):
    """History Dataset Association Object"""

    accessible: bool | None = None
    copied_from_ldda_id: str | None = None
    hda_ldda: DatasetSourceType | None = Field(
        None, description="Whether this dataset belongs to a history (HDA) or a library (LDDA)."
    )
    history_id: str
    id: str
    model_class: str = Field(description="The name of the database model class.")
    purged: bool
    state: DatasetState = Field(description="The current state of this dataset.")
    tags: list[str]


class StoreExportPayload(BaseModel):
    include_deleted: bool | None = Field(
        None, description="Include file contents for deleted datasets (if include_files is True)."
    )
    include_files: bool | None = Field(None, description="include materialized files in export when available")
    include_hidden: bool | None = Field(
        None, description="Include file contents for hidden datasets (if include_files is True)."
    )
    model_store_format: ModelStoreFormat | None = Field(None, description="format of model store to export")


class InputStep(BaseModel):
    source_step: int = Field(description="The identifier of the workflow step connected to this particular input.")
    step_output: str = Field(description="The name of the output generated by the source step.")


class CreateLibrariesFromStore(BaseModel):
    model_store_format: ModelStoreFormat | None = None
    store_content_uri: str | None = None
    store_dict: dict[str, Any] | None = None


class ImplicitCollectionJobsStateSummary(BaseModel):
    id: str
    model: str = Field(description="The name of the database model class.")
    populated_state: DatasetCollectionPopulatedState = Field(
        description="Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated."
    )
    states: dict[str, Any] | None = Field(
        None, description="A dictionary of job states and the number of jobs in that state."
    )


class InvocationStepOutput(BaseModel):
    id: str = Field(description="Dataset ID of the workflow step output.")
    src: str | None = Field(None, description="The source model of the output.")
    uuid: str | None = Field(None, description="Universal unique identifier of the workflow step output dataset.")


class RefactorActionExecutionMessage(BaseModel):
    from_order_index: int | None = Field(
        None,
        description="For dropped connections these optional attributes refer to the output\nside of the connection that was dropped.",
    )
    from_step_label: str | None = Field(
        None,
        description="For dropped connections these optional attributes refer to the output\nside of the connection that was dropped.",
    )
    input_name: str | None = Field(
        None,
        description="If this message is about an input to a step,\nthis field describes the target input name. $The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input').",
    )
    message: str
    message_type: RefactorActionExecutionMessageTypeEnum
    order_index: int | None = Field(
        None,
        description="Reference to the step the message refers to. $\n\nMessages don't have to be bound to a step, but if they are they will\nhave a step_label and order_index included in the execution message.\nThese are the label and order_index before applying the refactoring,\nthe result of applying the action may change one or both of these.\nIf connections are dropped this step reference will refer to the\nstep with the previously connected input.\n",
    )
    output_label: str | None = Field(
        None, description="If the message_type is workflow_output_drop_forced, this is the output label dropped."
    )
    output_name: str | None = Field(
        None,
        description="If this message is about an output to a step,\nthis field describes the target output name. The output name as defined by the workflow module corresponding to the step being referenced.\n",
    )
    step_label: str | None = Field(
        None,
        description="Reference to the step the message refers to. $\n\nMessages don't have to be bound to a step, but if they are they will\nhave a step_label and order_index included in the execution message.\nThese are the label and order_index before applying the refactoring,\nthe result of applying the action may change one or both of these.\nIf connections are dropped this step reference will refer to the\nstep with the previously connected input.\n",
    )


class HDAInaccessible(BaseModel):
    """History Dataset Association information when the user can not access it."""

    accessible: bool
    copied_from_ldda_id: str | None = None
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    hid: int = Field(description="The index position of this item in the History.")
    history_content_type: str = Field(description="This is always `dataset` for datasets.")
    history_id: str
    id: str
    name: str | None = Field(description="The name of the item.")
    state: DatasetState = Field(description="The current state of this dataset.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    type: str = Field(description="The type of this item.")
    type_id: str | None = Field(None, description="The type and the encoded ID of this item. Used for caching.")
    update_time: str | None = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    visible: bool = Field(description="Whether this item is visible or hidden to the user by default.")


class HelpForumGroup(BaseModel):
    """Model for a group in the help forum."""


class ClaimLandingPayload(BaseModel):
    client_secret: str | None = None


class LibraryFolderMetadata(BaseModel):
    can_add_library_item: bool
    can_modify_folder: bool
    folder_description: str
    folder_name: str
    full_path: list[list[Any]]
    parent_library_id: str
    total_rows: int


class HelpForumCategory(BaseModel):
    """Model for a category in the help forum."""


class NotificationChannelSettings(BaseModel):
    """The settings for each channel of a notification category."""

    email: bool | None = Field(
        None,
        description="Whether the user wants to receive email notifications for this category. This setting will be ignored unless the server supports asynchronous tasks.",
    )
    push: bool | None = Field(
        None, description="Whether the user wants to receive push notifications in the browser for this category."
    )


class UpdateInstanceSecretPayload(BaseModel):
    secret_name: str
    secret_value: str


class DatasetHash(BaseModel):
    extra_files_path: str | None = Field(None, description="The path to the extra files used to generate the hash.")
    hash_function: HashFunctionNameEnum = Field(description="The hash function used to generate the hash.")
    hash_value: str = Field(description="The hash value.")
    id: str = Field(description="Encoded ID of the dataset hash.")
    model_class: str = Field(description="The name of the database model class.")


class BasicRoleModel(BaseModel):
    id: str = Field(description="Encoded ID of the role")
    name: str = Field(description="Name of the role")
    type: str = Field(description="Type or category of the role")


class QuotaSummary(BaseModel):
    """Contains basic information about a Quota"""

    id: str = Field(description="The `encoded identifier` of the quota.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the quota. This must be unique within a Galaxy instance.")
    quota_source_label: str | None = Field(None, description="Quota source label")
    url: str = Field(description="The relative URL to get this particular Quota details from the rest API.")


class VisualizationRevisionResponse(BaseModel):
    config: dict[str, Any] = Field(description="The config of the visualization revision.")
    dbkey: str | None = Field(None, description="The database key of the visualization.")
    id: str = Field(description="Encoded ID of the Visualization Revision.")
    model_class: str = Field(description="The name of the database model class.")
    title: str = Field(description="The name of the visualization revision.")
    visualization_id: str = Field(description="Encoded ID of the Visualization.")


class ToolDataEntry(BaseModel):
    model_class: str = Field(description="The name of class modelling this tool data")
    name: str = Field(description="The name of this tool data entry")


class DatasetAssociationRoles(BaseModel):
    access_dataset_roles: list[list[str]] | None = Field(
        None,
        description="A list of roles that can access the dataset. The user has to **have all these roles** in order to access this dataset. Users without access permission **cannot** have other permissions on this dataset. If there are no access roles set on the dataset it is considered **unrestricted**.",
    )
    manage_dataset_roles: list[list[str]] | None = Field(
        None,
        description="A list of roles that can manage permissions on the dataset. Users with **any** of these roles can manage permissions of this dataset. If you remove yourself you will lose the ability to manage this dataset unless you are an admin.",
    )
    modify_item_roles: list[list[str]] | None = Field(
        None,
        description="A list of roles that can modify the library item. This is a library related permission. User with **any** of these roles can modify name, metadata, and other information about this library item.",
    )


class UpdateQuotaParams(BaseModel):
    amount: str | None = Field(None, description="Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)")
    default: DefaultQuotaValues | None = Field(
        None,
        description='Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. Calling this method with ``default="no"`` on a non-default quota will throw an error. Not passing this parameter is equivalent to passing ``no``.',
    )
    description: str | None = Field(None, description="Detailed text description for this Quota.")
    in_groups: list[str] | None = Field(None, description="A list of group IDs or names to associate with this quota.")
    in_users: list[str] | None = Field(
        None, description="A list of user IDs or user emails to associate with this quota."
    )
    name: str | None = Field(
        None, description="The new name of the quota. This must be unique within a Galaxy instance."
    )
    operation: QuotaOperation | None = Field(
        None,
        description="One of (``+``, ``-``, ``=``). If you wish to change this value, you must also provide the ``amount``, otherwise it will not take effect.",
    )


class LibraryFolderPermissionsPayload(BaseModel):
    action: LibraryFolderPermissionAction | None = Field(
        None, description="Indicates what action should be performed on the library folder."
    )
    add_ids__: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should be able to add items to the library."
    )
    manage_ids__: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have manage permission on the library."
    )
    modify_ids__: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have modify permission on the library."
    )


class XrefDict(BaseModel):
    type: str
    value: str


class WorkflowInvocationStateSummary(BaseModel):
    id: str
    model: str = Field(description="The name of the database model class.")
    populated_state: DatasetCollectionPopulatedState = Field(
        description="Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated."
    )
    states: dict[str, Any] | None = Field(
        None, description="A dictionary of job states and the number of jobs in that state."
    )


class CopyDatasetsPayloadSourceEntry(BaseModel):
    id: str
    type: str


class UpdateNameAction(BaseModel):
    action_type: str
    name: str


class ItemTagsResponse(BaseModel):
    """Response schema for showing an item tag."""

    id: str
    model_class: str
    user_tname: str
    user_value: str | None = None


class JobConsoleOutput(BaseModel):
    state: JobState | None = Field(None, description="The current job's state")
    stderr: str | None = Field(None, description="Tool STDERR from job.")
    stdout: str | None = Field(None, description="Tool STDOUT from job.")


class CreateHistoryFromStore(BaseModel):
    model_store_format: ModelStoreFormat | None = None
    store_content_uri: str | None = None
    store_dict: dict[str, Any] | None = None


class ContextResponse(BaseModel):
    config: dict[str, Any]
    session_csrf_token: str | None = None
    user: dict[str, Any]


class HelpForumTag(BaseModel):
    """Model for a tag in the help forum."""


class ChangeDatatypeOperationParams(BaseModel):
    datatype: str
    type: str


class InvokeWorkflowPayload(BaseModel):
    allow_tool_state_corrections: bool | None = Field(
        None, description="Indicates if tool state corrections are allowed for workflow invocation."
    )
    batch: bool | None = Field(None, description="Indicates if the workflow is invoked as a batch.")
    ds_map: dict[str, Any] | None = Field(
        None,
        description="An older alternative to specifying inputs using database IDs, do not use this and use inputs instead",
    )
    effective_outputs: Any | None = Field(None, description="TODO")
    history: str | None = Field(
        None,
        description="The encoded history id - passed exactly like this 'hist_id=...' -  into which to import. Or the name of the new history into which to import.",
    )
    history_id: str | None = Field(None, description="The encoded history id into which to import.")
    inputs: dict[str, Any] | None = Field(None, description="Specify values for formal inputs to the workflow")
    inputs_by: str | None = Field(
        None,
        description="How the 'inputs' field maps its inputs (datasets/collections/step parameters) to workflows steps.",
    )
    instance: bool | None = Field(
        None, description="True when fetching by Workflow ID, False when fetching by StoredWorkflow ID"
    )
    landing_uuid: str | None = Field(
        None, description="The UUID of the workflow landing request associated with this invocation."
    )
    legacy: bool | None = Field(None, description="Indicating if to use legacy workflow invocation.")
    new_history_name: str | None = Field(None, description="The name of the new history into which to import.")
    no_add_to_history: bool | None = Field(
        None, description="Indicates if the workflow invocation should not be added to the history."
    )
    parameters: dict[str, Any] | None = Field(
        None,
        description="Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead.",
    )
    parameters_normalized: bool | None = Field(
        None,
        description="Indicates if legacy parameters are already normalized to be indexed by the order_index and are specified as a dictionary per step. Legacy-style parameters could previously be specified as one parameter per step or by tool ID.",
    )
    preferred_intermediate_object_store_id: str | None = Field(
        None,
        description="The ID of the object store that should be used to store the intermediate datasets of this workflow -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences",
    )
    preferred_object_store_id: str | None = Field(
        None,
        description="The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences",
    )
    preferred_outputs_object_store_id: str | None = Field(
        None,
        description="The ID of the object store that should be used to store the marked output datasets of this workflow - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences.",
    )
    replacement_params: dict[str, Any] | None = Field(
        None,
        description="Class of parameters mostly used for string replacement in PJAs. In best practice workflows, these should be replaced with input parameters",
    )
    require_exact_tool_versions: bool | None = Field(
        None, description="If true, exact tool versions are required for workflow invocation."
    )
    resource_params: dict[str, Any] | None = Field(
        None,
        description="If a workflow_resource_params_file file is defined and the target workflow is configured to consumer resource parameters, they can be specified with this parameter. See https://github.com/galaxyproject/galaxy/pull/4830 for more information.",
    )
    scheduler: str | None = Field(None, description="Scheduler to use for workflow invocation.")
    use_cached_job: bool | None = Field(
        None, description="Indicated whether to use a cached job for workflow invocation."
    )
    version: int | None = Field(None, description="The version of the workflow to invoke.")


class ServiceType(BaseModel):
    artifact: str = Field(
        description="Name of the API or GA4GH specification implemented. Official GA4GH types should be assigned as part of standards approval process. Custom artifacts are supported."
    )
    group: str = Field(
        description="Namespace in reverse domain name format. Use `org.ga4gh` for implementations compliant with official GA4GH specifications. For services with custom APIs not standardized by GA4GH, or implementations diverging from official GA4GH specifications, use a different namespace (e.g. your organization's reverse domain name)."
    )
    version: str = Field(
        description="Version of the API or specification. GA4GH specifications use semantic versioning."
    )


class InvocationInputParameter(BaseModel):
    label: str = Field(description="Label of the workflow step associated with the input parameter.")
    parameter_value: Any = Field(description="Value of the input parameter.")
    workflow_step_id: str = Field(
        description="The encoded ID of the workflow step associated with the input parameter."
    )


class UpdateDatasetPermissionsPayloadAliasB(BaseModel):
    access: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have access permission on the dataset."
    )
    action: DatasetPermissionAction | None = Field(
        None, description="Indicates what action should be performed on the dataset."
    )
    manage: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have manage permission on the dataset."
    )
    modify: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have modify permission on the dataset."
    )


class LibraryContentsCreateDatasetResponse(BaseModel):
    created_from_basename: str | None
    data_type: str
    deleted: bool
    file_ext: str
    file_name: str
    file_size: int
    genome_build: str
    hda_ldda: str
    id: str
    library_dataset_id: str
    misc_blurb: str | None
    misc_info: str | None
    model_class: str = Field(description="The name of the database model class.")
    name: str
    parent_library_id: str
    state: str
    update_time: str
    uuid: str
    visible: bool


class JobDestinationParams(BaseModel):
    Handler: str | None = Field(None, description="Name of the process that handled the job.")
    Runner: str | None = Field(None, description="Job runner class")
    Runner_Job_ID: str | None = Field(None, description="ID assigned to submitted job by external job running system")


class WorkflowInput(BaseModel):
    label: str | None = Field(description="Label of the input.")
    uuid: str | None = Field(description="Universal unique identifier of the input.")
    value: Any | None = Field(description="TODO")


class GroupUserResponse(BaseModel):
    email: str = Field(description="Email of the user")
    id: str
    url: str = Field(description="The relative URL to access this item.")


class CwlDirectoryParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None


class ToolLandingRequest(BaseModel):
    origin: str | None = None
    request_state: dict[str, Any] | None = None
    state: LandingRequestState
    tool_id: str
    tool_version: str | None = None
    uuid: str = Field(description="Universal unique identifier for this dataset.")


class PathBasedDynamicToolCreatePayload(BaseModel):
    active: bool | None = None
    hidden: bool | None = None
    path: str
    src: str
    tool_directory: str | None = None


class HistorySummary(BaseModel):
    """History summary information."""

    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    archived: bool = Field(description="Whether this item has been archived and is no longer active.")
    count: int = Field(description="The number of items in the history.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    id: str
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the history.")
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    published: bool = Field(description="Whether this resource is currently publicly available to all users.")
    purged: bool = Field(description="Whether this item has been permanently removed.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    update_time: str = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")


class CreateHistoryContentFromStore(BaseModel):
    model_store_format: ModelStoreFormat | None = None
    store_content_uri: str | None = None
    store_dict: dict[str, Any] | None = None


class ColorParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str
    value: str | None = None


class CwlFloatParameterModel(BaseModel):
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    parameter_type: str | None = None


class DatasetInheritanceChainEntry(BaseModel):
    dep: str = Field(description="Name of the source of the referenced dataset at this point of the inheritance chain.")
    id: str = Field(description="ID of the referenced dataset")
    name: str = Field(description="Name of the referenced dataset")
    user_id: str = Field(description="ID of the user who owns the referenced dataset.")


class DrillDownOptionsDictOutput(BaseModel):
    name: str | None
    options: list[DrillDownOptionsDictOutput]
    selected: bool
    value: str


class VisualizationCreatePayload(BaseModel):
    annotation: str | None = Field(None, description="The annotation of the visualization.")
    config: dict[str, Any] | None = Field(None, description="The config of the visualization.")
    dbkey: str | None = Field(None, description="The database key of the visualization.")
    slug: str | None = Field(None, description="The slug of the visualization.")
    title: str | None = Field(None, description="The name of the visualization.")
    type: str = Field(description="The type of the visualization.")


class HistoryContentStats(BaseModel):
    total_matches: int = Field(
        description="The total number of items that match the search query without any pagination"
    )


class InvocationFailureDatasetFailedResponse(BaseModel):
    dependent_workflow_step_id: int | None = Field(None, description="Workflow step id of step that caused failure.")
    hda_id: str = Field(description="HistoryDatasetAssociation ID that relates to failure.")
    reason: str
    workflow_step_id: int = Field(description="Workflow step id of step that failed.")


class UpdateCollectionAttributePayload(BaseModel):
    """Contains attributes that can be updated for all elements in a dataset collection."""

    dbkey: str = Field(description="TODO")


class HelpForumGroupedSearchResult(BaseModel):
    """Model for a grouped search result."""


class BodyAi_agentsCustomTool_createCustomTool(BaseModel):
    context: dict[str, Any] | None = Field(None, description="Additional context for tool creation")
    query: str = Field(description="Description of the tool to create")


class EncodedHistoryContentItem(BaseModel):
    history_content_type: HistoryContentType = Field(description="The type of this item.")
    id: str


class LegacyLibraryPermissionsPayload(BaseModel):
    LIBRARY_ACCESS_in: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have access permission on the library."
    )
    LIBRARY_ADD_in: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have manage permission on the library."
    )
    LIBRARY_MANAGE_in: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have modify permission on the library."
    )
    LIBRARY_MODIFY_in: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should be able to add items to the library."
    )


class AccessURL(BaseModel):
    headers: list[str] | None = Field(
        None,
        description="An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes.",
    )
    url: str = Field(description="A fully resolvable URL that can be used to fetch the actual object bytes.")


class HistoryDetailed(BaseModel):
    """History detailed information."""

    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    archived: bool = Field(description="Whether this item has been archived and is no longer active.")
    contents_url: str = Field(description="The relative URL to access the contents of this History.")
    count: int = Field(description="The number of items in the history.")
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    genome_build: str | None = Field(None, description="TODO")
    id: str
    importable: bool = Field(description="Whether this History can be imported by other users with a shared link.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the history.")
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    published: bool = Field(description="Whether this resource is currently publicly available to all users.")
    purged: bool = Field(description="Whether this item has been permanently removed.")
    size: int = Field(description="The total size of the contents of this history in bytes.")
    slug: str | None = Field(
        None, description="Part of the URL to uniquely identify this History by link in a readable way."
    )
    state: DatasetState = Field(
        description="The current state of the History based on the states of the datasets it contains."
    )
    state_details: dict[str, Any] = Field(
        description="A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states."
    )
    state_ids: dict[str, Any] = Field(
        description="A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state."
    )
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    update_time: str = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    user_id: str | None = Field(None, description="The encoded ID of the user that owns this History.")
    username: str | None = Field(None, description="Owner of the history")
    username_and_slug: str | None = Field(None, description="The relative URL in the form of /u/{username}/h/{slug}")


class UserUpdatePayload(BaseModel):
    active: bool | None = Field(None, description="User is active")
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    username: str | None = Field(None, description="The name of the user.")


class ImportToolDataBundleDatasetSource(BaseModel):
    id: str
    src: Literal["hda", "ldda"] = Field(description="Indicates that the tool data should be resolved from a dataset.")


class SampleSheetColumnDefinition(BaseModel):
    default_value: int | float | bool | str | None = None
    description: str | None = None
    name: str
    optional: bool
    restrictions: list[int | float | bool | str | None] | None = None
    suggestions: list[int | float | bool | str | None] | None = None
    type: Literal["string", "int", "float", "boolean", "element_identifier"]
    validators: list[dict[str, Any]] | None = None


class GenomeBuildParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    multiple: bool
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str


class HDASummary(BaseModel):
    """History Dataset Association summary information."""

    copied_from_ldda_id: str | None = None
    create_time: str = Field(description="The time and date this item was created.")
    dataset_id: str = Field(description="The encoded ID of the dataset associated with this item.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    extension: str | None = Field(description="The extension of the dataset.")
    genome_build: str | None = Field(None, description="TODO")
    hid: int = Field(description="The index position of this item in the History.")
    history_content_type: str = Field(description="This is always `dataset` for datasets.")
    history_id: str
    id: str
    name: str | None = Field(description="The name of the item.")
    object_store_id: str | None = Field(None, description="The ID of the object store that this dataset is stored in.")
    purged: bool = Field(description="Whether this dataset has been removed from disk.")
    state: DatasetState = Field(description="The current state of this dataset.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    type: str = Field(description="The type of this item.")
    type_id: str | None = Field(None, description="The type and the encoded ID of this item. Used for caching.")
    update_time: str | None = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    visible: bool = Field(description="Whether this item is visible or hidden to the user by default.")


class UpdateHistoryContentsPayload(BaseModel):
    """Can contain arbitrary/dynamic fields that will be updated for a particular history item."""

    annotation: str | None = Field(None, description="A user-defined annotation for this item.")
    deleted: bool | None = Field(None, description="Whether this item is marked as deleted.")
    name: str | None = Field(None, description="The new name of the item.")
    tags: list[str] | None = Field(None, description="A list of tags to add to this item.")
    visible: bool | None = Field(None, description="Whether this item is visible in the history.")


class BaseUrlParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str


class JobLock(BaseModel):
    active: bool = Field(description="If active, jobs will not dispatch")


class DetailedUserModel(BaseModel):
    deleted: bool = Field(description=" User is deleted")
    email: str = Field(description="Email of the user")
    id: str = Field(description="Encoded ID of the user")
    is_admin: bool = Field(description="User is admin")
    nice_total_disk_usage: str = Field(
        description="Size of all non-purged, unique datasets of the user in a nice format."
    )
    preferences: dict[str, Any] = Field(description="Preferences of the user")
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    purged: bool = Field(description="User is purged")
    quota: str = Field(description="Quota applicable to the user")
    quota_bytes: int | None = Field(None, description="Quota applicable to the user in bytes.")
    quota_percent: float | None = Field(None, description="Percentage of the storage quota applicable to the user.")
    total_disk_usage: float = Field(description="Size of all non-purged, unique datasets of the user in bytes.")
    username: str = Field(description="The name of the user.")


class FolderLibraryFolderItem(BaseModel):
    can_manage: bool
    can_modify: bool
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool
    description: str | None = Field(None, description="A detailed description of the library folder.")
    id: str
    name: str
    type: str
    update_time: str = Field(description="The last time and date this item was updated.")


class DeleteHistoryPayload(BaseModel):
    purge: bool | None = Field(None, description="Whether to definitely remove this history from disk.")


class StepReferenceByOrderIndex(BaseModel):
    order_index: int = Field(
        description="The order_index of the step being referenced. The order indices of a workflow start at 0."
    )


class UndeleteHistoriesPayload(BaseModel):
    ids: list[str] = Field(description="List of history IDs to be undeleted.")


class UserDeletionPayload(BaseModel):
    purge: bool | None = Field(
        None, description="Purge the user. Deprecated, please use the `purge` query parameter instead."
    )


class JobRequest(BaseModel):
    history_id: str | None = Field(None, description="TODO")
    inputs: dict[str, Any] | None = Field(None, description="TODO")
    rerun_remap_job_id: str | None = Field(None, description="TODO")
    send_email_notification: bool | None = Field(None, description="TODO")
    strict: bool | None = Field(
        None,
        description="Turn on strict validation of the inputs that drops support for some inconsistent legacy behavior.",
    )
    tool_id: str | None = Field(None, description="TODO")
    tool_uuid: str | None = Field(None, description="TODO")
    tool_version: str | None = Field(None, description="TODO")
    use_cached_jobs: bool | None = None


class SelectCurrentGroupPayload(BaseModel):
    current_group_id: str | None = Field(None, description="The ID of the group to set as current (None to unset).")
    user_credentials_id: str = Field(description="The ID of the user credentials to update.")


class SecretResponse(BaseModel):
    is_set: bool = Field(description="Whether the secret has been set (value is not exposed).")
    name: str = Field(description="The name of the credential.")


class TestUpgradeInstancePayload(BaseModel):
    secrets: dict[str, Any]
    template_version: int
    variables: dict[str, Any]


class InvocationFailureJobFailedResponse(BaseModel):
    dependent_workflow_step_id: int = Field(description="Workflow step id of step that caused failure.")
    job_id: str = Field(description="Job ID that relates to failure.")
    reason: str
    workflow_step_id: int = Field(description="Workflow step id of step that failed.")


class EncodedJobParameterHistoryItem(BaseModel):
    hid: int | None = None
    id: str
    name: str
    src: DataItemSourceType = Field(
        description="The source of this dataset, either `hda`, `ldda`, `hdca`, `dce` or `dc` depending of its origin."
    )


class BodyLibraries_contents_createForm(BaseModel):
    create_type: Any
    dbkey: Any | None = None
    extended_metadata: Any | None = None
    file_type: Any | None = None
    files: list[str] | None = None
    filesystem_paths: Any | None = None
    folder_id: Any
    from_hda_id: Any | None = None
    from_hdca_id: Any | None = None
    ldda_message: Any | None = None
    link_data_only: Any | None = None
    roles: Any | None = None
    server_dir: Any | None = None
    tag_using_filenames: Any | None = None
    tags: Any | None = None
    upload_files: Any | None = None
    upload_option: Any | None = None
    uuid: Any | None = None


class CwlBooleanParameterModel(BaseModel):
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    parameter_type: str | None = None


class CreateLinkIncoming(BaseModel):
    app_name: str
    dataset_id: str
    kwd: dict[str, Any] | None = None
    link_name: str


class CreateQuotaResult(BaseModel):
    id: str = Field(description="The `encoded identifier` of the quota.")
    message: str = Field(description="Text message describing the result of the operation.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the quota. This must be unique within a Galaxy instance.")
    quota_source_label: str | None = Field(None, description="Quota source label")
    url: str = Field(description="The relative URL to get this particular Quota details from the rest API.")


class Position(BaseModel):
    left: float
    top: float


class ChatPayload(BaseModel):
    context: str | None = Field(None, description="The context for the chatbot.")
    exchange_id: int | None = Field(None, description="The ID of an existing chat exchange to continue.")
    query: str = Field(description="The query to be sent to the chatbot.")


class InvocationFailureExpressionEvaluationFailedResponse(BaseModel):
    details: str | None = Field(None, description="May contain details to help troubleshoot this problem.")
    reason: str
    workflow_step_id: int = Field(description="Workflow step id of step that failed.")


class GroupModel(BaseModel):
    """User group model"""

    id: str = Field(description="Encoded group ID")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the group.")


class WorkflowInvocationRequestModel(BaseModel):
    """Model a workflow invocation request (InvokeWorkflowPayload) for an existing invocation."""

    history_id: str = Field(description="The encoded history id the workflow was run in.")
    inputs: dict[str, Any] = Field(description="Values for inputs")
    inputs_by: str = Field(
        description="How the 'inputs' field maps its inputs (datasets/collections/step parameters) to workflows steps."
    )
    instance: bool | None = Field(
        None,
        description="This API yields a particular workflow instance, newer workflows belonging to the same storedworkflow may have different state.",
    )
    parameters: dict[str, Any] | None = Field(
        None,
        description="Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead. If these are set, the workflow was not executed in a best-practice fashion and we the resulting invocation request may not fully reflect the executed workflow state.",
    )
    parameters_normalized: bool | None = Field(
        None,
        description="Indicates if legacy parameters are already normalized to be indexed by the order_index and are specified as a dictionary per step. Legacy-style parameters could previously be specified as one parameter per step or by tool ID.",
    )
    preferred_intermediate_object_store_id: str | None = Field(
        None,
        description="The ID of the object store that should be used to store the intermediate datasets of this workflow -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences",
    )
    preferred_object_store_id: str | None = Field(
        None,
        description="The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences",
    )
    preferred_outputs_object_store_id: str | None = Field(
        None,
        description="The ID of the object store that should be used to store the marked output datasets of this workflow - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences.",
    )
    replacement_params: dict[str, Any] | None = Field(
        None,
        description="Class of parameters mostly used for string replacement in PJAs. In best practice workflows, these should be replaced with input parameters",
    )
    resource_params: dict[str, Any] | None = Field(
        None,
        description="If a workflow_resource_params_file file is defined and the target workflow is configured to consumer resource parameters, they can be specified with this parameter. See https://github.com/galaxyproject/galaxy/pull/4830 for more information.",
    )
    use_cached_job: bool | None = Field(
        None, description="Indicated whether to use a cached job for workflow invocation."
    )
    workflow_id: str = Field(description="The encoded Workflow ID associated with the invocation.")


class ItemTagsPayload(BaseModel):
    item_class: TaggableItemClass = Field(description="The name of the class of the item that will be tagged.")
    item_id: str = Field(description="The `encoded identifier` of the item whose tags will be updated.")
    item_tags: list[str] | None = Field(
        None, description="The list of tags that will replace the current tags associated with the item."
    )


class UpdateAnnotationAction(BaseModel):
    action_type: str
    annotation: str


class CreateLinkStep(BaseModel):
    name: str
    ready: bool | None = None
    state: str | None = None


class Checksum(BaseModel):
    checksum: str = Field(description="The hex-string encoded checksum for the data")
    type: str = Field(
        description="The digest method used to create the checksum.\nThe value (e.g. `sha-256`) SHOULD be listed as `Hash Name String` in the https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg[IANA Named Information Hash Algorithm Registry]. Other values MAY be used, as long as implementors are aware of the issues discussed in https://tools.ietf.org/html/rfc6920#section-9.4[RFC6920].\nGA4GH may provide more explicit guidance for use of non-IANA-registered algorithms in the future. Until then, if implementers do choose such an algorithm (e.g. because it's implemented by their storage provider), they SHOULD use an existing standard `type` value such as `md5`, `etag`, `crc32c`, `trunc512`, or `sha1`."
    )


class GroupTagParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    multiple: bool
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str


class ChangeDbkeyOperationParams(BaseModel):
    dbkey: str
    type: str


class CheckForUpdatesResponse(BaseModel):
    message: str = Field(description="Unstructured description of tool shed updates discovered or failure")
    status: Literal["ok", "error"] = Field(description="'ok' or 'error'")


class MessageNotificationContent(BaseModel):
    category: str | None = None
    message: str = Field(description="The message of the notification (supports Markdown).")
    subject: str = Field(description="The subject of the notification.")


class NoOptionsParameterValidatorModel(BaseModel):
    implicit: bool | None = None
    message: str | None = None
    negate: bool | None = None
    type: str | None = None


class OutputReferenceByLabel(BaseModel):
    label: str = Field(description="The unique label of the step being referenced.")
    output_name: str | None = Field(
        None,
        description="The output name as defined by the workflow module corresponding to the step being referenced. The default is 'output', corresponding to the output defined by input step types.",
    )


class CustomBuildCreationPayload(BaseModel):
    len_type: CustomBuildLenType = Field(description="The type of the len file.")
    len_value: str = Field(description="The content of the length file.")
    name: str = Field(description="The name of the custom build.")


class StepReferenceByLabel(BaseModel):
    label: str = Field(description="The unique label of the step being referenced.")


class LengthParameterValidatorModel(BaseModel):
    implicit: bool | None = None
    max: int | None = None
    message: str | None = None
    min: int | None = None
    negate: bool | None = None
    type: str | None = None


class PageSummary(BaseModel):
    author_deleted: bool = Field(description="Whether the author of this Page has been deleted.")
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this Page has been deleted.")
    email_hash: str = Field(description="The encoded email of the user.")
    id: str = Field(description="Encoded ID of the Page.")
    importable: bool = Field(description="Whether this Page can be imported.")
    latest_revision_id: str = Field(description="The encoded ID of the last revision of this Page.")
    model_class: str = Field(description="The name of the database model class.")
    published: bool = Field(description="Whether this Page has been published.")
    revision_ids: list[str] = Field(description="The history with the encoded ID of each revision of the Page.")
    slug: str = Field(description="The identifying slug for the page URL, must be unique.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    title: str = Field(description="The name of the page.")
    update_time: str = Field(description="The last time and date this item was updated.")
    username: str = Field(description="The name of the user owning this Page.")


class UpdateLibraryFolderPayload(BaseModel):
    description: str | None = Field(None, description="The new description of the library folder.")
    name: str | None = Field(None, description="The new name of the library folder.")


class NotificationRecipientsRequest(BaseModel):
    group_ids: list[str] | None = Field(
        None, description="The list of encoded group IDs of the groups that should receive the notification."
    )
    role_ids: list[str] | None = Field(
        None, description="The list of encoded role IDs of the roles that should receive the notification."
    )
    user_ids: list[str] | None = Field(
        None, description="The list of encoded user IDs of the users that should receive the notification."
    )


class DataParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    extensions: list[str] | None = Field(
        None, description="Limit inputs to datasets with these extensions. Use 'data' to allow all input datasets."
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    max: int | None = None
    min: int | None = None
    multiple: bool | None = Field(None, description="Allow multiple values to be selected.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str


class CreateLibraryPayload(BaseModel):
    description: str | None = Field(None, description="A detailed description of the Library.")
    name: str = Field(description="The name of the Library.")
    synopsis: str | None = Field(None, description="A short text describing the contents of the Library.")


class ShareWithPayload(BaseModel):
    share_option: SharingOptions | None = Field(
        None,
        description="User choice for sharing resources which its contents may be restricted:\n - None: The user did not choose anything yet or no option is needed.\n - make_public: The contents of the resource will be made publicly accessible.\n - make_accessible_to_shared: This will automatically create a new `sharing role` allowing protected contents to be accessed only by the desired users.\n - no_changes: This won't change the current permissions for the contents. The user which this resource will be shared may not be able to access all its contents.\n",
    )
    user_ids: list[str] = Field(
        description="A collection of encoded IDs (or email addresses) of users that this resource will be shared with."
    )


class RegexParameterValidatorModel(BaseModel):
    """Check if a regular expression **matches** the value, i.e. appears
    at the beginning of the value. To enforce a match of the complete value use
    ``$`` at the end of the expression. The expression is given is the content
    of the validator tag. Note that for ``selects`` each option is checked
    separately."""

    expression: str
    implicit: bool | None = None
    message: str | None = None
    negate: bool | None = None
    type: str | None = None


class LibraryContentsCollectionCreatePayload(BaseModel):
    collection_type: str
    copy_elements: bool | None = Field(None, description="if True, copy the elements into the collection")
    create_type: CreateType = Field(description="the type of item to create")
    element_identifiers: list[dict[str, Any]]
    extended_metadata: dict[str, Any] | None = Field(
        None, description="sub-dictionary containing any extended metadata to associate with the item"
    )
    folder_id: str = Field(description="the encoded id of the parent folder of the new item")
    from_hda_id: str | None = Field(
        None, description="(only if create_type is 'file') the encoded id of an accessible HDA to copy into the library"
    )
    from_hdca_id: str | None = Field(
        None,
        description="(only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library",
    )
    hide_source_items: bool | None = Field(None, description="if True, hide the source items in the collection")
    ldda_message: str | None = Field(None, description="the new message attribute of the LDDA created")
    name: str | None = None
    tag_using_filenames: bool | None = Field(None, description="create tags on datasets using the file's original name")
    tags: list[str] | None = Field(None, description="create the given list of tags on datasets")
    upload_option: UploadOption | None = Field(None, description="the method to use for uploading files")


class UpdateContentItem(BaseModel):
    """Used for updating a particular history item. All fields are optional."""

    history_content_type: HistoryContentType = Field(description="The type of this item.")
    id: str


class CreateWorkflowLandingRequestPayload(BaseModel):
    client_secret: str | None = None
    origin: str | None = Field(None, description="The origin of the landing request.")
    public: bool | None = Field(
        None,
        description="If workflow landing request is public anyone with the uuid can use the landing request. If not public the request must be claimed before use and additional verification might occur.",
    )
    request_state: dict[str, Any] | None = None
    workflow_id: str
    workflow_target_type: Literal["stored_workflow", "workflow", "trs_url"]


class Hyperlink(BaseModel):
    """Represents some text with an Hyperlink."""

    href: str = Field(description="The URL of the linked document.")
    target: str = Field(description="Specifies where to open the linked document.")
    text: str = Field(description="The text placeholder for the link.")


class ParsedWorkbookCollection(BaseModel):
    id: str
    model_class: str | None = None


class CreatePagePayload(BaseModel):
    annotation: str | None = Field(None, description="Annotation that will be attached to the page.")
    content: str | None = Field(
        None,
        description="Text contents of the last page revision with embedded directives expanded (type dependent on content_format).",
    )
    content_format: PageContentFormat | None = Field(None, description="Either `markdown` or `html`.")
    invocation_id: str | None = Field(None, description="Encoded ID used by workflow generated reports.")
    slug: str = Field(description="The identifying slug for the page URL, must be unique.")
    title: str = Field(description="The name of the page.")


class WriteStoreToPayload(BaseModel):
    include_deleted: bool | None = Field(
        None, description="Include file contents for deleted datasets (if include_files is True)."
    )
    include_files: bool | None = Field(None, description="include materialized files in export when available")
    include_hidden: bool | None = Field(
        None, description="Include file contents for hidden datasets (if include_files is True)."
    )
    model_store_format: ModelStoreFormat | None = Field(None, description="format of model store to export")
    target_uri: str = Field(description="Galaxy Files URI to write mode store content to.")


class TemplateSecret(BaseModel):
    help: str | None
    label: str | None = None
    name: str


class LibraryLegacySummary(BaseModel):
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this Library has been deleted.")
    description: str | None = Field(None, description="A detailed description of the Library.")
    id: str = Field(description="Encoded ID of the Library.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the Library.")
    root_folder_id: str = Field(description="Encoded ID of the Library's base folder.")
    synopsis: str | None = Field(None, description="A short text describing the contents of the Library.")


class EmptyFieldParameterValidatorModel(BaseModel):
    implicit: bool | None = None
    message: str | None = None
    negate: bool | None = None
    type: str | None = None


class InvocationFailureWhenNotBooleanResponse(BaseModel):
    details: str = Field(description="Contains details to help troubleshoot this problem.")
    reason: str
    workflow_step_id: int = Field(description="Workflow step id of step that failed.")


class ToolDataItem(BaseModel):
    values: str = Field(
        description="A `\\t` (TAB) separated list of column __contents__. You must specify a value for each of the columns of the data table."
    )


class ExitCodeJobMessage(BaseModel):
    code_desc: str | None = None
    desc: str | None
    error_level: float
    exit_code: int
    type: str


class Container(BaseModel):
    container_id: str
    type: Literal["docker", "singularity"]


class LibraryContentsCreateFileResponse(BaseModel):
    id: str
    name: str
    url: str


class BodyTools_fetch_fetchForm(BaseModel):
    files: list[str] | None = None
    history_id: Any
    landing_uuid: Any | None = None
    targets: Any


class ToolOutputFloat(BaseModel):
    hidden: Any = Field(description="If true, the output will not be shown in the history.")
    label: str | None = Field(None, description="Output label. Will be used as dataset name in history.")
    name: Any = Field(description="Parameter name. Used when referencing parameter in workflows.")
    type: str


class FillIdentifiers(BaseModel):
    deduplication_index_from: int | None = None
    deduplication_pattern: str | None = None
    fill_inner_list_identifiers: bool | None = None


class InputReferenceByOrderIndex(BaseModel):
    input_name: str = Field(
        description="The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input')."
    )
    order_index: int = Field(
        description="The order_index of the step being referenced. The order indices of a workflow start at 0."
    )


class DeleteJobPayload(BaseModel):
    message: str | None = Field(None, description="Stop message")


class TestUpdateInstancePayload(BaseModel):
    variables: dict[str, Any] | None = None


class JobImportHistoryResponse(BaseModel):
    create_time: str = Field(description="The time and date this item was created.")
    exit_code: int | None = Field(
        None, description="The exit code returned by the tool. Can be unset if the job is not completed yet."
    )
    galaxy_version: str | None = Field(None, description="The (major) version of Galaxy used to create this job.")
    history_id: str | None = Field(None, description="The encoded ID of the history associated with this item.")
    id: str
    message: str = Field(description="Text message containing information about the history import.")
    model_class: str = Field(description="The name of the database model class.")
    state: JobState = Field(description="Current state of the job.")
    tool_id: str = Field(description="Identifier of the tool that generated this job.")
    update_time: str = Field(description="The last time and date this item was updated.")


class DatatypeConverter(BaseModel):
    source: str = Field(description="Source type for conversion")
    target: str = Field(description="Target type for conversion")
    tool_id: str = Field(description="The converter tool identifier")


class DataCollectionParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    collection_type: str | None = None
    extensions: list[str] | None = None
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str
    value: dict[str, Any] | None


class HelpForumTopic(BaseModel):
    """Model for a topic in the help forum compatible with Discourse API."""

    archetype: Any = Field(description="The archetype of the topic.")
    archived: bool = Field(description="Whether the topic is archived.")
    bookmarked: bool | None = Field(None, description="Whether the topic is bookmarked.")
    bumped: bool = Field(description="Whether the topic was bumped.")
    bumped_at: str = Field(description="The date of the last bump of the topic.")
    category_id: int = Field(description="The ID of the category of the topic.")
    closed: bool = Field(description="Whether the topic is closed.")
    created_at: str = Field(description="The creation date of the topic.")
    fancy_title: str = Field(description="The fancy title of the topic.")
    has_accepted_answer: bool = Field(description="Whether the topic has an accepted answer.")
    highest_post_number: int = Field(description="The highest post number in the topic.")
    id: int = Field(description="The ID of the topic.")
    last_posted_at: str = Field(description="The date of the last post in the topic.")
    liked: bool | None = Field(None, description="Whether the topic is liked.")
    pinned: bool = Field(description="Whether the topic is pinned.")
    posts_count: int = Field(description="The number of posts in the topic.")
    reply_count: int = Field(description="The number of replies in the topic.")
    slug: str = Field(description="The slug of the topic.")
    tags: list[str] = Field(description="The tags of the topic.")
    tags_descriptions: Any | None = Field(None, description="The descriptions of the tags of the topic.")
    title: str = Field(description="The title of the topic.")
    unpinned: bool | None = Field(None, description="Whether the topic is unpinned.")
    unseen: bool = Field(description="Whether the topic is unseen.")
    visible: bool = Field(description="Whether the topic is visible.")


class InvocationCancellationReviewFailedResponse(BaseModel):
    reason: str
    workflow_step_id: int = Field(description="Workflow step id of paused step that did not pass review.")


class JobStateSummary(BaseModel):
    id: str
    model: str = Field(description="The name of the database model class.")
    populated_state: DatasetCollectionPopulatedState = Field(
        description="Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated."
    )
    states: dict[str, Any] | None = Field(
        None, description="A dictionary of job states and the number of jobs in that state."
    )


class TourStep(BaseModel):
    content: str | None = Field(None, description="Text shown to the user")
    element: str | None = Field(None, description="CSS selector for the element to be described/clicked")
    orphan: bool | None = Field(None, description="If true, the step is an orphan step")
    placement: str | None = Field(None, description="Placement of the text box relative to the selected element")
    postclick: bool | list[str] | None = Field(
        None, description="Elements that receive a click() event after the step is shown"
    )
    preclick: bool | list[str] | None = Field(
        None, description="Elements that receive a click() event before the step is shown"
    )
    textinsert: str | None = Field(
        None, description="Text to insert if element is a text box (e.g. tool search or upload)"
    )
    title: str | None = Field(None, description="Title displayed in the header of the step container")


class ToolDataField(BaseModel):
    base_dir: list[str] = Field(description="A list of directories where the data files are stored")
    fields: dict[str, Any] = Field(description="")
    files: dict[str, Any] = Field(description="A dictionary of file names and their size in bytes")
    fingerprint: str = Field(description="SHA1 Hash")
    model_class: str = Field(description="The name of class modelling this tool data field")
    name: str = Field(description="The name of the field")


class RemoteDirectory(BaseModel):
    class_: str
    name: str = Field(description="The name of the entry.")
    path: str = Field(description="The path of the entry.")
    uri: str = Field(description="The URI of the entry.")


class LabelValuePair(BaseModel):
    """Generic Label/Value pair model."""

    label: str = Field(description="The label of the item.")
    value: str = Field(description="The value of the item.")


class RulesParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str


class AnonUserModel(BaseModel):
    nice_total_disk_usage: str = Field(
        description="Size of all non-purged, unique datasets of the user in a nice format."
    )
    quota_percent: float | None = Field(None, description="Percentage of the storage quota applicable to the user.")
    total_disk_usage: float = Field(description="Size of all non-purged, unique datasets of the user in bytes.")


class DrillDownOptionsDictInput(BaseModel):
    name: str | None
    options: list[DrillDownOptionsDictInput]
    selected: bool
    value: str


class EncodedDatasetSourceId(BaseModel):
    id: str
    src: DatasetSourceType = Field(
        description="The source of this dataset, either `hda` or `ldda` depending of its origin."
    )


class ToolRequestImplicitCollectionReference(BaseModel):
    id: str
    output_name: str
    src: str


class CreateQuotaParams(BaseModel):
    amount: str = Field(description="Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)")
    default: DefaultQuotaValues | None = Field(
        None,
        description="Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. None is equivalent to ``no``.",
    )
    description: str = Field(description="Detailed text description for this Quota.")
    in_groups: list[str] | None = Field(None, description="A list of group IDs or names to associate with this quota.")
    in_users: list[str] | None = Field(
        None, description="A list of user IDs or user emails to associate with this quota."
    )
    name: str = Field(description="The name of the quota. This must be unique within a Galaxy instance.")
    operation: QuotaOperation | None = Field(
        None,
        description="Quotas can have one of three `operations`:- `=` : The quota is exactly the amount specified- `+` : The amount specified will be added to the amounts of the user's other associated quota definitions- `-` : The amount specified will be subtracted from the amounts of the user's other associated quota definitions",
    )
    quota_source_label: str | None = Field(
        None,
        description="If set, quota source label to apply this quota operation to. Otherwise, the default quota is used.",
    )


class ParsedColumn(BaseModel):
    title: str
    type: Literal[
        "list_identifiers",
        "paired_identifier",
        "paired_or_unpaired_identifier",
        "collection_name",
        "name_tag",
        "tags",
        "group_tags",
        "name",
        "dbkey",
        "hash_sha1",
        "hash_md5",
        "hash_sha256",
        "hash_sha512",
        "file_type",
        "url",
        "url_deferred",
        "info",
        "ftp_path",
        "deferred",
        "to_posix_lines",
        "space_to_tab",
        "auto_decompress",
    ]
    type_index: int


class ToolOutputText(BaseModel):
    hidden: Any = Field(description="If true, the output will not be shown in the history.")
    label: str | None = Field(None, description="Output label. Will be used as dataset name in history.")
    name: Any = Field(description="Parameter name. Used when referencing parameter in workflows.")
    type: str


class Citation(BaseModel):
    content: str
    type: str


class DatatypeEDAMDetails(BaseModel):
    definition: str | None = Field(description="The EDAM definition")
    label: str | None = Field(description="The EDAM label")
    prefix_IRI: str = Field(description="The EDAM prefixed Resource Identifier")


class ToolReportForDataset(BaseModel):
    content: str | None = Field(
        None,
        description="Text contents of the last page revision with embedded directives expanded (type dependent on content_format).",
    )
    generate_time: str | None = Field(None, description="The version of Galaxy this object was generated with.")
    generate_version: str | None = Field(None, description="The version of Galaxy this object was generated with.")


class CreateEntryPayload(BaseModel):
    name: str = Field(description="The name of the entry to create.")
    target: str = Field(description="The target file source to create the entry in.")


class CreateLibraryFolderPayload(BaseModel):
    description: str | None = Field(None, description="A detailed description of the library folder.")
    name: str = Field(description="The name of the library folder.")


class SuitableConverter(BaseModel):
    name: str = Field(description="The name of the converter.")
    original_type: str = Field(description="The type to convert from.")
    target_type: str = Field(description="The type to convert to.")
    tool_id: str = Field(description="The ID of the tool that can perform the type conversion.")


class LibraryPermissionsPayload(BaseModel):
    access_ids__: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have access permission on the library."
    )
    action: LibraryPermissionAction | None = Field(
        None, description="Indicates what action should be performed on the Library."
    )
    add_ids__: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should be able to add items to the library."
    )
    manage_ids__: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have manage permission on the library."
    )
    modify_ids__: list[str] | str | None = Field(
        None, description="A list of role encoded IDs defining roles that should have modify permission on the library."
    )


class ServiceParameterDefinition(BaseModel):
    description: str = Field(description="A description of what this credential is used for.")
    label: str = Field(description="The human-readable label for the credential.")
    name: str = Field(description="The name of the credential definition.")
    optional: bool = Field(description="Whether this credential is optional or required.")


class DefaultQuota(BaseModel):
    model_class: str = Field(description="The name of the database model class.")
    type: DefaultQuotaTypes = Field(
        description="The type of the default quota. Either one of:\n - `registered`: the associated quota will affect registered users.\n - `unregistered`: the associated quota will affect unregistered users.\n"
    )


class ReloadFeedback(BaseModel):
    failed: list[str | None]
    message: str
    reloaded: list[str | None]


class LibraryFolderCurrentPermissions(BaseModel):
    add_library_item_role_list: list[list[str]] = Field(
        description="A list containing pairs of role names and corresponding encoded IDs which can add items to the Library folder."
    )
    manage_folder_role_list: list[list[str]] = Field(
        description="A list containing pairs of role names and corresponding encoded IDs which can manage the Library folder."
    )
    modify_folder_role_list: list[list[str]] = Field(
        description="A list containing pairs of role names and corresponding encoded IDs which can modify the Library folder."
    )


class UserModel(BaseModel):
    """User in a transaction context."""

    active: bool = Field(description="User is active")
    deleted: bool = Field(description=" User is deleted")
    email: str = Field(description="Email of the user")
    id: str = Field(description="Encoded ID of the user")
    last_password_change: str | None = Field(description="")
    model_class: str = Field(description="The name of the database model class.")
    username: str = Field(description="The name of the user.")


class Link(BaseModel):
    name: str


class ToolRequestJobReference(BaseModel):
    id: str
    src: str


class OldestCreateTimeByObjectStoreId(BaseModel):
    """Represents the oldest creation time of a set of datasets stored in a specific object store."""

    object_store_id: str = Field(description="The ID of the object store.")
    oldest_create_time: str = Field(
        description="The oldest creation time of a set of datasets stored in this object store."
    )


class VisualizationPluginResponse(BaseModel):
    description: str = Field(description="The description of the plugin.")
    embeddable: bool = Field(description="Whether the plugin is embeddable.")
    entry_point: dict[str, Any] = Field(description="The entry point of the plugin.")
    href: str = Field(description="The href of the plugin.")
    html: str = Field(description="The HTML of the plugin.")
    logo: str | None = Field(None, description="The logo of the plugin.")
    name: str = Field(description="The name of the plugin.")
    settings: list[dict[str, Any]] | None = Field(None, description="The settings of the plugin.")
    specs: dict[str, Any] | None = Field(None, description="The specs of the plugin.")
    title: str | None = Field(None, description="The title of the plugin.")
    tracks: list[dict[str, Any]] | None = Field(None, description="The tracks of the plugin.")


class InvocationStepJobsResponseCollectionJobsModel(BaseModel):
    id: str = Field(description="The encoded ID of the collection job.")
    model: str
    populated_state: JobState = Field(description="The absolute state of all the jobs related to the Invocation.")
    states: dict[str, Any] = Field(description="The states of all the jobs related to the Invocation.")


class InvocationJobsResponse(BaseModel):
    id: str = Field(description="The encoded ID of the workflow invocation.")
    model: str
    populated_state: JobState = Field(description="The absolute state of all the jobs related to the Invocation.")
    states: dict[str, Any] = Field(description="The states of all the jobs related to the Invocation.")


class ReportJobErrorPayload(BaseModel):
    dataset_id: str = Field(description="The History Dataset Association ID related to the error.")
    email: str | None = Field(
        None, description="Email address for communication with the user. Only required for anonymous users."
    )
    message: str | None = Field(None, description="The optional message sent with the error report.")


class RoleDefinitionModel(BaseModel):
    description: str = Field(description="Description of the role")
    group_ids: list[str] | None = None
    name: str = Field(description="Name of the role")
    role_type: Literal["admin", "user_tool_create", "user_tool_execute"] | None = None
    user_ids: list[str] | None = None


class OutputReferenceByOrderIndex(BaseModel):
    order_index: int = Field(
        description="The order_index of the step being referenced. The order indices of a workflow start at 0."
    )
    output_name: str | None = Field(
        None,
        description="The output name as defined by the workflow module corresponding to the step being referenced. The default is 'output', corresponding to the output defined by input step types.",
    )


class InputReferenceByLabel(BaseModel):
    input_name: str = Field(
        description="The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input')."
    )
    label: str = Field(description="The unique label of the step being referenced.")


class HistoryActiveContentCounts(BaseModel):
    """Contains the number of active, deleted or hidden items in a History."""

    active: int = Field(description="Number of active datasets.")
    deleted: int = Field(description="Number of deleted datasets.")
    hidden: int = Field(description="Number of hidden datasets.")


class MaxDiscoveredFilesJobMessage(BaseModel):
    code_desc: str | None = None
    desc: str | None
    error_level: float
    type: str


class UpdateCreatorAction(BaseModel):
    action_type: str
    creator: Any | None = None


class ActionLink(BaseModel):
    """An action link to be displayed in the notification as a button."""

    action_name: str = Field(description="The name of the action, will be the button title.")
    link: str = Field(description="The link to be opened when the button is clicked.")


class GroupUpdatePayload(BaseModel):
    """Payload schema for updating a group."""

    name: str | None = None
    role_ids: list[str] | None = None
    user_ids: list[str] | None = None


class NotificationsBatchRequest(BaseModel):
    notification_ids: list[str] = Field(
        description="The list of encoded notification IDs of the notifications that should be updated."
    )


class Visualization(BaseModel):
    pass


class InvocationCancellationUserRequestResponse(BaseModel):
    reason: str


class CreateInstancePayload(BaseModel):
    description: str | None = None
    name: str
    secrets: dict[str, Any]
    template_id: str
    template_version: int
    uuid: str | None = None
    variables: dict[str, Any]


class InvocationFailureWorkflowParameterInvalidResponse(BaseModel):
    details: str = Field(description="Message raised by validator")
    reason: str
    workflow_step_id: int


class UpdateLibraryPayload(BaseModel):
    description: str | None = Field(
        None, description="A detailed description of the Library. Leave unset to keep the existing."
    )
    name: str | None = Field(None, description="The new name of the Library. Leave unset to keep the existing.")
    synopsis: str | None = Field(
        None, description="A short text describing the contents of the Library. Leave unset to keep the existing."
    )


class InvocationReport(BaseModel):
    """Report describing workflow invocation"""

    errors: list[dict[str, Any]] | None = Field(None, description="Errors associated with the invocation.")
    generate_time: str | None = Field(None, description="The version of Galaxy this object was generated with.")
    generate_version: str | None = Field(None, description="The version of Galaxy this object was generated with.")
    histories: dict[str, Any] | None = Field(None, description="Histories associated with the invocation.")
    history_dataset_collections: dict[str, Any] | None = Field(
        None, description="History dataset collections associated with the invocation."
    )
    history_datasets: dict[str, Any] | None = Field(
        None, description="History datasets associated with the invocation."
    )
    id: str = Field(description="The workflow this invocation has been triggered for.")
    invocation_markdown: str | None = Field(None, description="Raw galaxy-flavored markdown contents of the report.")
    invocations: dict[str, Any] | None = Field(None, description="Other invocations associated with the invocation.")
    jobs: dict[str, Any] | None = Field(None, description="Jobs associated with the invocation.")
    markdown: str | None = Field(None, description="Raw galaxy-flavored markdown contents of the report.")
    model_class: str = Field(description="The name of the database model class.")
    render_format: str | None = Field(None, description="Format of the invocation report.")
    title: str = Field(description="The name of the report.")
    username: str = Field(description="The name of the user who owns this report.")
    workflows: dict[str, Any] | None = Field(None, description="Workflows associated with the invocation.")


class GroupCreatePayload(BaseModel):
    """Payload schema for creating a group."""

    name: str
    role_ids: list[str] | None = None
    user_ids: list[str] | None = None


class DeleteHistoriesPayload(BaseModel):
    ids: list[str] = Field(description="List of history IDs to be deleted.")
    purge: bool | None = Field(None, description="Whether to definitely remove this history from disk.")


class LibraryContentsShowFolderResponse(BaseModel):
    deleted: bool
    description: str
    genome_build: str | None
    id: str
    item_count: int
    library_path: list[str]
    model_class: str = Field(description="The name of the database model class.")
    name: str
    parent_id: str | None
    parent_library_id: str
    update_time: str


class ToolRequestModel(BaseModel):
    id: str = Field(description="Encoded ID of the role")
    request: dict[str, Any]
    state: ToolRequestState
    state_message: str | None


class CreatedEntryResponse(BaseModel):
    external_link: str | None = Field(None, description="An optional external link to the created entry if available.")
    name: str = Field(description="The name of the created entry.")
    uri: str = Field(description="The URI of the created entry.")


class DeleteQuotaPayload(BaseModel):
    purge: bool | None = Field(None, description="Whether to also purge the Quota after deleting it.")


class BooleanParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    falsevalue: str | None = None
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    truevalue: str | None = None
    type: str
    value: bool | None = None


class ComputeDatasetHashPayload(BaseModel):
    extra_files_path: str | None = Field(None, description="If set, extra files path to compute a hash for.")
    hash_function: HashFunctionNameEnum | None = Field(
        None, description="Hash function name to use to compute dataset hashes."
    )


class QuotaModel(BaseModel):
    enabled: bool
    source: str | None = None


class UpdateDatasetPermissionsPayload(BaseModel):
    access_ids__: list[str] | str | None = None
    action: DatasetPermissionAction | None = Field(
        None, description="Indicates what action should be performed on the dataset."
    )
    manage_ids__: list[str] | str | None = None
    modify_ids__: list[str] | str | None = None


class InstalledRepositoryToolShedStatus(BaseModel):
    latest_installable_revision: str | None = Field(None, description="Most recent version available on the tool shed")
    repository_deprecated: str | None = Field(None, description="Repository has been depreciated on the tool shed")
    revision_update: str
    revision_upgrade: str | None = None


class NewSharedItemNotificationContent(BaseModel):
    category: str | None = None
    item_name: str = Field(description="The name of the shared item.")
    item_type: Literal["history", "workflow", "visualization", "page"] = Field(
        description="The type of the shared item."
    )
    owner_name: str = Field(description="The name of the owner of the shared item.")
    slug: str = Field(description="The slug of the shared item. Used for the link to the item.")


class Galaxy_schema_schema_Organization(BaseModel):
    address: str | None = None
    alternateName: str | None = None
    class_: str | None = None
    email: str | None = None
    faxNumber: str | None = None
    identifier: str | None = Field(None, description="Identifier (typically an orcid.org ID)")
    image: str | None = None
    name: str | None = Field(None, description="The name of the creator.")
    telephone: str | None = None
    url: str | None = None


class CopyDatasetsResponse(BaseModel):
    history_ids: list[str]


class ContentTypeMessage(BaseModel):
    content_type: str
    message: str


class XrefItem(BaseModel):
    access_time: str = Field(description="Date and time the external reference was accessed")
    ids: list[str] = Field(description="List of reference identifiers")
    name: str = Field(description="Name of external reference")
    namespace: str = Field(description="External resource vendor prefix")


class MessageExceptionModel(BaseModel):
    err_code: int
    err_msg: str


class LibraryContentsCreateFolderResponse(BaseModel):
    id: str
    name: str
    url: str


class WorkflowInvocationCollectionView(BaseModel):
    create_time: str = Field(description="The time and date this item was created.")
    history_id: str = Field(description="The encoded ID of the history associated with the invocation.")
    id: str = Field(description="The encoded ID of the workflow invocation.")
    landing_uuid: str | None = Field(
        None, description="The UUID of the workflow landing request associated with this invocation."
    )
    model_class: str = Field(description="The name of the database model class.")
    state: InvocationState = Field(description="State of workflow invocation.")
    update_time: str = Field(description="The last time and date this item was updated.")
    uuid: str | None = Field(None, description="Universal unique identifier of the workflow invocation.")
    workflow_id: str = Field(description="The encoded Workflow ID associated with the invocation.")


class VisualizationUpdatePayload(BaseModel):
    config: dict[str, Any] | str | None = Field(None, description="The config of the visualization.")
    dbkey: str | None = Field(None, description="The database key of the visualization.")
    deleted: bool | None = Field(None, description="Whether this Visualization has been deleted.")
    title: str | None = Field(None, description="The name of the visualization.")


class BadgeDict(BaseModel):
    message: str | None
    source: Literal["admin", "galaxy"]
    type: (
        Literal[
            "faster",
            "slower",
            "short_term",
            "backed_up",
            "not_backed_up",
            "more_secure",
            "less_secure",
            "more_stable",
            "less_stable",
        ]
        | Literal["cloud", "quota", "no_quota", "restricted", "user_defined"]
    )


class ImportToolDataBundleUriSource(BaseModel):
    src: str = Field(description="Indicates that the tool data should be resolved by a URI.")
    uri: str = Field(
        description="URI to fetch tool data bundle from (file:// URIs are fine because this is an admin-only operation)"
    )


class DatasetSourceTransform(BaseModel):
    action: DatasetSourceTransformActionType = Field(
        description="Action that was applied to dataset source content to transform it into the dataset"
    )
    datatype_ext: str | None = Field(
        None,
        description="If action is 'datatype_groom', this is the datatype that was used to find and run the grooming code as part of the transform action.",
    )


class Tour(BaseModel):
    description: str = Field(description="Tour description")
    id: str = Field(description="Tour identifier")
    name: str = Field(description="Name of tour")
    requirements: list[Requirement] = Field(description="Requirements to run the tour.")
    tags: list[str] = Field(description="Topic topic tags")


class CreateLibraryFilePayload(BaseModel):
    from_hda_id: str | None = Field(None, description="The ID of an accessible HDA to copy into the library.")
    from_hdca_id: str | None = Field(
        None,
        description="The ID of an accessible HDCA to copy into the library. Nested collections are not allowed, you must flatten the collection first.",
    )
    ldda_message: str | None = Field(None, description="The new message attribute of the LDDA created.")


class DatatypeVisualizationMapping(BaseModel):
    datatype: str = Field(description="The datatype extension this visualization applies to")
    visualization: str = Field(description="The visualization plugin to use")


class Metric(BaseModel):
    args: str = Field(description="A JSON string containing an array of extra data.")
    level: int = Field(description="An integer representing the metric's log level.")
    namespace: str = Field(description="Label indicating the source of the metric.")
    time: str = Field(description="The timestamp in ISO format.")


class ConvertedDatasetsMap(BaseModel):
    """Map of `file extension` -> `converted dataset encoded id`"""


class LimitedUserModel(BaseModel):
    """This is used when config options (expose_user_name and expose_user_email) are in place."""

    email: str | None = None
    id: str = Field(description="Encoded ID of the user")
    username: str | None = None


class MaterializeDatasetInstanceAPIRequest(BaseModel):
    content: str = Field(
        description="Depending on the `source` it can be:\n- The encoded id of the source library dataset\n- The encoded id of the HDA\n"
    )
    source: DatasetSourceType = Field(
        description="The source of the content. Can be other history element to be copied or library elements."
    )


class LibraryContentsFileCreatePayload(BaseModel):
    create_type: CreateType = Field(description="the type of item to create")
    dbkey: str | list[Any] | None = None
    extended_metadata: dict[str, Any] | None = Field(
        None, description="sub-dictionary containing any extended metadata to associate with the item"
    )
    file_type: str | None = None
    filesystem_paths: str | None = Field(
        None,
        description="(only if upload_option is 'upload_paths' and the user is an admin) file paths on the Galaxy server to upload to the library, one file per line",
    )
    folder_id: str = Field(description="the encoded id of the parent folder of the new item")
    from_hda_id: str | None = Field(
        None, description="(only if create_type is 'file') the encoded id of an accessible HDA to copy into the library"
    )
    from_hdca_id: str | None = Field(
        None,
        description="(only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library",
    )
    ldda_message: str | None = Field(None, description="the new message attribute of the LDDA created")
    link_data_only: LinkDataOnly | None = Field(
        None,
        description="(only when upload_option is 'upload_directory' or 'upload_paths').Setting to 'link_to_files' symlinks instead of copying the files",
    )
    roles: str | None = None
    server_dir: str | None = Field(
        None,
        description="(only if upload_option is 'upload_directory') relative path of the subdirectory of Galaxy ``library_import_dir`` (if admin) or ``user_library_import_dir`` (if non-admin) to upload. All and only the files (i.e. no subdirectories) contained in the specified directory will be uploaded.",
    )
    tag_using_filenames: bool | None = Field(None, description="create tags on datasets using the file's original name")
    tags: list[str] | None = Field(None, description="create the given list of tags on datasets")
    upload_files: list[dict[str, Any]] | None = None
    upload_option: UploadOption | None = Field(None, description="the method to use for uploading files")
    uuid: str | None = None


class GroupResponse(BaseModel):
    """Response schema for a group."""

    id: str
    model_class: str = Field(description="The name of the database model class.")
    name: str
    roles_url: str | None = None
    url: str
    users_url: str | None = None


class InvocationStepJobsResponseJobModel(BaseModel):
    id: str = Field(description="The encoded ID of the job.")
    model: str
    populated_state: JobState = Field(description="The absolute state of all the jobs related to the Invocation.")
    states: dict[str, Any] = Field(description="The states of all the jobs related to the Invocation.")


class InRangeParameterValidatorModel(BaseModel):
    exclude_max: bool | None = None
    exclude_min: bool | None = None
    implicit: bool | None = None
    max: float | int | None = None
    message: str | None = None
    min: float | int | None = None
    negate: bool | None = None
    type: str | None = None


class OAuth2Info(BaseModel):
    authorize_url: str


class UpdateHistoryPayload(BaseModel):
    annotation: str | None = None
    deleted: bool | None = None
    genome_build: str | None = None
    importable: bool | None = None
    name: str | None = None
    preferred_object_store_id: str | None = None
    published: bool | None = None
    purged: bool | None = None
    tags: list[str] | None = None


class LibraryDestination(BaseModel):
    description: str | None = Field(None, description="Description for library to create")
    name: str = Field(description="Must specify a library name")
    synopsis: str | None = Field(None, description="Description for library to create")
    type: str


class PluginAspectStatus(BaseModel):
    message: str
    state: Literal["ok", "not_ok", "unknown"]


class AgentQueryRequest(BaseModel):
    """Request to query an AI agent."""

    agent_type: str | None = Field(None, description="Preferred agent type ('auto' for routing)")
    context: dict[str, Any] | None = Field(None, description="Additional context for the query")
    query: str = Field(description="The user's question or request")
    stream: bool | None = Field(None, description="Whether to stream the response")


class InvocationUnexpectedFailureResponse(BaseModel):
    details: str | None = Field(None, description="May contains details to help troubleshoot this problem.")
    reason: str
    workflow_step_id: int | None = Field(None, description="Workflow step id of step that failed.")


class LibraryContentsShowDatasetResponse(BaseModel):
    created_from_basename: str | None
    data_type: str
    date_uploaded: str
    file_ext: str
    file_name: str
    file_size: int
    folder_id: str
    genome_build: str | None
    id: str
    ldda_id: str
    message: str | None
    misc_blurb: str | None
    misc_info: str | None
    model_class: str = Field(description="The name of the database model class.")
    name: str
    parent_library_id: str
    peek: str | None
    state: str
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    update_time: str
    uploaded_by: str | None
    uuid: str


class DeletedCustomBuild(BaseModel):
    message: str = Field(description="Confirmation of the custom build deletion.")


class ExtraFileEntry(BaseModel):
    class_: ExtraFilesEntryClass = Field(description="The class of this entry, either File or Directory.")
    path: str = Field(description="Relative path to the file or directory.")


class ParsedWorkbookHda(BaseModel):
    id: str
    model_class: str | None = None


class UserBeaconSetting(BaseModel):
    enabled: bool = Field(description="True if beacon sharing is enabled")


class DatasetTextContentDetails(BaseModel):
    item_data: str | None = Field(description="First chunk of text content (maximum 1MB) of the dataset.")
    item_url: str = Field(description="URL to access this dataset.")
    truncated: bool = Field(
        description="Whether the text in `item_data` has been truncated or contains the whole contents."
    )


class RemoveUnlabeledWorkflowOutputs(BaseModel):
    action_type: str


class FilePatternDatasetCollectionDescription(BaseModel):
    assign_primary_output: bool
    directory: str | None
    discover_via: str
    format: str | None
    match_relative_path: bool
    pattern: str
    recurse: bool
    sort_comp: Literal["lexical", "numeric"]
    sort_key: Literal["filename", "name", "designation", "dbkey"]
    sort_reverse: bool | None = None
    visible: bool


class UpgradeAllStepsAction(BaseModel):
    action_type: str


class HelpForumUser(BaseModel):
    """Model for a user in the help forum."""


class FieldDict(BaseModel):
    format: str | None = None
    name: str
    type: (
        Literal["File", "null", "boolean", "int", "float", "string"]
        | list[Literal["File", "null", "boolean", "int", "float", "string"]]
    )


class FileHash(BaseModel):
    hash_function: Literal["MD5", "SHA-1", "SHA-256", "SHA-512"]
    hash_value: str


class CleanableItemsSummary(BaseModel):
    total_items: int = Field(description="The total number of items that could be purged.")
    total_size: int = Field(description="The total size in bytes that can be recovered by purging all the items.")


class WorkflowJobMetric(BaseModel):
    job_id: str
    name: str = Field(description="The name of the metric variable.")
    plugin: str = Field(description="The instrumenter plugin that generated this metric.")
    raw_value: str = Field(description="The raw value of the metric as a string.")
    step_index: int
    step_label: str | None
    title: str = Field(description="A descriptive title for this metric.")
    tool_id: str
    value: str = Field(description="The textual representation of the metric value.")


class HdcaDestination(BaseModel):
    type: str


class CreateToolLandingRequestPayload(BaseModel):
    client_secret: str | None = None
    origin: str | None = Field(None, description="The origin of the landing request.")
    public: bool | None = None
    request_state: dict[str, Any] | None = None
    tool_id: str
    tool_version: str | None = None


class UserEmail(BaseModel):
    email: str = Field(description="The email of the user.")
    id: str = Field(description="The encoded ID of the user.")


class NotificationsBatchUpdateResponse(BaseModel):
    """The response of a batch update request."""

    updated_count: int = Field(description="The number of notifications that were updated.")


class DatatypesMap(BaseModel):
    class_to_classes: dict[str, Any] = Field(
        description="Dictionary mapping datatype's classes with their base classes"
    )
    ext_to_class_name: dict[str, Any] = Field(
        description="Dictionary mapping datatype's extensions with implementation classes"
    )


class VisualizationSummary(BaseModel):
    annotation: str | None = Field(None, description="The annotation of this Visualization.")
    create_time: str | None = Field(description="The time and date this item was created.")
    dbkey: str | None = Field(None, description="The database key of the visualization.")
    deleted: bool = Field(description="Whether this Visualization has been deleted.")
    id: str = Field(description="Encoded ID of the Visualization.")
    importable: bool = Field(description="Whether this Visualization can be imported.")
    published: bool = Field(description="Whether this Visualization has been published.")
    tags: list[str] | None = Field(description="A list of tags to add to this item.")
    title: str = Field(description="The name of the visualization.")
    type: str = Field(description="The type of the visualization.")
    update_time: str | None = Field(description="The last time and date this item was updated.")
    username: str = Field(description="The name of the user owning this Visualization.")


class LibrarySummary(BaseModel):
    can_user_add: bool = Field(description="Whether the current user can add contents to this Library.")
    can_user_manage: bool = Field(description="Whether the current user can manage the Library and its contents.")
    can_user_modify: bool = Field(description="Whether the current user can modify this Library.")
    create_time: str = Field(description="The time and date this item was created.")
    create_time_pretty: str = Field(description="Nice time representation of the creation date.")
    deleted: bool = Field(description="Whether this Library has been deleted.")
    description: str | None = Field(None, description="A detailed description of the Library.")
    id: str = Field(description="Encoded ID of the Library.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the Library.")
    public: bool = Field(description="Whether this Library has been deleted.")
    root_folder_id: str = Field(description="Encoded ID of the Library's base folder.")
    synopsis: str | None = Field(None, description="A short text describing the contents of the Library.")


class VisualizationCreateResponse(BaseModel):
    id: str = Field(description="Encoded ID of the Visualization.")


class ExportRecordData(BaseModel):
    """Data of an export record associated with a history that was archived."""

    include_deleted: bool | None = Field(
        None, description="Include file contents for deleted datasets (if include_files is True)."
    )
    include_files: bool | None = Field(None, description="include materialized files in export when available")
    include_hidden: bool | None = Field(
        None, description="Include file contents for hidden datasets (if include_files is True)."
    )
    model_store_format: ModelStoreFormat | None = Field(None, description="format of model store to export")
    target_uri: str = Field(description="Galaxy Files URI to write mode store content to.")


class HelpContent(BaseModel):
    content: str
    format: Literal["restructuredtext", "plain_text", "markdown"]


class APIKeyModel(BaseModel):
    create_time: str = Field(description="The time and date this API key was created.")
    key: str = Field(description="API key to interact with the Galaxy API")


class CustomBuildModel(BaseModel):
    count: str | None = Field(None, description="The number of chromosomes/contigs.")
    fasta: str | None = Field(None, description="The primary id of the fasta file from a history.")
    id: str = Field(description="The ID of the custom build.")
    len: str = Field(description="The primary id of the len file.")
    linecount: str | None = Field(None, description="The primary id of a linecount dataset.")
    name: str = Field(description="The name of the custom build.")


class HdaDestination(BaseModel):
    type: str


class LabelValue(BaseModel):
    label: str
    selected: bool
    value: str


class BodyAi_agentsErrorAnalysis_analyzeError(BaseModel):
    error_details: dict[str, Any] | None = Field(None, description="Additional error details")
    job_id: str | None = Field(None, description="Job ID for context")
    query: str = Field(description="Description of the error or problem")


class CwlStringParameterModel(BaseModel):
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    parameter_type: str | None = None


class InvocationOutput(BaseModel):
    id: str | None = Field(None, description="The encoded ID of the dataset/dataset collection.")
    src: str = Field(description="Source model of the output dataset.")
    workflow_step_id: str = Field(
        description="The encoded ID of the workflow step associated with the dataset/dataset collection."
    )


class SetSlugPayload(BaseModel):
    new_slug: str = Field(description="The slug that will be used to access this shared item.")


class StorageItemCleanupError(BaseModel):
    error: str
    item_id: str


class Galaxy_schema_drs_Organization(BaseModel):
    name: str = Field(description="Name of the organization responsible for the service")
    url: str = Field(description="URL of the website of the organization (RFC 3986 format)")


class EncodedDatasetJobInfo(BaseModel):
    id: str
    src: DataItemSourceType = Field(
        description="The source of this dataset, either `hda`, `ldda`, `hdca`, `dce` or `dc` depending of its origin."
    )
    uuid: str | None = Field(None, description="Universal unique identifier for this dataset.")


class CredentialPayload(BaseModel):
    name: str = Field(description="The name of the credential (variable or secret).")
    value: str | None = Field(None, description="The value of the credential.")


class CwlFileParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None


class UpdateObjectStoreIdPayload(BaseModel):
    object_store_id: str = Field(
        description="Object store ID to update to, it must be an object store with the same device ID as the target dataset currently."
    )


class Person(BaseModel):
    address: str | None = None
    alternateName: str | None = None
    class_: str | None = None
    email: str | None = None
    familyName: str | None = None
    faxNumber: str | None = None
    givenName: str | None = None
    honorificPrefix: str | None = Field(None, description="Honorific Prefix (e.g. Dr/Mrs/Mr)")
    honorificSuffix: str | None = Field(None, description="Honorific Suffix (e.g. M.D.)")
    identifier: str | None = Field(None, description="Identifier (typically an orcid.org ID)")
    image: str | None = None
    jobTitle: str | None = None
    name: str | None = Field(None, description="The name of the creator.")
    telephone: str | None = None
    url: str | None = None


class LibraryContentsDeletePayload(BaseModel):
    purge: bool | None = Field(None, description="if True, purge the library dataset")


class UserObjectstoreUsage(BaseModel):
    object_store_id: str
    total_disk_usage: float


class DeleteHistoryContentPayload(BaseModel):
    purge: bool | None = Field(
        None,
        description="Whether to remove the dataset from storage. Datasets will only be removed from storage once all HDAs or LDDAs that refer to this datasets are deleted.",
    )
    recursive: bool | None = Field(
        None, description="When deleting a dataset collection, whether to also delete containing datasets."
    )
    stop_job: bool | None = Field(
        None, description="Whether to stop the creating job if all the job's outputs are deleted."
    )


class ItemTagsCreatePayload(BaseModel):
    """Payload schema for creating an item tag."""

    value: str | None = None


class JobSummary(BaseModel):
    """Basic information about a job."""

    command_line: str | None = Field(
        None,
        description="The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.",
    )
    create_time: str = Field(description="The time and date this item was created.")
    exit_code: int | None = Field(
        None, description="The exit code returned by the tool. Can be unset if the job is not completed yet."
    )
    external_id: str | None = Field(
        None,
        description="The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value.",
    )
    galaxy_version: str | None = Field(None, description="The (major) version of Galaxy used to create this job.")
    handler: str | None = Field(
        None, description="The job handler process assigned to handle this job. Only administrator can see this value."
    )
    history_id: str | None = Field(None, description="The encoded ID of the history associated with this item.")
    id: str
    job_runner_name: str | None = Field(
        None, description="Name of the job runner plugin that handles this job. Only administrator can see this value."
    )
    model_class: str = Field(description="The name of the database model class.")
    state: JobState = Field(description="Current state of the job.")
    tool_id: str = Field(description="Identifier of the tool that generated this job.")
    update_time: str = Field(description="The last time and date this item was updated.")
    user_email: str | None = Field(
        None,
        description="The email of the user that owns this job. Only the owner of the job and administrators can see this value.",
    )
    user_id: str | None = Field(None, description="The encoded ID of the user that owns this job.")


class CompositeFileInfo(BaseModel):
    description: str | None = Field(description="Summary description of the purpouse of this file")
    is_binary: bool = Field(description="Whether this file is a binary file")
    mimetype: str | None = Field(description="The MIME type of this file")
    name: str = Field(description="The name of this composite file")
    optional: bool = Field(description="")
    space_to_tab: bool = Field(description="")
    substitute_name_with_metadata: str | None = Field(description="")
    to_posix_lines: bool = Field(description="")


class DatasetCollectionAttributesResult(BaseModel):
    dbkey: str = Field(description="TODO")
    dbkeys: list[str] | None
    extension: str = Field(description="The dataset file extension.")
    extensions: list[str] | None
    model_class: str = Field(description="The name of the database model class.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")


class GroupRoleResponse(BaseModel):
    id: str = Field(description="Encoded ID of the role")
    name: str = Field(description="Name of the role")
    url: str = Field(description="The relative URL to access this item.")


class DeleteLibraryPayload(BaseModel):
    undelete: bool = Field(description="Whether to restore this previously deleted library.")


class ToolDataDetails(BaseModel):
    columns: list[str] = Field(description="A list of column names")
    fields: list[list[str]] | None = Field(None, description="")
    model_class: str = Field(description="The name of class modelling this tool data")
    name: str = Field(description="The name of this tool data entry")


class WorkflowLandingRequest(BaseModel):
    origin: str | None = None
    request_state: dict[str, Any]
    state: LandingRequestState
    uuid: str = Field(description="Universal unique identifier for this dataset.")
    workflow_id: str
    workflow_target_type: Literal["stored_workflow", "workflow", "trs_url"]


class APIKeyResponse(BaseModel):
    api_key: str


class SearchJobsPayload(BaseModel):
    history_id: str | None = Field(None, description="The encoded ID of the history associated with this job.")
    inputs: dict[str, Any] = Field(description="The inputs of the job.")
    state: JobState | None = Field(None, description="Current state of the job.")
    tool_id: str = Field(description="The tool ID related to the job.")


class JavascriptRequirement(BaseModel):
    expression_lib: list[str] | None
    type: str


class FileLibraryFolderItem(BaseModel):
    can_manage: bool
    create_time: str = Field(description="The time and date this item was created.")
    date_uploaded: str
    deleted: bool
    file_ext: str
    file_size: str
    id: str
    is_private: bool
    is_unrestricted: bool
    ldda_id: str
    message: str | None = None
    name: str
    raw_size: int
    state: DatasetState = Field(description="The current state of this dataset.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    type: str
    update_time: str = Field(description="The last time and date this item was updated.")


class JobInputSummary(BaseModel):
    has_duplicate_inputs: bool = Field(description="Job has duplicate inputs.")
    has_empty_inputs: bool = Field(description="Job has empty inputs.")


class UpdatePagePayload(BaseModel):
    annotation: str | None = Field(None, description="Annotation that will be attached to the page.")
    slug: str = Field(description="The identifying slug for the page URL, must be unique.")
    title: str = Field(description="The name of the page.")


class TagOperationParams(BaseModel):
    tags: list[str]
    type: str


class ToolProvidedMetadataDatasetCollection(BaseModel):
    assign_primary_output: bool
    directory: str | None
    discover_via: str
    format: str | None
    match_relative_path: bool
    recurse: bool
    visible: bool


class ExportObjectResultMetadata(BaseModel):
    error: str | None = None
    success: bool
    uri: str | None = None


class LibraryContentsIndexDatasetResponse(BaseModel):
    id: str
    name: str
    type: str
    url: str


class RemoteUserCreationPayload(BaseModel):
    remote_user_email: str = Field(description="Email of the user")


class ArchiveHistoryRequestPayload(BaseModel):
    archive_export_id: str | None = Field(
        None,
        description="The encoded ID of the export record to associate with this history archival.This is used to be able to recover the history from the export record.",
    )
    purge_history: bool | None = Field(
        None,
        description="Whether to purge the history after archiving it. It requires an `archive_export_id` to be set.",
    )


class Report(BaseModel):
    markdown: str


class UpgradeInstancePayload(BaseModel):
    secrets: dict[str, Any]
    template_version: int
    variables: dict[str, Any]


class ToolOutputBoolean(BaseModel):
    hidden: Any = Field(description="If true, the output will not be shown in the history.")
    label: str | None = Field(None, description="Output label. Will be used as dataset name in history.")
    name: Any = Field(description="Parameter name. Used when referencing parameter in workflows.")
    type: str


class InvocationFailureOutputNotFoundResponse(BaseModel):
    dependent_workflow_step_id: int = Field(description="Workflow step id of step that caused failure.")
    output_name: str
    reason: str
    workflow_step_id: int = Field(description="Workflow step id of step that failed.")


class LibraryContentsIndexFolderResponse(BaseModel):
    id: str
    name: str
    type: str
    url: str


class ExpressionParameterValidatorModel(BaseModel):
    """Check if a one line python expression given expression evaluates to True.

    The expression is given is the content of the validator tag."""

    expression: str
    implicit: bool | None = None
    message: str | None = None
    negate: bool | None = None
    type: str | None = None


class AsyncTaskResultSummary(BaseModel):
    id: str = Field(description="Celery AsyncResult ID for this task")
    ignored: bool = Field(description="Indicated whether the Celery AsyncResult will be available for retrieval")
    name: str | None = None
    queue: str | None = None


class CleanupStorageItemsRequest(BaseModel):
    item_ids: list[str]


class BodyHistories_create(BaseModel):
    all_datasets: Any | None = None
    archive_file: Any | None = None
    archive_source: Any | None = None
    archive_type: Any | None = None
    history_id: Any | None = None
    name: Any | None = None


class FileDefaultsAction(BaseModel):
    action_type: str


class VariableResponse(BaseModel):
    name: str = Field(description="The name of the credential.")
    value: str | None = Field(None, description="The value of the variable (for variables, not secrets).")


class ShortTermStoreExportPayload(BaseModel):
    duration: int | float | None = None
    include_deleted: bool | None = Field(
        None, description="Include file contents for deleted datasets (if include_files is True)."
    )
    include_files: bool | None = Field(None, description="include materialized files in export when available")
    include_hidden: bool | None = Field(
        None, description="Include file contents for hidden datasets (if include_files is True)."
    )
    model_store_format: ModelStoreFormat | None = Field(None, description="format of model store to export")
    short_term_storage_request_id: str


class MetadataFile(BaseModel):
    """Metadata file associated with a dataset."""

    download_url: str = Field(description="The URL to download this item from the server.")
    file_type: str = Field(description="TODO")


class JobMetric(BaseModel):
    name: str = Field(description="The name of the metric variable.")
    plugin: str = Field(description="The instrumenter plugin that generated this metric.")
    raw_value: str = Field(description="The raw value of the metric as a string.")
    title: str = Field(description="A descriptive title for this metric.")
    value: str = Field(description="The textual representation of the metric value.")


class HistoryContentItem(BaseModel):
    history_content_type: HistoryContentType = Field(description="The type of this item.")
    id: str


class ActionSuggestion(BaseModel):
    """Structured suggestion for user action."""

    action_type: ActionType = Field(description="Type of action to take")
    confidence: ConfidenceLevel = Field(description="Confidence in this suggestion")
    description: str = Field(description="Human-readable description of the action")
    parameters: dict[str, Any] | None = Field(None, description="Parameters for the action")
    priority: int | None = Field(None, description="Priority level (1=high, 2=medium, 3=low)")


class HDCJobStateSummary(BaseModel):
    """Overview of the job states working inside a dataset collection."""

    all_jobs: int | None = Field(None, description="Total number of jobs associated with a dataset collection.")
    deleted: int | None = Field(None, description="Number of jobs in the `deleted` state.")
    deleted_new: int | None = Field(None, description="Number of jobs in the `deleted_new` state.")
    error: int | None = Field(None, description="Number of jobs in the `error` state.")
    failed: int | None = Field(None, description="Number of jobs in the `failed` state.")
    new: int | None = Field(None, description="Number of jobs in the `new` state.")
    ok: int | None = Field(None, description="Number of jobs in the `ok` state.")
    paused: int | None = Field(None, description="Number of jobs in the `paused` state.")
    queued: int | None = Field(None, description="Number of jobs in the `queued` state.")
    resubmitted: int | None = Field(None, description="Number of jobs in the `resubmitted` state.")
    running: int | None = Field(None, description="Number of jobs in the `running` state.")
    skipped: int | None = Field(
        None, description="Number of jobs that were skipped due to conditional workflow step execution."
    )
    upload: int | None = Field(None, description="Number of jobs in the `upload` state.")
    waiting: int | None = Field(None, description="Number of jobs in the `waiting` state.")


class DatasetSourceId(BaseModel):
    id: str
    src: DatasetSourceType = Field(
        description="The source of this dataset, either `hda` or `ldda` depending of its origin."
    )


class InferredColumnMapping(BaseModel):
    column_index: int
    column_title: str
    parsed_column: ParsedColumn


class FtpImportTarget(BaseModel):
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    column_definitions: list[SampleSheetColumnDefinition] | None = None
    destination: HdcaDestination
    ftp_path: str
    items_from: ElementsFromType | None = None
    name: str | None = None
    src: str
    tags: list[str] | None = None


class InvocationStep(BaseModel):
    """Information about workflow invocation step"""

    action: bool | None = Field(description="Whether to take action on the invocation step.")
    id: str
    implicit_collection_jobs_id: str | None = Field(
        None, description="The implicit collection job ID associated with the workflow invocation step."
    )
    job_id: str | None = Field(
        None, description="The encoded ID of the job associated with this workflow invocation step."
    )
    jobs: list[JobBaseModel] | None = Field(None, description="Jobs associated with the workflow invocation step.")
    model_class: str = Field(description="The name of the database model class.")
    order_index: int = Field(description="The index of the workflow step in the workflow.")
    output_collections: dict[str, Any] | None = Field(
        None, description="The dataset collection outputs of the workflow invocation step."
    )
    outputs: dict[str, Any] | None = Field(None, description="The outputs of the workflow invocation step.")
    state: InvocationStepState | JobState | None = Field(
        None, description="Describes where in the scheduling process the workflow invocation step is."
    )
    subworkflow_invocation_id: str | None = Field(None, description="The encoded ID of the subworkflow invocation.")
    update_time: str | None = Field(description="The last time and date this item was updated.")
    workflow_step_id: str = Field(
        description="The encoded ID of the workflow step associated with this workflow invocation step."
    )
    workflow_step_label: str | None = Field(None, description="The label of the workflow step")
    workflow_step_uuid: str | None = Field(None, description="Universal unique identifier of the workflow step.")


class UserNotificationResponse(BaseModel):
    """A notification response specific to the user."""

    category: PersonalNotificationCategory = Field(
        description="The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'."
    )
    content: MessageNotificationContent | NewSharedItemNotificationContent = Field(
        description="The content of the notification. The structure depends on the category."
    )
    create_time: str = Field(description="The time when the notification was created.")
    deleted: bool = Field(
        description="Whether the notification is marked as deleted by the user. Deleted notifications don't show up in the notification list."
    )
    expiration_time: str | None = Field(
        None,
        description="The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.",
    )
    id: str = Field(description="The encoded ID of the notification.")
    publication_time: str = Field(
        description="The time when the notification was published. Notifications can be created and then published at a later time."
    )
    seen_time: str | None = Field(
        None,
        description="The time when the notification was seen by the user. If not set, the notification was not seen yet.",
    )
    source: str = Field(
        description="The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'."
    )
    update_time: str = Field(description="The time when the notification was last updated.")
    variant: NotificationVariant = Field(
        description="The variant of the notification. Represents the intent or relevance of the notification. E.g. 'info' or 'urgent'."
    )


class TemplateVariableInteger(BaseModel):
    default: int | None = None
    help: str | None
    label: str | None = None
    name: str
    type: str
    validators: (
        list[RegexParameterValidatorModel | InRangeParameterValidatorModel | LengthParameterValidatorModel] | None
    ) = None


class InferredCollectionTypeLogEntry(BaseModel):
    from_columns: list[ParsedColumn]
    message: str


class DrillDownParameterModelOutput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    hierarchy: Literal["recurse", "exact"]
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    multiple: bool
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    options: list[DrillDownOptionsDictOutput] | None = None
    parameter_type: str | None = None
    type: str


class FileDataElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    name: str | int | float | bool | None = None
    row: list[int | float | bool | str | None] | None = None
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    src: str
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )


class IntegerParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    max: int | None = None
    min: int | None = None
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = None
    parameter_type: str | None = None
    type: str
    validators: list[InRangeParameterValidatorModel] | None = None
    value: int | None = None


class DisplayApplication(BaseModel):
    filename_: str
    id: str
    links: list[Link]
    name: str
    version: str


class ParseFetchWorkbook(BaseModel):
    content: str = Field(
        description="The workbook content (the contents of the xlsx file) that have been base64 encoded."
    )
    fill_identifiers: FillIdentifiers | None = None


class LibraryAvailablePermissions(BaseModel):
    page: int = Field(description="Current page.")
    page_limit: int = Field(description="Maximum number of items per page.")
    roles: list[BasicRoleModel] = Field(
        description="A list containing available roles that can be assigned to a particular permission."
    )
    total: int = Field(description="Total number of items")


class FloatParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    max: float | None = None
    min: float | None = None
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str
    validators: list[InRangeParameterValidatorModel] | None = None
    value: float | None = None


class DatatypesEDAMDetailsDict(BaseModel):
    pass


class DirectoryUriParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str
    validators: (
        list[
            LengthParameterValidatorModel
            | RegexParameterValidatorModel
            | ExpressionParameterValidatorModel
            | EmptyFieldParameterValidatorModel
        ]
        | None
    ) = None


class CwlUnionParameterModelOutput(BaseModel):
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    parameter_type: str | None = None
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelOutput
    ]


class UrlDataElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    name: str | int | float | bool | None = None
    row: list[int | float | bool | str | None] | None = None
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    src: str
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )
    url: str = Field(description="URL to upload")


class AccessMethod(BaseModel):
    access_id: str | None = Field(
        None,
        description="An arbitrary string to be passed to the `/access` method to get an `AccessURL`. This string must be unique within the scope of a single object. Note that at least one of `access_url` and `access_id` must be provided.",
    )
    access_url: AccessURL | None = None
    authorizations: Authorizations | None = None
    region: str | None = Field(
        None, description="Name of the region in the cloud service provider that the object belongs to."
    )
    type: AccessMethodType = Field(description="Type of the access method.")


class DatatypeDetails(BaseModel):
    composite_files: list[CompositeFileInfo] | None = Field(
        None, description="A collection of files composing this data type"
    )
    description: str | None = Field(description="A summary description for this data type")
    description_url: str | None = Field(description="The URL to a detailed description for this datatype")
    display_behavior: str | None = Field(
        None,
        description="How this datatype behaves when displayed with preview=True: 'inline' (can be displayed in browser) or 'download' (triggers download)",
    )
    display_in_upload: bool | None = Field(
        None,
        description="If True, the associated file extension will be displayed in the `File Format` select list in the `Upload File from your computer` tool in the `Get Data` tool section of the tool panel",
    )
    extension: str = Field(description="The data type’s Dataset file extension")
    upload_warning: str | None = Field(
        None, description="End-user information regarding potential pitfalls with this upload type."
    )


class UpdateHistoryContentsBatchPayload(BaseModel):
    """Contains property values that will be updated for all the history `items` provided."""

    items: list[UpdateContentItem] = Field(description="A list of content items to update with the changes.")


class JobParameter(BaseModel):
    depth: int = Field(description="The depth of the job parameter.")
    notes: str | None = Field(None, description="Notes associated with the job parameter.")
    text: str = Field(description="Text associated with the job parameter.")
    value: list[EncodedJobParameterHistoryItem | None] | float | int | bool | str | None = Field(
        None, description="The values of the job parameter"
    )


class ShowFullJobResponse(BaseModel):
    command_line: str | None = Field(
        None,
        description="The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.",
    )
    command_version: str | None = Field(None, description="Tool version indicated during job execution.")
    copied_from_job_id: str | None = Field(None, description="Reference to cached job if job execution was cached.")
    create_time: str = Field(description="The time and date this item was created.")
    dependencies: list[Any] | None = Field(None, description="The dependencies of the job.")
    exit_code: int | None = Field(
        None, description="The exit code returned by the tool. Can be unset if the job is not completed yet."
    )
    external_id: str | None = Field(
        None,
        description="The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value.",
    )
    galaxy_version: str | None = Field(None, description="The (major) version of Galaxy used to create this job.")
    handler: str | None = Field(
        None, description="The job handler process assigned to handle this job. Only administrator can see this value."
    )
    history_id: str | None = Field(None, description="The encoded ID of the history associated with this item.")
    id: str
    inputs: dict[str, Any] | None = Field(
        None, description="Dictionary mapping all the tool inputs (by name) to the corresponding data references."
    )
    job_messages: list[ExitCodeJobMessage | RegexJobMessage | MaxDiscoveredFilesJobMessage] | None = Field(
        None, description="List with additional information and possible reasons for a failed job."
    )
    job_metrics: JobMetricCollection | None = Field(
        None,
        description="Collections of metrics provided by `JobInstrumenter` plugins on a particular job. Only administrators can see these metrics.",
    )
    job_runner_name: str | None = Field(
        None, description="Name of the job runner plugin that handles this job. Only administrator can see this value."
    )
    job_stderr: str | None = Field(None, description="The captured standard error of the job execution.")
    job_stdout: str | None = Field(None, description="The captured standard output of the job execution.")
    model_class: str = Field(description="The name of the database model class.")
    output_collections: dict[str, Any] | None = Field(None, description="")
    outputs: dict[str, Any] | None = Field(
        None, description="Dictionary mapping all the tool outputs (by name) to the corresponding data references."
    )
    params: Any = Field(
        description="Object containing all the parameters of the tool associated with this job. The specific parameters depend on the tool itself."
    )
    state: JobState = Field(description="Current state of the job.")
    stderr: str | None = Field(None, description="Combined tool and job standard error streams.")
    stdout: str | None = Field(None, description="Combined tool and job standard output streams.")
    tool_id: str = Field(description="Identifier of the tool that generated this job.")
    tool_stderr: str | None = Field(None, description="The captured standard error of the tool executed by the job.")
    tool_stdout: str | None = Field(None, description="The captured standard output of the tool executed by the job.")
    update_time: str = Field(description="The last time and date this item was updated.")
    user_email: str | None = Field(
        None,
        description="The email of the user that owns this job. Only the owner of the job and administrators can see this value.",
    )
    user_id: str | None = Field(None, description="User ID of user that ran this job")


class InputDataCollectionStep(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    id: int = Field(
        description="The identifier of the step. It matches the index order of the step inside the workflow."
    )
    input_steps: dict[str, Any] = Field(
        description="A dictionary containing information about the inputs connected to this workflow step."
    )
    tool_id: str | None = Field(None, description="The unique name of the tool associated with this step.")
    tool_inputs: Any | None = Field(None, description="TODO")
    tool_uuid: str | None = Field(
        None,
        description="The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.",
    )
    tool_version: str | None = Field(None, description="The version of the tool associated with this step.")
    type: str
    when: str | None


class HDCASummary(BaseModel):
    """History Dataset Collection Association summary information."""

    collection_id: str
    collection_type: str = Field(
        description="The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`."
    )
    contents_url: str = Field(description="The relative URL to access the contents of this History.")
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    element_count: int | None = Field(
        None,
        description="The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.",
    )
    elements_datatypes: list[str] = Field(
        description="A set containing all the different element datatypes in the collection."
    )
    elements_deleted: int = Field(description="The number of elements in the collection that are marked as deleted.")
    elements_states: ElementsStatesDict = Field(
        description="A dictionary containing counts for each dataset state in the collection."
    )
    hid: int = Field(description="The index position of this item in the History.")
    history_content_type: str = Field(description="This is always `dataset_collection` for dataset collections.")
    history_id: str
    id: str
    job_source_id: str | None = Field(
        None,
        description="The encoded ID of the Job that produced this dataset collection. Used to track the state of the job.",
    )
    job_source_type: JobSourceType | None = Field(
        None,
        description="The type of job (model class) that produced this dataset collection. Used to track the state of the job.",
    )
    job_state_summary: HDCJobStateSummary | None = Field(
        None, description="Overview of the job states working inside the dataset collection."
    )
    model_class: str = Field(description="The name of the database model class.")
    name: str | None = Field(description="The name of the item.")
    populated_state: DatasetCollectionPopulatedState = Field(
        description="Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated."
    )
    populated_state_message: str | None = Field(
        None,
        description="Optional message with further information in case the population of the dataset collection failed.",
    )
    store_times_summary: list[OldestCreateTimeByObjectStoreId] | None = Field(
        None,
        description="A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.",
    )
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    type: str | None = Field(None, description="This is always `collection` for dataset collections.")
    type_id: str | None = Field(None, description="The type and the encoded ID of this item. Used for caching.")
    update_time: str | None = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    visible: bool = Field(description="Whether this item is visible or hidden to the user by default.")


class CustomArchivedHistoryView(BaseModel):
    """Archived History Response with all optional fields.

    It is used for serializing only specific attributes using the "keys"
    query parameter."""

    annotation: str | None = Field(
        None, description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    archived: bool | None = Field(None, description="Whether this item has been archived and is no longer active.")
    contents_active: HistoryActiveContentCounts | None = Field(
        None, description="Contains the number of active, deleted or hidden items in a History."
    )
    contents_states: dict[str, Any] | None = Field(
        None,
        description="A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.",
    )
    contents_url: str | None = Field(None, description="The relative URL to access the contents of this History.")
    count: int | None = Field(None, description="The number of items in the history.")
    create_time: str | None = Field(None, description="The time and date this item was created.")
    deleted: bool | None = Field(None, description="Whether this item is marked as deleted.")
    export_record_data: ExportRecordData | None = Field(
        None, description="The export record data associated with this archived history. Used to recover the history."
    )
    genome_build: str | None = Field(None, description="TODO")
    id: str | None = None
    importable: bool | None = Field(
        None, description="Whether this History can be imported by other users with a shared link."
    )
    model_class: str | None = Field(None, description="The name of the database model class.")
    name: str | None = Field(None, description="The name of the history.")
    nice_size: str | None = Field(
        None, description="The total size of the contents of this history in a human-readable format."
    )
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    published: bool | None = Field(
        None, description="Whether this resource is currently publicly available to all users."
    )
    purged: bool | None = Field(None, description="Whether this item has been permanently removed.")
    size: int | None = Field(None, description="The total size of the contents of this history in bytes.")
    slug: str | None = Field(
        None, description="Part of the URL to uniquely identify this History by link in a readable way."
    )
    state: DatasetState | None = Field(
        None, description="The current state of the History based on the states of the datasets it contains."
    )
    state_details: dict[str, Any] | None = Field(
        None,
        description="A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.",
    )
    state_ids: dict[str, Any] | None = Field(
        None,
        description="A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.",
    )
    tags: list[str] | None = Field(None, description="The collection of tags associated with an item.")
    update_time: str | None = Field(None, description="The last time and date this item was updated.")
    url: str | None = Field(None, description="The relative URL to access this item.")
    user_id: str | None = Field(None, description="The encoded ID of the user that owns this History.")
    username: str | None = Field(None, description="Owner of the history")
    username_and_slug: str | None = Field(None, description="The relative URL in the form of /u/{username}/h/{slug}")


class BulkOperationItemError(BaseModel):
    error: str
    item: EncodedHistoryContentItem


class ServerDirElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    link_data_only: bool | None = None
    name: str | int | float | bool | None = None
    row: list[int | float | bool | str | None] | None = None
    server_dir: str
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    src: str
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )


class CustomBuildsMetadataResponse(BaseModel):
    fasta_hdas: list[LabelValuePair] = Field(
        description="A list of label/value pairs with all the datasets of type `FASTA` contained in the History.\n - `label` is item position followed by the name of the dataset.\n - `value` is the encoded database ID of the dataset.\n"
    )
    installed_builds: list[LabelValuePair] = Field(description="TODO")


class InstalledToolShedRepository(BaseModel):
    changeset_revision: str = Field(description="Changeset revision of the repository - a mercurial commit hash")
    ctx_rev: str | None = Field(
        description="The linearized 0-based index of the changeset on the tool shed (0, 1, 2,...)"
    )
    deleted: bool
    dist_to_shed: bool
    error_message: str | None = None
    id: str = Field(description="Encoded ID of the install tool shed repository.")
    installed_changeset_revision: str = Field(
        description="Initially installed changeset revision. Used to construct path to repository within Galaxies filesystem. Does not change if a repository is updated."
    )
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="Name of repository")
    owner: str = Field(description="Owner of repository")
    status: str
    tool_shed: str = Field(description="Hostname of the tool shed this was installed from")
    tool_shed_status: InstalledRepositoryToolShedStatus | None = None
    uninstalled: bool


class DrillDownParameterModelInput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    hierarchy: Literal["recurse", "exact"]
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    multiple: bool
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    options: list[DrillDownOptionsDictInput] | None = None
    parameter_type: str | None = None
    type: str


class FtpImportElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    ftp_path: str
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    name: str | int | float | bool | None = None
    row: list[int | float | bool | str | None] | None = None
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    src: str
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )


class AgentResponse(BaseModel):
    """Structured response from an AI agent."""

    agent_type: str = Field(description="Type of agent that generated this response")
    confidence: ConfidenceLevel = Field(description="Confidence in the response")
    content: str = Field(description="Main response content")
    metadata: dict[str, Any] | None = Field(None, description="Additional metadata")
    reasoning: str | None = Field(None, description="Explanation of the agent's reasoning")
    suggestions: list[ActionSuggestion] | None = Field(None, description="Actionable suggestions")


class ParsedWorkbookElement(BaseModel):
    element_identifier: str
    element_index: int
    element_type: Literal["hda", "child_collection"]
    object: ParsedWorkbookHda | ParsedWorkbookCollection


class UserQuota(BaseModel):
    model_class: str = Field(description="The name of the database model class.")
    user: UserModel = Field(description="Information about a user associated with a quota.")


class EncodedJobDetails(BaseModel):
    command_line: str | None = Field(
        None,
        description="The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.",
    )
    command_version: str | None = Field(None, description="Tool version indicated during job execution.")
    copied_from_job_id: str | None = Field(None, description="Reference to cached job if job execution was cached.")
    create_time: str = Field(description="The time and date this item was created.")
    exit_code: int | None = Field(
        None, description="The exit code returned by the tool. Can be unset if the job is not completed yet."
    )
    external_id: str | None = Field(
        None,
        description="The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value.",
    )
    galaxy_version: str | None = Field(None, description="The (major) version of Galaxy used to create this job.")
    handler: str | None = Field(
        None, description="The job handler process assigned to handle this job. Only administrator can see this value."
    )
    history_id: str | None = Field(None, description="The encoded ID of the history associated with this item.")
    id: str
    inputs: dict[str, Any] | None = Field(
        None, description="Dictionary mapping all the tool inputs (by name) to the corresponding data references."
    )
    job_runner_name: str | None = Field(
        None, description="Name of the job runner plugin that handles this job. Only administrator can see this value."
    )
    model_class: str = Field(description="The name of the database model class.")
    output_collections: dict[str, Any] | None = Field(None, description="")
    outputs: dict[str, Any] | None = Field(
        None, description="Dictionary mapping all the tool outputs (by name) to the corresponding data references."
    )
    params: Any = Field(
        description="Object containing all the parameters of the tool associated with this job. The specific parameters depend on the tool itself."
    )
    state: JobState = Field(description="Current state of the job.")
    tool_id: str = Field(description="Identifier of the tool that generated this job.")
    update_time: str = Field(description="The last time and date this item was updated.")
    user_email: str | None = Field(
        None,
        description="The email of the user that owns this job. Only the owner of the job and administrators can see this value.",
    )
    user_id: str | None = Field(None, description="User ID of user that ran this job")


class TourDetails(BaseModel):
    description: str = Field(description="Tour description")
    name: str = Field(description="Name of tour")
    requirements: list[Requirement] = Field(description="Requirements to run the tour.")
    steps: list[TourStep] = Field(description="Tour steps")
    tags: list[str] = Field(description="Topic topic tags")
    title_default: str | None = Field(None, description="Default title for each step")


class JobInputAssociation(BaseModel):
    dataset: EncodedDataItemSourceId = Field(description="Reference to the associated item.")
    name: str = Field(description="Name of the job input parameter.")


class NotificationCategorySettings(BaseModel):
    """The settings for a notification category."""

    channels: NotificationChannelSettings | None = Field(
        None, description="The channels that the user wants to receive notifications from for this category."
    )
    enabled: bool | None = Field(None, description="Whether the user wants to receive notifications for this category.")


class CreateMetricsPayload(BaseModel):
    metrics: list[Metric] | None = None


class TemplateVariablePathComponent(BaseModel):
    default: str | None = None
    help: str | None
    label: str | None = None
    name: str
    type: str
    validators: (
        list[RegexParameterValidatorModel | InRangeParameterValidatorModel | LengthParameterValidatorModel] | None
    ) = None


class UserConcreteObjectStoreModel(BaseModel):
    active: bool
    badges: list[BadgeDict]
    description: str | None = None
    device: str | None = None
    hidden: bool
    name: str | None = None
    object_expires_after_days: int | None = None
    object_store_id: str | None = None
    private: bool
    purged: bool
    quota: QuotaModel
    secrets: list[str]
    template_id: str
    template_version: int
    type: Literal["aws_s3", "azure_blob", "boto3", "disk", "generic_s3", "onedata", "rucio", "irods"]
    uuid: str
    variables: dict[str, Any] | None


class ArchivedHistoryDetailed(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    archived: bool = Field(description="Whether this item has been archived and is no longer active.")
    contents_url: str = Field(description="The relative URL to access the contents of this History.")
    count: int = Field(description="The number of items in the history.")
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    export_record_data: ExportRecordData | None = Field(
        None, description="The export record data associated with this archived history. Used to recover the history."
    )
    genome_build: str | None = Field(None, description="TODO")
    id: str
    importable: bool = Field(description="Whether this History can be imported by other users with a shared link.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the history.")
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    published: bool = Field(description="Whether this resource is currently publicly available to all users.")
    purged: bool = Field(description="Whether this item has been permanently removed.")
    size: int = Field(description="The total size of the contents of this history in bytes.")
    slug: str | None = Field(
        None, description="Part of the URL to uniquely identify this History by link in a readable way."
    )
    state: DatasetState = Field(
        description="The current state of the History based on the states of the datasets it contains."
    )
    state_details: dict[str, Any] = Field(
        description="A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states."
    )
    state_ids: dict[str, Any] = Field(
        description="A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state."
    )
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    update_time: str = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    user_id: str | None = Field(None, description="The encoded ID of the user that owns this History.")
    username: str | None = Field(None, description="Owner of the history")
    username_and_slug: str | None = Field(None, description="The relative URL in the form of /u/{username}/h/{slug}")


class HdcaDataItemsFromTarget(BaseModel):
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    column_definitions: list[SampleSheetColumnDefinition] | None = None
    destination: HdcaDestination
    ftp_path: str | None = None
    items_from: ElementsFromType
    name: str | None = None
    path: str | None = None
    server_dir: str | None = None
    src: ItemsFromSrc
    tags: list[str] | None = None
    url: str | None = None


class PrepareStoreDownloadPayload(BaseModel):
    bco_merge_history_metadata: bool | None = Field(
        None, description="When reading tags/annotations to generate BCO object include history metadata."
    )
    bco_override_algorithmic_error: dict[str, Any] | None = Field(
        None, description="Override algorithmic error for 'error domain' when generating BioCompute object."
    )
    bco_override_empirical_error: dict[str, Any] | None = Field(
        None, description="Override empirical error for 'error domain' when generating BioCompute object."
    )
    bco_override_environment_variables: dict[str, Any] | None = Field(
        None, description="Override environment variables for 'execution_domain' when generating BioCompute object."
    )
    bco_override_xref: list[XrefItem] | None = Field(
        None, description="Override xref for 'description domain' when generating BioCompute object."
    )
    include_deleted: bool | None = Field(
        None, description="Include file contents for deleted datasets (if include_files is True)."
    )
    include_files: bool | None = Field(None, description="include materialized files in export when available")
    include_hidden: bool | None = Field(
        None, description="Include file contents for hidden datasets (if include_files is True)."
    )
    model_store_format: ModelStoreFormat | None = Field(None, description="format of model store to export")


class HistoryContentBulkOperationPayload(BaseModel):
    items: list[HistoryContentItem] | None = None
    operation: HistoryContentItemOperation
    params: ChangeDatatypeOperationParams | ChangeDbkeyOperationParams | TagOperationParams | None = None


class JobOutputAssociation(BaseModel):
    dataset: EncodedDataItemSourceId = Field(description="Reference to the associated item.")
    name: str = Field(description="Name of the job output parameter.")


class FilesSourcePlugin(BaseModel):
    browsable: bool = Field(description="Whether this file source plugin can list items.")
    doc: str | None = Field(None, description="Documentation or extended description for this plugin.")
    id: str = Field(description="The `FilesSource` plugin identifier")
    label: str = Field(description="The display label for this plugin.")
    requires_groups: str | None = Field(
        None, description="Only users belonging to the groups specified here can access this files source."
    )
    requires_roles: str | None = Field(
        None, description="Only users with the roles specified here can access this files source."
    )
    supports: FilesSourceSupports | None = Field(None, description="Features supported by this file source.")
    type: str = Field(description="The type of the plugin.")
    url: str | None = Field(
        None, description="Optional URL that might be provided by some plugins to link to the remote source."
    )
    writable: bool = Field(description="Whether this files source plugin allows write access.")


class AddStepAction(BaseModel):
    """Add a new action to the workflow.

    After the workflow is updated, an order_index will be assigned
    and this step may cause other steps to have their output_index
    adjusted."""

    action_type: str
    label: str | None = Field(
        None,
        description="A unique label for the step being added, must be distinct from the labels already present in the workflow.",
    )
    position: Position | None = Field(None, description="The location of the step in the Galaxy workflow editor.")
    tool_state: dict[str, Any] | None = None
    type: str = Field(description="Module type of the step to add, see galaxy.workflow.modules for available types.")


class ExtractUntypedParameter(BaseModel):
    action_type: str
    label: str | None = None
    name: str
    position: Position | None = None


class IncomingToolOutputDataset(BaseModel):
    discover_datasets: list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None = (
        None
    )
    format: str | None = Field(None, description="The short name for the output datatype.")
    format_source: str | None = Field(
        None,
        description="This sets the data type of the output dataset(s) to be the same format as that of the specified tool input.",
    )
    from_work_dir: str | None = Field(
        None,
        description="Relative path to a file produced by the tool in its working directory. Output’s contents are set to this file’s contents.",
    )
    hidden: bool | None = Field(None, description="If true, the output will not be shown in the history.")
    label: str | None = Field(None, description="Output label. Will be used as dataset name in history.")
    metadata_source: str | None = Field(
        None,
        description="This copies the metadata information from the tool’s input dataset to serve as default for information that cannot be detected from the output. One prominent use case is interval data with a non-standard column order that cannot be deduced from a header line, but which is known to be identical in the input and output datasets.",
    )
    name: str | None = Field(None, description="Parameter name. Used when referencing parameter in workflows.")
    precreate_directory: bool | None = None
    type: str


class AsyncFile(BaseModel):
    storage_request_id: str
    task: AsyncTaskResultSummary


class RemoteFile(BaseModel):
    class_: str
    ctime: str = Field(description="The creation time of the file.")
    hashes: list[RemoteFileHash] | None = Field(
        None, description="List of precomputed hashes for the file, if available."
    )
    name: str = Field(description="The name of the entry.")
    path: str = Field(description="The path of the entry.")
    size: int = Field(description="The size of the file in bytes.")
    uri: str = Field(description="The URI of the entry.")


class SubworkflowStep(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    id: int = Field(
        description="The identifier of the step. It matches the index order of the step inside the workflow."
    )
    input_steps: dict[str, Any] = Field(
        description="A dictionary containing information about the inputs connected to this workflow step."
    )
    tool_id: str | None = Field(None, description="The unique name of the tool associated with this step.")
    tool_inputs: Any | None = Field(None, description="TODO")
    tool_uuid: str | None = Field(
        None,
        description="The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.",
    )
    tool_version: str | None = Field(None, description="The version of the tool associated with this step.")
    type: str
    when: str | None
    workflow_id: str = Field(description="The encoded ID of the workflow that will be run on this step.")


class Service(BaseModel):
    contactUrl: str | None = Field(
        None,
        description="URL of the contact for the provider of this service, e.g. a link to a contact form (RFC 3986 format), or an email (RFC 2368 format).",
    )
    createdAt: str | None = Field(
        None, description="Timestamp describing when the service was first deployed and available (RFC 3339 format)"
    )
    description: str | None = Field(
        None,
        description="Description of the service. Should be human readable and provide information about the service.",
    )
    documentationUrl: str | None = Field(
        None,
        description="URL of the documentation of this service (RFC 3986 format). This should help someone learn how to use your service, including any specifics required to access data, e.g. authentication.",
    )
    environment: str | None = Field(
        None,
        description="Environment the service is running in. Use this to distinguish between production, development and testing/staging deployments. Suggested values are prod, test, dev, staging. However this is advised and not enforced.",
    )
    id: str = Field(
        description="Unique ID of this service. Reverse domain name notation is recommended, though not required. The identifier should attempt to be globally unique so it can be used in downstream aggregator services e.g. Service Registry."
    )
    name: str = Field(description="Name of this service. Should be human readable.")
    organization: Galaxy_schema_drs_Organization = Field(description="Organization providing the service")
    type: ServiceType
    updatedAt: str | None = Field(
        None, description="Timestamp describing when the service was last updated (RFC 3339 format)"
    )
    version: str = Field(
        description="Version of the service being described. Semantic versioning is recommended, but other identifiers, such as dates or commit hashes, are also allowed. The version should be changed whenever the service is updated."
    )


class UpdateStepPositionAction(BaseModel):
    action_type: str
    position_shift: Position
    step: StepReferenceByOrderIndex | StepReferenceByLabel = Field(description="The target step for this action.")


class CollectionElementDataRequestUri(BaseModel):
    class_: str
    created_from_basename: str | None = None
    dbkey: str | None = None
    deferred: bool | None = None
    ext: str
    hashes: list[FileHash] | None = None
    identifier: str = Field(description="A unique identifier for this element within the collection.")
    info: str | None = None
    location: str
    name: str | None = None
    space_to_tab: bool | None = None
    src: None | None = None
    tags: list[str] | None = None
    to_posix_lines: bool | None = None


class ServiceCredentialGroupResponse(BaseModel):
    id: str = Field(description="Encoded ID of the credential group.")
    name: str = Field(description="The name of the credential group.")
    secrets: list[SecretResponse]
    update_time: str = Field(description="The last time the credential group was updated.")
    variables: list[VariableResponse]


class VisualizationShowResponse(BaseModel):
    annotation: str | None = Field(None, description="The annotation of this Visualization.")
    dbkey: str | None = Field(None, description="The database key of the visualization.")
    email_hash: str = Field(description="The hash of the email of the user owning this Visualization.")
    id: str = Field(description="Encoded ID of the Visualization.")
    latest_revision: VisualizationRevisionResponse = Field(description="The latest revision of this Visualization.")
    model_class: str = Field(description="The name of the database model class.")
    plugin: VisualizationPluginResponse | None = Field(None, description="The plugin of this Visualization.")
    revisions: list[str] = Field(description="A list of encoded IDs of the revisions of this Visualization.")
    slug: str | None = Field(None, description="The slug of the visualization.")
    tags: list[str] | None = Field(None, description="A list of tags to add to this item.")
    title: str = Field(description="The name of the visualization.")
    type: str = Field(description="The type of the visualization.")
    url: str = Field(description="The URL of the visualization.")
    user_id: str = Field(description="The ID of the user owning this Visualization.")
    username: str = Field(description="The name of the user owning this Visualization.")


class BroadcastNotificationContent(BaseModel):
    action_links: list[ActionLink] | None = Field(
        None, description="The optional action links (buttons) to be displayed in the notification."
    )
    category: str | None = None
    message: str = Field(description="The message of the notification (supports Markdown).")
    subject: str = Field(description="The subject of the notification.")


class UpdateReportAction(BaseModel):
    action_type: str
    report: Report


class StorageItemsCleanupResult(BaseModel):
    errors: list[StorageItemCleanupError]
    success_item_count: int
    total_free_bytes: int
    total_item_count: int


class UserNotificationsBatchUpdateRequest(BaseModel):
    """A batch update request specific for user notifications."""

    changes: UserNotificationUpdateRequest = Field(
        description="The changes that should be applied to the notifications. Only the fields that are set will be changed."
    )
    notification_ids: list[str] = Field(
        description="The list of encoded notification IDs of the notifications that should be updated."
    )


class DisplayApp(BaseModel):
    """Basic linked information about an application that can display certain datatypes."""

    label: str = Field(description="The label or title of the Display Application.")
    links: list[Hyperlink] = Field(description="The collection of link details for this Display Application.")


class SelectParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    multiple: bool | None = None
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    options: list[LabelValue] | None = None
    parameter_type: str | None = None
    type: str
    validators: list[NoOptionsParameterValidatorModel] | None = None


class PauseStep(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    id: int = Field(
        description="The identifier of the step. It matches the index order of the step inside the workflow."
    )
    input_steps: dict[str, Any] = Field(
        description="A dictionary containing information about the inputs connected to this workflow step."
    )
    tool_id: str | None = Field(None, description="The unique name of the tool associated with this step.")
    tool_inputs: Any | None = Field(None, description="TODO")
    tool_uuid: str | None = Field(
        None,
        description="The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.",
    )
    tool_version: str | None = Field(None, description="The version of the tool associated with this step.")
    type: str
    when: str | None


class ServiceCredentialGroupPayload(BaseModel):
    name: str = Field(description="The name of the credential group (minimum 3 characters).")
    secrets: list[CredentialPayload] = Field(description="List of secrets for this credential group.")
    variables: list[CredentialPayload] = Field(description="List of variables for this credential group.")


class HiddenParameterModel(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str
    validators: (
        list[
            LengthParameterValidatorModel
            | RegexParameterValidatorModel
            | ExpressionParameterValidatorModel
            | EmptyFieldParameterValidatorModel
        ]
        | None
    ) = None
    value: str | None


class WriteInvocationStoreToPayload(BaseModel):
    bco_merge_history_metadata: bool | None = Field(
        None, description="When reading tags/annotations to generate BCO object include history metadata."
    )
    bco_override_algorithmic_error: dict[str, Any] | None = Field(
        None, description="Override algorithmic error for 'error domain' when generating BioCompute object."
    )
    bco_override_empirical_error: dict[str, Any] | None = Field(
        None, description="Override empirical error for 'error domain' when generating BioCompute object."
    )
    bco_override_environment_variables: dict[str, Any] | None = Field(
        None, description="Override environment variables for 'execution_domain' when generating BioCompute object."
    )
    bco_override_xref: list[XrefItem] | None = Field(
        None, description="Override xref for 'description domain' when generating BioCompute object."
    )
    include_deleted: bool | None = Field(
        None, description="Include file contents for deleted datasets (if include_files is True)."
    )
    include_files: bool | None = Field(None, description="include materialized files in export when available")
    include_hidden: bool | None = Field(
        None, description="Include file contents for hidden datasets (if include_files is True)."
    )
    model_store_format: ModelStoreFormat | None = Field(None, description="format of model store to export")
    target_uri: str = Field(description="Galaxy Files URI to write mode store content to.")


class JobOutputCollectionAssociation(BaseModel):
    dataset_collection_instance: EncodedDataItemSourceId = Field(description="Reference to the associated item.")
    name: str = Field(description="Name of the job parameter.")


class SharingStatus(BaseModel):
    email_hash: str | None = Field(None, description="Encoded owner email.")
    id: str = Field(description="The encoded ID of the resource to be shared.")
    importable: bool = Field(description="Whether this resource can be published using a link.")
    published: bool = Field(description="Whether this resource is currently published.")
    title: str = Field(description="The title or name of the resource.")
    username: str | None = Field(None, description="The owner's username.")
    username_and_slug: str | None = Field(
        None, description="The relative URL in the form of /u/{username}/{resource_single_char}/{slug}"
    )
    users_shared_with: list[UserEmail] | None = Field(
        None, description="The list of encoded ids for users the resource has been shared."
    )


class TextParameterModel(BaseModel):
    area: bool | None = None
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    default_options: list[LabelValue] | None = None
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    type: str
    validators: (
        list[
            LengthParameterValidatorModel
            | RegexParameterValidatorModel
            | ExpressionParameterValidatorModel
            | EmptyFieldParameterValidatorModel
        ]
        | None
    ) = None
    value: str | None = None


class ExtractInputAction(BaseModel):
    action_type: str
    input: InputReferenceByOrderIndex | InputReferenceByLabel
    label: str | None = None
    position: Position | None = None


class DataElementsFromTarget(BaseModel):
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    destination: HdaDestination | LibraryFolderDestination | LibraryDestination
    elements_from: ElementsFromType
    ftp_path: str | None = None
    path: str | None = None
    server_dir: str | None = None
    src: ItemsFromSrc
    url: str | None = None


class CsvDialectInferenceMessage(BaseModel):
    dialect: CsvDialect
    message: str


class CreateHistoryContentPayload(BaseModel):
    collection_type: str | None = Field(
        None,
        description="The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.",
    )
    column_definitions: list[SampleSheetColumnDefinition] | None = Field(
        None, description="Specify definitions for row data if collection_type is sample_sheet"
    )
    content: str | None = Field(
        None,
        description="Depending on the `source` it can be:\n- The encoded id from the library dataset\n- The encoded id from the library folder\n- The encoded id from the HDA\n- The encoded id from the HDCA\n",
    )
    copy_elements: bool | None = Field(
        None,
        description="If the source is a collection, whether to copy child HDAs into the target history as well. Prior to the galaxy release 23.1 this defaulted to false.",
    )
    dbkey: str | None = Field(None, description="TODO")
    element_identifiers: list[CollectionElementIdentifier] | None = Field(
        None, description="List of elements that should be in the new collection."
    )
    fields: str | list[FieldDict] | None = Field(
        None,
        description="List of fields to create for this collection. Set to 'auto' to guess fields from identifiers.",
    )
    folder_id: str | None = Field(
        None,
        description="The ID of the library folder that will contain the collection. Required if `instance_type=library`.",
    )
    hide_source_items: bool | None = Field(None, description="Whether to mark the original HDAs as hidden.")
    history_id: str | None = Field(
        None, description="The ID of the history that will contain the collection. Required if `instance_type=history`."
    )
    instance_type: Literal["history", "library"] | None = Field(
        None, description="The type of the instance, either `history` (default) or `library`."
    )
    name: str | None = Field(None, description="The name of the new collection.")
    rows: dict[str, Any] | None = Field(
        None,
        description="Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet",
    )
    source: HistoryContentSource | None = Field(
        None, description="The source of the content. Can be other history element to be copied or library elements."
    )
    type: HistoryContentType | None = Field(None, description="The type of content to be created in the history.")


class ImportToolDataBundle(BaseModel):
    source: ImportToolDataBundleDatasetSource | ImportToolDataBundleUriSource


class JobOutput(BaseModel):
    label: Any = Field(description="The output label")
    value: EncodedDataItemSourceId = Field(description="The associated dataset.")


class CustomHistoryView(BaseModel):
    """History Response with all optional fields.

    It is used for serializing only specific attributes using the "keys"
    query parameter. Unfortunately, we cannot know the exact fields that
    will be requested, so we have to allow all fields to be optional."""

    annotation: str | None = Field(
        None, description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    archived: bool | None = Field(None, description="Whether this item has been archived and is no longer active.")
    contents_active: HistoryActiveContentCounts | None = Field(
        None, description="Contains the number of active, deleted or hidden items in a History."
    )
    contents_states: dict[str, Any] | None = Field(
        None,
        description="A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.",
    )
    contents_url: str | None = Field(None, description="The relative URL to access the contents of this History.")
    count: int | None = Field(None, description="The number of items in the history.")
    create_time: str | None = Field(None, description="The time and date this item was created.")
    deleted: bool | None = Field(None, description="Whether this item is marked as deleted.")
    genome_build: str | None = Field(None, description="TODO")
    id: str | None = None
    importable: bool | None = Field(
        None, description="Whether this History can be imported by other users with a shared link."
    )
    model_class: str | None = Field(None, description="The name of the database model class.")
    name: str | None = Field(None, description="The name of the history.")
    nice_size: str | None = Field(
        None, description="The total size of the contents of this history in a human-readable format."
    )
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    published: bool | None = Field(
        None, description="Whether this resource is currently publicly available to all users."
    )
    purged: bool | None = Field(None, description="Whether this item has been permanently removed.")
    size: int | None = Field(None, description="The total size of the contents of this history in bytes.")
    slug: str | None = Field(
        None, description="Part of the URL to uniquely identify this History by link in a readable way."
    )
    state: DatasetState | None = Field(
        None, description="The current state of the History based on the states of the datasets it contains."
    )
    state_details: dict[str, Any] | None = Field(
        None,
        description="A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.",
    )
    state_ids: dict[str, Any] | None = Field(
        None,
        description="A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.",
    )
    tags: list[str] | None = Field(None, description="The collection of tags associated with an item.")
    update_time: str | None = Field(None, description="The last time and date this item was updated.")
    url: str | None = Field(None, description="The relative URL to access this item.")
    user_id: str | None = Field(None, description="The encoded ID of the user that owns this History.")
    username: str | None = Field(None, description="Owner of the history")
    username_and_slug: str | None = Field(None, description="The relative URL in the form of /u/{username}/h/{slug}")


class GroupQuota(BaseModel):
    group: GroupModel = Field(description="Information about a user group associated with a quota.")
    model_class: str = Field(description="The name of the database model class.")


class ContainerRequirement(BaseModel):
    container: Container
    type: str


class SampleSheetColumnDefinitionModel(BaseModel):
    default_value: int | float | bool | str | None = None
    description: str | None = None
    name: str
    optional: bool
    restrictions: list[int | float | bool | str | None] | None = None
    suggestions: list[int | float | bool | str | None] | None = None
    type: Literal["string", "int", "float", "boolean", "element_identifier"]
    validators: (
        list[RegexParameterValidatorModel | InRangeParameterValidatorModel | LengthParameterValidatorModel] | None
    ) = None


class HelpForumSearchResponse(BaseModel):
    """Response model for the help search API endpoint.

    This model is based on the Discourse API response for the search endpoint."""

    categories: list[HelpForumCategory] | None = Field(
        None, description="The list of categories returned by the search."
    )
    grouped_search_result: HelpForumGroupedSearchResult | None = Field(None, description="The grouped search result.")
    groups: list[HelpForumGroup] | None = Field(None, description="The list of groups returned by the search.")
    posts: list[HelpForumPost] | None = Field(None, description="The list of posts returned by the search.")
    tags: list[HelpForumTag] | None = Field(None, description="The list of tags returned by the search.")
    topics: list[HelpForumTopic] | None = Field(None, description="The list of topics returned by the search.")
    users: list[HelpForumUser] | None = Field(None, description="The list of users returned by the search.")


class CwlUnionParameterModelInput(BaseModel):
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    parameter_type: str | None = None
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelInput
    ]


class DisconnectAction(BaseModel):
    action_type: str
    input: InputReferenceByOrderIndex | InputReferenceByLabel
    output: OutputReferenceByOrderIndex | OutputReferenceByLabel


class CopyDatasetsPayload(BaseModel):
    source_content: list[CopyDatasetsPayloadSourceEntry]
    target_history_ids: list[str] | None = None
    target_history_name: str | None = None


class UpdateOutputLabelAction(BaseModel):
    action_type: str
    output: OutputReferenceByOrderIndex | OutputReferenceByLabel
    output_label: str


class ToolStep(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    id: int = Field(
        description="The identifier of the step. It matches the index order of the step inside the workflow."
    )
    input_steps: dict[str, Any] = Field(
        description="A dictionary containing information about the inputs connected to this workflow step."
    )
    tool_id: str | None = Field(None, description="The unique name of the tool associated with this step.")
    tool_inputs: Any | None = Field(None, description="TODO")
    tool_uuid: str | None = Field(
        None,
        description="The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.",
    )
    tool_version: str | None = Field(None, description="The version of the tool associated with this step.")
    type: str
    when: str | None


class AgentListResponse(BaseModel):
    """Response listing available agents."""

    agents: list[AvailableAgent] = Field(description="List of available agents")
    total_count: int = Field(description="Total number of agents")


class TemplateVariableBoolean(BaseModel):
    default: bool | None = None
    help: str | None
    label: str | None = None
    name: str
    type: str
    validators: (
        list[RegexParameterValidatorModel | InRangeParameterValidatorModel | LengthParameterValidatorModel] | None
    ) = None


class AddInputAction(BaseModel):
    action_type: str
    collection_type: str | None = None
    default: Any | None = None
    label: str | None = None
    optional: bool | None = None
    position: Position | None = None
    restrict_on_connections: bool | None = None
    restrictions: list[str] | None = None
    suggestions: list[str] | None = None
    type: str


class CreateNewCollectionPayload(BaseModel):
    collection_type: str | None = Field(
        None,
        description="The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.",
    )
    column_definitions: list[SampleSheetColumnDefinition] | None = Field(
        None, description="Specify definitions for row data if collection_type is sample_sheet"
    )
    copy_elements: bool | None = Field(
        None, description="Whether to create a copy of the source HDAs for the new collection."
    )
    element_identifiers: list[CollectionElementIdentifier] | None = Field(
        None, description="List of elements that should be in the new collection."
    )
    fields: str | list[FieldDict] | None = Field(
        None,
        description="List of fields to create for this collection. Set to 'auto' to guess fields from identifiers.",
    )
    folder_id: str | None = Field(
        None,
        description="The ID of the library folder that will contain the collection. Required if `instance_type=library`.",
    )
    hide_source_items: bool | None = Field(None, description="Whether to mark the original HDAs as hidden.")
    history_id: str | None = Field(
        None, description="The ID of the history that will contain the collection. Required if `instance_type=history`."
    )
    instance_type: Literal["history", "library"] | None = Field(
        None, description="The type of the instance, either `history` (default) or `library`."
    )
    name: str | None = Field(None, description="The name of the new collection.")
    rows: dict[str, Any] | None = Field(
        None,
        description="Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet",
    )


class PluginStatus(BaseModel):
    connection: PluginAspectStatus | None = None
    oauth2_access_token_generation: PluginAspectStatus | None = None
    template_definition: PluginAspectStatus
    template_settings: PluginAspectStatus | None = None


class TemplateVariableString(BaseModel):
    default: str | None = None
    help: str | None
    label: str | None = None
    name: str
    type: str
    validators: (
        list[RegexParameterValidatorModel | InRangeParameterValidatorModel | LengthParameterValidatorModel] | None
    ) = None


class CreateLinkFeedback(BaseModel):
    messages: list[list[Any]] | None = None
    preparable_steps: list[CreateLinkStep] | None = None
    refresh: bool | None = None
    resource: str | None = None


class DatasetErrorMessage(BaseModel):
    dataset: EncodedDatasetSourceId = Field(description="The encoded ID of the dataset and its source.")
    error_message: str = Field(description="The error message returned while processing this dataset.")


class FillStepDefaultsAction(BaseModel):
    action_type: str
    step: StepReferenceByOrderIndex | StepReferenceByLabel


class ConcreteObjectStoreModel(BaseModel):
    badges: list[BadgeDict]
    description: str | None = None
    device: str | None = None
    name: str | None = None
    object_expires_after_days: int | None = None
    object_store_id: str | None = None
    private: bool
    quota: QuotaModel


class ConnectAction(BaseModel):
    action_type: str
    input: InputReferenceByOrderIndex | InputReferenceByLabel
    output: OutputReferenceByOrderIndex | OutputReferenceByLabel


class LibraryFolderContentsIndexResult(BaseModel):
    folder_contents: list[FileLibraryFolderItem | FolderLibraryFolderItem]
    metadata: LibraryFolderMetadata


class PastedDataElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    name: str | int | float | bool | None = None
    paste_content: str | int | float | bool = Field(
        description="This is the text of the content to import if the 'src' of the item is 'pasted'.\n"
    )
    row: list[int | float | bool | str | None] | None = None
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    src: str
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )


class FileRequestUri(BaseModel):
    class_: str
    created_from_basename: str | None = None
    dbkey: str | None = None
    deferred: bool | None = None
    ext: str
    hashes: list[FileHash] | None = None
    info: str | None = None
    location: str
    name: str | None = None
    space_to_tab: bool | None = None
    src: None | None = None
    tags: list[str] | None = None
    to_posix_lines: bool | None = None


class DatatypesCombinedMap(BaseModel):
    datatypes: list[str] = Field(description="List of datatypes extensions")
    datatypes_mapping: DatatypesMap = Field(
        description="Dictionaries for mapping datatype's extensions/classes with their implementation classes"
    )


class UpgradeToolAction(BaseModel):
    action_type: str
    step: StepReferenceByOrderIndex | StepReferenceByLabel = Field(description="The target step for this action.")
    tool_version: str | None = None


class InputDataStep(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    id: int = Field(
        description="The identifier of the step. It matches the index order of the step inside the workflow."
    )
    input_steps: dict[str, Any] = Field(
        description="A dictionary containing information about the inputs connected to this workflow step."
    )
    tool_id: str | None = Field(None, description="The unique name of the tool associated with this step.")
    tool_inputs: Any | None = Field(None, description="TODO")
    tool_uuid: str | None = Field(
        None,
        description="The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.",
    )
    tool_version: str | None = Field(None, description="The version of the tool associated with this step.")
    type: str
    when: str | None


class ExportObjectRequestMetadata(BaseModel):
    object_id: str
    object_type: ExportObjectType
    payload: WriteStoreToPayload | ShortTermStoreExportPayload
    user_id: str | None = None


class JobCreateResponse(BaseModel):
    task_result: AsyncTaskResultSummary
    tool_request_id: str


class InputParameterStep(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    id: int = Field(
        description="The identifier of the step. It matches the index order of the step inside the workflow."
    )
    input_steps: dict[str, Any] = Field(
        description="A dictionary containing information about the inputs connected to this workflow step."
    )
    tool_id: str | None = Field(None, description="The unique name of the tool associated with this step.")
    tool_inputs: Any | None = Field(None, description="TODO")
    tool_uuid: str | None = Field(
        None,
        description="The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.",
    )
    tool_version: str | None = Field(None, description="The version of the tool associated with this step.")
    type: str
    when: str | None


class UpdateStepLabelAction(BaseModel):
    action_type: str
    label: str = Field(description="The unique label of the step being referenced.")
    step: StepReferenceByOrderIndex | StepReferenceByLabel = Field(description="The target step for this action.")


class ToolOutputCollectionStructure(BaseModel):
    collection_type: str | None = None
    collection_type_from_rules: str | None = None
    collection_type_source: str | None = None
    discover_datasets: list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None = (
        None
    )
    structured_like: str | None = None


class DatasetStorageDetails(BaseModel):
    badges: list[BadgeDict] = Field(
        description="A list of badges describing object store properties for concrete object store dataset is stored in."
    )
    dataset_state: str = Field(description="The model state of the supplied dataset instance.")
    description: str | None = Field(description="A description of how this dataset is stored.")
    hashes: list[dict[str, Any]] = Field(
        description="The file contents hashes associated with the supplied dataset instance."
    )
    name: str | None = Field(description="The display name of the destination ObjectStore for this dataset.")
    object_store_id: str | None = Field(description="The identifier of the destination ObjectStore for this dataset.")
    percent_used: float | None = Field(description="The percentage indicating how full the store is.")
    private: bool = Field(description="Indicator of whether the objectstore is marked as private.")
    quota: ConcreteObjectStoreQuotaSourceDetails = Field(
        description="Information about quota sources around dataset storage."
    )
    relocatable: bool = Field(
        description="Indicator of whether the objectstore for this dataset can be switched by this user."
    )
    shareable: bool = Field(description="Is this dataset shareable.")
    sources: list[dict[str, Any]] = Field(description="The file sources associated with the supplied dataset instance.")


class DeleteDatasetBatchPayload(BaseModel):
    datasets: list[DatasetSourceId] = Field(
        description="The list of datasets IDs with their sources to be deleted/purged."
    )
    purge: bool | None = Field(
        None,
        description="Whether to permanently delete from disk the specified datasets. *Warning*: this is a destructive operation.",
    )


class ArchivedHistorySummary(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    archived: bool = Field(description="Whether this item has been archived and is no longer active.")
    count: int = Field(description="The number of items in the history.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    export_record_data: ExportRecordData | None = Field(
        None, description="The export record data associated with this archived history. Used to recover the history."
    )
    id: str
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the history.")
    preferred_object_store_id: str | None = Field(
        None, description="The ID of the object store that should be used to store new datasets in this history."
    )
    published: bool = Field(description="Whether this resource is currently publicly available to all users.")
    purged: bool = Field(description="Whether this item has been permanently removed.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    update_time: str = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")


class PathDataElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    link_data_only: bool | None = None
    name: str | int | float | bool | None = None
    path: str
    row: list[int | float | bool | str | None] | None = None
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    src: str
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )


class ToolRequestDetailedModel(BaseModel):
    id: str = Field(description="Encoded ID of the role")
    implicit_collections: list[ToolRequestImplicitCollectionReference] | None = None
    jobs: list[ToolRequestJobReference] | None = None
    request: dict[str, Any]
    state: ToolRequestState
    state_message: str | None


class DatasetSource(BaseModel):
    extra_files_path: str | None = Field(None, description="The path to the extra files.")
    id: str = Field(description="Encoded ID of the dataset source.")
    source_uri: str = Field(description="The URI of the dataset source.")
    transform: list[DatasetSourceTransform] | None = Field(
        None, description="The transformations applied to the dataset source."
    )


class ServiceCredentialsDefinition(BaseModel):
    description: str = Field(description="A description of the service.")
    label: str | None = Field(None, description="A human-readable label for the service.")
    name: str = Field(description="The name of the service.")
    optional: bool = Field(
        description="If true, tools can run without credentials; if false, credentials must be provided before execution."
    )
    secrets: list[ServiceParameterDefinition]
    variables: list[ServiceParameterDefinition]
    version: str = Field(description="The version of the service.")


class BrowsableFilesSourcePlugin(BaseModel):
    browsable: bool
    doc: str | None = Field(None, description="Documentation or extended description for this plugin.")
    id: str = Field(description="The `FilesSource` plugin identifier")
    label: str = Field(description="The display label for this plugin.")
    requires_groups: str | None = Field(
        None, description="Only users belonging to the groups specified here can access this files source."
    )
    requires_roles: str | None = Field(
        None, description="Only users with the roles specified here can access this files source."
    )
    supports: FilesSourceSupports | None = Field(None, description="Features supported by this file source.")
    type: str = Field(description="The type of the plugin.")
    uri_root: str = Field(description="The URI root used by this type of plugin.")
    url: str | None = Field(
        None, description="Optional URL that might be provided by some plugins to link to the remote source."
    )
    writable: bool = Field(description="Whether this files source plugin allows write access.")


class UpgradeSubworkflowAction(BaseModel):
    action_type: str
    content_id: str | None = None
    step: StepReferenceByOrderIndex | StepReferenceByLabel = Field(description="The target step for this action.")


class SelectServiceCredentialPayload(BaseModel):
    service_credentials: list[SelectCurrentGroupPayload] = Field(
        description="List of user credentials to update with current group selections."
    )
    source_id: str = Field(description="The ID of the source (e.g., tool ID).")
    source_type: str = Field(description="The type of source requiring credentials.")
    source_version: str = Field(description="The version of the source.")


class SplitUpPairedDataLogEntry(BaseModel):
    message: str
    new_paired_status_column: int
    old_forward_column: ParsedColumn
    old_reverse_column: ParsedColumn


class ShareWithStatus(BaseModel):
    email_hash: str | None = Field(None, description="Encoded owner email.")
    errors: list[str] | None = Field(
        None,
        description="Collection of messages indicating that the resource was not shared with some (or all users) due to an error.",
    )
    extra: ShareWithExtra | None = Field(
        None,
        description="Optional extra information about this shareable resource that may be of interest. The contents of this field depend on the particular resource.",
    )
    id: str = Field(description="The encoded ID of the resource to be shared.")
    importable: bool = Field(description="Whether this resource can be published using a link.")
    published: bool = Field(description="Whether this resource is currently published.")
    title: str = Field(description="The title or name of the resource.")
    username: str | None = Field(None, description="The owner's username.")
    username_and_slug: str | None = Field(
        None, description="The relative URL in the form of /u/{username}/{resource_single_char}/{slug}"
    )
    users_shared_with: list[UserEmail] | None = Field(
        None, description="The list of encoded ids for users the resource has been shared."
    )


class ShareHistoryExtra(BaseModel):
    accessible_count: int | None = Field(
        None, description="The number of datasets in the history that are public or accessible by all the target users."
    )
    can_change: list[HDABasicInfo] | None = Field(
        None,
        description="A collection of datasets that are not accessible by one or more of the target users and that can be made accessible for others by the user sharing the history.",
    )
    can_share: bool | None = Field(
        None, description="Indicates whether the resource can be directly shared or requires further actions."
    )
    cannot_change: list[HDABasicInfo] | None = Field(
        None,
        description="A collection of datasets that are not accessible by one or more of the target users and that cannot be made accessible for others by the user sharing the history.",
    )


class DrsObject(BaseModel):
    access_methods: list[AccessMethod] | None = Field(
        None,
        description="The list of access methods that can be used to fetch the `DrsObject`.\nRequired for single blobs; optional for bundles.",
    )
    aliases: list[str] | None = Field(
        None,
        description="A list of strings that can be used to find other metadata about this `DrsObject` from external metadata sources. These aliases can be used to represent secondary accession numbers or external GUIDs.",
    )
    checksums: list[Checksum] = Field(
        description="The checksum of the `DrsObject`. At least one checksum must be provided.\nFor blobs, the checksum is computed over the bytes in the blob.\nFor bundles, the checksum is computed over a sorted concatenation of the checksums of its top-level contained objects (not recursive, names not included). The list of checksums is sorted alphabetically (hex-code) before concatenation and a further checksum is performed on the concatenated checksum value.\nFor example, if a bundle contains blobs with the following checksums:\nmd5(blob1) = 72794b6d\nmd5(blob2) = 5e089d29\nThen the checksum of the bundle is:\nmd5( concat( sort( md5(blob1), md5(blob2) ) ) )\n= md5( concat( sort( 72794b6d, 5e089d29 ) ) )\n= md5( concat( 5e089d29, 72794b6d ) )\n= md5( 5e089d2972794b6d )\n= f7a29a04"
    )
    contents: list[ContentsObject] | None = Field(
        None,
        description="If not set, this `DrsObject` is a single blob.\nIf set, this `DrsObject` is a bundle containing the listed `ContentsObject` s (some of which may be further nested).",
    )
    created_time: str = Field(
        description="Timestamp of content creation in RFC3339.\n(This is the creation time of the underlying content, not of the JSON object.)"
    )
    description: str | None = Field(None, description="A human readable description of the `DrsObject`.")
    id: str = Field(description="An identifier unique to this `DrsObject`")
    mime_type: str | None = Field(None, description="A string providing the mime-type of the `DrsObject`.")
    name: str | None = Field(
        None,
        description="A string that can be used to name a `DrsObject`.\nThis string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames].",
    )
    self_uri: str = Field(
        description="A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object.\nThe intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around.  For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the `self_uri` presents you with a hostname and properly encoded DRS ID for use in subsequent `access` endpoint calls."
    )
    size: int = Field(
        description="For blobs, the blob size in bytes.\nFor bundles, the cumulative size, in bytes, of items in the `contents` field."
    )
    updated_time: str | None = Field(
        None,
        description="Timestamp of content update in RFC3339, identical to `created_time` in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.)",
    )
    version: str | None = Field(
        None,
        description="A string representing a version.\n(Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.)",
    )


class ParsedFetchWorkbookForCollections(BaseModel):
    collection_type: Literal["list", "list:paired", "list:list", "list:list:paired", "list:paired_or_unpaired"]
    columns: list[ParsedColumn]
    parse_log: list[
        SplitUpPairedDataLogEntry
        | InferredCollectionTypeLogEntry
        | InferredColumnMapping
        | ContentTypeMessage
        | CsvDialectInferenceMessage
    ]
    rows: list[dict[str, Any]]
    workbook_type: Literal["datasets", "collection", "collections"] | None = None


class StoredWorkflowDetailed(BaseModel):
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    annotations: list[str] | None = Field(
        None,
        description="An list of annotations to provide details or to help understand the purpose and usage of this workflow.",
    )
    create_time: str = Field(description="The time and date this item was created.")
    creator: list[Person | Galaxy_schema_schema_Organization] | None = Field(
        None, description="Additional information about the creator (or multiple creators) of this workflow."
    )
    creator_deleted: bool = Field(description="Whether the creator of this Workflow has been deleted.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    doi: list[str] | None = Field(
        None, description="A list of Digital Object Identifiers associated with this workflow."
    )
    email_hash: str | None = Field(description="The hash of the email of the creator of this workflow")
    help: str | None = Field(
        description="The detailed help text for how to use the workflow and debug problems with it."
    )
    hidden: bool = Field(description="TODO")
    id: str
    importable: bool | None = Field(description="Indicates if the workflow is importable by the current user.")
    inputs: dict[str, Any] | None = Field(
        None, description="A dictionary containing information about all the inputs of the workflow."
    )
    latest_workflow_uuid: str | None = Field(None, description="TODO")
    license: str | None = Field(None, description="SPDX Identifier of the license associated with this workflow.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the history.")
    number_of_steps: int | None = Field(None, description="The number of steps that make up this workflow.")
    owner: str = Field(description="The name of the user who owns this workflow.")
    published: bool = Field(description="Whether this workflow is currently publicly available to all users.")
    readme: str | None = Field(description="The detailed markdown readme of the workflow.")
    show_in_tool_panel: bool | None = Field(None, description="Whether to display this workflow in the Tools Panel.")
    slug: str | None = Field(description="The slug of the workflow.")
    source_metadata: dict[str, Any] | None = Field(description="The source metadata of the workflow.")
    steps: dict[str, Any] | None = Field(
        None, description="A dictionary with information about all the steps of the workflow."
    )
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    update_time: str = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    version: int = Field(description="The version of the workflow represented by an incremental number.")


class CreateWorkbookForCollectionApi(BaseModel):
    column_definitions: list[SampleSheetColumnDefinitionModel] = Field(
        description="A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'"
    )
    prefix_values: list[list[int | float | bool | str | None]] | None = Field(
        None, description="An area to pre-populate URIs, etc..."
    )


class QuotaDetails(BaseModel):
    bytes: int = Field(description="The amount, expressed in bytes, of this Quota.")
    default: list[DefaultQuota] | None = Field(
        None,
        description="A list indicating which types of default user quotas, if any, are associated with this quota.",
    )
    description: str = Field(description="Detailed text description for this Quota.")
    display_amount: str = Field(description="Human-readable representation of the `amount` field.")
    groups: list[GroupQuota] | None = Field(
        None, description="A list of specific groups of users associated with this quota."
    )
    id: str = Field(description="The `encoded identifier` of the quota.")
    model_class: str = Field(description="The name of the database model class.")
    name: str = Field(description="The name of the quota. This must be unique within a Galaxy instance.")
    operation: QuotaOperation | None = Field(
        None,
        description="Quotas can have one of three `operations`:- `=` : The quota is exactly the amount specified- `+` : The amount specified will be added to the amounts of the user's other associated quota definitions- `-` : The amount specified will be subtracted from the amounts of the user's other associated quota definitions",
    )
    quota_source_label: str | None = Field(None, description="Quota source label")
    users: list[UserQuota] | None = Field(None, description="A list of specific users associated with this quota.")


class HDACustom(BaseModel):
    """Can contain any serializable property of an HDA.

    Allows arbitrary custom keys to be specified in the serialization
    parameters without a particular view (predefined set of keys)."""

    accessible: bool | None = Field(
        None, description="Whether this item is accessible to the current user due to permissions."
    )
    annotation: str | None = Field(
        None, description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    api_type: str | None = Field(None, description="TODO")
    copied_from_history_dataset_association_id: str | None = Field(
        None, description="ID of HDA this HDA was copied from."
    )
    copied_from_ldda_id: str | None = None
    copied_from_library_dataset_dataset_association_id: str | None = Field(
        None, description="ID of LDDA this HDA was copied from."
    )
    create_time: str | None = Field(None, description="The time and date this item was created.")
    created_from_basename: str | None = Field(
        None, description="The basename of the output that produced this dataset."
    )
    creating_job: str | None = Field(None, description="The encoded ID of the job that created this dataset.")
    data_type: str | None = Field(
        None, description="The fully qualified name of the class implementing the data type of this dataset."
    )
    dataset_id: str | None = Field(None, description="The encoded ID of the dataset associated with this item.")
    deleted: bool | None = Field(None, description="Whether this item is marked as deleted.")
    display_apps: list[DisplayApp] | None = Field(None, description="Contains new-style display app urls.")
    display_types: list[DisplayApp] | None = Field(None, description="Contains old-style display app urls.")
    download_url: str | None = Field(None, description="The URL to download this item from the server.")
    drs_id: str | None = Field(None, description="The DRS ID of the dataset.")
    extension: str | None = Field(None, description="The extension of the dataset.")
    file_ext: str | None = Field(None, description="The extension of the file.")
    file_name: str | None = Field(None, description="The full path to the dataset file.")
    file_size: int | None = Field(None, description="The file size in bytes.")
    genome_build: str | None = Field(None, description="TODO")
    hashes: list[DatasetHash] | None = Field(None, description="The list of hashes associated with this dataset.")
    hda_ldda: DatasetSourceType | None = Field(
        None, description="Whether this dataset belongs to a history (HDA) or a library (LDDA)."
    )
    hid: int | None = Field(None, description="The index position of this item in the History.")
    history_content_type: str | None = Field(None, description="This is always `dataset` for datasets.")
    history_id: str | None = None
    id: str | None = None
    meta_files: list[MetadataFile] | None = Field(
        None, description="Collection of metadata files associated with this dataset."
    )
    metadata: Any | None = Field(None, description="The metadata associated with this dataset.")
    misc_blurb: str | None = Field(None, description="TODO")
    misc_info: str | None = Field(None, description="TODO")
    model_class: str | None = Field(None, description="The name of the database model class.")
    name: str | None = Field(None, description="The name of the item.")
    object_store_id: str | None = Field(None, description="The ID of the object store that this dataset is stored in.")
    peek: str | None = Field(None, description="A few lines of contents from the start of the file.")
    permissions: DatasetPermissions | None = Field(
        None, description="Role-based access and manage control permissions for the dataset."
    )
    purged: bool | None = Field(None, description="Whether this dataset has been removed from disk.")
    rerunnable: bool | None = Field(None, description="Whether the job creating this dataset can be run again.")
    resubmitted: bool | None = Field(None, description="Whether the job creating this dataset has been resubmitted.")
    sources: list[DatasetSource] | None = Field(None, description="The list of sources associated with this dataset.")
    state: DatasetState | None = Field(None, description="The current state of this dataset.")
    tags: list[str] | None = Field(None, description="The collection of tags associated with an item.")
    type: str | None = Field(None, description="This is always `file` for datasets.")
    type_id: str | None = Field(None, description="The type and the encoded ID of this item. Used for caching.")
    update_time: str | None = Field(None, description="The last time and date this item was updated.")
    url: str | None = Field(None, description="The relative URL to access this item.")
    uuid: str | None = None
    validated_state: DatasetValidatedState | None = Field(
        None, description="The state of the datatype validation for this dataset."
    )
    validated_state_message: str | None = Field(
        None, description="The message with details about the datatype validation result for this dataset."
    )
    visible: bool | None = Field(None, description="Whether this item is visible or hidden to the user by default.")
    visualizations: list[Visualization] | None = Field(
        None, description="The collection of visualizations that can be applied to this dataset."
    )


class UserNotificationPreferences(BaseModel):
    """Contains the full notification preferences of a user."""

    preferences: dict[str, Any] = Field(description="The notification preferences of the user.")


class CollectionElementCollectionRequestUri(BaseModel):
    class_: str
    collection_type: str
    elements: list[CollectionElementCollectionRequestUri | CollectionElementDataRequestUri]
    identifier: str = Field(description="A unique identifier for this element within the collection.")


class HistoryContentBulkOperationResult(BaseModel):
    errors: list[BulkOperationItemError]
    success_count: int


class AgentQueryResponse(BaseModel):
    """Response from an AI agent query."""

    processing_time: float | None = Field(None, description="Time taken to process the query in seconds")
    response: AgentResponse = Field(description="The agent's response")
    routing_info: dict[str, Any] | None = Field(None, description="Information about how the query was routed")


class DeleteDatasetBatchResult(BaseModel):
    errors: list[DatasetErrorMessage] | None = Field(
        None,
        description="A list of dataset IDs and the corresponding error message if something went wrong while processing the dataset.",
    )
    success_count: int = Field(description="The number of datasets successfully processed.")


class RefactorActionExecution(BaseModel):
    action: (
        AddInputAction
        | AddStepAction
        | ConnectAction
        | DisconnectAction
        | ExtractInputAction
        | ExtractUntypedParameter
        | FileDefaultsAction
        | FillStepDefaultsAction
        | UpdateAnnotationAction
        | UpdateCreatorAction
        | UpdateNameAction
        | UpdateLicenseAction
        | UpdateOutputLabelAction
        | UpdateReportAction
        | UpdateStepLabelAction
        | UpdateStepPositionAction
        | UpgradeSubworkflowAction
        | UpgradeToolAction
        | UpgradeAllStepsAction
        | RemoveUnlabeledWorkflowOutputs
    )
    messages: list[RefactorActionExecutionMessage]


class ParseWorkbookForCollectionApi(BaseModel):
    column_definitions: list[SampleSheetColumnDefinitionModel] = Field(
        description="A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'"
    )
    content: str = Field(
        description="The workbook content (the contents of the xlsx file) that have been base64 encoded."
    )


class CompositeItems(BaseModel):
    elements: list[
        FileDataElement | PastedDataElement | UrlDataElement | PathDataElement | ServerDirElement | FtpImportElement
    ]


class IncomingToolOutputCollectionOutput(BaseModel):
    hidden: bool | None = Field(None, description="If true, the output will not be shown in the history.")
    label: str | None = Field(None, description="Output label. Will be used as dataset name in history.")
    name: str | None = Field(None, description="Parameter name. Used when referencing parameter in workflows.")
    structure: ToolOutputCollectionStructure
    type: str


class UpdateUserNotificationPreferencesRequest(BaseModel):
    """Contains the new notification preferences of a user."""

    preferences: dict[str, Any] = Field(description="The new notification preferences of the user.")


class GenerateTourResponse(BaseModel):
    tour: TourDetails = Field(description="The actual Tour being generated.")
    uploaded_hids: list[int] = Field(description="List of hids for the datasets uploaded for the tour.")
    use_datasets: bool = Field(description="Indicates whether the tour should use (and wait for) datasets.")


class ObjectStoreTemplateSummary(BaseModel):
    badges: list[BadgeDict]
    description: str | None
    hidden: bool | None = None
    id: str
    name: str | None
    secrets: list[TemplateSecret] | None = None
    type: Literal["aws_s3", "azure_blob", "boto3", "disk", "generic_s3", "onedata", "rucio", "irods"]
    variables: (
        list[TemplateVariableString | TemplateVariableInteger | TemplateVariablePathComponent | TemplateVariableBoolean]
        | None
    ) = None
    version: int | None = None


class ExportObjectMetadata(BaseModel):
    request_data: ExportObjectRequestMetadata
    result_data: ExportObjectResultMetadata | None = None


class FileSourceTemplateSummary(BaseModel):
    description: str | None
    hidden: bool | None = None
    id: str
    name: str | None
    secrets: list[TemplateSecret] | None = None
    type: Literal[
        "ftp",
        "posix",
        "s3fs",
        "azure",
        "azureflat",
        "onedata",
        "webdav",
        "dropbox",
        "googledrive",
        "elabftw",
        "inveniordm",
        "zenodo",
        "rspace",
        "dataverse",
        "huggingface",
        "omero",
    ]
    variables: (
        list[TemplateVariableString | TemplateVariableInteger | TemplateVariablePathComponent | TemplateVariableBoolean]
        | None
    ) = None
    version: int | None = None


class ParsedWorkbookForCollection(BaseModel):
    elements: list[ParsedWorkbookElement]
    extra_columns: list[ParsedColumn]
    parse_log: list[InferredColumnMapping | ContentTypeMessage | CsvDialectInferenceMessage]
    rows: list[dict[str, Any]]


class IncomingToolOutputCollectionInput(BaseModel):
    hidden: bool | None = Field(None, description="If true, the output will not be shown in the history.")
    label: str | None = Field(None, description="Output label. Will be used as dataset name in history.")
    name: str | None = Field(None, description="Parameter name. Used when referencing parameter in workflows.")
    structure: ToolOutputCollectionStructure
    type: str


class RefactorRequest(BaseModel):
    actions: list[
        AddInputAction
        | AddStepAction
        | ConnectAction
        | DisconnectAction
        | ExtractInputAction
        | ExtractUntypedParameter
        | FileDefaultsAction
        | FillStepDefaultsAction
        | UpdateAnnotationAction
        | UpdateCreatorAction
        | UpdateNameAction
        | UpdateLicenseAction
        | UpdateOutputLabelAction
        | UpdateReportAction
        | UpdateStepLabelAction
        | UpdateStepPositionAction
        | UpgradeSubworkflowAction
        | UpgradeToolAction
        | UpgradeAllStepsAction
        | RemoveUnlabeledWorkflowOutputs
    ]
    dry_run: bool | None = None
    style: str | None = None


class BroadcastNotificationResponse(BaseModel):
    """A notification response specific for broadcasting."""

    category: str | None = None
    content: BroadcastNotificationContent
    create_time: str = Field(description="The time when the notification was created.")
    expiration_time: str | None = Field(
        None,
        description="The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.",
    )
    id: str = Field(description="The encoded ID of the notification.")
    publication_time: str = Field(
        description="The time when the notification was published. Notifications can be created and then published at a later time."
    )
    source: str = Field(
        description="The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'."
    )
    update_time: str = Field(description="The time when the notification was last updated.")
    variant: NotificationVariant = Field(
        description="The variant of the notification. Represents the intent or relevance of the notification. E.g. 'info' or 'urgent'."
    )


class BroadcastNotificationCreateRequest(BaseModel):
    """A notification create request specific for broadcasting."""

    category: str | None = None
    content: BroadcastNotificationContent = Field(
        description="The content of the broadcast notification. Broadcast notifications are displayed prominently to all users and can contain action links to redirect the user to a specific page."
    )
    expiration_time: str | None = Field(
        None,
        description="The time when the notification should expire. By default it will expire after 6 months. Expired notifications will be permanently deleted.",
    )
    publication_time: str | None = Field(
        None,
        description="The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.",
    )
    source: str = Field(
        description="The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'."
    )
    variant: NotificationVariant = Field(
        description="The variant of the notification. Represents the intent or relevance of the notification. E.g. 'info' or 'urgent'."
    )


class CreateWorkbookRequest(BaseModel):
    collection_type: Literal[
        "sample_sheet", "sample_sheet:paired", "sample_sheet:paired_or_unpaired", "sample_sheet:record"
    ]
    column_definitions: list[SampleSheetColumnDefinitionModel] = Field(
        description="A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'"
    )
    prefix_columns_type: str | None = None
    prefix_values: list[list[int | float | bool | str | None]] | None = None
    title: str | None = Field(None, description="A short title to give the workbook.")


class ServiceCredentialPayload(BaseModel):
    group: ServiceCredentialGroupPayload = Field(description="The credential group containing variables and secrets.")
    name: str = Field(description="The name of the service requiring credentials.")
    version: str = Field(description="The version of the service.")


class UserServiceCredentialsResponse(BaseModel):
    current_group_id: str | None = Field(None, description="The ID of the currently active credential group.")
    groups: list[ServiceCredentialGroupResponse]
    id: str = Field(description="The encoded ID of the user credentials.")
    name: str = Field(description="The name of the service requiring credentials.")
    source_id: str = Field(description="The ID of the source (e.g., tool ID).")
    source_type: str = Field(description="The type of source (e.g., 'tool').")
    source_version: str = Field(description="The version of the source.")
    user_id: str = Field(description="The ID of the user who owns these credentials.")
    version: str = Field(description="The version of the service.")


class ParsedFetchWorkbookForDatasets(BaseModel):
    columns: list[ParsedColumn]
    parse_log: list[
        SplitUpPairedDataLogEntry
        | InferredCollectionTypeLogEntry
        | InferredColumnMapping
        | ContentTypeMessage
        | CsvDialectInferenceMessage
    ]
    rows: list[dict[str, Any]]
    workbook_type: Literal["datasets", "collection", "collections"] | None = None


class JobDisplayParametersSummary(BaseModel):
    has_parameter_errors: bool = Field(description="The job has parameter errors")
    outputs: dict[str, Any] = Field(
        description="Dictionary mapping all the tool outputs (by name) with the corresponding dataset information in a nested format."
    )
    parameters: list[JobParameter] = Field(description="The parameters of the job in a nested format.")


class NotificationResponse(BaseModel):
    """Basic common fields for all notification responses."""

    category: MandatoryNotificationCategory | PersonalNotificationCategory = Field(
        description="The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'."
    )
    content: MessageNotificationContent | NewSharedItemNotificationContent | BroadcastNotificationContent = Field(
        description="The content of the notification. The structure depends on the category."
    )
    create_time: str = Field(description="The time when the notification was created.")
    expiration_time: str | None = Field(
        None,
        description="The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.",
    )
    id: str = Field(description="The encoded ID of the notification.")
    publication_time: str = Field(
        description="The time when the notification was published. Notifications can be created and then published at a later time."
    )
    source: str = Field(
        description="The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'."
    )
    update_time: str = Field(description="The time when the notification was last updated.")
    variant: NotificationVariant = Field(
        description="The variant of the notification. Represents the intent or relevance of the notification. E.g. 'info' or 'urgent'."
    )


class NotificationBroadcastUpdateRequest(BaseModel):
    """A notification update request specific for broadcasting."""

    content: BroadcastNotificationContent | None = Field(
        None,
        description="The content of the broadcast notification. Broadcast notifications are displayed prominently to all users and can contain action links to redirect the user to a specific page.",
    )
    expiration_time: str | None = Field(
        None,
        description="The time when the notification should expire. By default it will expire after 6 months. Expired notifications will be permanently deleted.",
    )
    publication_time: str | None = Field(
        None,
        description="The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.",
    )
    source: str | None = Field(
        None, description="The source of the notification. Represents the agent that created the notification."
    )
    variant: NotificationVariant | None = Field(
        None, description="The variant of the notification. Used to express the importance of the notification."
    )


class WorkflowInvocationElementView(BaseModel):
    create_time: str = Field(description="The time and date this item was created.")
    history_id: str = Field(description="The encoded ID of the history associated with the invocation.")
    id: str = Field(description="The encoded ID of the workflow invocation.")
    input_step_parameters: dict[str, Any] = Field(description="Input step parameters of the workflow invocation.")
    inputs: dict[str, Any] = Field(description="Input datasets/dataset collections of the workflow invocation.")
    landing_uuid: str | None = Field(
        None, description="The UUID of the workflow landing request associated with this invocation."
    )
    messages: list[Any] = Field(description="A list of messages about why the invocation did not succeed.")
    model_class: str = Field(description="The name of the database model class.")
    output_collections: dict[str, Any] = Field(description="Output dataset collections of the workflow invocation.")
    output_values: dict[str, Any] = Field(description="Output values of the workflow invocation.")
    outputs: dict[str, Any] = Field(description="Output datasets of the workflow invocation.")
    state: InvocationState = Field(description="State of workflow invocation.")
    steps: list[InvocationStep] = Field(description="Steps of the workflow invocation.")
    update_time: str = Field(description="The last time and date this item was updated.")
    uuid: str | None = Field(None, description="Universal unique identifier of the workflow invocation.")
    workflow_id: str = Field(description="The encoded Workflow ID associated with the invocation.")


class NotificationCreateData(BaseModel):
    """Basic common fields for all notification create requests."""

    category: MandatoryNotificationCategory | PersonalNotificationCategory = Field(
        description="The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'."
    )
    content: MessageNotificationContent | NewSharedItemNotificationContent | BroadcastNotificationContent = Field(
        description="The content of the notification. The structure depends on the category."
    )
    expiration_time: str | None = Field(
        None,
        description="The time when the notification should expire. By default it will expire after 6 months. Expired notifications will be permanently deleted.",
    )
    publication_time: str | None = Field(
        None,
        description="The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.",
    )
    source: str = Field(
        description="The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'."
    )
    variant: NotificationVariant = Field(
        description="The variant of the notification. Represents the intent or relevance of the notification. E.g. 'info' or 'urgent'."
    )


class ParsedWorkbook(BaseModel):
    extra_columns: list[ParsedColumn]
    parse_log: list[InferredColumnMapping | ContentTypeMessage | CsvDialectInferenceMessage]
    rows: list[dict[str, Any]]


class HDADetailed(BaseModel):
    """History Dataset Association detailed information."""

    accessible: bool = Field(description="Whether this item is accessible to the current user due to permissions.")
    annotation: str | None = Field(
        description="An annotation to provide details or to help understand the purpose and usage of this item."
    )
    api_type: str | None = Field(None, description="TODO")
    copied_from_history_dataset_association_id: str | None = Field(
        None, description="ID of HDA this HDA was copied from."
    )
    copied_from_ldda_id: str | None = None
    copied_from_library_dataset_dataset_association_id: str | None = Field(
        None, description="ID of LDDA this HDA was copied from."
    )
    create_time: str = Field(description="The time and date this item was created.")
    created_from_basename: str | None = Field(
        None, description="The basename of the output that produced this dataset."
    )
    creating_job: str = Field(description="The encoded ID of the job that created this dataset.")
    data_type: str = Field(
        description="The fully qualified name of the class implementing the data type of this dataset."
    )
    dataset_id: str = Field(description="The encoded ID of the dataset associated with this item.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    display_apps: list[DisplayApp] = Field(description="Contains new-style display app urls.")
    display_types: list[DisplayApp] = Field(description="Contains old-style display app urls.")
    download_url: str = Field(description="The URL to download this item from the server.")
    drs_id: str = Field(description="The DRS ID of the dataset.")
    extension: str | None = Field(description="The extension of the dataset.")
    file_ext: str = Field(description="The extension of the file.")
    file_name: str | None = Field(None, description="The full path to the dataset file.")
    file_size: int = Field(description="The file size in bytes.")
    genome_build: str | None = Field(None, description="TODO")
    hashes: list[DatasetHash] = Field(description="The list of hashes associated with this dataset.")
    hda_ldda: DatasetSourceType | None = Field(
        None, description="Whether this dataset belongs to a history (HDA) or a library (LDDA)."
    )
    hid: int = Field(description="The index position of this item in the History.")
    history_content_type: str = Field(description="This is always `dataset` for datasets.")
    history_id: str
    id: str
    meta_files: list[MetadataFile] = Field(description="Collection of metadata files associated with this dataset.")
    metadata: Any | None = Field(None, description="The metadata associated with this dataset.")
    misc_blurb: str | None = Field(None, description="TODO")
    misc_info: str | None = Field(None, description="TODO")
    model_class: str = Field(description="The name of the database model class.")
    name: str | None = Field(description="The name of the item.")
    object_store_id: str | None = Field(None, description="The ID of the object store that this dataset is stored in.")
    peek: str | None = Field(None, description="A few lines of contents from the start of the file.")
    permissions: DatasetPermissions = Field(
        description="Role-based access and manage control permissions for the dataset."
    )
    purged: bool = Field(description="Whether this dataset has been removed from disk.")
    rerunnable: bool = Field(description="Whether the job creating this dataset can be run again.")
    resubmitted: bool = Field(description="Whether the job creating this dataset has been resubmitted.")
    sources: list[DatasetSource] = Field(description="The list of sources associated with this dataset.")
    state: DatasetState = Field(description="The current state of this dataset.")
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    type: str | None = Field(None, description="This is always `file` for datasets.")
    type_id: str | None = Field(None, description="The type and the encoded ID of this item. Used for caching.")
    update_time: str | None = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    uuid: str = Field(description="Universal unique identifier for this dataset.")
    validated_state: DatasetValidatedState = Field(description="The state of the datatype validation for this dataset.")
    validated_state_message: str | None = Field(
        None, description="The message with details about the datatype validation result for this dataset."
    )
    visible: bool = Field(description="Whether this item is visible or hidden to the user by default.")


class ShareHistoryWithStatus(BaseModel):
    email_hash: str | None = Field(None, description="Encoded owner email.")
    errors: list[str] | None = Field(
        None,
        description="Collection of messages indicating that the resource was not shared with some (or all users) due to an error.",
    )
    extra: ShareHistoryExtra = Field(
        description="Optional extra information about this shareable resource that may be of interest. The contents of this field depend on the particular resource."
    )
    id: str = Field(description="The encoded ID of the resource to be shared.")
    importable: bool = Field(description="Whether this resource can be published using a link.")
    published: bool = Field(description="Whether this resource is currently published.")
    title: str = Field(description="The title or name of the resource.")
    username: str | None = Field(None, description="The owner's username.")
    username_and_slug: str | None = Field(
        None, description="The relative URL in the form of /u/{username}/{resource_single_char}/{slug}"
    )
    users_shared_with: list[UserEmail] | None = Field(
        None, description="The list of encoded ids for users the resource has been shared."
    )


class UserServiceCredentialsWithDefinitionResponse(BaseModel):
    current_group_id: str | None = Field(None, description="The ID of the currently active credential group.")
    definition: ServiceCredentialsDefinition
    groups: list[ServiceCredentialGroupResponse]
    id: str = Field(description="The encoded ID of the user credentials.")
    name: str = Field(description="The name of the service requiring credentials.")
    source_id: str = Field(description="The ID of the source (e.g., tool ID).")
    source_type: str = Field(description="The type of source (e.g., 'tool').")
    source_version: str = Field(description="The version of the source.")
    user_id: str = Field(description="The ID of the user who owns these credentials.")
    version: str = Field(description="The version of the service.")


class ParseWorkbook(BaseModel):
    collection_type: Literal[
        "sample_sheet", "sample_sheet:paired", "sample_sheet:paired_or_unpaired", "sample_sheet:record"
    ]
    column_definitions: list[SampleSheetColumnDefinitionModel] = Field(
        description="A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'"
    )
    content: str = Field(
        description="The workbook content (the contents of the xlsx file) that have been base64 encoded."
    )
    prefix_columns_type: Literal["URI", "ModelObjects"] | None = None


class ObjectExportTaskResponse(BaseModel):
    create_time: str = Field(description="The time and date this item was created.")
    export_metadata: ExportObjectMetadata | None = None
    id: str = Field(description="The encoded database ID of the export request.")
    preparing: bool = Field(description="Whether the archive is currently being built or in preparation.")
    ready: bool = Field(description="Whether the export has completed successfully and the archive is ready")
    task_uuid: str = Field(description="The identifier of the task processing the export.")
    up_to_date: bool = Field(description="False, if a new export archive should be generated.")


class RefactorResponse(BaseModel):
    action_executions: list[RefactorActionExecution]
    dry_run: bool
    workflow: str


class NotificationStatusSummary(BaseModel):
    """A summary of the notification status for a user. Contains only updates since a particular timestamp."""

    broadcasts: list[BroadcastNotificationResponse] = Field(description="The list of updated broadcasts.")
    notifications: list[UserNotificationResponse] = Field(description="The list of updated notifications for the user.")
    total_unread_count: int = Field(description="The total number of unread notifications for the user.")


class CreateSourceCredentialsPayload(BaseModel):
    service_credential: ServiceCredentialPayload = Field(
        description="The service credential details including group and credentials."
    )
    source_id: str = Field(description="The ID of the source (e.g., tool ID).")
    source_type: str = Field(description="The type of source requiring credentials.")
    source_version: str = Field(description="The version of the source.")


class AdminToolSource(BaseModel):
    citations: list[Citation] | None = None
    class_: str
    command: str
    container: str | None = None
    description: str | None = None
    edam_operations: list[str] | None = None
    edam_topics: list[str] | None = None
    help: HelpContent | None = None
    id: str | None = None
    inputs: list[Any] | None = None
    license: str | None = None
    name: str | None = None
    outputs: (
        list[
            IncomingToolOutputDataset
            | IncomingToolOutputCollectionInput
            | ToolOutputText
            | ToolOutputInteger
            | ToolOutputFloat
            | ToolOutputBoolean
        ]
        | None
    ) = None
    profile: float | None = None
    requirements: list[JavascriptRequirement | ResourceRequirement | ContainerRequirement] | None = None
    version: str | None = None
    xrefs: list[XrefDict] | None = None


class UserToolSourceOutput(BaseModel):
    citations: list[Citation] | None = None
    class_: str
    configfiles: list[YamlTemplateConfigFile] | None = Field(None, description="A list of config files for this tool.")
    container: str = Field(description="Container image to use for this tool.")
    description: str | None = Field(
        None,
        description="The description is displayed in the tool menu immediately following the hyperlink for the tool.",
    )
    edam_operations: list[str] | None = None
    edam_topics: list[str] | None = None
    help: HelpContent | None = Field(None, description="Help text shown below the tool interface.")
    id: str = Field(
        description="Unique identifier for the tool. Should be all lower-case and should not include whitespace."
    )
    inputs: list[Any] | None = None
    license: str | None = Field(
        None,
        description="A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool.",
    )
    name: str = Field(
        description="The name of the tool, displayed in the tool menu. This is not the same as the tool id, which is a unique identifier for the tool."
    )
    outputs: (
        list[
            IncomingToolOutputDataset
            | IncomingToolOutputCollectionOutput
            | ToolOutputText
            | ToolOutputInteger
            | ToolOutputFloat
            | ToolOutputBoolean
        ]
        | None
    ) = None
    requirements: list[JavascriptRequirement | ResourceRequirement | ContainerRequirement] | None = Field(
        None,
        description="A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images.",
    )
    shell_command: str = Field(
        description="A string that contains the command to be executed. Parameters can be referenced inside $()."
    )
    version: str = Field(description="Version for the tool.")
    xrefs: list[XrefDict] | None = None


class CompositeDataElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    composite: CompositeItems
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    metadata: dict[str, Any] | None = None
    name: str | int | float | bool | None = None
    row: list[int | float | bool | str | None] | None = None
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    src: str
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )


class DataRequestCollectionUri(BaseModel):
    class_: str
    collection_type: str
    deferred: bool | None = None
    elements: list[CollectionElementCollectionRequestUri | CollectionElementDataRequestUri]
    name: str | None = None
    src: None | None = None


class UserToolSourceInput(BaseModel):
    citations: list[Citation] | None = None
    class_: str
    configfiles: list[YamlTemplateConfigFile] | None = Field(None, description="A list of config files for this tool.")
    container: str = Field(description="Container image to use for this tool.")
    description: str | None = Field(
        None,
        description="The description is displayed in the tool menu immediately following the hyperlink for the tool.",
    )
    edam_operations: list[str] | None = None
    edam_topics: list[str] | None = None
    help: HelpContent | None = Field(None, description="Help text shown below the tool interface.")
    id: str = Field(
        description="Unique identifier for the tool. Should be all lower-case and should not include whitespace."
    )
    inputs: list[Any] | None = None
    license: str | None = Field(
        None,
        description="A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool.",
    )
    name: str = Field(
        description="The name of the tool, displayed in the tool menu. This is not the same as the tool id, which is a unique identifier for the tool."
    )
    outputs: (
        list[
            IncomingToolOutputDataset
            | IncomingToolOutputCollectionInput
            | ToolOutputText
            | ToolOutputInteger
            | ToolOutputFloat
            | ToolOutputBoolean
        ]
        | None
    ) = None
    requirements: list[JavascriptRequirement | ResourceRequirement | ContainerRequirement] | None = Field(
        None,
        description="A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images.",
    )
    shell_command: str = Field(
        description="A string that contains the command to be executed. Parameters can be referenced inside $()."
    )
    version: str = Field(description="Version for the tool.")
    xrefs: list[XrefDict] | None = None


class NotificationCreateRequest(BaseModel):
    notification: NotificationCreateData = Field(
        description="The notification to create. The structure depends on the category."
    )
    recipients: NotificationRecipientsRequest = Field(
        description="The recipients of the notification. Can be a combination of users, groups and roles."
    )


class NotificationCreatedResponse(BaseModel):
    notification: NotificationResponse = Field(
        description="The notification that was created. The structure depends on the category."
    )
    total_notifications_sent: int = Field(
        description="The total number of notifications that were sent to the recipients."
    )


class DynamicToolCreatePayload(BaseModel):
    active: bool | None = None
    hidden: bool | None = None
    representation: UserToolSourceInput | AdminToolSource
    src: str | None = None


class DynamicUnprivilegedToolCreatePayload(BaseModel):
    active: bool | None = None
    hidden: bool | None = None
    representation: UserToolSourceInput
    src: str | None = None


class NestedElement(BaseModel):
    MD5: str | None = Field(
        None,
        description="The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).\n",
    )
    SHA_1: str | None = Field(
        None,
        description="The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).\n",
    )
    SHA_256: str | None = Field(
        None,
        description="The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    SHA_512: str | None = Field(
        None,
        description="The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the\nintegrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).\n",
    )
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    created_from_basename: str | None = None
    dbkey: str | None = Field(
        None,
        description='This identifier is used to associate datasets with specific reference genomes. If set, the dbkey\nis a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10"\nfor mouse genome version 10. In other parts of of the API this is referred to as the "genome_build".\nThe Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to\nindicate that the dataset does not have a dbkey set.\n',
    )
    deferred: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not\nimmediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred\ndatasets, most datasets should not be deferred unless you are sure you want to use this feature.\n",
    )
    description: str | None = None
    elements: list[
        FileDataElement
        | PastedDataElement
        | UrlDataElement
        | PathDataElement
        | ServerDirElement
        | FtpImportElement
        | CompositeDataElement
        | NestedElement
    ]
    ext: str | None = Field(
        None,
        description='The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset.\nThe default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on\nthe contents of the file.\n',
    )
    extra_files: ExtraFiles | None = None
    hashes: list[FetchDatasetHash] | None = None
    info: str | None = Field(
        None,
        description="Free text field that can be used to store arbitrary information about the dataset. This used to be prominently\ndisplayed in the Galaxy user interface, but now is largely unused.\n",
    )
    items_from: ElementsFromType | None = None
    name: str | int | float | bool | None = None
    row: list[int | float | bool | str | None] | None = None
    space_to_tab: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs.\nThis should typically be set to false for most applications, but sometimes when pasting data into the Galaxy\nuser interface, it is useful to set this to true to ensure that the data is converted to a tabular format\ncorrectly.\n",
    )
    tags: list[str] | None = Field(
        None,
        description="Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to\ngroup datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be\nused to search for datasets in the Galaxy API.\n",
    )
    to_posix_lines: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX\nline endings (LF). The Galaxy user interface will typically set this to true so that all datasets default\nto having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false\nthough assuming the API user is more likely to be want to be precise about file handling details.\n",
    )


class UnprivilegedToolResponse(BaseModel):
    active: bool
    create_time: str
    hidden: bool
    id: str
    representation: UserToolSourceOutput
    tool_format: str | None
    tool_id: str | None
    uuid: str


class CreateFileLandingPayload(BaseModel):
    client_secret: str | None = None
    origin: str | None = None
    public: bool | None = None
    request_state: list[FileRequestUri | DataRequestCollectionUri]


class DataElementsTarget(BaseModel):
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    destination: HdaDestination | LibraryFolderDestination | LibraryDestination
    elements: list[
        FileDataElement
        | PastedDataElement
        | UrlDataElement
        | PathDataElement
        | ServerDirElement
        | FtpImportElement
        | CompositeDataElement
        | NestedElement
    ]


class HdcaDataItemsTarget(BaseModel):
    auto_decompress: bool | None = Field(
        None,
        description="This is a boolean value that indicates whether the dataset should be automatically decompressed if it is\ncompressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not\nexplicitly set to a compressed datatype.\n",
    )
    collection_type: str | None = None
    column_definitions: list[SampleSheetColumnDefinition] | None = None
    destination: HdcaDestination
    elements: list[
        FileDataElement
        | PastedDataElement
        | UrlDataElement
        | PathDataElement
        | ServerDirElement
        | FtpImportElement
        | CompositeDataElement
        | NestedElement
    ]
    name: str | None = None
    tags: list[str] | None = None


class DataLandingRequestState(BaseModel):
    targets: list[
        DataElementsTarget | HdcaDataItemsTarget | DataElementsFromTarget | HdcaDataItemsFromTarget | FtpImportTarget
    ]


class FetchDataPayload(BaseModel):
    history_id: str
    landing_uuid: str | None = None
    targets: list[
        DataElementsTarget | HdcaDataItemsTarget | DataElementsFromTarget | HdcaDataItemsFromTarget | FtpImportTarget
    ]


class CreateDataLandingPayload(BaseModel):
    client_secret: str | None = None
    origin: str | None = None
    public: bool | None = None
    request_state: DataLandingRequestState


class SectionParameterModelOutput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelOutput
        | TextParameterModel
        | IntegerParameterModel
        | FloatParameterModel
        | BooleanParameterModel
        | HiddenParameterModel
        | SelectParameterModel
        | DataParameterModel
        | DataCollectionParameterModel
        | DataColumnParameterModel
        | DirectoryUriParameterModel
        | RulesParameterModel
        | DrillDownParameterModelOutput
        | GroupTagParameterModel
        | BaseUrlParameterModel
        | GenomeBuildParameterModel
        | ColorParameterModel
        | ConditionalParameterModelOutput
        | RepeatParameterModelOutput
        | SectionParameterModelOutput
    ]
    type: str


class ConditionalWhenInput(BaseModel):
    discriminator: bool | str
    is_default_when: bool
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelInput
        | TextParameterModel
        | IntegerParameterModel
        | FloatParameterModel
        | BooleanParameterModel
        | HiddenParameterModel
        | SelectParameterModel
        | DataParameterModel
        | DataCollectionParameterModel
        | DataColumnParameterModel
        | DirectoryUriParameterModel
        | RulesParameterModel
        | DrillDownParameterModelInput
        | GroupTagParameterModel
        | BaseUrlParameterModel
        | GenomeBuildParameterModel
        | ColorParameterModel
        | ConditionalParameterModelInput
        | RepeatParameterModelInput
        | SectionParameterModelInput
    ]


class ConditionalParameterModelInput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    test_parameter: BooleanParameterModel | SelectParameterModel
    type: str
    whens: list[ConditionalWhenInput]


class RepeatParameterModelOutput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    max: int | None = None
    min: int | None = None
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelOutput
        | TextParameterModel
        | IntegerParameterModel
        | FloatParameterModel
        | BooleanParameterModel
        | HiddenParameterModel
        | SelectParameterModel
        | DataParameterModel
        | DataCollectionParameterModel
        | DataColumnParameterModel
        | DirectoryUriParameterModel
        | RulesParameterModel
        | DrillDownParameterModelOutput
        | GroupTagParameterModel
        | BaseUrlParameterModel
        | GenomeBuildParameterModel
        | ColorParameterModel
        | ConditionalParameterModelOutput
        | RepeatParameterModelOutput
        | SectionParameterModelOutput
    ]
    type: str


class RepeatParameterModelInput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    max: int | None = None
    min: int | None = None
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelInput
        | TextParameterModel
        | IntegerParameterModel
        | FloatParameterModel
        | BooleanParameterModel
        | HiddenParameterModel
        | SelectParameterModel
        | DataParameterModel
        | DataCollectionParameterModel
        | DataColumnParameterModel
        | DirectoryUriParameterModel
        | RulesParameterModel
        | DrillDownParameterModelInput
        | GroupTagParameterModel
        | BaseUrlParameterModel
        | GenomeBuildParameterModel
        | ColorParameterModel
        | ConditionalParameterModelInput
        | RepeatParameterModelInput
        | SectionParameterModelInput
    ]
    type: str


class SectionParameterModelInput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelInput
        | TextParameterModel
        | IntegerParameterModel
        | FloatParameterModel
        | BooleanParameterModel
        | HiddenParameterModel
        | SelectParameterModel
        | DataParameterModel
        | DataCollectionParameterModel
        | DataColumnParameterModel
        | DirectoryUriParameterModel
        | RulesParameterModel
        | DrillDownParameterModelInput
        | GroupTagParameterModel
        | BaseUrlParameterModel
        | GenomeBuildParameterModel
        | ColorParameterModel
        | ConditionalParameterModelInput
        | RepeatParameterModelInput
        | SectionParameterModelInput
    ]
    type: str


class ConditionalWhenOutput(BaseModel):
    discriminator: bool | str
    is_default_when: bool
    parameters: list[
        CwlIntegerParameterModel
        | CwlFloatParameterModel
        | CwlStringParameterModel
        | CwlBooleanParameterModel
        | CwlNullParameterModel
        | CwlFileParameterModel
        | CwlDirectoryParameterModel
        | CwlUnionParameterModelOutput
        | TextParameterModel
        | IntegerParameterModel
        | FloatParameterModel
        | BooleanParameterModel
        | HiddenParameterModel
        | SelectParameterModel
        | DataParameterModel
        | DataCollectionParameterModel
        | DataColumnParameterModel
        | DirectoryUriParameterModel
        | RulesParameterModel
        | DrillDownParameterModelOutput
        | GroupTagParameterModel
        | BaseUrlParameterModel
        | GenomeBuildParameterModel
        | ColorParameterModel
        | ConditionalParameterModelOutput
        | RepeatParameterModelOutput
        | SectionParameterModelOutput
    ]


class ConditionalParameterModelOutput(BaseModel):
    argument: str | None = Field(
        None,
        description='If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit).',
    )
    help: str | None = Field(
        None,
        description="Short bit of text, rendered on the tool form just below the associated field to provide information about the field.",
    )
    hidden: bool | None = None
    is_dynamic: bool | None = None
    label: str | None = Field(None, description="Will be displayed on the tool page as the label of the parameter.")
    name: str = Field(
        description="Parameter name. Used when referencing parameter in workflows or inside command templating."
    )
    optional: bool | None = Field(None, description="If `false`, parameter must have a value.")
    parameter_type: str | None = None
    test_parameter: BooleanParameterModel | SelectParameterModel
    type: str
    whens: list[ConditionalWhenOutput]


class HistoryContentsWithStatsResult(BaseModel):
    """Includes stats with items counting"""

    contents: list[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary] = (
        Field(
            description="The items matching the search query. Only the items fitting in the current page limit will be returned."
        )
    )
    stats: HistoryContentStats = Field(description="Contains counting stats for the query.")


class HDCADetailed(BaseModel):
    """History Dataset Collection Association detailed information."""

    collection_id: str
    collection_type: str = Field(
        description="The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`."
    )
    column_definitions: list[SampleSheetColumnDefinition] | None = Field(
        None, description="Column data associated with each element of this collection."
    )
    contents_url: str = Field(description="The relative URL to access the contents of this History.")
    create_time: str = Field(description="The time and date this item was created.")
    deleted: bool = Field(description="Whether this item is marked as deleted.")
    element_count: int | None = Field(
        None,
        description="The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.",
    )
    elements: list[DCESummary] | None = Field(
        None, description="The summary information of each of the elements inside the dataset collection."
    )
    elements_datatypes: list[str] = Field(
        description="A set containing all the different element datatypes in the collection."
    )
    elements_deleted: int = Field(description="The number of elements in the collection that are marked as deleted.")
    elements_states: ElementsStatesDict = Field(
        description="A dictionary containing counts for each dataset state in the collection."
    )
    hid: int = Field(description="The index position of this item in the History.")
    history_content_type: str = Field(description="This is always `dataset_collection` for dataset collections.")
    history_id: str
    id: str
    implicit_collection_jobs_id: str | None = Field(
        None,
        description="Encoded ID for the ICJ object describing the collection of jobs corresponding to this collection",
    )
    job_source_id: str | None = Field(
        None,
        description="The encoded ID of the Job that produced this dataset collection. Used to track the state of the job.",
    )
    job_source_type: JobSourceType | None = Field(
        None,
        description="The type of job (model class) that produced this dataset collection. Used to track the state of the job.",
    )
    job_state_summary: HDCJobStateSummary | None = Field(
        None, description="Overview of the job states working inside the dataset collection."
    )
    model_class: str = Field(description="The name of the database model class.")
    name: str | None = Field(description="The name of the item.")
    populated: bool | None = Field(
        None,
        description="Whether the dataset collection elements (and any subcollections elements) were successfully populated.",
    )
    populated_state: DatasetCollectionPopulatedState = Field(
        description="Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated."
    )
    populated_state_message: str | None = Field(
        None,
        description="Optional message with further information in case the population of the dataset collection failed.",
    )
    store_times_summary: list[OldestCreateTimeByObjectStoreId] | None = Field(
        None,
        description="A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.",
    )
    tags: list[str] = Field(description="The collection of tags associated with an item.")
    type: str | None = Field(None, description="This is always `collection` for dataset collections.")
    type_id: str | None = Field(None, description="The type and the encoded ID of this item. Used for caching.")
    update_time: str | None = Field(description="The last time and date this item was updated.")
    url: str = Field(description="The relative URL to access this item.")
    visible: bool = Field(description="Whether this item is visible or hidden to the user by default.")


class HDCACustom(BaseModel):
    """Can contain any serializable property of an HDCA.

    Allows arbitrary custom keys to be specified in the serialization
    parameters without a particular view (predefined set of keys)."""

    collection_id: str | None = None
    collection_type: str | None = Field(
        None,
        description="The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.",
    )
    column_definitions: list[SampleSheetColumnDefinition] | None = Field(
        None, description="Column data associated with each element of this collection."
    )
    contents_url: str | None = Field(None, description="The relative URL to access the contents of this History.")
    create_time: str | None = Field(None, description="The time and date this item was created.")
    deleted: bool | None = Field(None, description="Whether this item is marked as deleted.")
    element_count: int | None = Field(
        None,
        description="The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.",
    )
    elements: list[DCESummary] | None = Field(
        None, description="The summary information of each of the elements inside the dataset collection."
    )
    elements_datatypes: list[str] | None = Field(
        None, description="A set containing all the different element datatypes in the collection."
    )
    elements_deleted: int | None = Field(
        None, description="The number of elements in the collection that are marked as deleted."
    )
    elements_states: ElementsStatesDict | None = Field(
        None, description="A dictionary containing counts for each dataset state in the collection."
    )
    hid: int | None = Field(None, description="The index position of this item in the History.")
    history_content_type: str | None = Field(
        None, description="This is always `dataset_collection` for dataset collections."
    )
    history_id: str | None = None
    id: str | None = None
    implicit_collection_jobs_id: str | None = Field(
        None,
        description="Encoded ID for the ICJ object describing the collection of jobs corresponding to this collection",
    )
    job_source_id: str | None = Field(
        None,
        description="The encoded ID of the Job that produced this dataset collection. Used to track the state of the job.",
    )
    job_source_type: JobSourceType | None = Field(
        None,
        description="The type of job (model class) that produced this dataset collection. Used to track the state of the job.",
    )
    job_state_summary: HDCJobStateSummary | None = Field(
        None, description="Overview of the job states working inside the dataset collection."
    )
    model_class: str | None = Field(None, description="The name of the database model class.")
    name: str | None = Field(None, description="The name of the item.")
    populated: bool | None = Field(
        None,
        description="Whether the dataset collection elements (and any subcollections elements) were successfully populated.",
    )
    populated_state: DatasetCollectionPopulatedState | None = Field(
        None,
        description="Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated.",
    )
    populated_state_message: str | None = Field(
        None,
        description="Optional message with further information in case the population of the dataset collection failed.",
    )
    store_times_summary: list[OldestCreateTimeByObjectStoreId] | None = Field(
        None,
        description="A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.",
    )
    tags: list[str] | None = Field(None, description="The collection of tags associated with an item.")
    type: str | None = Field(None, description="This is always `collection` for dataset collections.")
    type_id: str | None = Field(None, description="The type and the encoded ID of this item. Used for caching.")
    update_time: str | None = Field(None, description="The last time and date this item was updated.")
    url: str | None = Field(None, description="The relative URL to access this item.")
    visible: bool | None = Field(None, description="Whether this item is visible or hidden to the user by default.")


class DCESummary(BaseModel):
    """Dataset Collection Element summary information."""

    columns: list[int | float | bool | str | None] | None = Field(
        None, description="A row (or list of columns) of data associated with this element"
    )
    element_identifier: str = Field(description="The actual name of this element.")
    element_index: int = Field(description="The position index of this element inside the collection.")
    element_type: DCEType | None = Field(
        None, description="The type of the element. Used to interpret the `object` field."
    )
    id: str
    model_class: str = Field(description="The name of the database model class.")
    object: HDAObject | HDADetailed | DCObject | None = Field(
        None, description="The element's specific data depending on the value of `element_type`."
    )


class DCObject(BaseModel):
    """Dataset Collection Object"""

    collection_type: str = Field(
        description="The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`."
    )
    column_definitions: list[SampleSheetColumnDefinition] | None = Field(
        None, description="Column definitions for sample sheet collections."
    )
    contents_url: str | None = None
    element_count: int | None = Field(
        None,
        description="The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.",
    )
    elements: list[DCESummary] | None = Field(
        None, description="The summary information of each of the elements inside the dataset collection."
    )
    elements_datatypes: list[str] = Field(
        description="A set containing all the different element datatypes in the collection."
    )
    elements_deleted: int = Field(description="The number of elements in the collection that are marked as deleted.")
    elements_states: ElementsStatesDict = Field(
        description="A dictionary containing counts for each dataset state in the collection."
    )
    id: str
    model_class: str = Field(description="The name of the database model class.")
    populated: bool | None = Field(
        None,
        description="Whether the dataset collection elements (and any subcollections elements) were successfully populated.",
    )


# Rebuild all models to resolve forward references
FetchDatasetHash.model_rebuild()
UserNotificationUpdateRequest.model_rebuild()
LibraryContentsDeleteResponse.model_rebuild()
UpdateLicenseAction.model_rebuild()
YamlTemplateConfigFile.model_rebuild()
ChatResponse.model_rebuild()
CwlIntegerParameterModel.model_rebuild()
FavoriteObject.model_rebuild()
HDABasicInfo.model_rebuild()
CreatedUserModel.model_rebuild()
CollectionElementIdentifier.model_rebuild()
ExportHistoryArchivePayload.model_rebuild()
JobErrorSummary.model_rebuild()
UserQuotaUsage.model_rebuild()
ShareWithExtra.model_rebuild()
DatasetPermissions.model_rebuild()
ExtraFiles.model_rebuild()
FavoriteObjectsSummary.model_rebuild()
RootModelDictStr_int_.model_rebuild()
ElementsStatesDict.model_rebuild()
CwlNullParameterModel.model_rebuild()
ResourceRequirement.model_rebuild()
ToolOutputInteger.model_rebuild()
EncodedHdcaSourceId.model_rebuild()
RegexJobMessage.model_rebuild()
HelpForumPost.model_rebuild()
EncodedDataItemSourceId.model_rebuild()
CsvDialect.model_rebuild()
LicenseMetadataModel.model_rebuild()
InvocationCancellationHistoryDeletedResponse.model_rebuild()
ReportInvocationErrorPayload.model_rebuild()
LibraryContentsFolderCreatePayload.model_rebuild()
StoredItem.model_rebuild()
RoleModelResponse.model_rebuild()
InvocationFailureCollectionFailedResponse.model_rebuild()
Authorizations.model_rebuild()
InvocationInput.model_rebuild()
ContentsObject.model_rebuild()
LibraryFolderDetails.model_rebuild()
PageDetails.model_rebuild()
InvocationStepJobsResponseStepModel.model_rebuild()
UserFileSourceModel.model_rebuild()
ConcreteObjectStoreQuotaSourceDetails.model_rebuild()
RemoteFileHash.model_rebuild()
UpdateInstancePayload.model_rebuild()
InvocationStepCollectionOutput.model_rebuild()
LibraryCurrentPermissions.model_rebuild()
VisualizationUpdateResponse.model_rebuild()
LibraryFolderDestination.model_rebuild()
FilesSourceSupports.model_rebuild()
JobBaseModel.model_rebuild()
InvocationEvaluationWarningWorkflowOutputNotFoundResponse.model_rebuild()
JobIdResponse.model_rebuild()
TaskResult.model_rebuild()
UpdateDatasetPermissionsPayloadAliasC.model_rebuild()
UserCreationPayload.model_rebuild()
CreateInvocationsFromStorePayload.model_rebuild()
InvocationOutputCollection.model_rebuild()
InvocationUpdatePayload.model_rebuild()
AvailableAgent.model_rebuild()
DataColumnParameterModel.model_rebuild()
JobExportHistoryArchiveModel.model_rebuild()
HDAObject.model_rebuild()
StoreExportPayload.model_rebuild()
InputStep.model_rebuild()
CreateLibrariesFromStore.model_rebuild()
ImplicitCollectionJobsStateSummary.model_rebuild()
InvocationStepOutput.model_rebuild()
RefactorActionExecutionMessage.model_rebuild()
HDAInaccessible.model_rebuild()
HelpForumGroup.model_rebuild()
ClaimLandingPayload.model_rebuild()
LibraryFolderMetadata.model_rebuild()
HelpForumCategory.model_rebuild()
NotificationChannelSettings.model_rebuild()
UpdateInstanceSecretPayload.model_rebuild()
DatasetHash.model_rebuild()
BasicRoleModel.model_rebuild()
QuotaSummary.model_rebuild()
VisualizationRevisionResponse.model_rebuild()
ToolDataEntry.model_rebuild()
DatasetAssociationRoles.model_rebuild()
UpdateQuotaParams.model_rebuild()
LibraryFolderPermissionsPayload.model_rebuild()
XrefDict.model_rebuild()
WorkflowInvocationStateSummary.model_rebuild()
CopyDatasetsPayloadSourceEntry.model_rebuild()
UpdateNameAction.model_rebuild()
ItemTagsResponse.model_rebuild()
JobConsoleOutput.model_rebuild()
CreateHistoryFromStore.model_rebuild()
ContextResponse.model_rebuild()
HelpForumTag.model_rebuild()
ChangeDatatypeOperationParams.model_rebuild()
InvokeWorkflowPayload.model_rebuild()
ServiceType.model_rebuild()
InvocationInputParameter.model_rebuild()
UpdateDatasetPermissionsPayloadAliasB.model_rebuild()
LibraryContentsCreateDatasetResponse.model_rebuild()
JobDestinationParams.model_rebuild()
WorkflowInput.model_rebuild()
GroupUserResponse.model_rebuild()
CwlDirectoryParameterModel.model_rebuild()
ToolLandingRequest.model_rebuild()
PathBasedDynamicToolCreatePayload.model_rebuild()
HistorySummary.model_rebuild()
CreateHistoryContentFromStore.model_rebuild()
ColorParameterModel.model_rebuild()
CwlFloatParameterModel.model_rebuild()
DatasetInheritanceChainEntry.model_rebuild()
DrillDownOptionsDictOutput.model_rebuild()
VisualizationCreatePayload.model_rebuild()
HistoryContentStats.model_rebuild()
InvocationFailureDatasetFailedResponse.model_rebuild()
UpdateCollectionAttributePayload.model_rebuild()
HelpForumGroupedSearchResult.model_rebuild()
BodyAi_agentsCustomTool_createCustomTool.model_rebuild()
EncodedHistoryContentItem.model_rebuild()
LegacyLibraryPermissionsPayload.model_rebuild()
AccessURL.model_rebuild()
HistoryDetailed.model_rebuild()
UserUpdatePayload.model_rebuild()
ImportToolDataBundleDatasetSource.model_rebuild()
SampleSheetColumnDefinition.model_rebuild()
GenomeBuildParameterModel.model_rebuild()
HDASummary.model_rebuild()
UpdateHistoryContentsPayload.model_rebuild()
BaseUrlParameterModel.model_rebuild()
JobLock.model_rebuild()
DetailedUserModel.model_rebuild()
FolderLibraryFolderItem.model_rebuild()
DeleteHistoryPayload.model_rebuild()
StepReferenceByOrderIndex.model_rebuild()
UndeleteHistoriesPayload.model_rebuild()
UserDeletionPayload.model_rebuild()
JobRequest.model_rebuild()
SelectCurrentGroupPayload.model_rebuild()
SecretResponse.model_rebuild()
TestUpgradeInstancePayload.model_rebuild()
InvocationFailureJobFailedResponse.model_rebuild()
EncodedJobParameterHistoryItem.model_rebuild()
BodyLibraries_contents_createForm.model_rebuild()
CwlBooleanParameterModel.model_rebuild()
CreateLinkIncoming.model_rebuild()
CreateQuotaResult.model_rebuild()
Position.model_rebuild()
ChatPayload.model_rebuild()
InvocationFailureExpressionEvaluationFailedResponse.model_rebuild()
GroupModel.model_rebuild()
WorkflowInvocationRequestModel.model_rebuild()
ItemTagsPayload.model_rebuild()
UpdateAnnotationAction.model_rebuild()
CreateLinkStep.model_rebuild()
Checksum.model_rebuild()
GroupTagParameterModel.model_rebuild()
ChangeDbkeyOperationParams.model_rebuild()
CheckForUpdatesResponse.model_rebuild()
MessageNotificationContent.model_rebuild()
NoOptionsParameterValidatorModel.model_rebuild()
OutputReferenceByLabel.model_rebuild()
CustomBuildCreationPayload.model_rebuild()
StepReferenceByLabel.model_rebuild()
LengthParameterValidatorModel.model_rebuild()
PageSummary.model_rebuild()
UpdateLibraryFolderPayload.model_rebuild()
NotificationRecipientsRequest.model_rebuild()
DataParameterModel.model_rebuild()
CreateLibraryPayload.model_rebuild()
ShareWithPayload.model_rebuild()
RegexParameterValidatorModel.model_rebuild()
LibraryContentsCollectionCreatePayload.model_rebuild()
UpdateContentItem.model_rebuild()
CreateWorkflowLandingRequestPayload.model_rebuild()
Hyperlink.model_rebuild()
ParsedWorkbookCollection.model_rebuild()
CreatePagePayload.model_rebuild()
WriteStoreToPayload.model_rebuild()
TemplateSecret.model_rebuild()
LibraryLegacySummary.model_rebuild()
EmptyFieldParameterValidatorModel.model_rebuild()
InvocationFailureWhenNotBooleanResponse.model_rebuild()
ToolDataItem.model_rebuild()
ExitCodeJobMessage.model_rebuild()
Container.model_rebuild()
LibraryContentsCreateFileResponse.model_rebuild()
BodyTools_fetch_fetchForm.model_rebuild()
ToolOutputFloat.model_rebuild()
FillIdentifiers.model_rebuild()
InputReferenceByOrderIndex.model_rebuild()
DeleteJobPayload.model_rebuild()
TestUpdateInstancePayload.model_rebuild()
JobImportHistoryResponse.model_rebuild()
DatatypeConverter.model_rebuild()
DataCollectionParameterModel.model_rebuild()
HelpForumTopic.model_rebuild()
InvocationCancellationReviewFailedResponse.model_rebuild()
JobStateSummary.model_rebuild()
TourStep.model_rebuild()
ToolDataField.model_rebuild()
RemoteDirectory.model_rebuild()
LabelValuePair.model_rebuild()
RulesParameterModel.model_rebuild()
AnonUserModel.model_rebuild()
DrillDownOptionsDictInput.model_rebuild()
EncodedDatasetSourceId.model_rebuild()
ToolRequestImplicitCollectionReference.model_rebuild()
CreateQuotaParams.model_rebuild()
ParsedColumn.model_rebuild()
ToolOutputText.model_rebuild()
Citation.model_rebuild()
DatatypeEDAMDetails.model_rebuild()
ToolReportForDataset.model_rebuild()
CreateEntryPayload.model_rebuild()
CreateLibraryFolderPayload.model_rebuild()
SuitableConverter.model_rebuild()
LibraryPermissionsPayload.model_rebuild()
ServiceParameterDefinition.model_rebuild()
DefaultQuota.model_rebuild()
ReloadFeedback.model_rebuild()
LibraryFolderCurrentPermissions.model_rebuild()
UserModel.model_rebuild()
Link.model_rebuild()
ToolRequestJobReference.model_rebuild()
OldestCreateTimeByObjectStoreId.model_rebuild()
VisualizationPluginResponse.model_rebuild()
InvocationStepJobsResponseCollectionJobsModel.model_rebuild()
InvocationJobsResponse.model_rebuild()
ReportJobErrorPayload.model_rebuild()
RoleDefinitionModel.model_rebuild()
OutputReferenceByOrderIndex.model_rebuild()
InputReferenceByLabel.model_rebuild()
HistoryActiveContentCounts.model_rebuild()
MaxDiscoveredFilesJobMessage.model_rebuild()
UpdateCreatorAction.model_rebuild()
ActionLink.model_rebuild()
GroupUpdatePayload.model_rebuild()
NotificationsBatchRequest.model_rebuild()
Visualization.model_rebuild()
InvocationCancellationUserRequestResponse.model_rebuild()
CreateInstancePayload.model_rebuild()
InvocationFailureWorkflowParameterInvalidResponse.model_rebuild()
UpdateLibraryPayload.model_rebuild()
InvocationReport.model_rebuild()
GroupCreatePayload.model_rebuild()
DeleteHistoriesPayload.model_rebuild()
LibraryContentsShowFolderResponse.model_rebuild()
ToolRequestModel.model_rebuild()
CreatedEntryResponse.model_rebuild()
DeleteQuotaPayload.model_rebuild()
BooleanParameterModel.model_rebuild()
ComputeDatasetHashPayload.model_rebuild()
QuotaModel.model_rebuild()
UpdateDatasetPermissionsPayload.model_rebuild()
InstalledRepositoryToolShedStatus.model_rebuild()
NewSharedItemNotificationContent.model_rebuild()
Galaxy_schema_schema_Organization.model_rebuild()
CopyDatasetsResponse.model_rebuild()
ContentTypeMessage.model_rebuild()
XrefItem.model_rebuild()
MessageExceptionModel.model_rebuild()
LibraryContentsCreateFolderResponse.model_rebuild()
WorkflowInvocationCollectionView.model_rebuild()
VisualizationUpdatePayload.model_rebuild()
BadgeDict.model_rebuild()
ImportToolDataBundleUriSource.model_rebuild()
DatasetSourceTransform.model_rebuild()
Tour.model_rebuild()
CreateLibraryFilePayload.model_rebuild()
DatatypeVisualizationMapping.model_rebuild()
Metric.model_rebuild()
ConvertedDatasetsMap.model_rebuild()
LimitedUserModel.model_rebuild()
MaterializeDatasetInstanceAPIRequest.model_rebuild()
LibraryContentsFileCreatePayload.model_rebuild()
GroupResponse.model_rebuild()
InvocationStepJobsResponseJobModel.model_rebuild()
InRangeParameterValidatorModel.model_rebuild()
OAuth2Info.model_rebuild()
UpdateHistoryPayload.model_rebuild()
LibraryDestination.model_rebuild()
PluginAspectStatus.model_rebuild()
AgentQueryRequest.model_rebuild()
InvocationUnexpectedFailureResponse.model_rebuild()
LibraryContentsShowDatasetResponse.model_rebuild()
DeletedCustomBuild.model_rebuild()
ExtraFileEntry.model_rebuild()
ParsedWorkbookHda.model_rebuild()
UserBeaconSetting.model_rebuild()
DatasetTextContentDetails.model_rebuild()
RemoveUnlabeledWorkflowOutputs.model_rebuild()
FilePatternDatasetCollectionDescription.model_rebuild()
UpgradeAllStepsAction.model_rebuild()
HelpForumUser.model_rebuild()
FieldDict.model_rebuild()
FileHash.model_rebuild()
CleanableItemsSummary.model_rebuild()
WorkflowJobMetric.model_rebuild()
HdcaDestination.model_rebuild()
CreateToolLandingRequestPayload.model_rebuild()
UserEmail.model_rebuild()
NotificationsBatchUpdateResponse.model_rebuild()
DatatypesMap.model_rebuild()
VisualizationSummary.model_rebuild()
LibrarySummary.model_rebuild()
VisualizationCreateResponse.model_rebuild()
ExportRecordData.model_rebuild()
HelpContent.model_rebuild()
APIKeyModel.model_rebuild()
CustomBuildModel.model_rebuild()
HdaDestination.model_rebuild()
LabelValue.model_rebuild()
BodyAi_agentsErrorAnalysis_analyzeError.model_rebuild()
CwlStringParameterModel.model_rebuild()
InvocationOutput.model_rebuild()
SetSlugPayload.model_rebuild()
StorageItemCleanupError.model_rebuild()
Galaxy_schema_drs_Organization.model_rebuild()
EncodedDatasetJobInfo.model_rebuild()
CredentialPayload.model_rebuild()
CwlFileParameterModel.model_rebuild()
UpdateObjectStoreIdPayload.model_rebuild()
Person.model_rebuild()
LibraryContentsDeletePayload.model_rebuild()
UserObjectstoreUsage.model_rebuild()
DeleteHistoryContentPayload.model_rebuild()
ItemTagsCreatePayload.model_rebuild()
JobSummary.model_rebuild()
CompositeFileInfo.model_rebuild()
DatasetCollectionAttributesResult.model_rebuild()
GroupRoleResponse.model_rebuild()
DeleteLibraryPayload.model_rebuild()
ToolDataDetails.model_rebuild()
WorkflowLandingRequest.model_rebuild()
APIKeyResponse.model_rebuild()
SearchJobsPayload.model_rebuild()
JavascriptRequirement.model_rebuild()
FileLibraryFolderItem.model_rebuild()
JobInputSummary.model_rebuild()
UpdatePagePayload.model_rebuild()
TagOperationParams.model_rebuild()
ToolProvidedMetadataDatasetCollection.model_rebuild()
ExportObjectResultMetadata.model_rebuild()
LibraryContentsIndexDatasetResponse.model_rebuild()
RemoteUserCreationPayload.model_rebuild()
ArchiveHistoryRequestPayload.model_rebuild()
Report.model_rebuild()
UpgradeInstancePayload.model_rebuild()
ToolOutputBoolean.model_rebuild()
InvocationFailureOutputNotFoundResponse.model_rebuild()
LibraryContentsIndexFolderResponse.model_rebuild()
ExpressionParameterValidatorModel.model_rebuild()
AsyncTaskResultSummary.model_rebuild()
CleanupStorageItemsRequest.model_rebuild()
BodyHistories_create.model_rebuild()
FileDefaultsAction.model_rebuild()
VariableResponse.model_rebuild()
ShortTermStoreExportPayload.model_rebuild()
MetadataFile.model_rebuild()
JobMetric.model_rebuild()
HistoryContentItem.model_rebuild()
ActionSuggestion.model_rebuild()
HDCJobStateSummary.model_rebuild()
DatasetSourceId.model_rebuild()
InferredColumnMapping.model_rebuild()
FtpImportTarget.model_rebuild()
InvocationStep.model_rebuild()
UserNotificationResponse.model_rebuild()
TemplateVariableInteger.model_rebuild()
InferredCollectionTypeLogEntry.model_rebuild()
DrillDownParameterModelOutput.model_rebuild()
FileDataElement.model_rebuild()
IntegerParameterModel.model_rebuild()
DisplayApplication.model_rebuild()
ParseFetchWorkbook.model_rebuild()
LibraryAvailablePermissions.model_rebuild()
FloatParameterModel.model_rebuild()
DatatypesEDAMDetailsDict.model_rebuild()
DirectoryUriParameterModel.model_rebuild()
CwlUnionParameterModelOutput.model_rebuild()
UrlDataElement.model_rebuild()
AccessMethod.model_rebuild()
DatatypeDetails.model_rebuild()
UpdateHistoryContentsBatchPayload.model_rebuild()
JobParameter.model_rebuild()
ShowFullJobResponse.model_rebuild()
InputDataCollectionStep.model_rebuild()
HDCASummary.model_rebuild()
CustomArchivedHistoryView.model_rebuild()
BulkOperationItemError.model_rebuild()
ServerDirElement.model_rebuild()
CustomBuildsMetadataResponse.model_rebuild()
InstalledToolShedRepository.model_rebuild()
DrillDownParameterModelInput.model_rebuild()
FtpImportElement.model_rebuild()
AgentResponse.model_rebuild()
ParsedWorkbookElement.model_rebuild()
UserQuota.model_rebuild()
EncodedJobDetails.model_rebuild()
TourDetails.model_rebuild()
JobInputAssociation.model_rebuild()
NotificationCategorySettings.model_rebuild()
CreateMetricsPayload.model_rebuild()
TemplateVariablePathComponent.model_rebuild()
UserConcreteObjectStoreModel.model_rebuild()
ArchivedHistoryDetailed.model_rebuild()
HdcaDataItemsFromTarget.model_rebuild()
PrepareStoreDownloadPayload.model_rebuild()
HistoryContentBulkOperationPayload.model_rebuild()
JobOutputAssociation.model_rebuild()
FilesSourcePlugin.model_rebuild()
AddStepAction.model_rebuild()
ExtractUntypedParameter.model_rebuild()
IncomingToolOutputDataset.model_rebuild()
AsyncFile.model_rebuild()
RemoteFile.model_rebuild()
SubworkflowStep.model_rebuild()
Service.model_rebuild()
UpdateStepPositionAction.model_rebuild()
CollectionElementDataRequestUri.model_rebuild()
ServiceCredentialGroupResponse.model_rebuild()
VisualizationShowResponse.model_rebuild()
BroadcastNotificationContent.model_rebuild()
UpdateReportAction.model_rebuild()
StorageItemsCleanupResult.model_rebuild()
UserNotificationsBatchUpdateRequest.model_rebuild()
DisplayApp.model_rebuild()
SelectParameterModel.model_rebuild()
PauseStep.model_rebuild()
ServiceCredentialGroupPayload.model_rebuild()
HiddenParameterModel.model_rebuild()
WriteInvocationStoreToPayload.model_rebuild()
JobOutputCollectionAssociation.model_rebuild()
SharingStatus.model_rebuild()
TextParameterModel.model_rebuild()
ExtractInputAction.model_rebuild()
DataElementsFromTarget.model_rebuild()
CsvDialectInferenceMessage.model_rebuild()
CreateHistoryContentPayload.model_rebuild()
ImportToolDataBundle.model_rebuild()
JobOutput.model_rebuild()
CustomHistoryView.model_rebuild()
GroupQuota.model_rebuild()
ContainerRequirement.model_rebuild()
SampleSheetColumnDefinitionModel.model_rebuild()
HelpForumSearchResponse.model_rebuild()
CwlUnionParameterModelInput.model_rebuild()
DisconnectAction.model_rebuild()
CopyDatasetsPayload.model_rebuild()
UpdateOutputLabelAction.model_rebuild()
ToolStep.model_rebuild()
AgentListResponse.model_rebuild()
TemplateVariableBoolean.model_rebuild()
AddInputAction.model_rebuild()
CreateNewCollectionPayload.model_rebuild()
PluginStatus.model_rebuild()
TemplateVariableString.model_rebuild()
CreateLinkFeedback.model_rebuild()
DatasetErrorMessage.model_rebuild()
FillStepDefaultsAction.model_rebuild()
ConcreteObjectStoreModel.model_rebuild()
ConnectAction.model_rebuild()
LibraryFolderContentsIndexResult.model_rebuild()
PastedDataElement.model_rebuild()
FileRequestUri.model_rebuild()
DatatypesCombinedMap.model_rebuild()
UpgradeToolAction.model_rebuild()
InputDataStep.model_rebuild()
ExportObjectRequestMetadata.model_rebuild()
JobCreateResponse.model_rebuild()
InputParameterStep.model_rebuild()
UpdateStepLabelAction.model_rebuild()
ToolOutputCollectionStructure.model_rebuild()
DatasetStorageDetails.model_rebuild()
DeleteDatasetBatchPayload.model_rebuild()
ArchivedHistorySummary.model_rebuild()
PathDataElement.model_rebuild()
ToolRequestDetailedModel.model_rebuild()
DatasetSource.model_rebuild()
ServiceCredentialsDefinition.model_rebuild()
BrowsableFilesSourcePlugin.model_rebuild()
UpgradeSubworkflowAction.model_rebuild()
SelectServiceCredentialPayload.model_rebuild()
SplitUpPairedDataLogEntry.model_rebuild()
ShareWithStatus.model_rebuild()
ShareHistoryExtra.model_rebuild()
DrsObject.model_rebuild()
ParsedFetchWorkbookForCollections.model_rebuild()
StoredWorkflowDetailed.model_rebuild()
CreateWorkbookForCollectionApi.model_rebuild()
QuotaDetails.model_rebuild()
HDACustom.model_rebuild()
UserNotificationPreferences.model_rebuild()
CollectionElementCollectionRequestUri.model_rebuild()
HistoryContentBulkOperationResult.model_rebuild()
AgentQueryResponse.model_rebuild()
DeleteDatasetBatchResult.model_rebuild()
RefactorActionExecution.model_rebuild()
ParseWorkbookForCollectionApi.model_rebuild()
CompositeItems.model_rebuild()
IncomingToolOutputCollectionOutput.model_rebuild()
UpdateUserNotificationPreferencesRequest.model_rebuild()
GenerateTourResponse.model_rebuild()
ObjectStoreTemplateSummary.model_rebuild()
ExportObjectMetadata.model_rebuild()
FileSourceTemplateSummary.model_rebuild()
ParsedWorkbookForCollection.model_rebuild()
IncomingToolOutputCollectionInput.model_rebuild()
RefactorRequest.model_rebuild()
BroadcastNotificationResponse.model_rebuild()
BroadcastNotificationCreateRequest.model_rebuild()
CreateWorkbookRequest.model_rebuild()
ServiceCredentialPayload.model_rebuild()
UserServiceCredentialsResponse.model_rebuild()
ParsedFetchWorkbookForDatasets.model_rebuild()
JobDisplayParametersSummary.model_rebuild()
NotificationResponse.model_rebuild()
NotificationBroadcastUpdateRequest.model_rebuild()
WorkflowInvocationElementView.model_rebuild()
NotificationCreateData.model_rebuild()
ParsedWorkbook.model_rebuild()
HDADetailed.model_rebuild()
ShareHistoryWithStatus.model_rebuild()
UserServiceCredentialsWithDefinitionResponse.model_rebuild()
ParseWorkbook.model_rebuild()
ObjectExportTaskResponse.model_rebuild()
RefactorResponse.model_rebuild()
NotificationStatusSummary.model_rebuild()
CreateSourceCredentialsPayload.model_rebuild()
AdminToolSource.model_rebuild()
UserToolSourceOutput.model_rebuild()
CompositeDataElement.model_rebuild()
DataRequestCollectionUri.model_rebuild()
UserToolSourceInput.model_rebuild()
NotificationCreateRequest.model_rebuild()
NotificationCreatedResponse.model_rebuild()
DynamicToolCreatePayload.model_rebuild()
DynamicUnprivilegedToolCreatePayload.model_rebuild()
NestedElement.model_rebuild()
UnprivilegedToolResponse.model_rebuild()
CreateFileLandingPayload.model_rebuild()
DataElementsTarget.model_rebuild()
HdcaDataItemsTarget.model_rebuild()
DataLandingRequestState.model_rebuild()
FetchDataPayload.model_rebuild()
CreateDataLandingPayload.model_rebuild()
SectionParameterModelOutput.model_rebuild()
ConditionalWhenInput.model_rebuild()
ConditionalParameterModelInput.model_rebuild()
RepeatParameterModelOutput.model_rebuild()
RepeatParameterModelInput.model_rebuild()
SectionParameterModelInput.model_rebuild()
ConditionalWhenOutput.model_rebuild()
ConditionalParameterModelOutput.model_rebuild()
HistoryContentsWithStatsResult.model_rebuild()
HDCADetailed.model_rebuild()
HDCACustom.model_rebuild()
DCESummary.model_rebuild()
DCObject.model_rebuild()
