from dataclasses import dataclass, field

from .sharing_status_email_hash import SharingStatusEmailHash
from .sharing_status_username import SharingStatusUsername
from .sharing_status_username_and_slug import SharingStatusUsernameAndSlug
from .user_email import UserEmail

__all__ = ["SharingStatus"]


@dataclass
class SharingStatus:
    """
    SharingStatus dataclass

    Args:
        id_ (str)                : The encoded ID of the resource to be shared. (maps from
                                   'id')
        importable (bool)        : Whether this resource can be published using a link.
        published (bool)         : Whether this resource is currently published.
        title (str)              : The title or name of the resource.
        email_hash (SharingStatusEmailHash | None)
                                 : Encoded owner email.
        username (SharingStatusUsername | None)
                                 : The owner's username.
        username_and_slug (SharingStatusUsernameAndSlug | None)
                                 : The relative URL in the form of
                                   /u/{username}/{resource_single_char}/{slug}
        users_shared_with (List[UserEmail] | None)
                                 : The list of encoded ids for users the resource has been
                                   shared.
    """

    id_: str  # The encoded ID of the resource to be shared. (maps from 'id')
    importable: bool  # Whether this resource can be published using a link.
    published: bool  # Whether this resource is currently published.
    title: str  # The title or name of the resource.
    email_hash: SharingStatusEmailHash | None = None  # Encoded owner email.
    username: SharingStatusUsername | None = None  # The owner's username.
    username_and_slug: SharingStatusUsernameAndSlug | None = (
        None  # The relative URL in the form of /u/{username}/{resource_single_char}/{slug}
    )
    users_shared_with: list[UserEmail] | None = field(
        default_factory=list
    )  # The list of encoded ids for users the resource has been shared.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email_hash": "email_hash",
            "id": "id_",
            "importable": "importable",
            "published": "published",
            "title": "title",
            "username": "username",
            "username_and_slug": "username_and_slug",
            "users_shared_with": "users_shared_with",
        }
        key_transform_with_dump = {
            "email_hash": "email_hash",
            "id_": "id",
            "importable": "importable",
            "published": "published",
            "title": "title",
            "username": "username",
            "username_and_slug": "username_and_slug",
            "users_shared_with": "users_shared_with",
        }
