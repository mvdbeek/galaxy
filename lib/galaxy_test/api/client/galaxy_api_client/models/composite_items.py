from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_data_element import FileDataElement
    from ..models.ftp_import_element import FtpImportElement
    from ..models.pasted_data_element import PastedDataElement
    from ..models.path_data_element import PathDataElement
    from ..models.server_dir_element import ServerDirElement
    from ..models.url_data_element import UrlDataElement


T = TypeVar("T", bound="CompositeItems")


@_attrs_define
class CompositeItems:
    """
    Attributes:
        elements (list[FileDataElement | FtpImportElement | PastedDataElement | PathDataElement | ServerDirElement |
            UrlDataElement]):
    """

    elements: list[
        FileDataElement | FtpImportElement | PastedDataElement | PathDataElement | ServerDirElement | UrlDataElement
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_data_element import FileDataElement
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        elements = []
        for elements_item_data in self.elements:
            elements_item: dict[str, Any]
            if isinstance(elements_item_data, FileDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, PastedDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, UrlDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, PathDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, ServerDirElement):
                elements_item = elements_item_data.to_dict()
            else:
                elements_item = elements_item_data.to_dict()

            elements.append(elements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "elements": elements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_data_element import FileDataElement
        from ..models.ftp_import_element import FtpImportElement
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        d = dict(src_dict)
        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:

            def _parse_elements_item(
                data: object,
            ) -> (
                FileDataElement
                | FtpImportElement
                | PastedDataElement
                | PathDataElement
                | ServerDirElement
                | UrlDataElement
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0 = FileDataElement.from_dict(data)

                    return elements_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_1 = PastedDataElement.from_dict(data)

                    return elements_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_2 = UrlDataElement.from_dict(data)

                    return elements_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_3 = PathDataElement.from_dict(data)

                    return elements_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_4 = ServerDirElement.from_dict(data)

                    return elements_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                elements_item_type_5 = FtpImportElement.from_dict(data)

                return elements_item_type_5

            elements_item = _parse_elements_item(elements_item_data)

            elements.append(elements_item)

        composite_items = cls(
            elements=elements,
        )

        composite_items.additional_properties = d
        return composite_items

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
