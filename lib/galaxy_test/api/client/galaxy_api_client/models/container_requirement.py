from dataclasses import dataclass

from .container import Container

__all__ = ["ContainerRequirement"]


@dataclass
class ContainerRequirement:
    """
    ContainerRequirement dataclass.

    Args:
        container (Optional[Container])
                                 :
        type_ (str)              :
    """

    container: Container | None
    type_: str
