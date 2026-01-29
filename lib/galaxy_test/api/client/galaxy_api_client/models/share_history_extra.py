from dataclasses import dataclass, field

from .hda_basic_info_2 import HdaBasicInfo2

__all__ = ["ShareHistoryExtra"]


@dataclass
class ShareHistoryExtra:
    """
    ShareHistoryExtra dataclass

    Args:
        accessible_count (int | None)
                                 : The number of datasets in the history that are public or
                                   accessible by all the target users.
        can_change (List[HdaBasicInfo2] | None)
                                 : A collection of datasets that are not accessible by one
                                   or more of the target users and that can be made
                                   accessible for others by the user sharing the history.
        can_share (bool | None)  : Indicates whether the resource can be directly shared or
                                   requires further actions.
        cannot_change (List[HdaBasicInfo2] | None)
                                 : A collection of datasets that are not accessible by one
                                   or more of the target users and that cannot be made
                                   accessible for others by the user sharing the history.
    """

    accessible_count: int | None = (
        0  # The number of datasets in the history that are public or accessible by all the target users.
    )
    can_change: list[HdaBasicInfo2] | None = field(
        default_factory=list
    )  # A collection of datasets that are not accessible by one or more of the target users and that can be made accessible for others by the user sharing the history.
    can_share: bool | None = False  # Indicates whether the resource can be directly shared or requires further actions.
    cannot_change: list[HdaBasicInfo2] | None = field(
        default_factory=list
    )  # A collection of datasets that are not accessible by one or more of the target users and that cannot be made accessible for others by the user sharing the history.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "accessible_count": "accessible_count",
            "can_change": "can_change",
            "can_share": "can_share",
            "cannot_change": "cannot_change",
        }
        key_transform_with_dump = {
            "accessible_count": "accessible_count",
            "can_change": "can_change",
            "can_share": "can_share",
            "cannot_change": "cannot_change",
        }
