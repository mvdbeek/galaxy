from enum import Enum, unique

__all__ = ["Type9"]


@unique
class Type9(str, Enum):
    """
    Type9 Enum

    Args:
        list_identifiers (str)   : Value for LIST_IDENTIFIERS
        paired_identifier (str)  : Value for PAIRED_IDENTIFIER
        paired_or_unpaired_identifier (str)
                                 : Value for PAIRED_OR_UNPAIRED_IDENTIFIER
        collection_name (str)    : Value for COLLECTION_NAME
        name_tag (str)           : Value for NAME_TAG
        tags (str)               : Value for TAGS
        group_tags (str)         : Value for GROUP_TAGS
        name (str)               : Value for NAME
        dbkey (str)              : Value for DBKEY
        hash_sha1 (str)          : Value for HASH_SHA1
        hash_md5 (str)           : Value for HASH_MD5
        hash_sha256 (str)        : Value for HASH_SHA256
        hash_sha512 (str)        : Value for HASH_SHA512
        file_type (str)          : Value for FILE_TYPE
        url (str)                : Value for URL
        url_deferred (str)       : Value for URL_DEFERRED
        info (str)               : Value for INFO
        ftp_path (str)           : Value for FTP_PATH
        deferred (str)           : Value for DEFERRED
        to_posix_lines (str)     : Value for TO_POSIX_LINES
        space_to_tab (str)       : Value for SPACE_TO_TAB
        auto_decompress (str)    : Value for AUTO_DECOMPRESS
    """

    LIST_IDENTIFIERS = "list_identifiers"
    PAIRED_IDENTIFIER = "paired_identifier"
    PAIRED_OR_UNPAIRED_IDENTIFIER = "paired_or_unpaired_identifier"
    COLLECTION_NAME = "collection_name"
    NAME_TAG = "name_tag"
    TAGS = "tags"
    GROUP_TAGS = "group_tags"
    NAME = "name"
    DBKEY = "dbkey"
    HASH_SHA1 = "hash_sha1"
    HASH_MD5 = "hash_md5"
    HASH_SHA256 = "hash_sha256"
    HASH_SHA512 = "hash_sha512"
    FILE_TYPE = "file_type"
    URL = "url"
    URL_DEFERRED = "url_deferred"
    INFO = "info"
    FTP_PATH = "ftp_path"
    DEFERRED = "deferred"
    TO_POSIX_LINES = "to_posix_lines"
    SPACE_TO_TAB = "space_to_tab"
    AUTO_DECOMPRESS = "auto_decompress"
