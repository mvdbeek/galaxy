from dataclasses import dataclass, field

from .help_forum_post import HelpForumPost
from .help_forum_search_response_categories import HelpForumSearchResponseCategories
from .help_forum_search_response_grouped_search_result import HelpForumSearchResponseGroupedSearchResult
from .help_forum_search_response_groups import HelpForumSearchResponseGroups
from .help_forum_search_response_tags import HelpForumSearchResponseTags
from .help_forum_search_response_users import HelpForumSearchResponseUsers
from .help_forum_topic import HelpForumTopic

__all__ = ["HelpForumSearchResponse"]


@dataclass
class HelpForumSearchResponse:
    """
    Response model for the help search API endpoint.  This model is based on the Discourse
    API response for the search endpoint.

    Args:
        categories (HelpForumSearchResponseCategories | None)
                                 : The list of categories returned by the search.
        grouped_search_result (HelpForumSearchResponseGroupedSearchResult | None)
                                 : The grouped search result.
        groups (HelpForumSearchResponseGroups | None)
                                 : The list of groups returned by the search.
        posts (List[HelpForumPost] | None)
                                 : The list of posts returned by the search.
        tags (HelpForumSearchResponseTags | None)
                                 : The list of tags returned by the search.
        topics (List[HelpForumTopic] | None)
                                 : The list of topics returned by the search.
        users (HelpForumSearchResponseUsers | None)
                                 : The list of users returned by the search.
    """

    categories: HelpForumSearchResponseCategories | None = None  # The list of categories returned by the search.
    grouped_search_result: HelpForumSearchResponseGroupedSearchResult | None = None  # The grouped search result.
    groups: HelpForumSearchResponseGroups | None = None  # The list of groups returned by the search.
    posts: list[HelpForumPost] | None = field(default_factory=list)  # The list of posts returned by the search.
    tags: HelpForumSearchResponseTags | None = None  # The list of tags returned by the search.
    topics: list[HelpForumTopic] | None = field(default_factory=list)  # The list of topics returned by the search.
    users: HelpForumSearchResponseUsers | None = None  # The list of users returned by the search.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "categories": "categories",
            "grouped_search_result": "grouped_search_result",
            "groups": "groups",
            "posts": "posts",
            "tags": "tags",
            "topics": "topics",
            "users": "users",
        }
        key_transform_with_dump = {
            "categories": "categories",
            "grouped_search_result": "grouped_search_result",
            "groups": "groups",
            "posts": "posts",
            "tags": "tags",
            "topics": "topics",
            "users": "users",
        }
