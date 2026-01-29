from dataclasses import dataclass

__all__ = ["EncodedHdcaSourceId"]


@dataclass
class EncodedHdcaSourceId:
    """
    EncodedHdcaSourceId dataclass.

    Args:
        id_ (str)                :
        src (str)                : The source of this dataset, which in the case of the
                                   model can only be `hdca`.
    """

    id_: str
    src: str  # The source of this dataset, which in the case of the model can only be `hdca`.
