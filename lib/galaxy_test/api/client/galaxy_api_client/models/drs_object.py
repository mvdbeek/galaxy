from dataclasses import dataclass
from datetime import datetime

from .access_methods import AccessMethods
from .aliases import Aliases
from .checksum import Checksum
from .contents import Contents
from .description import Description
from .mime_type import MimeType
from .name import Name
from .updated_time import UpdatedTime
from .version import Version

__all__ = ["DrsObject"]


@dataclass
class DrsObject:
    """
    DrsObject dataclass.

    Args:
        checksums (List[Checksum]): The checksum of the `DrsObject`. At least one checksum
                                    must be provided. For blobs, the checksum is computed
                                    over the bytes in the blob. For bundles, the checksum is
                                    computed over a sorted concatenation of the checksums of
                                    its top-level contained objects (not recursive, names
                                    not included). The list of checksums is sorted
                                    alphabetically (hex-code) before concatenation and a
                                    further checksum is performed on the concatenated
                                    checksum value. For example, if a bundle contains blobs
                                    with the following checksums: md5(blob1) = 72794b6d
                                    md5(blob2) = 5e089d29 Then the checksum of the bundle
                                    is: md5( concat( sort( md5(blob1), md5(blob2) ) ) ) =
                                    md5( concat( sort( 72794b6d, 5e089d29 ) ) ) = md5(
                                    concat( 5e089d29, 72794b6d ) ) = md5( 5e089d2972794b6d )
                                    = f7a29a04
        created_time (datetime)  : Timestamp of content creation in RFC3339. (This is the
                                   creation time of the underlying content, not of the JSON
                                   object.)
        id_ (str)                : An identifier unique to this `DrsObject`
        self_uri (str)           : A drs:// hostname-based URI, as defined in the DRS
                                   documentation, that tells clients how to access this
                                   object. The intent of this field is to make DRS objects
                                   self-contained, and therefore easier for clients to store
                                   and pass around.  For example, if you arrive at this DRS
                                   JSON by resolving a compact identifier-based DRS URI, the
                                   `self_uri` presents you with a hostname and properly
                                   encoded DRS ID for use in subsequent `access` endpoint
                                   calls.
        size (int)               : For blobs, the blob size in bytes. For bundles, the
                                   cumulative size, in bytes, of items in the `contents`
                                   field.
        access_methods (Optional[AccessMethods])
                                 : The list of access methods that can be used to fetch the
                                   `DrsObject`. Required for single blobs; optional for
                                   bundles.
        aliases (Optional[Aliases])
                                 : A list of strings that can be used to find other metadata
                                   about this `DrsObject` from external metadata sources.
                                   These aliases can be used to represent secondary
                                   accession numbers or external GUIDs.
        contents (Optional[Contents])
                                 : The items matching the search query. Only the items
                                   fitting in the current page limit will be returned.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        mime_type (Optional[MimeType])
                                 : A string providing the mime-type of the `DrsObject`.
        name (Optional[Name])    : The name of the creator.
        updated_time (Optional[UpdatedTime])
                                 : Timestamp of content update in RFC3339, identical to
                                   `created_time` in systems that do not support updates.
                                   (This is the update time of the underlying content, not
                                   of the JSON object.)
        version (Optional[Version])
                                 : The version of the workflow to invoke.
    """

    checksums: list[
        Checksum
    ]  # The checksum of the `DrsObject`. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob. For bundles, the checksum is computed over a sorted concatenation of the checksums of its top-level contained objects (not recursive, names not included). The list of checksums is sorted alphabetically (hex-code) before concatenation and a further checksum is performed on the concatenated checksum value. For example, if a bundle contains blobs with the following checksums: md5(blob1) = 72794b6d md5(blob2) = 5e089d29 Then the checksum of the bundle is: md5( concat( sort( md5(blob1), md5(blob2) ) ) ) = md5( concat( sort( 72794b6d, 5e089d29 ) ) ) = md5( concat( 5e089d29, 72794b6d ) ) = md5( 5e089d2972794b6d ) = f7a29a04
    created_time: datetime  # Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.)
    id_: str  # An identifier unique to this `DrsObject`
    self_uri: str  # A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around.  For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the `self_uri` presents you with a hostname and properly encoded DRS ID for use in subsequent `access` endpoint calls.
    size: int  # For blobs, the blob size in bytes. For bundles, the cumulative size, in bytes, of items in the `contents` field.
    access_methods: AccessMethods | None = (
        None  # The list of access methods that can be used to fetch the `DrsObject`. Required for single blobs; optional for bundles.
    )
    aliases: Aliases | None = (
        None  # A list of strings that can be used to find other metadata about this `DrsObject` from external metadata sources. These aliases can be used to represent secondary accession numbers or external GUIDs.
    )
    contents: Contents | None = (
        None  # The items matching the search query. Only the items fitting in the current page limit will be returned.
    )
    description: Description | None = ""  # Detailed text description for this Quota.
    mime_type: MimeType | None = None  # A string providing the mime-type of the `DrsObject`.
    name: Name | None = None  # The name of the creator.
    updated_time: UpdatedTime | None = (
        None  # Timestamp of content update in RFC3339, identical to `created_time` in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.)
    )
    version: Version | None = "1.0"  # The version of the workflow to invoke.
