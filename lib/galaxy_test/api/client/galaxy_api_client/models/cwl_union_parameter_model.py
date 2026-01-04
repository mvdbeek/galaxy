from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cwl_boolean_parameter_model import CwlBooleanParameterModel
    from ..models.cwl_directory_parameter_model import CwlDirectoryParameterModel
    from ..models.cwl_file_parameter_model import CwlFileParameterModel
    from ..models.cwl_float_parameter_model import CwlFloatParameterModel
    from ..models.cwl_integer_parameter_model import CwlIntegerParameterModel
    from ..models.cwl_null_parameter_model import CwlNullParameterModel
    from ..models.cwl_string_parameter_model import CwlStringParameterModel


T = TypeVar("T", bound="CwlUnionParameterModel")


@_attrs_define
class CwlUnionParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        parameters (list[CwlBooleanParameterModel | CwlDirectoryParameterModel | CwlFileParameterModel |
            CwlFloatParameterModel | CwlIntegerParameterModel | CwlNullParameterModel | CwlStringParameterModel |
            CwlUnionParameterModel]):
        parameter_type (Literal['cwl_union'] | Unset):  Default: 'cwl_union'.
    """

    name: str
    parameters: list[
        CwlBooleanParameterModel
        | CwlDirectoryParameterModel
        | CwlFileParameterModel
        | CwlFloatParameterModel
        | CwlIntegerParameterModel
        | CwlNullParameterModel
        | CwlStringParameterModel
        | CwlUnionParameterModel
    ]
    parameter_type: Literal["cwl_union"] | Unset = "cwl_union"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cwl_boolean_parameter_model import CwlBooleanParameterModel
        from ..models.cwl_directory_parameter_model import CwlDirectoryParameterModel
        from ..models.cwl_file_parameter_model import CwlFileParameterModel
        from ..models.cwl_float_parameter_model import CwlFloatParameterModel
        from ..models.cwl_integer_parameter_model import CwlIntegerParameterModel
        from ..models.cwl_null_parameter_model import CwlNullParameterModel
        from ..models.cwl_string_parameter_model import CwlStringParameterModel

        name = self.name

        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item: dict[str, Any]
            if isinstance(parameters_item_data, CwlIntegerParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlFloatParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlStringParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlBooleanParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlNullParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlFileParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlDirectoryParameterModel):
                parameters_item = parameters_item_data.to_dict()
            else:
                parameters_item = parameters_item_data.to_dict()

            parameters.append(parameters_item)

        parameter_type = self.parameter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parameters": parameters,
            }
        )
        if parameter_type is not UNSET:
            field_dict["parameter_type"] = parameter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cwl_boolean_parameter_model import CwlBooleanParameterModel
        from ..models.cwl_directory_parameter_model import CwlDirectoryParameterModel
        from ..models.cwl_file_parameter_model import CwlFileParameterModel
        from ..models.cwl_float_parameter_model import CwlFloatParameterModel
        from ..models.cwl_integer_parameter_model import CwlIntegerParameterModel
        from ..models.cwl_null_parameter_model import CwlNullParameterModel
        from ..models.cwl_string_parameter_model import CwlStringParameterModel

        d = dict(src_dict)
        name = d.pop("name")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:

            def _parse_parameters_item(
                data: object,
            ) -> (
                CwlBooleanParameterModel
                | CwlDirectoryParameterModel
                | CwlFileParameterModel
                | CwlFloatParameterModel
                | CwlIntegerParameterModel
                | CwlNullParameterModel
                | CwlStringParameterModel
                | CwlUnionParameterModel
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_0 = CwlIntegerParameterModel.from_dict(data)

                    return parameters_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_1 = CwlFloatParameterModel.from_dict(data)

                    return parameters_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_2 = CwlStringParameterModel.from_dict(data)

                    return parameters_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_3 = CwlBooleanParameterModel.from_dict(data)

                    return parameters_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_4 = CwlNullParameterModel.from_dict(data)

                    return parameters_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_5 = CwlFileParameterModel.from_dict(data)

                    return parameters_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_6 = CwlDirectoryParameterModel.from_dict(data)

                    return parameters_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_item_type_7 = CwlUnionParameterModel.from_dict(data)

                return parameters_item_type_7

            parameters_item = _parse_parameters_item(parameters_item_data)

            parameters.append(parameters_item)

        parameter_type = cast(Literal["cwl_union"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "cwl_union" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'cwl_union', got '{parameter_type}'")

        cwl_union_parameter_model = cls(
            name=name,
            parameters=parameters,
            parameter_type=parameter_type,
        )

        cwl_union_parameter_model.additional_properties = d
        return cwl_union_parameter_model

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
