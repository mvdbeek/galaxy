from dataclasses import dataclass, field

from .share_history_extra import ShareHistoryExtra
from .share_history_with_status_email_hash import ShareHistoryWithStatusEmailHash
from .share_history_with_status_username import ShareHistoryWithStatusUsername
from .share_history_with_status_username_and_slug import ShareHistoryWithStatusUsernameAndSlug
from .user_email import UserEmail

__all__ = ["ShareHistoryWithStatus"]


@dataclass
class ShareHistoryWithStatus:
    """
    ShareHistoryWithStatus dataclass

    Args:
        extra (ShareHistoryExtra):
        id_ (str)                : The encoded ID of the resource to be shared. (maps from
                                   'id')
        importable (bool)        : Whether this resource can be published using a link.
        published (bool)         : Whether this resource is currently published.
        title (str)              : The title or name of the resource.
        email_hash (ShareHistoryWithStatusEmailHash | None)
                                 : Encoded owner email.
        errors (List[str] | None): Collection of messages indicating that the resource was
                                   not shared with some (or all users) due to an error.
        username (ShareHistoryWithStatusUsername | None)
                                 : The owner's username.
        username_and_slug (ShareHistoryWithStatusUsernameAndSlug | None)
                                 : The relative URL in the form of
                                   /u/{username}/{resource_single_char}/{slug}
        users_shared_with (List[UserEmail] | None)
                                 : The list of encoded ids for users the resource has been
                                   shared.
    """

    extra: ShareHistoryExtra
    id_: str  # The encoded ID of the resource to be shared. (maps from 'id')
    importable: bool  # Whether this resource can be published using a link.
    published: bool  # Whether this resource is currently published.
    title: str  # The title or name of the resource.
    email_hash: ShareHistoryWithStatusEmailHash | None = None  # Encoded owner email.
    errors: list[str] | None = field(
        default_factory=list
    )  # Collection of messages indicating that the resource was not shared with some (or all users) due to an error.
    username: ShareHistoryWithStatusUsername | None = None  # The owner's username.
    username_and_slug: ShareHistoryWithStatusUsernameAndSlug | None = (
        None  # The relative URL in the form of /u/{username}/{resource_single_char}/{slug}
    )
    users_shared_with: list[UserEmail] | None = field(
        default_factory=list
    )  # The list of encoded ids for users the resource has been shared.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email_hash": "email_hash",
            "errors": "errors",
            "extra": "extra",
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
            "errors": "errors",
            "extra": "extra",
            "id_": "id",
            "importable": "importable",
            "published": "published",
            "title": "title",
            "username": "username",
            "username_and_slug": "username_and_slug",
            "users_shared_with": "users_shared_with",
        }
