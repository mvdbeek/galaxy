from enum import Enum


class ParsedColumnType(str, Enum):
    AUTO_DECOMPRESS = "auto_decompress"
    COLLECTION_NAME = "collection_name"
    DBKEY = "dbkey"
    DEFERRED = "deferred"
    FILE_TYPE = "file_type"
    FTP_PATH = "ftp_path"
    GROUP_TAGS = "group_tags"
    HASH_MD5 = "hash_md5"
    HASH_SHA1 = "hash_sha1"
    HASH_SHA256 = "hash_sha256"
    HASH_SHA512 = "hash_sha512"
    INFO = "info"
    LIST_IDENTIFIERS = "list_identifiers"
    NAME = "name"
    NAME_TAG = "name_tag"
    PAIRED_IDENTIFIER = "paired_identifier"
    PAIRED_OR_UNPAIRED_IDENTIFIER = "paired_or_unpaired_identifier"
    SPACE_TO_TAB = "space_to_tab"
    TAGS = "tags"
    TO_POSIX_LINES = "to_posix_lines"
    URL = "url"
    URL_DEFERRED = "url_deferred"

    def __str__(self) -> str:
        return str(self.value)
