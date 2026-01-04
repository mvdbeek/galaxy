from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sharing_options import SharingOptions
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareWithPayload")


@_attrs_define
class ShareWithPayload:
    """
    Attributes:
        user_ids (list[str]): A collection of encoded IDs (or email addresses) of users that this resource will be
            shared with.
        share_option (None | SharingOptions | Unset): User choice for sharing resources which its contents may be
            restricted:
             - None: The user did not choose anything yet or no option is needed.
             - make_public: The contents of the resource will be made publicly accessible.
             - make_accessible_to_shared: This will automatically create a new `sharing role` allowing protected contents to
            be accessed only by the desired users.
             - no_changes: This won't change the current permissions for the contents. The user which this resource will be
            shared may not be able to access all its contents.
    """

    user_ids: list[str]
    share_option: None | SharingOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_ids = []
        for user_ids_item_data in self.user_ids:
            user_ids_item: str
            user_ids_item = user_ids_item_data
            user_ids.append(user_ids_item)

        share_option: None | str | Unset
        if isinstance(self.share_option, Unset):
            share_option = UNSET
        elif isinstance(self.share_option, SharingOptions):
            share_option = self.share_option.value
        else:
            share_option = self.share_option

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_ids": user_ids,
            }
        )
        if share_option is not UNSET:
            field_dict["share_option"] = share_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_ids = []
        _user_ids = d.pop("user_ids")
        for user_ids_item_data in _user_ids:

            def _parse_user_ids_item(data: object) -> str:
                return cast(str, data)

            user_ids_item = _parse_user_ids_item(user_ids_item_data)

            user_ids.append(user_ids_item)

        def _parse_share_option(data: object) -> None | SharingOptions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_option_type_0 = SharingOptions(data)

                return share_option_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SharingOptions | Unset, data)

        share_option = _parse_share_option(d.pop("share_option", UNSET))

        share_with_payload = cls(
            user_ids=user_ids,
            share_option=share_option,
        )

        share_with_payload.additional_properties = d
        return share_with_payload

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
