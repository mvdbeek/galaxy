from dataclasses import dataclass

from .composite_data_element_collection_type import CompositeDataElementCollectionType
from .composite_data_element_created_from_basename import CompositeDataElementCreatedFromBasename
from .composite_data_element_description import CompositeDataElementDescription
from .composite_data_element_extra_files import CompositeDataElementExtraFiles
from .composite_data_element_hashes import CompositeDataElementHashes
from .composite_data_element_info import CompositeDataElementInfo
from .composite_data_element_items_from import CompositeDataElementItemsFrom
from .composite_data_element_md_5 import CompositeDataElementMd5
from .composite_data_element_metadata import CompositeDataElementMetadata
from .composite_data_element_name import CompositeDataElementName
from .composite_data_element_row import CompositeDataElementRow
from .composite_data_element_sha_1 import CompositeDataElementSha1
from .composite_data_element_sha_256 import CompositeDataElementSha256
from .composite_data_element_sha_512 import CompositeDataElementSha512
from .composite_data_element_tags import CompositeDataElementTags
from .composite_items import CompositeItems

__all__ = ["CompositeDataElement"]


@dataclass
class CompositeDataElement:
    """
    CompositeDataElement dataclass

    Args:
        composite (CompositeItems):
        src (str)                :
        md5 (CompositeDataElementMd5 | None)
                                 : The MD5 checksum of the dataset. This is a hash of the
                                   dataset contents that can be used to verify the integrity
                                   of the dataset. More information on MD5 checksums can be
                                   found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).
                                   (maps from 'MD5')
        sha_1 (CompositeDataElementSha1 | None)
                                 : The SHA1 checksum of the dataset. This is a hash of the
                                   dataset contents that can be used to verify the integrity
                                   of the dataset. More information on SHA1 checksums can be
                                   found on
                                   [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).  (maps
                                   from 'SHA-1')
        sha_256 (CompositeDataElementSha256 | None)
                                 : The SHA-256 checksum of the dataset. This is a hash of
                                   the dataset contents that can be used to verify the
                                   integrity of the dataset. More information on SHA-256
                                   checksums can be found on
                                   [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).  (maps
                                   from 'SHA-256')
        sha_512 (CompositeDataElementSha512 | None)
                                 : The SHA-512 checksum of the dataset. This is a hash of
                                   the dataset contents that can be used to verify the
                                   integrity of the dataset. More information on SHA-512
                                   checksums can be found on
                                   [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).  (maps
                                   from 'SHA-512')
        auto_decompress (bool | None)
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        collection_type (CompositeDataElementCollectionType | None)
                                 :
        created_from_basename (CompositeDataElementCreatedFromBasename | None)
                                 :
        dbkey (str | None)       : This identifier is used to associate datasets with
                                   specific reference genomes. If set, the dbkey is a string
                                   that represents the genome assembly, such as "hg19" for
                                   human genome version 19 or "mm10" for mouse genome
                                   version 10. In other parts of of the API this is referred
                                   to as the "genome_build". The Galaxy user interface also
                                   refers to this as "build" or "custom build". The value
                                   "?" is used to indicate that the dataset does not have a
                                   dbkey set.
        deferred (bool | None)   : This is a boolean value that indicates whether the
                                   dataset is deferred. Deferred datasets are not
                                   immediately ingested into Galaxy on data import and may
                                   lack some metadata. Given open bugs with deferred
                                   datasets, most datasets should not be deferred unless you
                                   are sure you want to use this feature.
        description (CompositeDataElementDescription | None)
                                 :
        ext (str | None)         : The file extension of the dataset. This is shorthand
                                   description of the datatype corresponding to this
                                   dataset. The default "auto" is used to indicate that the
                                   datatype should be automatically determined by Galaxy
                                   based on the contents of the file.
        extra_files (CompositeDataElementExtraFiles | None)
                                 :
        hashes (CompositeDataElementHashes | None)
                                 :
        info (CompositeDataElementInfo | None)
                                 : Free text field that can be used to store arbitrary
                                   information about the dataset. This used to be
                                   prominently displayed in the Galaxy user interface, but
                                   now is largely unused.
        items_from (CompositeDataElementItemsFrom | None)
                                 :
        metadata (CompositeDataElementMetadata | None)
                                 :
        name (CompositeDataElementName | None)
                                 :
        row (CompositeDataElementRow | None)
                                 :
        space_to_tab (bool | None): This is a boolean value that indicates whether the
                                    spaces in the dataset contents should be converted to
                                    tabs. This should typically be set to false for most
                                    applications, but sometimes when pasting data into the
                                    Galaxy user interface, it is useful to set this to true
                                    to ensure that the data is converted to a tabular format
                                    correctly.
        tags (CompositeDataElementTags | None)
                                 : Tags are a way to categorize datasets in Galaxy. They are
                                   free-form text strings that can be used to group datasets
                                   together. Tags can be used to filter datasets in the
                                   Galaxy user interface and can be used to search for
                                   datasets in the Galaxy API.
        to_posix_lines (bool | None)
                                 : This is a boolean value that indicates whether the line
                                   endings in the dataset should be converted to POSIX line
                                   endings (LF). The Galaxy user interface will typically
                                   set this to true so that all datasets default to having
                                   POSIX line endings as most tools and workflows expect.
                                   The actual upload API will default this to false though
                                   assuming the API user is more likely to be want to be
                                   precise about file handling details.
    """

    composite: CompositeItems
    src: str
    md5: CompositeDataElementMd5 | None = (
        None  # The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).  (maps from 'MD5')
    )
    sha_1: CompositeDataElementSha1 | None = (
        None  # The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).  (maps from 'SHA-1')
    )
    sha_256: CompositeDataElementSha256 | None = (
        None  # The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).  (maps from 'SHA-256')
    )
    sha_512: CompositeDataElementSha512 | None = (
        None  # The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).  (maps from 'SHA-512')
    )
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    collection_type: CompositeDataElementCollectionType | None = None
    created_from_basename: CompositeDataElementCreatedFromBasename | None = None
    dbkey: str | None = (
        "?"  # This identifier is used to associate datasets with specific reference genomes. If set, the dbkey is a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10" for mouse genome version 10. In other parts of of the API this is referred to as the "genome_build". The Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to indicate that the dataset does not have a dbkey set.
    )
    deferred: bool | None = (
        False  # This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not immediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred datasets, most datasets should not be deferred unless you are sure you want to use this feature.
    )
    description: CompositeDataElementDescription | None = None
    ext: str | None = (
        "auto"  # The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset. The default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on the contents of the file.
    )
    extra_files: CompositeDataElementExtraFiles | None = None
    hashes: CompositeDataElementHashes | None = None
    info: CompositeDataElementInfo | None = (
        None  # Free text field that can be used to store arbitrary information about the dataset. This used to be prominently displayed in the Galaxy user interface, but now is largely unused.
    )
    items_from: CompositeDataElementItemsFrom | None = None
    metadata: CompositeDataElementMetadata | None = None
    name: CompositeDataElementName | None = None
    row: CompositeDataElementRow | None = None
    space_to_tab: bool | None = (
        False  # This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs. This should typically be set to false for most applications, but sometimes when pasting data into the Galaxy user interface, it is useful to set this to true to ensure that the data is converted to a tabular format correctly.
    )
    tags: CompositeDataElementTags | None = (
        None  # Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to group datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be used to search for datasets in the Galaxy API.
    )
    to_posix_lines: bool | None = (
        False  # This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX line endings (LF). The Galaxy user interface will typically set this to true so that all datasets default to having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false though assuming the API user is more likely to be want to be precise about file handling details.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "MD5": "md5",
            "SHA-1": "sha_1",
            "SHA-256": "sha_256",
            "SHA-512": "sha_512",
            "auto_decompress": "auto_decompress",
            "collection_type": "collection_type",
            "composite": "composite",
            "created_from_basename": "created_from_basename",
            "dbkey": "dbkey",
            "deferred": "deferred",
            "description": "description",
            "ext": "ext",
            "extra_files": "extra_files",
            "hashes": "hashes",
            "info": "info",
            "items_from": "items_from",
            "metadata": "metadata",
            "name": "name",
            "row": "row",
            "space_to_tab": "space_to_tab",
            "src": "src",
            "tags": "tags",
            "to_posix_lines": "to_posix_lines",
        }
        key_transform_with_dump = {
            "auto_decompress": "auto_decompress",
            "collection_type": "collection_type",
            "composite": "composite",
            "created_from_basename": "created_from_basename",
            "dbkey": "dbkey",
            "deferred": "deferred",
            "description": "description",
            "ext": "ext",
            "extra_files": "extra_files",
            "hashes": "hashes",
            "info": "info",
            "items_from": "items_from",
            "md5": "MD5",
            "metadata": "metadata",
            "name": "name",
            "row": "row",
            "sha_1": "SHA-1",
            "sha_256": "SHA-256",
            "sha_512": "SHA-512",
            "space_to_tab": "space_to_tab",
            "src": "src",
            "tags": "tags",
            "to_posix_lines": "to_posix_lines",
        }
