from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.help_forum_category import HelpForumCategory
    from ..models.help_forum_group import HelpForumGroup
    from ..models.help_forum_grouped_search_result import HelpForumGroupedSearchResult
    from ..models.help_forum_post import HelpForumPost
    from ..models.help_forum_tag import HelpForumTag
    from ..models.help_forum_topic import HelpForumTopic
    from ..models.help_forum_user import HelpForumUser


T = TypeVar("T", bound="HelpForumSearchResponse")


@_attrs_define
class HelpForumSearchResponse:
    """Response model for the help search API endpoint.

    This model is based on the Discourse API response for the search endpoint.

        Attributes:
            categories (list[HelpForumCategory] | None | Unset): The list of categories returned by the search.
            grouped_search_result (HelpForumGroupedSearchResult | None | Unset): The grouped search result.
            groups (list[HelpForumGroup] | None | Unset): The list of groups returned by the search.
            posts (list[HelpForumPost] | Unset): The list of posts returned by the search.
            tags (list[HelpForumTag] | None | Unset): The list of tags returned by the search.
            topics (list[HelpForumTopic] | Unset): The list of topics returned by the search.
            users (list[HelpForumUser] | None | Unset): The list of users returned by the search.
    """

    categories: list[HelpForumCategory] | None | Unset = UNSET
    grouped_search_result: HelpForumGroupedSearchResult | None | Unset = UNSET
    groups: list[HelpForumGroup] | None | Unset = UNSET
    posts: list[HelpForumPost] | Unset = UNSET
    tags: list[HelpForumTag] | None | Unset = UNSET
    topics: list[HelpForumTopic] | Unset = UNSET
    users: list[HelpForumUser] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_forum_grouped_search_result import HelpForumGroupedSearchResult

        categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        grouped_search_result: dict[str, Any] | None | Unset
        if isinstance(self.grouped_search_result, Unset):
            grouped_search_result = UNSET
        elif isinstance(self.grouped_search_result, HelpForumGroupedSearchResult):
            grouped_search_result = self.grouped_search_result.to_dict()
        else:
            grouped_search_result = self.grouped_search_result

        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if grouped_search_result is not UNSET:
            field_dict["grouped_search_result"] = grouped_search_result
        if groups is not UNSET:
            field_dict["groups"] = groups
        if posts is not UNSET:
            field_dict["posts"] = posts
        if tags is not UNSET:
            field_dict["tags"] = tags
        if topics is not UNSET:
            field_dict["topics"] = topics
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.help_forum_category import HelpForumCategory
        from ..models.help_forum_group import HelpForumGroup
        from ..models.help_forum_grouped_search_result import HelpForumGroupedSearchResult
        from ..models.help_forum_post import HelpForumPost
        from ..models.help_forum_tag import HelpForumTag
        from ..models.help_forum_topic import HelpForumTopic
        from ..models.help_forum_user import HelpForumUser

        d = dict(src_dict)

        def _parse_categories(data: object) -> list[HelpForumCategory] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = HelpForumCategory.from_dict(categories_type_0_item_data)

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HelpForumCategory] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_grouped_search_result(data: object) -> HelpForumGroupedSearchResult | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grouped_search_result_type_0 = HelpForumGroupedSearchResult.from_dict(data)

                return grouped_search_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HelpForumGroupedSearchResult | None | Unset, data)

        grouped_search_result = _parse_grouped_search_result(d.pop("grouped_search_result", UNSET))

        def _parse_groups(data: object) -> list[HelpForumGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = HelpForumGroup.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HelpForumGroup] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        _posts = d.pop("posts", UNSET)
        posts: list[HelpForumPost] | Unset = UNSET
        if _posts is not UNSET:
            posts = []
            for posts_item_data in _posts:
                posts_item = HelpForumPost.from_dict(posts_item_data)

                posts.append(posts_item)

        def _parse_tags(data: object) -> list[HelpForumTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = HelpForumTag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HelpForumTag] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        _topics = d.pop("topics", UNSET)
        topics: list[HelpForumTopic] | Unset = UNSET
        if _topics is not UNSET:
            topics = []
            for topics_item_data in _topics:
                topics_item = HelpForumTopic.from_dict(topics_item_data)

                topics.append(topics_item)

        def _parse_users(data: object) -> list[HelpForumUser] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = HelpForumUser.from_dict(users_type_0_item_data)

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HelpForumUser] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        help_forum_search_response = cls(
            categories=categories,
            grouped_search_result=grouped_search_result,
            groups=groups,
            posts=posts,
            tags=tags,
            topics=topics,
            users=users,
        )

        help_forum_search_response.additional_properties = d
        return help_forum_search_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
