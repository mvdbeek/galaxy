from dataclasses import dataclass

from .archetype import Archetype
from .bookmarked import Bookmarked
from .liked import Liked
from .tags import Tags
from .tags_descriptions import TagsDescriptions
from .unpinned import Unpinned

__all__ = ["HelpForumTopic"]


@dataclass
class HelpForumTopic:
    """
    Model for a topic in the help forum compatible with Discourse API.

    Args:
        archetype (Archetype)    : The archetype of the topic.
        archived (bool)          : Whether the topic is archived.
        bumped (bool)            : Whether the topic was bumped.
        bumped_at (str)          : The date of the last bump of the topic.
        category_id (int)        : The ID of the category of the topic.
        closed (bool)            : Whether the topic is closed.
        created_at (str)         : The creation date of the topic.
        fancy_title (str)        : The fancy title of the topic.
        has_accepted_answer (bool): Whether the topic has an accepted answer.
        highest_post_number (int): The highest post number in the topic.
        id_ (int)                : The ID of the topic.
        last_posted_at (str)     : The date of the last post in the topic.
        pinned (bool)            : Whether the topic is pinned.
        posts_count (int)        : The number of posts in the topic.
        reply_count (int)        : The number of replies in the topic.
        slug (str)               : The slug of the topic.
        tags (Tags)              : The tags of the topic.
        title (str)              : The title of the topic.
        unseen (bool)            : Whether the topic is unseen.
        visible (bool)           : Whether the topic is visible.
        bookmarked (Optional[Bookmarked])
                                 : Whether the topic is bookmarked.
        liked (Optional[Liked])  : Whether the topic is liked.
        tags_descriptions (Optional[TagsDescriptions])
                                 : The descriptions of the tags of the topic.
        unpinned (Optional[Unpinned])
                                 : Whether the topic is unpinned.
    """

    archetype: Archetype  # The archetype of the topic.
    archived: bool  # Whether the topic is archived.
    bumped: bool  # Whether the topic was bumped.
    bumped_at: str  # The date of the last bump of the topic.
    category_id: int  # The ID of the category of the topic.
    closed: bool  # Whether the topic is closed.
    created_at: str  # The creation date of the topic.
    fancy_title: str  # The fancy title of the topic.
    has_accepted_answer: bool  # Whether the topic has an accepted answer.
    highest_post_number: int  # The highest post number in the topic.
    id_: int  # The ID of the topic.
    last_posted_at: str  # The date of the last post in the topic.
    pinned: bool  # Whether the topic is pinned.
    posts_count: int  # The number of posts in the topic.
    reply_count: int  # The number of replies in the topic.
    slug: str  # The slug of the topic.
    tags: Tags  # The tags of the topic.
    title: str  # The title of the topic.
    unseen: bool  # Whether the topic is unseen.
    visible: bool  # Whether the topic is visible.
    bookmarked: Bookmarked | None = None  # Whether the topic is bookmarked.
    liked: Liked | None = None  # Whether the topic is liked.
    tags_descriptions: TagsDescriptions | None = None  # The descriptions of the tags of the topic.
    unpinned: Unpinned | None = None  # Whether the topic is unpinned.
