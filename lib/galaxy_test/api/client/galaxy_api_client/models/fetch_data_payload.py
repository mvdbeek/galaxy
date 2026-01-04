from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_elements_from_target import DataElementsFromTarget
    from ..models.data_elements_target import DataElementsTarget
    from ..models.ftp_import_target import FtpImportTarget
    from ..models.hdca_data_items_from_target import HdcaDataItemsFromTarget
    from ..models.hdca_data_items_target import HdcaDataItemsTarget


T = TypeVar("T", bound="FetchDataPayload")


@_attrs_define
class FetchDataPayload:
    """
    Attributes:
        history_id (str):  Example: 0123456789ABCDEF.
        targets (list[DataElementsFromTarget | DataElementsTarget | FtpImportTarget | HdcaDataItemsFromTarget |
            HdcaDataItemsTarget]):
        landing_uuid (None | str | Unset):
    """

    history_id: str
    targets: list[
        DataElementsFromTarget | DataElementsTarget | FtpImportTarget | HdcaDataItemsFromTarget | HdcaDataItemsTarget
    ]
    landing_uuid: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_elements_from_target import DataElementsFromTarget
        from ..models.data_elements_target import DataElementsTarget
        from ..models.hdca_data_items_from_target import HdcaDataItemsFromTarget
        from ..models.hdca_data_items_target import HdcaDataItemsTarget

        history_id = self.history_id

        targets = []
        for targets_item_data in self.targets:
            targets_item: dict[str, Any]
            if isinstance(targets_item_data, DataElementsTarget):
                targets_item = targets_item_data.to_dict()
            elif isinstance(targets_item_data, HdcaDataItemsTarget):
                targets_item = targets_item_data.to_dict()
            elif isinstance(targets_item_data, DataElementsFromTarget):
                targets_item = targets_item_data.to_dict()
            elif isinstance(targets_item_data, HdcaDataItemsFromTarget):
                targets_item = targets_item_data.to_dict()
            else:
                targets_item = targets_item_data.to_dict()

            targets.append(targets_item)

        landing_uuid: None | str | Unset
        if isinstance(self.landing_uuid, Unset):
            landing_uuid = UNSET
        else:
            landing_uuid = self.landing_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_id": history_id,
                "targets": targets,
            }
        )
        if landing_uuid is not UNSET:
            field_dict["landing_uuid"] = landing_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_elements_from_target import DataElementsFromTarget
        from ..models.data_elements_target import DataElementsTarget
        from ..models.ftp_import_target import FtpImportTarget
        from ..models.hdca_data_items_from_target import HdcaDataItemsFromTarget
        from ..models.hdca_data_items_target import HdcaDataItemsTarget

        d = dict(src_dict)
        history_id = d.pop("history_id")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:

            def _parse_targets_item(
                data: object,
            ) -> (
                DataElementsFromTarget
                | DataElementsTarget
                | FtpImportTarget
                | HdcaDataItemsFromTarget
                | HdcaDataItemsTarget
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_0 = DataElementsTarget.from_dict(data)

                    return targets_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_1 = HdcaDataItemsTarget.from_dict(data)

                    return targets_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_2 = DataElementsFromTarget.from_dict(data)

                    return targets_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_3 = HdcaDataItemsFromTarget.from_dict(data)

                    return targets_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                targets_item_type_4 = FtpImportTarget.from_dict(data)

                return targets_item_type_4

            targets_item = _parse_targets_item(targets_item_data)

            targets.append(targets_item)

        def _parse_landing_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        landing_uuid = _parse_landing_uuid(d.pop("landing_uuid", UNSET))

        fetch_data_payload = cls(
            history_id=history_id,
            targets=targets,
            landing_uuid=landing_uuid,
        )

        fetch_data_payload.additional_properties = d
        return fetch_data_payload

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
