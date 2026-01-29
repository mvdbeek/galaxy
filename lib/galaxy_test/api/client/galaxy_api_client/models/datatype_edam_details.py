from dataclasses import dataclass

from .datatype_edam_details_definition import DatatypeEdamDetailsDefinition
from .datatype_edam_details_label import DatatypeEdamDetailsLabel

__all__ = ["DatatypeEdamDetails"]


@dataclass
class DatatypeEdamDetails:
    """
    DatatypeEdamDetails dataclass

    Args:
        definition (DatatypeEdamDetailsDefinition)
                                 : The EDAM definition
        label (DatatypeEdamDetailsLabel)
                                 : The EDAM label
        prefix_iri (str)         : The EDAM prefixed Resource Identifier (maps from
                                   'prefix_IRI')
    """

    definition: DatatypeEdamDetailsDefinition  # The EDAM definition
    label: DatatypeEdamDetailsLabel  # The EDAM label
    prefix_iri: str  # The EDAM prefixed Resource Identifier (maps from 'prefix_IRI')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "definition": "definition",
            "label": "label",
            "prefix_IRI": "prefix_iri",
        }
        key_transform_with_dump = {
            "definition": "definition",
            "label": "label",
            "prefix_iri": "prefix_IRI",
        }
