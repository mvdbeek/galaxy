from dataclasses import dataclass

from .definition import Definition
from .label import Label

__all__ = ["DatatypeEdamDetails"]


@dataclass
class DatatypeEdamDetails:
    """
    DatatypeEdamDetails dataclass.

    Args:
        definition (Optional[Definition])
                                 : The EDAM definition
        label (Optional[Label])  : Label of the input.
        prefix_iri (str)         : The EDAM prefixed Resource Identifier
    """

    definition: Definition | None  # The EDAM definition
    label: Label | None  # Label of the input.
    prefix_iri: str  # The EDAM prefixed Resource Identifier
