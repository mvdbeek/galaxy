from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_store_format import ModelStoreFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_libraries_from_store_store_dict_type_0 import CreateLibrariesFromStoreStoreDictType0


T = TypeVar("T", bound="CreateLibrariesFromStore")


@_attrs_define
class CreateLibrariesFromStore:
    """
    Attributes:
        model_store_format (ModelStoreFormat | None | Unset):
        store_content_uri (None | str | Unset):
        store_dict (CreateLibrariesFromStoreStoreDictType0 | None | Unset):
    """

    model_store_format: ModelStoreFormat | None | Unset = UNSET
    store_content_uri: None | str | Unset = UNSET
    store_dict: CreateLibrariesFromStoreStoreDictType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_libraries_from_store_store_dict_type_0 import CreateLibrariesFromStoreStoreDictType0

        model_store_format: None | str | Unset
        if isinstance(self.model_store_format, Unset):
            model_store_format = UNSET
        elif isinstance(self.model_store_format, ModelStoreFormat):
            model_store_format = self.model_store_format.value
        else:
            model_store_format = self.model_store_format

        store_content_uri: None | str | Unset
        if isinstance(self.store_content_uri, Unset):
            store_content_uri = UNSET
        else:
            store_content_uri = self.store_content_uri

        store_dict: dict[str, Any] | None | Unset
        if isinstance(self.store_dict, Unset):
            store_dict = UNSET
        elif isinstance(self.store_dict, CreateLibrariesFromStoreStoreDictType0):
            store_dict = self.store_dict.to_dict()
        else:
            store_dict = self.store_dict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_store_format is not UNSET:
            field_dict["model_store_format"] = model_store_format
        if store_content_uri is not UNSET:
            field_dict["store_content_uri"] = store_content_uri
        if store_dict is not UNSET:
            field_dict["store_dict"] = store_dict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_libraries_from_store_store_dict_type_0 import CreateLibrariesFromStoreStoreDictType0

        d = dict(src_dict)

        def _parse_model_store_format(data: object) -> ModelStoreFormat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_store_format_type_0 = ModelStoreFormat(data)

                return model_store_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelStoreFormat | None | Unset, data)

        model_store_format = _parse_model_store_format(d.pop("model_store_format", UNSET))

        def _parse_store_content_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        store_content_uri = _parse_store_content_uri(d.pop("store_content_uri", UNSET))

        def _parse_store_dict(data: object) -> CreateLibrariesFromStoreStoreDictType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                store_dict_type_0 = CreateLibrariesFromStoreStoreDictType0.from_dict(data)

                return store_dict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateLibrariesFromStoreStoreDictType0 | None | Unset, data)

        store_dict = _parse_store_dict(d.pop("store_dict", UNSET))

        create_libraries_from_store = cls(
            model_store_format=model_store_format,
            store_content_uri=store_content_uri,
            store_dict=store_dict,
        )

        create_libraries_from_store.additional_properties = d
        return create_libraries_from_store

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
