from enum import Enum
from typing import (
    List,
    Optional,
    Union,
)

from pydantic import (
    BaseModel,
    Extra,
    Field,
)
from typing_extensions import (
    Annotated,
    Literal,
)

from galaxy.schema.fields import EncodedDatabaseIdField
from .schema import HistoryIdField


class FetchBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True


class ElementsFromType(str, Enum):
    ARCHIVE = "archive"
    BAGIT = "bagit"
    BAGIT_ARCHIVE = "bagit_archive"
    DIRECTORY = "directory"


AutoDecompressField = Field(False, description="Decompress compressed data before sniffing?")


class BaseFetchDataTarget(FetchBaseModel):
    auto_decompress: bool = AutoDecompressField


class ItemsFromSrc(str, Enum):
    url = "url"
    files = "files"
    path = "path"
    ftp_import = "ftp_import"
    server_dir = "server_id"


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
    library_folder_id: EncodedDatabaseIdField


class BaseCollectionTarget(BaseFetchDataTarget):
    destination: HdcaDestination
    collection_type: Optional[str]
    tags: Optional[List[str]]
    name: Optional[str]


class LibraryDestination(FetchBaseModel):
    type: Literal["library"]
    name: str = Field(..., description="Must specify a library name")
    description: Optional[str] = Field(None, description="Description for library to create")
    synopsis: Optional[str] = Field(None, description="Description for library to create")


class ExtraFiles(FetchBaseModel):
    items_from: Optional[str]
    src: Src
    fuzzy_root: Optional[bool] = Field(
        True,
        description="Prevent Galaxy from checking for a single file in a directory and re-interpreting the archive",
    )


class BaseDataElement(FetchBaseModel):
    name: Optional[str]
    dbkey: str = Field("?")
    info: Optional[str]
    ext: str = Field("auto")
    space_to_tab: bool = False
    to_posix_lines: bool = False
    tags: Optional[List[str]]
    extra_files: Optional[ExtraFiles]
    auto_decompress: bool = AutoDecompressField
    items_from: Optional[ElementsFromType] = Field(alias="elements_from")
    collection_type: Optional[str]
    MD5: Optional[str]

    class Config:
        # reject unknown extra attributes
        extra = Extra.forbid


class FileDataElement(BaseDataElement):
    src: Literal["files"]


class PastedDataElement(BaseDataElement):
    src: Literal["pasted"]
    paste_content: str = Field(..., description="Content to upload")


class UrlDataElement(BaseDataElement):
    src: Literal["url"]
    url: str = Field(..., description="URL to upload")


class ServerDirElement(BaseDataElement):
    src: Literal["server_dir"]
    server_dir: str
    link_data_only: Optional[bool]


class FtpImportElement(BaseDataElement):
    src: Literal["ftp_import"]
    ftp_path: str
    items_from: Optional[ElementsFromType] = Field(alias="elements_from")
    name: Optional[str]
    collection_type: Optional[str]


class ItemsFromModel(BaseModel):
    src: ItemsFromSrc
    path: Optional[str]
    ftp_path: Optional[str]
    server_dir: Optional[str]
    url: Optional[str]


class FtpImportTarget(BaseCollectionTarget):
    src: Literal["ftp_import"]
    ftp_path: str
    items_from: Optional[ElementsFromType] = Field(alias="elements_from")


class PathDataElement(BaseDataElement):
    src: Literal["path"]
    path: str
    items_from: Optional[ElementsFromType] = Field(alias="elements_from")
    link_data_only: Optional[bool]


class CompositeDataElement(BaseDataElement):
    src: Literal["composite"]
    composite: "CompositeItems"


class CompositeItems(FetchBaseModel):
    items: List[
        Union[FileDataElement, PastedDataElement, UrlDataElement, PathDataElement, ServerDirElement, FtpImportElement]
    ] = Field(..., alias="elements")


CompositeDataElement.update_forward_refs()


class NestedElement(BaseDataElement):
    items: List["AnyElement"] = Field(..., alias="elements")


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

NestedElement.update_forward_refs()


class BaseDataTarget(BaseFetchDataTarget):
    destination: Union[HdaDestination, LibraryFolderDestination, LibraryDestination] = Field(..., discriminator="type")


class DataElementsTarget(BaseDataTarget):
    items: List[Union[AnyElement, NestedElement]] = Field(..., alias="elements")


class DataElementsFromTarget(BaseDataTarget, ItemsFromModel):
    items_from: ElementsFromType = Field(..., alias="elements_from")


class HdcaDataItemsTarget(BaseCollectionTarget):
    items: List[Union[AnyElement2, NestedElement]] = Field(..., alias="elements")


class HdcaDataItemsFromTarget(BaseCollectionTarget, ItemsFromModel):
    items_from: ElementsFromType = Field(..., alias="elements_from")


class FetchDataPayload(FetchBaseModel):
    history_id: EncodedDatabaseIdField = HistoryIdField
    targets: List[
        Union[
            DataElementsTarget,
            HdcaDataItemsTarget,
            DataElementsFromTarget,
            HdcaDataItemsFromTarget,
            FtpImportTarget,
        ]
    ] = []

    class Config:
        # file payloads are just tacked on, so we need to allow everything
        extra = Extra.allow
