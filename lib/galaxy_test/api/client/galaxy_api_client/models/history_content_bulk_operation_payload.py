from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.history_content_item_operation import HistoryContentItemOperation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.change_datatype_operation_params import ChangeDatatypeOperationParams
    from ..models.change_dbkey_operation_params import ChangeDbkeyOperationParams
    from ..models.history_content_item import HistoryContentItem
    from ..models.tag_operation_params import TagOperationParams


T = TypeVar("T", bound="HistoryContentBulkOperationPayload")


@_attrs_define
class HistoryContentBulkOperationPayload:
    """
    Attributes:
        operation (HistoryContentItemOperation):
        items (list[HistoryContentItem] | None | Unset):
        params (ChangeDatatypeOperationParams | ChangeDbkeyOperationParams | None | TagOperationParams | Unset):
    """

    operation: HistoryContentItemOperation
    items: list[HistoryContentItem] | None | Unset = UNSET
    params: ChangeDatatypeOperationParams | ChangeDbkeyOperationParams | None | TagOperationParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.change_datatype_operation_params import ChangeDatatypeOperationParams
        from ..models.change_dbkey_operation_params import ChangeDbkeyOperationParams
        from ..models.tag_operation_params import TagOperationParams

        operation = self.operation.value

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, ChangeDatatypeOperationParams):
            params = self.params.to_dict()
        elif isinstance(self.params, ChangeDbkeyOperationParams):
            params = self.params.to_dict()
        elif isinstance(self.params, TagOperationParams):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_datatype_operation_params import ChangeDatatypeOperationParams
        from ..models.change_dbkey_operation_params import ChangeDbkeyOperationParams
        from ..models.history_content_item import HistoryContentItem
        from ..models.tag_operation_params import TagOperationParams

        d = dict(src_dict)
        operation = HistoryContentItemOperation(d.pop("operation"))

        def _parse_items(data: object) -> list[HistoryContentItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = HistoryContentItem.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HistoryContentItem] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        def _parse_params(
            data: object,
        ) -> ChangeDatatypeOperationParams | ChangeDbkeyOperationParams | None | TagOperationParams | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = ChangeDatatypeOperationParams.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_1 = ChangeDbkeyOperationParams.from_dict(data)

                return params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_2 = TagOperationParams.from_dict(data)

                return params_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ChangeDatatypeOperationParams | ChangeDbkeyOperationParams | None | TagOperationParams | Unset, data
            )

        params = _parse_params(d.pop("params", UNSET))

        history_content_bulk_operation_payload = cls(
            operation=operation,
            items=items,
            params=params,
        )

        history_content_bulk_operation_payload.additional_properties = d
        return history_content_bulk_operation_payload

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
