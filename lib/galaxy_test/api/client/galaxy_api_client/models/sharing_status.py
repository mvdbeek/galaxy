from dataclasses import dataclass, field

from .email_hash import EmailHash
from .user_email_7 import UserEmail7
from .username import Username
from .username_and_slug import UsernameAndSlug

__all__ = ["SharingStatus"]


@dataclass
class SharingStatus:
    """
    SharingStatus dataclass.

    Args:
        id_ (str)                : The encoded ID of the resource to be shared.
        importable (bool)        : Whether this resource can be published using a link.
        published (bool)         : Whether this resource is currently published.
        title (str)              : The title or name of the resource.
        email_hash (Optional[EmailHash])
                                 : The hash of the email of the creator of this workflow
        username (Optional[Username])
                                 : The name of the user.
        username_and_slug (Optional[UsernameAndSlug])
                                 : The relative URL in the form of
                                   /u/{username}/{resource_single_char}/{slug}
        users_shared_with (Optional[List[UserEmail7]])
                                 : The list of encoded ids for users the resource has been
                                   shared.
    """

    id_: str  # The encoded ID of the resource to be shared.
    importable: bool  # Whether this resource can be published using a link.
    published: bool  # Whether this resource is currently published.
    title: str  # The title or name of the resource.
    email_hash: EmailHash | None = None  # The hash of the email of the creator of this workflow
    username: Username | None = None  # The name of the user.
    username_and_slug: UsernameAndSlug | None = (
        None  # The relative URL in the form of /u/{username}/{resource_single_char}/{slug}
    )
    users_shared_with: list[UserEmail7] | None = field(
        default_factory=list
    )  # The list of encoded ids for users the resource has been shared.
