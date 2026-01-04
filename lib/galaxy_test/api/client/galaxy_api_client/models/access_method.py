from dataclasses import dataclass

from .access_id import AccessId
from .access_method_type import AccessMethodType
from .access_url_2 import AccessUrl2
from .authorizations import Authorizations
from .region import Region

__all__ = ["AccessMethod"]


@dataclass
class AccessMethod:
    """
    AccessMethod dataclass.

    Args:
        type_ (AccessMethodType) :
        access_id (Optional[AccessId])
                                 : An arbitrary string to be passed to the `/access` method
                                   to get an `AccessURL`. This string must be unique within
                                   the scope of a single object. Note that at least one of
                                   `access_url` and `access_id` must be provided.
        access_url (Optional[AccessUrl2])
                                 :
        authorizations (Optional[Authorizations])
                                 :
        region (Optional[Region]): Name of the region in the cloud service provider that the
                                   object belongs to.
    """

    type_: AccessMethodType
    access_id: AccessId | None = (
        None  # An arbitrary string to be passed to the `/access` method to get an `AccessURL`. This string must be unique within the scope of a single object. Note that at least one of `access_url` and `access_id` must be provided.
    )
    access_url: AccessUrl2 | None = None
    authorizations: Authorizations | None = None
    region: Region | None = None  # Name of the region in the cloud service provider that the object belongs to.
