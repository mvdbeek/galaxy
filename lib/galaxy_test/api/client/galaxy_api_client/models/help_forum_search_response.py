from dataclasses import dataclass, field

from .categories import Categories
from .grouped_search_result import GroupedSearchResult
from .groups import Groups
from .help_forum_post import HelpForumPost
from .help_forum_topic import HelpForumTopic
from .tags import Tags
from .users import Users

__all__ = ["HelpForumSearchResponse"]


@dataclass
class HelpForumSearchResponse:
    """
    Response model for the help search API endpoint.  This model is based on the Discourse
    API response for the search endpoint.

    Args:
        categories (Optional[Categories])
                                 : The list of categories returned by the search.
        grouped_search_result (Optional[GroupedSearchResult])
                                 : The grouped search result.
        groups (Optional[Groups]): The list of groups returned by the search.
        posts (Optional[List[HelpForumPost]])
                                 : The list of posts returned by the search.
        tags (Optional[Tags])    : The list of tags returned by the search.
        topics (Optional[List[HelpForumTopic]])
                                 : The list of topics returned by the search.
        users (Optional[Users])  : The list of users returned by the search.
    """

    categories: Categories | None = None  # The list of categories returned by the search.
    grouped_search_result: GroupedSearchResult | None = None  # The grouped search result.
    groups: Groups | None = None  # The list of groups returned by the search.
    posts: list[HelpForumPost] | None = field(default_factory=list)  # The list of posts returned by the search.
    tags: Tags | None = None  # The list of tags returned by the search.
    topics: list[HelpForumTopic] | None = field(default_factory=list)  # The list of topics returned by the search.
    users: Users | None = None  # The list of users returned by the search.
