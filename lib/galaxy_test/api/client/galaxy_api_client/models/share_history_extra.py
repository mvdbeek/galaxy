from dataclasses import dataclass, field

from .hda_basic_info_5 import HdaBasicInfo5

__all__ = ["ShareHistoryExtra"]


@dataclass
class ShareHistoryExtra:
    """
    ShareHistoryExtra dataclass.

    Args:
        accessible_count (Optional[int])
                                 : The number of datasets in the history that are public or
                                   accessible by all the target users.
        can_change (Optional[List[HdaBasicInfo5]])
                                 : A collection of datasets that are not accessible by one
                                   or more of the target users and that can be made
                                   accessible for others by the user sharing the history.
        can_share (Optional[bool]): Indicates whether the resource can be directly shared or
                                    requires further actions.
        cannot_change (Optional[List[HdaBasicInfo5]])
                                 : A collection of datasets that are not accessible by one
                                   or more of the target users and that cannot be made
                                   accessible for others by the user sharing the history.
    """

    accessible_count: int | None = (
        0  # The number of datasets in the history that are public or accessible by all the target users.
    )
    can_change: list[HdaBasicInfo5] | None = field(
        default_factory=list
    )  # A collection of datasets that are not accessible by one or more of the target users and that can be made accessible for others by the user sharing the history.
    can_share: bool | None = False  # Indicates whether the resource can be directly shared or requires further actions.
    cannot_change: list[HdaBasicInfo5] | None = field(
        default_factory=list
    )  # A collection of datasets that are not accessible by one or more of the target users and that cannot be made accessible for others by the user sharing the history.
