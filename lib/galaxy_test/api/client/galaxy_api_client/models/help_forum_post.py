from dataclasses import dataclass

from .help_forum_post_avatar_template import HelpForumPostAvatarTemplate
from .help_forum_post_blurb import HelpForumPostBlurb
from .help_forum_post_created_at import HelpForumPostCreatedAt
from .help_forum_post_like_count import HelpForumPostLikeCount
from .help_forum_post_name import HelpForumPostName
from .help_forum_post_post_number import HelpForumPostPostNumber
from .help_forum_post_topic_id import HelpForumPostTopicId
from .help_forum_post_username import HelpForumPostUsername

__all__ = ["HelpForumPost"]


@dataclass
class HelpForumPost:
    """
    Model for a post in the help forum.

    Args:
        avatar_template (HelpForumPostAvatarTemplate)
                                 : The avatar template of the user.
        blurb (HelpForumPostBlurb): The blurb of the post.
        created_at (HelpForumPostCreatedAt)
                                 : The creation date of the post.
        id_ (int)                : The ID of the post. (maps from 'id')
        like_count (HelpForumPostLikeCount)
                                 : The number of likes of the post.
        name (HelpForumPostName) : The name of the post.
        post_number (HelpForumPostPostNumber)
                                 : The post number of the post.
        topic_id (HelpForumPostTopicId)
                                 : The ID of the topic of the post.
        username (HelpForumPostUsername)
                                 : The username of the post author.
    """

    avatar_template: HelpForumPostAvatarTemplate  # The avatar template of the user.
    blurb: HelpForumPostBlurb  # The blurb of the post.
    created_at: HelpForumPostCreatedAt  # The creation date of the post.
    id_: int  # The ID of the post. (maps from 'id')
    like_count: HelpForumPostLikeCount  # The number of likes of the post.
    name: HelpForumPostName  # The name of the post.
    post_number: HelpForumPostPostNumber  # The post number of the post.
    topic_id: HelpForumPostTopicId  # The ID of the topic of the post.
    username: HelpForumPostUsername  # The username of the post author.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "avatar_template": "avatar_template",
            "blurb": "blurb",
            "created_at": "created_at",
            "id": "id_",
            "like_count": "like_count",
            "name": "name",
            "post_number": "post_number",
            "topic_id": "topic_id",
            "username": "username",
        }
        key_transform_with_dump = {
            "avatar_template": "avatar_template",
            "blurb": "blurb",
            "created_at": "created_at",
            "id_": "id",
            "like_count": "like_count",
            "name": "name",
            "post_number": "post_number",
            "topic_id": "topic_id",
            "username": "username",
        }
