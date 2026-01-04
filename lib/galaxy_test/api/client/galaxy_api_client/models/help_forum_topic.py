from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HelpForumTopic")


@_attrs_define
class HelpForumTopic:
    """Model for a topic in the help forum compatible with Discourse API.

    Attributes:
        archetype (Any): The archetype of the topic.
        archived (bool): Whether the topic is archived.
        bumped (bool): Whether the topic was bumped.
        bumped_at (str): The date of the last bump of the topic.
        category_id (int): The ID of the category of the topic.
        closed (bool): Whether the topic is closed.
        created_at (str): The creation date of the topic.
        fancy_title (str): The fancy title of the topic.
        has_accepted_answer (bool): Whether the topic has an accepted answer.
        highest_post_number (int): The highest post number in the topic.
        id (int): The ID of the topic.
        last_posted_at (str): The date of the last post in the topic.
        pinned (bool): Whether the topic is pinned.
        posts_count (int): The number of posts in the topic.
        reply_count (int): The number of replies in the topic.
        slug (str): The slug of the topic.
        tags (list[str]): The tags of the topic.
        title (str): The title of the topic.
        unseen (bool): Whether the topic is unseen.
        visible (bool): Whether the topic is visible.
        bookmarked (bool | None | Unset): Whether the topic is bookmarked.
        liked (bool | None | Unset): Whether the topic is liked.
        tags_descriptions (Any | None | Unset): The descriptions of the tags of the topic.
        unpinned (bool | None | Unset): Whether the topic is unpinned.
    """

    archetype: Any
    archived: bool
    bumped: bool
    bumped_at: str
    category_id: int
    closed: bool
    created_at: str
    fancy_title: str
    has_accepted_answer: bool
    highest_post_number: int
    id: int
    last_posted_at: str
    pinned: bool
    posts_count: int
    reply_count: int
    slug: str
    tags: list[str]
    title: str
    unseen: bool
    visible: bool
    bookmarked: bool | None | Unset = UNSET
    liked: bool | None | Unset = UNSET
    tags_descriptions: Any | None | Unset = UNSET
    unpinned: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archetype = self.archetype

        archived = self.archived

        bumped = self.bumped

        bumped_at = self.bumped_at

        category_id = self.category_id

        closed = self.closed

        created_at = self.created_at

        fancy_title = self.fancy_title

        has_accepted_answer = self.has_accepted_answer

        highest_post_number = self.highest_post_number

        id = self.id

        last_posted_at = self.last_posted_at

        pinned = self.pinned

        posts_count = self.posts_count

        reply_count = self.reply_count

        slug = self.slug

        tags = self.tags

        title = self.title

        unseen = self.unseen

        visible = self.visible

        bookmarked: bool | None | Unset
        if isinstance(self.bookmarked, Unset):
            bookmarked = UNSET
        else:
            bookmarked = self.bookmarked

        liked: bool | None | Unset
        if isinstance(self.liked, Unset):
            liked = UNSET
        else:
            liked = self.liked

        tags_descriptions: Any | None | Unset
        if isinstance(self.tags_descriptions, Unset):
            tags_descriptions = UNSET
        else:
            tags_descriptions = self.tags_descriptions

        unpinned: bool | None | Unset
        if isinstance(self.unpinned, Unset):
            unpinned = UNSET
        else:
            unpinned = self.unpinned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archetype": archetype,
                "archived": archived,
                "bumped": bumped,
                "bumped_at": bumped_at,
                "category_id": category_id,
                "closed": closed,
                "created_at": created_at,
                "fancy_title": fancy_title,
                "has_accepted_answer": has_accepted_answer,
                "highest_post_number": highest_post_number,
                "id": id,
                "last_posted_at": last_posted_at,
                "pinned": pinned,
                "posts_count": posts_count,
                "reply_count": reply_count,
                "slug": slug,
                "tags": tags,
                "title": title,
                "unseen": unseen,
                "visible": visible,
            }
        )
        if bookmarked is not UNSET:
            field_dict["bookmarked"] = bookmarked
        if liked is not UNSET:
            field_dict["liked"] = liked
        if tags_descriptions is not UNSET:
            field_dict["tags_descriptions"] = tags_descriptions
        if unpinned is not UNSET:
            field_dict["unpinned"] = unpinned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archetype = d.pop("archetype")

        archived = d.pop("archived")

        bumped = d.pop("bumped")

        bumped_at = d.pop("bumped_at")

        category_id = d.pop("category_id")

        closed = d.pop("closed")

        created_at = d.pop("created_at")

        fancy_title = d.pop("fancy_title")

        has_accepted_answer = d.pop("has_accepted_answer")

        highest_post_number = d.pop("highest_post_number")

        id = d.pop("id")

        last_posted_at = d.pop("last_posted_at")

        pinned = d.pop("pinned")

        posts_count = d.pop("posts_count")

        reply_count = d.pop("reply_count")

        slug = d.pop("slug")

        tags = cast(list[str], d.pop("tags"))

        title = d.pop("title")

        unseen = d.pop("unseen")

        visible = d.pop("visible")

        def _parse_bookmarked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        bookmarked = _parse_bookmarked(d.pop("bookmarked", UNSET))

        def _parse_liked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        liked = _parse_liked(d.pop("liked", UNSET))

        def _parse_tags_descriptions(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        tags_descriptions = _parse_tags_descriptions(d.pop("tags_descriptions", UNSET))

        def _parse_unpinned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        unpinned = _parse_unpinned(d.pop("unpinned", UNSET))

        help_forum_topic = cls(
            archetype=archetype,
            archived=archived,
            bumped=bumped,
            bumped_at=bumped_at,
            category_id=category_id,
            closed=closed,
            created_at=created_at,
            fancy_title=fancy_title,
            has_accepted_answer=has_accepted_answer,
            highest_post_number=highest_post_number,
            id=id,
            last_posted_at=last_posted_at,
            pinned=pinned,
            posts_count=posts_count,
            reply_count=reply_count,
            slug=slug,
            tags=tags,
            title=title,
            unseen=unseen,
            visible=visible,
            bookmarked=bookmarked,
            liked=liked,
            tags_descriptions=tags_descriptions,
            unpinned=unpinned,
        )

        help_forum_topic.additional_properties = d
        return help_forum_topic

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
