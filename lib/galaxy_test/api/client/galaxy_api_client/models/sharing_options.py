from enum import Enum, unique

__all__ = ["SharingOptions"]


@unique
class SharingOptions(str, Enum):
    """
    Options for sharing resources that may have restricted access to all or part of their
    contents.

    Args:
        make_public (str)        : Value for MAKE_PUBLIC
        make_accessible_to_shared (str)
                                 : Value for MAKE_ACCESSIBLE_TO_SHARED
        no_changes (str)         : Value for NO_CHANGES
    """

    MAKE_PUBLIC = "make_public"
    MAKE_ACCESSIBLE_TO_SHARED = "make_accessible_to_shared"
    NO_CHANGES = "no_changes"
