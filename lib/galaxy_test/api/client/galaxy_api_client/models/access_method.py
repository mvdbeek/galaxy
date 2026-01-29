from dataclasses import dataclass

from .access_method_access_id import AccessMethodAccessId
from .access_method_access_url import AccessMethodAccessUrl
from .access_method_authorizations import AccessMethodAuthorizations
from .access_method_region import AccessMethodRegion
from .access_method_type import AccessMethodType

__all__ = ["AccessMethod"]


@dataclass
class AccessMethod:
    """
    AccessMethod dataclass

    Args:
        type_ (AccessMethodType) : Maps from 'type'
        access_id (AccessMethodAccessId | None)
                                 : An arbitrary string to be passed to the `/access` method
                                   to get an `AccessURL`. This string must be unique within
                                   the scope of a single object. Note that at least one of
                                   `access_url` and `access_id` must be provided.
        access_url (AccessMethodAccessUrl | None)
                                 :
        authorizations (AccessMethodAuthorizations | None)
                                 :
        region (AccessMethodRegion | None)
                                 : Name of the region in the cloud service provider that the
                                   object belongs to.
    """

    type_: AccessMethodType  # Maps from 'type'
    access_id: AccessMethodAccessId | None = (
        None  # An arbitrary string to be passed to the `/access` method to get an `AccessURL`. This string must be unique within the scope of a single object. Note that at least one of `access_url` and `access_id` must be provided.
    )
    access_url: AccessMethodAccessUrl | None = None
    authorizations: AccessMethodAuthorizations | None = None
    region: AccessMethodRegion | None = (
        None  # Name of the region in the cloud service provider that the object belongs to.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_id": "access_id",
            "access_url": "access_url",
            "authorizations": "authorizations",
            "region": "region",
            "type": "type_",
        }
        key_transform_with_dump = {
            "access_id": "access_id",
            "access_url": "access_url",
            "authorizations": "authorizations",
            "region": "region",
            "type_": "type",
        }
