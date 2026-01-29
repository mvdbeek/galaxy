from dataclasses import dataclass

from .avatar_template import AvatarTemplate
from .blurb import Blurb
from .created_at import CreatedAt
from .like_count import LikeCount
from .name import Name
from .post_number import PostNumber
from .topic_id import TopicId
from .username import Username

__all__ = ["HelpForumPost"]


@dataclass
class HelpForumPost:
    """
    Model for a post in the help forum.

    Args:
        avatar_template (Optional[AvatarTemplate])
                                 : The avatar template of the user.
        blurb (Optional[Blurb])  : The blurb of the post.
        created_at (Optional[CreatedAt])
                                 : Timestamp describing when the service was first deployed
                                   and available (RFC 3339 format)
        id_ (int)                : The ID of the post.
        like_count (Optional[LikeCount])
                                 : The number of likes of the post.
        name (Optional[Name])    : The name of the creator.
        post_number (Optional[PostNumber])
                                 : The post number of the post.
        topic_id (Optional[TopicId])
                                 : The ID of the topic of the post.
        username (Optional[Username])
                                 : The name of the user.
    """

    avatar_template: AvatarTemplate | None  # The avatar template of the user.
    blurb: Blurb | None  # The blurb of the post.
    created_at: (
        CreatedAt | None
    )  # Timestamp describing when the service was first deployed and available (RFC 3339 format)
    id_: int  # The ID of the post.
    like_count: LikeCount | None  # The number of likes of the post.
    name: Name | None  # The name of the creator.
    post_number: PostNumber | None  # The post number of the post.
    topic_id: TopicId | None  # The ID of the topic of the post.
    username: Username | None  # The name of the user.
