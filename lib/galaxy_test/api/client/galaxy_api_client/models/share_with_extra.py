from dataclasses import dataclass

__all__ = ["ShareWithExtra"]


@dataclass
class ShareWithExtra:
    """
    ShareWithExtra dataclass

    Args:
        can_share (bool | None)  : Indicates whether the resource can be directly shared or
                                   requires further actions.
    """

    can_share: bool | None = False  # Indicates whether the resource can be directly shared or requires further actions.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "can_share": "can_share",
        }
        key_transform_with_dump = {
            "can_share": "can_share",
        }
