from dataclasses import dataclass

from .label_value_pair import LabelValuePair

__all__ = ["CustomBuildsMetadataResponse"]


@dataclass
class CustomBuildsMetadataResponse:
    """
    CustomBuildsMetadataResponse dataclass.

    Args:
        fasta_hdas (List[LabelValuePair])
                                 : A list of label/value pairs with all the datasets of type
                                   `FASTA` contained in the History.  - `label` is item
                                   position followed by the name of the dataset.  - `value`
                                   is the encoded database ID of the dataset.
        installed_builds (List[LabelValuePair])
                                 : TODO
    """

    fasta_hdas: list[
        LabelValuePair
    ]  # A list of label/value pairs with all the datasets of type `FASTA` contained in the History.  - `label` is item position followed by the name of the dataset.  - `value` is the encoded database ID of the dataset.
    installed_builds: list[LabelValuePair]  # TODO
