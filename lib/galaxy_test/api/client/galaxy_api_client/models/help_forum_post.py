from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HelpForumPost")


@_attrs_define
class HelpForumPost:
    """Model for a post in the help forum.

    Attributes:
        avatar_template (None | str): The avatar template of the user.
        blurb (None | str): The blurb of the post.
        created_at (None | str): The creation date of the post.
        id (int): The ID of the post.
        like_count (int | None): The number of likes of the post.
        name (None | str): The name of the post.
        post_number (int | None): The post number of the post.
        topic_id (int | None): The ID of the topic of the post.
        username (None | str): The username of the post author.
    """

    avatar_template: None | str
    blurb: None | str
    created_at: None | str
    id: int
    like_count: int | None
    name: None | str
    post_number: int | None
    topic_id: int | None
    username: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_template: None | str
        avatar_template = self.avatar_template

        blurb: None | str
        blurb = self.blurb

        created_at: None | str
        created_at = self.created_at

        id = self.id

        like_count: int | None
        like_count = self.like_count

        name: None | str
        name = self.name

        post_number: int | None
        post_number = self.post_number

        topic_id: int | None
        topic_id = self.topic_id

        username: None | str
        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar_template": avatar_template,
                "blurb": blurb,
                "created_at": created_at,
                "id": id,
                "like_count": like_count,
                "name": name,
                "post_number": post_number,
                "topic_id": topic_id,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_avatar_template(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_template = _parse_avatar_template(d.pop("avatar_template"))

        def _parse_blurb(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        blurb = _parse_blurb(d.pop("blurb"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        id = d.pop("id")

        def _parse_like_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        like_count = _parse_like_count(d.pop("like_count"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_post_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        post_number = _parse_post_number(d.pop("post_number"))

        def _parse_topic_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        topic_id = _parse_topic_id(d.pop("topic_id"))

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        help_forum_post = cls(
            avatar_template=avatar_template,
            blurb=blurb,
            created_at=created_at,
            id=id,
            like_count=like_count,
            name=name,
            post_number=post_number,
            topic_id=topic_id,
            username=username,
        )

        help_forum_post.additional_properties = d
        return help_forum_post

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
