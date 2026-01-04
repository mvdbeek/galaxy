from enum import Enum


class FetchDatasetHashHashFunction(str, Enum):
    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"

    def __str__(self) -> str:
        return str(self.value)
