from enum import Enum, unique

__all__ = ["Type_"]


@unique
class Type_(str, Enum):
    """
    Type_ Enum

    Args:
        docker (str)             : Value for DOCKER
        singularity (str)        : Value for SINGULARITY
    """

    DOCKER = "docker"
    SINGULARITY = "singularity"
