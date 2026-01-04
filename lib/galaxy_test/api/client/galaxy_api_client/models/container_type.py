from enum import Enum


class ContainerType(str, Enum):
    DOCKER = "docker"
    SINGULARITY = "singularity"

    def __str__(self) -> str:
        return str(self.value)
