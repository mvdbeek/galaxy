from dataclasses import dataclass
from datetime import datetime

from .checksum import Checksum
from .drs_object_access_methods import DrsObjectAccessMethods
from .drs_object_aliases import DrsObjectAliases
from .drs_object_contents import DrsObjectContents
from .drs_object_description import DrsObjectDescription
from .drs_object_mime_type import DrsObjectMimeType
from .drs_object_name import DrsObjectName
from .drs_object_updated_time import DrsObjectUpdatedTime
from .drs_object_version import DrsObjectVersion

__all__ = ["DrsObject"]


@dataclass
class DrsObject:
    """
    DrsObject dataclass

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
        id_ (str)                : An identifier unique to this `DrsObject` (maps from 'id')
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
        access_methods (DrsObjectAccessMethods | None)
                                 : The list of access methods that can be used to fetch the
                                   `DrsObject`. Required for single blobs; optional for
                                   bundles.
        aliases (DrsObjectAliases | None)
                                 : A list of strings that can be used to find other metadata
                                   about this `DrsObject` from external metadata sources.
                                   These aliases can be used to represent secondary
                                   accession numbers or external GUIDs.
        contents (DrsObjectContents | None)
                                 : If not set, this `DrsObject` is a single blob. If set,
                                   this `DrsObject` is a bundle containing the listed
                                   `ContentsObject` s (some of which may be further nested).
        description (DrsObjectDescription | None)
                                 : A human readable description of the `DrsObject`.
        mime_type (DrsObjectMimeType | None)
                                 : A string providing the mime-type of the `DrsObject`.
        name (DrsObjectName | None)
                                 : A string that can be used to name a `DrsObject`. This
                                   string is made up of uppercase and lowercase letters,
                                   decimal digits, hyphen, period, and underscore
                                   [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/
                                   9699919799/basedefs/V1_chap03.html#tag_03_282[portable
                                   filenames].
        updated_time (DrsObjectUpdatedTime | None)
                                 : Timestamp of content update in RFC3339, identical to
                                   `created_time` in systems that do not support updates.
                                   (This is the update time of the underlying content, not
                                   of the JSON object.)
        version (DrsObjectVersion | None)
                                 : A string representing a version. (Some systems may use
                                   checksum, a RFC3339 timestamp, or an incrementing version
                                   number.)
    """

    checksums: list[
        Checksum
    ]  # The checksum of the `DrsObject`. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob. For bundles, the checksum is computed over a sorted concatenation of the checksums of its top-level contained objects (not recursive, names not included). The list of checksums is sorted alphabetically (hex-code) before concatenation and a further checksum is performed on the concatenated checksum value. For example, if a bundle contains blobs with the following checksums: md5(blob1) = 72794b6d md5(blob2) = 5e089d29 Then the checksum of the bundle is: md5( concat( sort( md5(blob1), md5(blob2) ) ) ) = md5( concat( sort( 72794b6d, 5e089d29 ) ) ) = md5( concat( 5e089d29, 72794b6d ) ) = md5( 5e089d2972794b6d ) = f7a29a04
    created_time: datetime  # Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.)
    id_: str  # An identifier unique to this `DrsObject` (maps from 'id')
    self_uri: str  # A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around.  For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the `self_uri` presents you with a hostname and properly encoded DRS ID for use in subsequent `access` endpoint calls.
    size: int  # For blobs, the blob size in bytes. For bundles, the cumulative size, in bytes, of items in the `contents` field.
    access_methods: DrsObjectAccessMethods | None = (
        None  # The list of access methods that can be used to fetch the `DrsObject`. Required for single blobs; optional for bundles.
    )
    aliases: DrsObjectAliases | None = (
        None  # A list of strings that can be used to find other metadata about this `DrsObject` from external metadata sources. These aliases can be used to represent secondary accession numbers or external GUIDs.
    )
    contents: DrsObjectContents | None = (
        None  # If not set, this `DrsObject` is a single blob. If set, this `DrsObject` is a bundle containing the listed `ContentsObject` s (some of which may be further nested).
    )
    description: DrsObjectDescription | None = None  # A human readable description of the `DrsObject`.
    mime_type: DrsObjectMimeType | None = None  # A string providing the mime-type of the `DrsObject`.
    name: DrsObjectName | None = (
        None  # A string that can be used to name a `DrsObject`. This string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames].
    )
    updated_time: DrsObjectUpdatedTime | None = (
        None  # Timestamp of content update in RFC3339, identical to `created_time` in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.)
    )
    version: DrsObjectVersion | None = (
        None  # A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.)
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_methods": "access_methods",
            "aliases": "aliases",
            "checksums": "checksums",
            "contents": "contents",
            "created_time": "created_time",
            "description": "description",
            "id": "id_",
            "mime_type": "mime_type",
            "name": "name",
            "self_uri": "self_uri",
            "size": "size",
            "updated_time": "updated_time",
            "version": "version",
        }
        key_transform_with_dump = {
            "access_methods": "access_methods",
            "aliases": "aliases",
            "checksums": "checksums",
            "contents": "contents",
            "created_time": "created_time",
            "description": "description",
            "id_": "id",
            "mime_type": "mime_type",
            "name": "name",
            "self_uri": "self_uri",
            "size": "size",
            "updated_time": "updated_time",
            "version": "version",
        }
