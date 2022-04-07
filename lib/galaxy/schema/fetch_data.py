from enum import Enum
from typing import (
    List,
    Literal,
    Optional,
    Union,
)

from pydantic import (
    BaseModel,
    Extra,
    Field,
)

from galaxy.schema.fields import EncodedDatabaseIdField
from .schema import HistoryIdField

AutoDecompressField = Field(False, description="Decompress compressed data before sniffing?")


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


class HdaDestination(BaseModel):
    type: Literal["hdas"]


class HdcaDestination(BaseModel):
    type: Literal["hdca"]


class LibraryDestination(BaseModel):
    type: str = "library"
    name: str = Field(..., description="Must specify a library name")
    description: Optional[str] = Field(None, description="Description for library to create")
    synopsis: Optional[str] = Field(None, description="Description for library to create")


class BaseFetchDatatarget:
    type: DestinationType
    src: Src


class BaseFetchDataTarget(BaseModel):
    auto_decompress: bool = AutoDecompressField


class ExtraFiles(BaseModel):
    items_from: Optional[str]
    src: Src
    fuzzy_root: Optional[bool] = Field(
        True,
        description="Prevent Galaxy from checking for a single file in a directory and re-interpreting the archive",
    )


class BaseDataElement(BaseModel):
    name: Optional[str] = Field(None)
    dbkey: str = Field("?")
    info: Optional[str] = Field(None)
    ext: str = Field("auto")
    space_to_tab: bool = Field(False)
    to_posix_lines: bool = Field(False)
    tags: Optional[List[str]]
    extra_files: Optional[ExtraFiles]
    auto_decompress: bool = AutoDecompressField


class FileDataElement(BaseDataElement):
    src: Literal["files"]


class PastedDataElement(BaseDataElement):
    src: Literal["pasted"]
    paste_content: str = Field(..., description="Content to upload")


class UrlDataElement(BaseDataElement):
    src: Literal["url"]
    url: str = Field(..., description="URL to upload")


class PathDataElement(BaseDataElement):
    src: Literal["path"]
    path: str


class ServerDirElement(BaseDataElement):
    src: Literal["server_dir"]
    server_dir: str


class FtpImportElement(BaseDataElement):
    src: Literal["ftp_import"]
    ftp_path: str


class CompositeDataElement(BaseDataElement):
    src: Literal["composite"]
    composite: "CompositeItems"


class CompositeItems(BaseModel):
    items: List[
        Union[FileDataElement, PastedDataElement, UrlDataElement, PathDataElement, ServerDirElement, FtpImportElement]
    ]


CompositeDataElement.update_forward_refs()


class NestedElement(BaseDataElement):
    elements: List["AnyElement"]


AnyElement = Union[
    FileDataElement,
    PastedDataElement,
    UrlDataElement,
    PathDataElement,
    ServerDirElement,
    FtpImportElement,
    CompositeDataElement,
    NestedElement,
]

NestedElement.update_forward_refs()


class BaseCollectionTarget(BaseFetchDataTarget):
    destination: HdcaDestination
    collection_type: Optional[str]
    tags: Optional[List[str]]
    name: Optional[str]


class HdaDataElementsTarget(BaseFetchDataTarget):
    destination: HdaDestination
    elements: List[AnyElement]


class HdaDataItemsTarget(BaseFetchDataTarget):
    destination: HdaDestination
    items: List[AnyElement]


class HdcaDataElementsTarget(BaseCollectionTarget):
    elements: List[AnyElement]
    elements_from: Optional[str] = None


class HdcaDataItemsTarget(BaseCollectionTarget):
    items: List[AnyElement]
    items_from: Optional[str] = None


class FetchDataPayload(BaseModel):
    history_id: EncodedDatabaseIdField = HistoryIdField
    targets: List[Union[HdaDataElementsTarget, HdaDataItemsTarget, HdcaDataElementsTarget, HdcaDataItemsTarget]] = []

    class Config:
        # file payloads are just tacked on, so we need to allow everything
        extra = Extra.allow
