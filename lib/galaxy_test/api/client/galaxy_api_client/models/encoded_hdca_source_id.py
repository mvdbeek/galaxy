from dataclasses import dataclass

__all__ = ["EncodedHdcaSourceId"]


@dataclass
class EncodedHdcaSourceId:
    """
    EncodedHdcaSourceId dataclass

    Args:
        id_ (str)                : Maps from 'id'
        src (str)                : The source of this dataset, which in the case of the
                                   model can only be `hdca`.
    """

    id_: str  # Maps from 'id'
    src: str  # The source of this dataset, which in the case of the model can only be `hdca`.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
        }
