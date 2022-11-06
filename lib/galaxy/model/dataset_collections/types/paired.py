from galaxy.model import (
    DatasetCollectionElement,
    HistoryDatasetAssociation,
)
from ..types import BaseDatasetCollectionType

FORWARD_IDENTIFIER = "forward"
REVERSE_IDENTIFIER = "reverse"


class PairedDatasetCollectionType(BaseDatasetCollectionType):
    """
    Paired (left/right) datasets.
    """

    collection_type = "paired"

    def generate_elements(self, elements, **kwds):
        forward_dataset = elements.get(FORWARD_IDENTIFIER)
        reverse_dataset = elements.get(REVERSE_IDENTIFIER)
        if forward_dataset:
            left_association = DatasetCollectionElement(
                element=forward_dataset,
                element_identifier=FORWARD_IDENTIFIER,
            )
            yield left_association
        if reverse_dataset:
            right_association = DatasetCollectionElement(
                element=reverse_dataset,
                element_identifier=REVERSE_IDENTIFIER,
            )
            yield right_association

    def prototype_elements(self, **kwds):
        left_association = DatasetCollectionElement(
            element=HistoryDatasetAssociation(),
            element_identifier=FORWARD_IDENTIFIER,
        )
        right_association = DatasetCollectionElement(
            element=HistoryDatasetAssociation(),
            element_identifier=REVERSE_IDENTIFIER,
        )
        yield left_association
        yield right_association
