from dataclasses import dataclass

from .collection_type import CollectionType
from .composite_items import CompositeItems
from .created_from_basename import CreatedFromBasename
from .description import Description
from .extra_files import ExtraFiles
from .hashes import Hashes
from .info import Info
from .items_from import ItemsFrom
from .md_5 import Md5
from .metadata import Metadata
from .name import Name
from .row import Row
from .sha_1 import Sha1
from .sha_256 import Sha256
from .sha_512 import Sha512
from .tags import Tags

__all__ = ["CompositeDataElement"]


@dataclass
class CompositeDataElement:
    """
    CompositeDataElement dataclass.

    Args:
        composite (CompositeItems):
        src (str)                :
        md5 (Optional[Md5])      : The MD5 checksum of the dataset. This is a hash of the
                                   dataset contents that can be used to verify the integrity
                                   of the dataset. More information on MD5 checksums can be
                                   found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).
        sha_1 (Optional[Sha1])   : The SHA1 checksum of the dataset. This is a hash of the
                                   dataset contents that can be used to verify the integrity
                                   of the dataset. More information on SHA1 checksums can be
                                   found on
                                   [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).
        sha_256 (Optional[Sha256]): The SHA-256 checksum of the dataset. This is a hash of
                                    the dataset contents that can be used to verify the
                                    integrity of the dataset. More information on SHA-256
                                    checksums can be found on
                                    [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
        sha_512 (Optional[Sha512]): The SHA-512 checksum of the dataset. This is a hash of
                                    the dataset contents that can be used to verify the
                                    integrity of the dataset. More information on SHA-512
                                    checksums can be found on
                                    [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
        auto_decompress (Optional[bool])
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        created_from_basename (Optional[CreatedFromBasename])
                                 : The basename of the output that produced this dataset.
        dbkey (Optional[str])    : This identifier is used to associate datasets with
                                   specific reference genomes. If set, the dbkey is a string
                                   that represents the genome assembly, such as "hg19" for
                                   human genome version 19 or "mm10" for mouse genome
                                   version 10. In other parts of of the API this is referred
                                   to as the "genome_build". The Galaxy user interface also
                                   refers to this as "build" or "custom build". The value
                                   "?" is used to indicate that the dataset does not have a
                                   dbkey set.
        deferred (Optional[bool]): This is a boolean value that indicates whether the
                                   dataset is deferred. Deferred datasets are not
                                   immediately ingested into Galaxy on data import and may
                                   lack some metadata. Given open bugs with deferred
                                   datasets, most datasets should not be deferred unless you
                                   are sure you want to use this feature.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        ext (Optional[str])      : The file extension of the dataset. This is shorthand
                                   description of the datatype corresponding to this
                                   dataset. The default "auto" is used to indicate that the
                                   datatype should be automatically determined by Galaxy
                                   based on the contents of the file.
        extra_files (Optional[ExtraFiles])
                                 :
        hashes (Optional[Hashes]): List of precomputed hashes for the file, if available.
        info (Optional[Info])    : Free text field that can be used to store arbitrary
                                   information about the dataset. This used to be
                                   prominently displayed in the Galaxy user interface, but
                                   now is largely unused.
        items_from (Optional[ItemsFrom])
                                 :
        metadata (Optional[Metadata])
                                 : The metadata associated with this dataset.
        name (Optional[Name])    : The name of the creator.
        row (Optional[Row])      :
        space_to_tab (Optional[bool])
                                 : This is a boolean value that indicates whether the spaces
                                   in the dataset contents should be converted to tabs. This
                                   should typically be set to false for most applications,
                                   but sometimes when pasting data into the Galaxy user
                                   interface, it is useful to set this to true to ensure
                                   that the data is converted to a tabular format correctly.
        tags (Optional[Tags])    : Tags are a way to categorize datasets in Galaxy. They are
                                   free-form text strings that can be used to group datasets
                                   together. Tags can be used to filter datasets in the
                                   Galaxy user interface and can be used to search for
                                   datasets in the Galaxy API.
        to_posix_lines (Optional[bool])
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
    md5: Md5 | None = (
        None  # The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).
    )
    sha_1: Sha1 | None = (
        None  # The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).
    )
    sha_256: Sha256 | None = (
        None  # The SHA-256 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on SHA-256 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
    )
    sha_512: Sha512 | None = (
        None  # The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the integrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
    )
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    created_from_basename: CreatedFromBasename | None = None  # The basename of the output that produced this dataset.
    dbkey: str | None = (
        "?"  # This identifier is used to associate datasets with specific reference genomes. If set, the dbkey is a string that represents the genome assembly, such as "hg19" for human genome version 19 or "mm10" for mouse genome version 10. In other parts of of the API this is referred to as the "genome_build". The Galaxy user interface also refers to this as "build" or "custom build". The value "?" is used to indicate that the dataset does not have a dbkey set.
    )
    deferred: bool | None = (
        False  # This is a boolean value that indicates whether the dataset is deferred. Deferred datasets are not immediately ingested into Galaxy on data import and may lack some metadata. Given open bugs with deferred datasets, most datasets should not be deferred unless you are sure you want to use this feature.
    )
    description: Description | None = ""  # Detailed text description for this Quota.
    ext: str | None = (
        "auto"  # The file extension of the dataset. This is shorthand description of the datatype corresponding to this dataset. The default "auto" is used to indicate that the datatype should be automatically determined by Galaxy based on the contents of the file.
    )
    extra_files: ExtraFiles | None = None
    hashes: Hashes | None = None  # List of precomputed hashes for the file, if available.
    info: Info | None = (
        None  # Free text field that can be used to store arbitrary information about the dataset. This used to be prominently displayed in the Galaxy user interface, but now is largely unused.
    )
    items_from: ItemsFrom | None = None
    metadata: Metadata | None = None  # The metadata associated with this dataset.
    name: Name | None = None  # The name of the creator.
    row: Row | None = None
    space_to_tab: bool | None = (
        False  # This is a boolean value that indicates whether the spaces in the dataset contents should be converted to tabs. This should typically be set to false for most applications, but sometimes when pasting data into the Galaxy user interface, it is useful to set this to true to ensure that the data is converted to a tabular format correctly.
    )
    tags: Tags | None = (
        None  # Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to group datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be used to search for datasets in the Galaxy API.
    )
    to_posix_lines: bool | None = (
        False  # This is a boolean value that indicates whether the line endings in the dataset should be converted to POSIX line endings (LF). The Galaxy user interface will typically set this to true so that all datasets default to having POSIX line endings as most tools and workflows expect. The actual upload API will default this to false though assuming the API user is more likely to be want to be precise about file handling details.
    )
