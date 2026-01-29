from dataclasses import dataclass

__all__ = ["ShareWithExtra"]


@dataclass
class ShareWithExtra:
    """
    ShareWithExtra dataclass.

    Args:
        can_share (Optional[bool]): Indicates whether the resource can be directly shared or
                                    requires further actions.
    """

    can_share: bool | None = False  # Indicates whether the resource can be directly shared or requires further actions.
