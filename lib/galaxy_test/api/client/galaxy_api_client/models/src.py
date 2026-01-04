from enum import Enum


class Src(str, Enum):
    COMPOSITE = "composite"
    FILES = "files"
    FTP_IMPORT = "ftp_import"
    PASTED = "pasted"
    PATH = "path"
    SERVER_DIR = "server_dir"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
