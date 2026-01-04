from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetCollectionAttributesResult")


@_attrs_define
class DatasetCollectionAttributesResult:
    """
    Attributes:
        dbkey (str): TODO
        dbkeys (list[str] | None):
        extension (str): The dataset file extension.
        extensions (list[str] | None):
        model_class (Literal['HistoryDatasetCollectionAssociation']): The name of the database model class.
        tags (list[str]): The collection of tags associated with an item.
    """

    dbkey: str
    dbkeys: list[str] | None
    extension: str
    extensions: list[str] | None
    model_class: Literal["HistoryDatasetCollectionAssociation"]
    tags: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dbkey = self.dbkey

        dbkeys: list[str] | None
        if isinstance(self.dbkeys, list):
            dbkeys = self.dbkeys

        else:
            dbkeys = self.dbkeys

        extension = self.extension

        extensions: list[str] | None
        if isinstance(self.extensions, list):
            extensions = self.extensions

        else:
            extensions = self.extensions

        model_class = self.model_class

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dbkey": dbkey,
                "dbkeys": dbkeys,
                "extension": extension,
                "extensions": extensions,
                "model_class": model_class,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dbkey = d.pop("dbkey")

        def _parse_dbkeys(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dbkeys_type_0 = cast(list[str], data)

                return dbkeys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        dbkeys = _parse_dbkeys(d.pop("dbkeys"))

        extension = d.pop("extension")

        def _parse_extensions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extensions_type_0 = cast(list[str], data)

                return extensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        extensions = _parse_extensions(d.pop("extensions"))

        model_class = cast(Literal["HistoryDatasetCollectionAssociation"], d.pop("model_class"))
        if model_class != "HistoryDatasetCollectionAssociation":
            raise ValueError(f"model_class must match const 'HistoryDatasetCollectionAssociation', got '{model_class}'")

        tags = cast(list[str], d.pop("tags"))

        dataset_collection_attributes_result = cls(
            dbkey=dbkey,
            dbkeys=dbkeys,
            extension=extension,
            extensions=extensions,
            model_class=model_class,
            tags=tags,
        )

        dataset_collection_attributes_result.additional_properties = d
        return dataset_collection_attributes_result

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
