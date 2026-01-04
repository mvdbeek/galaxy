from enum import Enum


class UploadOption(str, Enum):
    UPLOAD_DIRECTORY = "upload_directory"
    UPLOAD_FILE = "upload_file"
    UPLOAD_PATHS = "upload_paths"

    def __str__(self) -> str:
        return str(self.value)
