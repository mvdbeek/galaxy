from dataclasses import dataclass

from .select_current_group_payload import SelectCurrentGroupPayload

__all__ = ["SelectServiceCredentialPayload"]


@dataclass
class SelectServiceCredentialPayload:
    """
    SelectServiceCredentialPayload dataclass.

    Args:
        service_credentials (List[SelectCurrentGroupPayload])
                                 : List of user credentials to update with current group
                                   selections.
        source_id (str)          : The ID of the source (e.g., tool ID).
        source_type (str)        : The type of source requiring credentials.
        source_version (str)     : The version of the source.
    """

    service_credentials: list[
        SelectCurrentGroupPayload
    ]  # List of user credentials to update with current group selections.
    source_id: str  # The ID of the source (e.g., tool ID).
    source_type: str  # The type of source requiring credentials.
    source_version: str  # The version of the source.
