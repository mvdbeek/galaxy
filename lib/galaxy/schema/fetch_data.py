import json
from enum import Enum
from typing import (
    Annotated,
    Any,
    Optional,
    Union,
)

from pydantic import (
    AliasChoices,
    ConfigDict,
    Field,
    field_validator,
    HttpUrl,
    Json,
    model_validator,
    TypeAdapter,
    UUID4,
)
from typing_extensions import (
    Literal,
    Self,
)

from galaxy.schema.fields import DecodedDatabaseIdField
from galaxy.schema.schema import (
    Model,
    RecordFields,
    SampleSheetColumnDefinitions,
    SampleSheetRow,
)
from galaxy.schema.terms import HelpTerms
from galaxy.schema.types import CoercedStringType
from galaxy.tool_util_models import CollectionType
from galaxy.tool_util_models.parameters import FileOrCollectionRequest
from galaxy.util.hash_util import HashFunctionNames

HELP_TERMS = HelpTerms()


class FetchBaseModel(Model):
    model_config = ConfigDict(populate_by_name=True)


class ElementsFromType(str, Enum):
    archive = "archive"
    bagit = "bagit"
    bagit_archive = "bagit_archive"
    directory = "directory"


AutoDecompressField = Field(False, description=HELP_TERMS.get_term("galaxy.dataFetch.auto_decompress"))


class BaseFetchDataTarget(FetchBaseModel):
    auto_decompress: bool = AutoDecompressField


class ItemsFromSrc(str, Enum):
    url = "url"
    files = "files"
    path = "path"
    ftp_import = "ftp_import"
    server_dir = "server_dir"


class Src(str, Enum):
    url = "url"
    pasted = "pasted"
    files = "files"
    path = "path"
    composite = "composite"
    ftp_import = "ftp_import"
    server_dir = "server_dir"


class DestinationType(str, Enum):
    library = "library"
    library_folder = "library_folder"
    hdcas = "hdcas"
    hdas = "hdas"


class HdaDestination(FetchBaseModel):
    type: Literal["hdas"]


class HdcaDestination(FetchBaseModel):
    type: Literal["hdca"]


class LibraryFolderDestination(FetchBaseModel):
    type: Literal["library_folder"]
    library_folder_id: DecodedDatabaseIdField  # For some reason this folder ID must NOT have the 'F' prefix


class BaseCollectionTarget(BaseFetchDataTarget):
    destination: HdcaDestination
    collection_type: CollectionType = None
    tags: Optional[list[str]] = None
    name: Optional[str] = None
    # For sample_sheet collections
    column_definitions: Optional[SampleSheetColumnDefinitions] = None
    # For record collections
    fields: Optional[RecordFields] = None

    @model_validator(mode="after")
    def validate_collection_metadata(self) -> Self:
        """Validate that appropriate metadata is provided for special collection types.

        - record collections require 'fields'
        - sample_sheet collections require 'column_definitions'
        """
        if self.collection_type == "record" and not self.fields:
            raise ValueError("Record collections require 'fields' to be specified")
        if self.collection_type == "sample_sheet" and not self.column_definitions:
            raise ValueError("Sample sheet collections require 'column_definitions' to be specified")
        return self


class LibraryDestination(FetchBaseModel):
    type: Literal["library"]
    name: str = Field(..., description="Must specify a library name")
    description: Optional[str] = Field(None, description="Description for library to create")
    synopsis: Optional[str] = Field(None, description="Description for library to create")


class ExtraFiles(FetchBaseModel):
    items_from: Optional[str] = None
    src: Src
    fuzzy_root: Optional[bool] = Field(
        True,
        description="Prevent Galaxy from checking for a single file in a directory and re-interpreting the archive",
    )


class FetchDatasetHash(Model):
    hash_function: HashFunctionNames
    hash_value: str

    model_config = ConfigDict(extra="forbid")


class BaseDataElement(FetchBaseModel):
    name: Optional[CoercedStringType] = None
    dbkey: str = Field("?", description=HELP_TERMS.get_term("galaxy.dataFetch.dbkey"))
    info: Optional[str] = Field(None, description=HELP_TERMS.get_term("galaxy.dataFetch.info"))
    ext: str = Field("auto", description=HELP_TERMS.get_term("galaxy.dataFetch.ext"))
    space_to_tab: bool = Field(False, description=HELP_TERMS.get_term("galaxy.dataFetch.space_to_tab"))
    to_posix_lines: bool = Field(False, description=HELP_TERMS.get_term("galaxy.dataFetch.to_posix_lines"))
    deferred: bool = Field(False, description=HELP_TERMS.get_term("galaxy.dataFetch.deferred"))
    tags: Optional[list[str]] = Field(None, description=HELP_TERMS.get_term("galaxy.dataFetch.tags"))
    created_from_basename: Optional[str] = None
    extra_files: Optional[ExtraFiles] = None
    auto_decompress: bool = AutoDecompressField
    items_from: Optional[ElementsFromType] = Field(None, validation_alias=AliasChoices("items_from", "elements_from"))
    collection_type: CollectionType = None
    MD5: Optional[str] = Field(None, description=HELP_TERMS.get_term("galaxy.dataFetch.MD5"))
    SHA1: Optional[str] = Field(None, alias="SHA-1", description=HELP_TERMS.get_term("galaxy.dataFetch.SHA1"))
    SHA256: Optional[str] = Field(None, alias="SHA-256", description=HELP_TERMS.get_term("galaxy.dataFetch.SHA256"))
    SHA512: Optional[str] = Field(None, alias="SHA-512", description=HELP_TERMS.get_term("galaxy.dataFetch.SHA512"))
    hashes: Optional[list[FetchDatasetHash]] = None
    description: Optional[str] = None
    model_config = ConfigDict(extra="forbid")
    # It'd be nice to restrict this to just the top level and only if creating a collection
    row: Optional[SampleSheetRow] = None


class FileDataElement(BaseDataElement):
    src: Literal["files"]


class PastedDataElement(BaseDataElement):
    src: Literal["pasted"]
    paste_content: CoercedStringType = Field(..., description=HELP_TERMS.get_term("galaxy.dataFetch.paste_content"))


class UrlDataElement(BaseDataElement):
    src: Literal["url"]
    url: str = Field(..., description="URL to upload")


class ServerDirElement(BaseDataElement):
    src: Literal["server_dir"]
    server_dir: str
    link_data_only: Optional[bool] = None


class FtpImportElement(BaseDataElement):
    src: Literal["ftp_import"]
    ftp_path: str
    collection_type: CollectionType = None


class ItemsFromModel(Model):
    src: ItemsFromSrc
    path: Optional[str] = None
    ftp_path: Optional[str] = None
    server_dir: Optional[str] = None
    url: Optional[str] = None


class FtpImportTarget(BaseCollectionTarget):
    src: Literal["ftp_import"]
    ftp_path: str
    items_from: Optional[ElementsFromType] = Field(None, validation_alias=AliasChoices("items_from", "elements_from"))


class PathDataElement(BaseDataElement):
    src: Literal["path"]
    path: str
    items_from: Optional[ElementsFromType] = Field(None, validation_alias=AliasChoices("items_from", "elements_from"))
    link_data_only: Optional[bool] = None


class CompositeDataElement(BaseDataElement):
    src: Literal["composite"]
    composite: "CompositeItems"
    metadata: Optional[dict[str, Any]] = None


class CompositeItems(FetchBaseModel):
    elements: list[
        Union[FileDataElement, PastedDataElement, UrlDataElement, PathDataElement, ServerDirElement, FtpImportElement]
    ] = Field(..., validation_alias=AliasChoices("elements", "items"))


CompositeDataElement.model_rebuild()


class NestedElement(BaseDataElement):
    elements: list[Union["AnyElement", "NestedElement"]] = Field(
        ..., validation_alias=AliasChoices("elements", "items")
    )


AnyElement = Annotated[
    Union[
        FileDataElement,
        PastedDataElement,
        UrlDataElement,
        PathDataElement,
        ServerDirElement,
        FtpImportElement,
        CompositeDataElement,
    ],
    Field(default_factory=None, discriminator="src"),
]


# Seems to be a bug in pydantic ... can't reuse AnyElement in more than one model
AnyElement2 = Annotated[
    Union[
        FileDataElement,
        PastedDataElement,
        UrlDataElement,
        PathDataElement,
        ServerDirElement,
        FtpImportElement,
        CompositeDataElement,
    ],
    Field(default_factory=None, discriminator="src"),
]

NestedElement.model_rebuild()


class BaseDataTarget(BaseFetchDataTarget):
    destination: Union[HdaDestination, LibraryFolderDestination, LibraryDestination] = Field(..., discriminator="type")


class DataElementsTarget(BaseDataTarget):
    elements: list[Union[AnyElement, NestedElement]] = Field(..., validation_alias=AliasChoices("elements", "items"))


class DataElementsFromTarget(BaseDataTarget, ItemsFromModel):
    items_from: ElementsFromType = Field(..., alias="elements_from")


class HdcaDataItemsTarget(BaseCollectionTarget):
    elements: list[Union[AnyElement2, NestedElement]] = Field(..., validation_alias=AliasChoices("elements", "items"))


class HdcaDataItemsFromTarget(BaseCollectionTarget, ItemsFromModel):
    items_from: ElementsFromType = Field(..., validation_alias=AliasChoices("items_from", "elements_from"))


class FilesPayload(Model):
    filename: str
    local_filename: str


class BaseDataPayload(FetchBaseModel):
    history_id: DecodedDatabaseIdField
    model_config = ConfigDict(extra="allow")
    landing_uuid: Optional[UUID4] = None

    @field_validator("targets", mode="before", check_fields=False)
    @classmethod
    def targets_string_to_json(cls, v):
        if isinstance(v, str):
            return json.loads(v)
        return v


Targets = list[
    Union[
        DataElementsTarget,
        HdcaDataItemsTarget,
        DataElementsFromTarget,
        HdcaDataItemsFromTarget,
        FtpImportTarget,
    ]
]


TargetsAdapter = TypeAdapter(Targets)


class FetchDataPayload(BaseDataPayload):
    targets: Targets


class FetchDataFormPayload(BaseDataPayload):
    targets: Union[Json[Targets], Targets]


class DataLandingRequestState(Model):
    targets: Targets


FileOrCollectionRequests = list[FileOrCollectionRequest]

FileOrCollectionRequestsAdapter = TypeAdapter(FileOrCollectionRequests)


# Vaguely matches the schema.schema.ToolLandingState but we don't allow data_fetch to be called directly
# via the tool API so we have a more specific model here.
class CreateDataLandingPayload(Model):
    request_state: DataLandingRequestState
    client_secret: Optional[str] = None
    public: bool = False
    origin: Optional[HttpUrl] = None

    model_config = ConfigDict(extra="forbid")


class CreateFileLandingPayload(Model):
    request_state: FileOrCollectionRequests
    client_secret: Optional[str] = None
    public: bool = False
    origin: Optional[HttpUrl] = None

    model_config = ConfigDict(extra="forbid")
