from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.share_history_extra import ShareHistoryExtra
    from ..models.user_email import UserEmail


T = TypeVar("T", bound="ShareHistoryWithStatus")


@_attrs_define
class ShareHistoryWithStatus:
    """
    Attributes:
        extra (ShareHistoryExtra):
        id (str): The encoded ID of the resource to be shared. Example: 0123456789ABCDEF.
        importable (bool): Whether this resource can be published using a link.
        published (bool): Whether this resource is currently published.
        title (str): The title or name of the resource.
        email_hash (None | str | Unset): Encoded owner email.
        errors (list[str] | Unset): Collection of messages indicating that the resource was not shared with some (or all
            users) due to an error.
        username (None | str | Unset): The owner's username.
        username_and_slug (None | str | Unset): The relative URL in the form of
            /u/{username}/{resource_single_char}/{slug}
        users_shared_with (list[UserEmail] | Unset): The list of encoded ids for users the resource has been shared.
    """

    extra: ShareHistoryExtra
    id: str
    importable: bool
    published: bool
    title: str
    email_hash: None | str | Unset = UNSET
    errors: list[str] | Unset = UNSET
    username: None | str | Unset = UNSET
    username_and_slug: None | str | Unset = UNSET
    users_shared_with: list[UserEmail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extra = self.extra.to_dict()

        id = self.id

        importable = self.importable

        published = self.published

        title = self.title

        email_hash: None | str | Unset
        if isinstance(self.email_hash, Unset):
            email_hash = UNSET
        else:
            email_hash = self.email_hash

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        username_and_slug: None | str | Unset
        if isinstance(self.username_and_slug, Unset):
            username_and_slug = UNSET
        else:
            username_and_slug = self.username_and_slug

        users_shared_with: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users_shared_with, Unset):
            users_shared_with = []
            for users_shared_with_item_data in self.users_shared_with:
                users_shared_with_item = users_shared_with_item_data.to_dict()
                users_shared_with.append(users_shared_with_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extra": extra,
                "id": id,
                "importable": importable,
                "published": published,
                "title": title,
            }
        )
        if email_hash is not UNSET:
            field_dict["email_hash"] = email_hash
        if errors is not UNSET:
            field_dict["errors"] = errors
        if username is not UNSET:
            field_dict["username"] = username
        if username_and_slug is not UNSET:
            field_dict["username_and_slug"] = username_and_slug
        if users_shared_with is not UNSET:
            field_dict["users_shared_with"] = users_shared_with

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_history_extra import ShareHistoryExtra
        from ..models.user_email import UserEmail

        d = dict(src_dict)
        extra = ShareHistoryExtra.from_dict(d.pop("extra"))

        id = d.pop("id")

        importable = d.pop("importable")

        published = d.pop("published")

        title = d.pop("title")

        def _parse_email_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_hash = _parse_email_hash(d.pop("email_hash", UNSET))

        errors = cast(list[str], d.pop("errors", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_username_and_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username_and_slug = _parse_username_and_slug(d.pop("username_and_slug", UNSET))

        _users_shared_with = d.pop("users_shared_with", UNSET)
        users_shared_with: list[UserEmail] | Unset = UNSET
        if _users_shared_with is not UNSET:
            users_shared_with = []
            for users_shared_with_item_data in _users_shared_with:
                users_shared_with_item = UserEmail.from_dict(users_shared_with_item_data)

                users_shared_with.append(users_shared_with_item)

        share_history_with_status = cls(
            extra=extra,
            id=id,
            importable=importable,
            published=published,
            title=title,
            email_hash=email_hash,
            errors=errors,
            username=username,
            username_and_slug=username_and_slug,
            users_shared_with=users_shared_with,
        )

        share_history_with_status.additional_properties = d
        return share_history_with_status

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
