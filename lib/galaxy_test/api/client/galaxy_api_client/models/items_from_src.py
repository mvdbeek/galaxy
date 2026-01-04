from enum import Enum


class ItemsFromSrc(str, Enum):
    FILES = "files"
    FTP_IMPORT = "ftp_import"
    PATH = "path"
    SERVER_DIR = "server_dir"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
