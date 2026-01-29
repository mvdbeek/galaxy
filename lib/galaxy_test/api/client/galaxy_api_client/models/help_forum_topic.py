from dataclasses import dataclass

from .help_forum_topic_archetype import HelpForumTopicArchetype
from .help_forum_topic_bookmarked import HelpForumTopicBookmarked
from .help_forum_topic_liked import HelpForumTopicLiked
from .help_forum_topic_tags_descriptions import HelpForumTopicTagsDescriptions
from .help_forum_topic_unpinned import HelpForumTopicUnpinned

__all__ = ["HelpForumTopic"]


@dataclass
class HelpForumTopic:
    """
    Model for a topic in the help forum compatible with Discourse API.

    Args:
        archetype (HelpForumTopicArchetype)
                                 : The archetype of the topic.
        archived (bool)          : Whether the topic is archived.
        bumped (bool)            : Whether the topic was bumped.
        bumped_at (str)          : The date of the last bump of the topic.
        category_id (int)        : The ID of the category of the topic.
        closed (bool)            : Whether the topic is closed.
        created_at (str)         : The creation date of the topic.
        fancy_title (str)        : The fancy title of the topic.
        has_accepted_answer (bool): Whether the topic has an accepted answer.
        highest_post_number (int): The highest post number in the topic.
        id_ (int)                : The ID of the topic. (maps from 'id')
        last_posted_at (str)     : The date of the last post in the topic.
        pinned (bool)            : Whether the topic is pinned.
        posts_count (int)        : The number of posts in the topic.
        reply_count (int)        : The number of replies in the topic.
        slug (str)               : The slug of the topic.
        tags (List[str])         : The tags of the topic.
        title (str)              : The title of the topic.
        unseen (bool)            : Whether the topic is unseen.
        visible (bool)           : Whether the topic is visible.
        bookmarked (HelpForumTopicBookmarked | None)
                                 : Whether the topic is bookmarked.
        liked (HelpForumTopicLiked | None)
                                 : Whether the topic is liked.
        tags_descriptions (HelpForumTopicTagsDescriptions | None)
                                 : The descriptions of the tags of the topic.
        unpinned (HelpForumTopicUnpinned | None)
                                 : Whether the topic is unpinned.
    """

    archetype: HelpForumTopicArchetype  # The archetype of the topic.
    archived: bool  # Whether the topic is archived.
    bumped: bool  # Whether the topic was bumped.
    bumped_at: str  # The date of the last bump of the topic.
    category_id: int  # The ID of the category of the topic.
    closed: bool  # Whether the topic is closed.
    created_at: str  # The creation date of the topic.
    fancy_title: str  # The fancy title of the topic.
    has_accepted_answer: bool  # Whether the topic has an accepted answer.
    highest_post_number: int  # The highest post number in the topic.
    id_: int  # The ID of the topic. (maps from 'id')
    last_posted_at: str  # The date of the last post in the topic.
    pinned: bool  # Whether the topic is pinned.
    posts_count: int  # The number of posts in the topic.
    reply_count: int  # The number of replies in the topic.
    slug: str  # The slug of the topic.
    tags: list[str]  # The tags of the topic.
    title: str  # The title of the topic.
    unseen: bool  # Whether the topic is unseen.
    visible: bool  # Whether the topic is visible.
    bookmarked: HelpForumTopicBookmarked | None = None  # Whether the topic is bookmarked.
    liked: HelpForumTopicLiked | None = None  # Whether the topic is liked.
    tags_descriptions: HelpForumTopicTagsDescriptions | None = None  # The descriptions of the tags of the topic.
    unpinned: HelpForumTopicUnpinned | None = None  # Whether the topic is unpinned.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "archetype": "archetype",
            "archived": "archived",
            "bookmarked": "bookmarked",
            "bumped": "bumped",
            "bumped_at": "bumped_at",
            "category_id": "category_id",
            "closed": "closed",
            "created_at": "created_at",
            "fancy_title": "fancy_title",
            "has_accepted_answer": "has_accepted_answer",
            "highest_post_number": "highest_post_number",
            "id": "id_",
            "last_posted_at": "last_posted_at",
            "liked": "liked",
            "pinned": "pinned",
            "posts_count": "posts_count",
            "reply_count": "reply_count",
            "slug": "slug",
            "tags": "tags",
            "tags_descriptions": "tags_descriptions",
            "title": "title",
            "unpinned": "unpinned",
            "unseen": "unseen",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "archetype": "archetype",
            "archived": "archived",
            "bookmarked": "bookmarked",
            "bumped": "bumped",
            "bumped_at": "bumped_at",
            "category_id": "category_id",
            "closed": "closed",
            "created_at": "created_at",
            "fancy_title": "fancy_title",
            "has_accepted_answer": "has_accepted_answer",
            "highest_post_number": "highest_post_number",
            "id_": "id",
            "last_posted_at": "last_posted_at",
            "liked": "liked",
            "pinned": "pinned",
            "posts_count": "posts_count",
            "reply_count": "reply_count",
            "slug": "slug",
            "tags": "tags",
            "tags_descriptions": "tags_descriptions",
            "title": "title",
            "unpinned": "unpinned",
            "unseen": "unseen",
            "visible": "visible",
        }
